#!/usr/bin/env python3
"""
릴리스 전 사이트 검사기.

의존성 없음 (python3 표준 라이브러리만). 먼저 사이트를 빌드한 뒤 실행합니다.

    bundle exec jekyll build
    python3 tools/verify.py

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

    def parse(block: str) -> dict[str, str]:
        out = {}
        for m in re.finditer(r"- name:\s*(\S+)\s*\n\s+slug:\s*(\S+)\s*\n\s+generation:\s*(\d+)", block):
            out[m.group(2)] = (m.group(1), m.group(3))
        return out

    current, alumni = parse(current_block), parse(alumni_block)

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
        for key in ("title", "date", "slug", "status", "summary", "overview"):
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
