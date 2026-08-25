#!/usr/bin/env python3
"""
릴리스 전 사이트 검사기.

의존성 없음 (python3 표준 라이브러리만). 먼저 사이트를 빌드한 뒤 실행합니다.

    bundle exec jekyll build
    python3 tools/verify.py

baseurl 을 붙여 빌드했다면 검사기에도 같은 값을 넘깁니다. 넘기지 않으면
접두어가 붙은 모든 링크를 깨진 링크로 잡습니다.

    bundle exec jekyll build --baseurl /testrepo
    python3 tools/verify.py --baseurl /testrepo

빌드 산출물(_site)과 소스를 함께 보고, 실패 항목이 있으면 종료 코드 1을 반환합니다.
CI 에서 쓰려면 그대로 실행하면 됩니다.
"""

from __future__ import annotations

import glob
import os
import re
import sys
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "_site")


def parse_baseurl() -> str:
    """`--baseurl /foo` 또는 `--baseurl=/foo` 를 읽습니다.

    CI 는 `jekyll build --baseurl "${{ steps.pages.outputs.base_path }}"` 로
    빌드하므로, 프로젝트 페이지로 옮기면 모든 링크에 접두어가 붙습니다.
    검사기가 이 값을 모르면 정상 링크를 전부 깨졌다고 보고합니다.
    """
    args = sys.argv[1:]
    value = ""
    for i, arg in enumerate(args):
        if arg == "--baseurl" and i + 1 < len(args):
            value = args[i + 1]
        elif arg.startswith("--baseurl="):
            value = arg.split("=", 1)[1]
    return "/" + value.strip("/") if value.strip("/") else ""


BASEURL = parse_baseurl()

# 방문자에게 보여선 안 되는 편집자용 자리표시 문구.
# 콘텐츠에 이런 문구가 들어가면 템플릿을 그대로 배포한 것처럼 읽힙니다.
EDITOR_PLACEHOLDERS = [
    "추가 예정",
    "이 영역에",
    "등록할 수 있습니다",
    "준비된 영역",
    "업데이트 가능",
    "추후 등록",
    "TODO",
    "Lorem ipsum",
    # 아래는 실제로 새어 나간 적이 있는 표현입니다.
    "확정된 항목부터",   # "접속 URL은 확정된 항목부터 등록합니다" - 편집자 지시문
    "연결 가능",         # "향후 산출물 링크 연결 가능" - 실적이 아닌 추측
    "축적 가능",         # "케이스 기반 자료 축적 가능"
    "이관 출처",         # 이전 저장소 이름은 유지보수 기록이지 방문자용이 아닙니다.
]

failures: list[str] = []
warnings: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def read(path: str) -> str:
    with open(path, encoding="utf-8", errors="ignore") as f:
        return f.read()


def pages() -> list[str]:
    return sorted(glob.glob(os.path.join(SITE, "**", "*.html"), recursive=True))


# ---------------------------------------------------------------- 1. 빌드 존재
def check_build() -> bool:
    if not os.path.isdir(SITE):
        fail("_site 가 없습니다. 먼저 `bundle exec jekyll build` 를 실행하세요.")
        return False
    if not pages():
        fail("_site 에 HTML 이 없습니다. 빌드가 실패했는지 확인하세요.")
        return False
    return True


# ------------------------------------------------------------- 2. 내부 링크
def check_links() -> None:
    for p in pages():
        rel = p[len(SITE) :]
        for m in re.finditer(r'(?:href|src)="(/[^"#?]*)"', read(p)):
            url = urllib.parse.unquote(m.group(1))
            if BASEURL:
                # baseurl 이 있는데 접두어가 없으면 relative_url 을 빼먹은 것.
                # 루트 도메인에서는 우연히 동작하고 프로젝트 페이지에서만 깨집니다.
                if url == BASEURL or url.startswith(BASEURL + "/"):
                    url = url[len(BASEURL) :] or "/"
                else:
                    fail(f"baseurl 접두어 없는 절대 경로: {url}  (출처 {rel}, relative_url 누락)")
                    continue
            target = os.path.join(SITE, url.lstrip("/"))
            if url.endswith("/"):
                target = os.path.join(target, "index.html")
            if not os.path.exists(target):
                fail(f"깨진 내부 링크: {url}  (출처 {rel})")


# ------------------------------------------------- 3. 구조 / 접근성 기본기
def check_structure() -> None:
    for p in pages():
        rel = p[len(SITE) :]
        s = read(p)

        levels = [int(m.group(1)) for m in re.finditer(r"<h([1-6])[ >]", s)]
        if levels.count(1) != 1:
            fail(f"h1 이 {levels.count(1)}개: {rel}  (페이지마다 정확히 하나)")
        for i in range(1, len(levels)):
            if levels[i] - levels[i - 1] > 1:
                fail(f"헤딩 단계 건너뜀 h{levels[i-1]}->h{levels[i]}: {rel}")

        if "skip-link" not in s:
            fail(f"건너뛰기 링크 없음: {rel}  (WCAG 2.4.1)")
        if 'id="main"' not in s:
            fail(f"본문 앵커(#main) 없음: {rel}")
        if 'lang="' not in s:
            fail(f"lang 속성 없음: {rel}")

        for m in re.finditer(r"<img\b[^>]*>", s):
            if "alt=" not in m.group(0):
                fail(f"alt 없는 이미지: {rel}  {m.group(0)[:70]}")

        if re.search(r"<p>\s*</p>|<dd>\s*</dd>|<h[1-6]>\s*</h[1-6]>", s):
            fail(f"빈 요소가 렌더됨: {rel}  (front matter 필드가 비었는지 확인)")


# ----------------------------------------- 3-1. 페이지별 고유 meta description
def check_meta_descriptions() -> None:
    """같은 설명을 여러 페이지가 쓰면 검색 결과에서 서로 구분되지 않습니다.

    jekyll-seo-tag 는 page.description 이 없으면 site.description 으로 대체하므로,
    front matter 를 빼먹으면 조용히 전 페이지가 같은 문구를 갖게 됩니다.
    _people 과 _project_pages 는 `description:` 필드가 본문 리드와 SEO 설명을
    겸합니다. 이름을 `summary:` 로 되돌리면 이 검사가 잡습니다.
    """
    seen: dict[str, list[str]] = {}
    for p in pages():
        rel = p[len(SITE) :]
        if rel.endswith("404.html"):
            continue
        m = re.search(r'<meta name="description" content="(.*?)"', read(p), re.S)
        if not m:
            fail(f"meta description 없음: {rel}")
            continue
        seen.setdefault(m.group(1).strip(), []).append(rel)

    for desc, urls in seen.items():
        if len(urls) > 1:
            fail(
                f"meta description 중복 ({len(urls)}개 페이지): "
                f'"{desc[:40]}..."  {", ".join(urls[:3])}'
                + (" 외" if len(urls) > 3 else "")
            )


# ------------------------------------------- 4. 편집자용 문구가 새어 나갔는지
def check_editor_placeholders() -> None:
    for p in pages():
        rel = p[len(SITE) :]
        # 운영 가이드 성격의 글은 예외로 둡니다.
        if "posting-guide" in rel:
            continue
        s = read(p)
        for needle in EDITOR_PLACEHOLDERS:
            if needle in s:
                fail(f'편집자용 문구가 방문자에게 노출: "{needle}"  ({rel})')


# --------------------------------------------------- 5. 업로드 자산 고아 검사
def check_orphan_assets() -> None:
    used: set[str] = set()
    scan = pages() + glob.glob(os.path.join(SITE, "assets", "css", "*.css"))
    for p in scan:
        for m in re.finditer(r"/assets/uploads/[^\"')\s]+", read(p)):
            used.add(urllib.parse.unquote(m.group(0)))

    for p in glob.glob(os.path.join(SITE, "assets", "uploads", "**", "*"), recursive=True):
        if not os.path.isfile(p) or p.endswith(".gitkeep"):
            continue
        url = "/" + os.path.relpath(p, SITE)
        if url not in used:
            warn(f"업로드했지만 아무 데서도 참조하지 않는 파일: {url}")


# ------------------------------- 6. researchers.yml 과 _people 정합성
def check_researcher_consistency() -> None:
    yml = os.path.join(ROOT, "_data", "researchers.yml")
    if not os.path.exists(yml):
        fail("_data/researchers.yml 이 없습니다.")
        return

    text = read(yml)
    if "alumni:" not in text:
        fail("_data/researchers.yml 에 alumni: 섹션이 없습니다.")
        return
    current_block, alumni_block = text.split("alumni:", 1)

    entry = re.compile(r"- name:\s*(\S+)\s*\n\s+slug:\s*(\S+)\s*\n\s+generation:\s*(\d+)")

    def parse(block: str, label: str) -> dict[str, str]:
        """slug -> (name, generation). 같은 slug 가 두 번 나오면 잡습니다.

        명단은 1기까지 거슬러 채우는 중이라 계속 길어집니다. slug 가 겹치면
        두 사람이 같은 상세 페이지 URL 을 갖게 되는데, dict 로 뭉개지면
        조용히 한 명이 사라집니다.
        """
        out = {}
        for m in entry.finditer(block):
            name, slug, gen = m.group(1), m.group(2), m.group(3)
            if slug in out:
                fail(f"researchers.yml {label}: slug '{slug}' 가 중복입니다 ({out[slug][0]}, {name})")
            out[slug] = (name, gen)
        return out

    current, alumni = parse(current_block, "current"), parse(alumni_block, "alumni")

    overlap = set(current) & set(alumni)
    for slug in sorted(overlap):
        fail(f"researchers.yml: slug '{slug}' 가 current 와 alumni 에 모두 있습니다.")

    # 기수는 센터 첫 기수 이상이어야 합니다. site.yml 의 first_generation 이 기준입니다.
    site_yml = os.path.join(ROOT, "_data", "site.yml")
    first_gen = None
    if os.path.exists(site_yml):
        m = re.search(r"^\s+first_generation:\s*(\d+)", read(site_yml), re.M)
        if m:
            first_gen = int(m.group(1))
    if first_gen is None:
        fail("_data/site.yml 에 center.first_generation 이 없습니다. 홈 문구가 기수 범위를 이 값에서 읽습니다.")
    else:
        for label, group in (("current", current), ("alumni", alumni)):
            for slug, (name, gen) in group.items():
                if int(gen) < first_gen:
                    fail(
                        f"researchers.yml {label}: {name}({slug}) 의 기수 {gen} 가 "
                        f"센터 첫 기수 {first_gen} 보다 앞섭니다."
                    )

    for path in sorted(glob.glob(os.path.join(ROOT, "_people", "*.md"))):
        s = read(path)
        base = os.path.basename(path)

        def field(key: str) -> str | None:
            m = re.search(rf"^{key}:\s*(.+)$", s, re.M)
            return m.group(1).strip() if m else None

        slug, gen, status = field("slug"), field("generation"), field("status")
        if not field("title"):
            fail(f"{base}: title 이 없습니다. 없으면 브라우저 탭 제목이 영문 슬러그로 나옵니다.")
        if slug is None:
            fail(f"{base}: slug 이 없습니다.")
            continue

        if slug in current:
            want_gen, want_status = current[slug][1], "현재 연구원"
        elif slug in alumni:
            want_gen, want_status = alumni[slug][1], "졸업 및 진출 연구원"
        else:
            fail(f"{base}: slug '{slug}' 가 researchers.yml 에 없습니다. 목록에서 상세로 연결되지 않습니다.")
            continue

        if gen != want_gen:
            fail(f"{base}: 기수 불일치 (_people {gen} vs researchers.yml {want_gen})")
        if status != want_status:
            fail(f'{base}: 구분 불일치 (_people "{status}" vs researchers.yml 기준 "{want_status}")')


# ------------------------------------- 7. 프로젝트 front matter 필수 필드
def check_projects() -> None:
    for path in sorted(glob.glob(os.path.join(ROOT, "_project_pages", "*.md"))):
        s = read(path)
        base = os.path.basename(path)
        if s.count("\n---") < 1 or not s.startswith("---"):
            fail(f"{base}: front matter 구분자가 잘못됐습니다. `---` 로 시작하고 `---` 로 닫아야 합니다.")
        for key in ("title", "date", "slug", "status", "description", "overview"):
            if not re.search(rf"^{key}:\s*\S", s, re.M):
                fail(f"{base}: 필수 필드 '{key}' 가 없습니다.")
        # cover_image 존재 확인은 check_attachments() 가 front matter 기준으로 처리합니다.


# -------------------------------------------------- 8. 첨부파일 실제 존재
def front_matter(text: str) -> str:
    """front matter 만 잘라 냅니다. 본문 코드 블록의 예시 경로를 실제 설정으로
    오인하지 않기 위해 필요합니다."""
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return text[3:end] if end != -1 else ""


def check_attachments() -> None:
    targets = sorted(
        glob.glob(os.path.join(ROOT, "_blog", "*.md"))
        + glob.glob(os.path.join(ROOT, "_news", "*.md"))
        + glob.glob(os.path.join(ROOT, "_project_pages", "*.md"))
    )
    for path in targets:
        fm = front_matter(read(path))
        base = os.path.basename(path)
        for m in re.finditer(r"^\s+url:\s*(/\S+)", fm, re.M):
            target = os.path.join(ROOT, urllib.parse.unquote(m.group(1)).lstrip("/"))
            if not os.path.exists(target):
                fail(f"{base}: 첨부파일이 없습니다 -> {m.group(1)}")
        m = re.search(r"^cover_image:\s*(\S+)", fm, re.M)
        if m:
            target = os.path.join(ROOT, m.group(1).lstrip("/"))
            if not os.path.exists(target):
                fail(f"{base}: cover_image 파일이 없습니다 -> {m.group(1)}")


# ------------------------------------------------------- 9. 배포 설정 점검
def check_config() -> None:
    cfg = read(os.path.join(ROOT, "_config.yml"))
    if not re.search(r'^url:\s*"?https://', cfg, re.M):
        fail("_config.yml 의 url 이 비어 있습니다. canonical 과 og:url 이 '/' 로 깨집니다.")
    if not re.search(r"^email:", cfg, re.M):
        warn("_config.yml 에 email 이 없습니다. 푸터 연락처가 사라집니다.")
    for p in pages():
        s = read(p)
        if "og:image" not in s:
            warn(f"og:image 없음: {p[len(SITE):]}  (링크 공유 미리보기가 비어 보입니다)")
            break


def main() -> int:
    if not check_build():
        print("\n".join("  실패  " + f for f in failures))
        return 1

    check_links()
    check_structure()
    check_meta_descriptions()
    check_editor_placeholders()
    check_orphan_assets()
    check_researcher_consistency()
    check_projects()
    check_attachments()
    check_config()

    print(f"검사 대상: {len(pages())} 페이지")
    if warnings:
        print(f"\n경고 {len(warnings)}건 (배포를 막지는 않습니다)")
        for w in warnings:
            print("  경고  " + w)
    if failures:
        print(f"\n실패 {len(failures)}건")
        for f in failures:
            print("  실패  " + f)
        print("\n배포하지 마세요. 위 항목을 고친 뒤 다시 실행하세요.")
        return 1

    print("\n실패 0건. 배포 가능합니다.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
