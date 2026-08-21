# SCH사이버보안연구센터 사이트 유지보수 가이드라인

콘텐츠 운영은 [QUICK_START_FOR_RESEARCHERS.md](QUICK_START_FOR_RESEARCHERS.md)를 먼저 보세요. 이 문서는 **구조를 바꾸거나 디자인을 손볼 때** 지켜야 할 것을 다룹니다.

- 시각 시스템의 토큰·금지 사항: [DESIGN.md](DESIGN.md)
- 제품 맥락(사용자, 목적, 제약, 발명 금지 사항): [PRODUCT.md](PRODUCT.md)

---

## 1. 기본 원칙

1. **내용이 없으면 필드를 지운다.** "추가 예정", "이 영역에 등록할 수 있습니다" 같은 편집자용 문구를 채우지 않습니다. 레이아웃이 빈 영역을 알아서 생략합니다. `tools/verify.py` 가 이 문구를 배포 차단 사유로 잡습니다.
2. **없는 실적을 만들지 않는다.** 논문 목록, 수치 벤치마크, 추천사, 예산 규모는 이 센터에 없는 자료입니다. PRODUCT.md 의 "없는 것" 목록을 확인하세요.
3. **한 가지를 한 번만 말한다.** 제목이 이미 설명한 것을 리드 문단이 되풀이하면 리드를 지웁니다.
4. **정보 원본은 한 곳에만 둔다.** 프로젝트는 `_project_pages/*.md` 하나가 원본입니다. 같은 내용을 데이터 파일에 또 적지 않습니다.
5. **올리기 전에 `tools/verify.py` 를 돌린다.** 통과하지 않으면 배포하지 않습니다.

---

## 2. 파일 구조

```
_config.yml              사이트 설정 (url, email, 컬렉션, defaults)
_data/
  researchers.yml        연구원 명단 (current / alumni)
  history.yml            연혁
  infrastructure.yml     인프라 항목
  site.yml               연구 분야 3종
_news/                   센터 소식
_blog/                   센터 블로그 (반기 보고서 포함)
_project_pages/          프로젝트 (목록 + 상세의 유일한 원본)
_people/                 연구원 상세 페이지
_layouts/                default / post / project / researcher
_includes/
  project-row.html       프로젝트 목록 행 (홈과 /projects/ 가 공유)
assets/
  css/style.scss         전체 스타일
  js/site.js             모바일 메뉴 + 스크롤 상태
  branding/              로고, OG 이미지
  uploads/               게시물 이미지·첨부·프로젝트·연혁·히어로
tools/verify.py          릴리스 전 검사기
404.html                 이전 사이트 링크로 들어온 방문자 안내
```

컬렉션과 URL 규칙은 `_config.yml` 의 `collections` 에 있습니다.

| 컬렉션 | URL | 레이아웃 |
|---|---|---|
| `news` | `/news/:name/` | `post` |
| `blog` | `/blog/:name/` | `post` |
| `project_pages` | `/projects/:name/` | `project` |
| `people` | `/researchers/:name/` | `researcher` |

`defaults` 가 `section_path` 를 넣어 주어 내비게이션의 현재 위치 표시가 동작합니다. 새 컬렉션을 만들면 `section_path` 도 같이 넣으세요.

---

## 3. 데이터 파일 스펙

### `_data/researchers.yml`

```yml
current:
  - name: 이름          # 필수
    slug: slug          # 필수. _people/<slug>.md 와 일치
    generation: 27      # 필수
    role: 연구원
    focus: 한 문장       # 선택. 태그와 같은 말이면 넣지 않습니다
    tags: [악성코드 분석]

alumni:
  - name: 이름
    slug: slug
    generation: 22
    outcome: 진로 한 문장   # 기록이 없으면 "-"
```

`slug` 에 대응하는 `_people/<slug>.md` 가 있으면 목록에서 상세 페이지로 링크가 걸리고, 없으면 이름만 텍스트로 나옵니다. 상세 페이지가 없는 연구원을 명단에 올리는 것은 정상입니다.

### `_data/history.yml`

```yml
  - year: 2026
    label: 센터 활동      # 필수. 짧은 분류
    title: 제목           # 필수
    description: 설명     # 필수
    image: /assets/uploads/history/...   # 선택
    image_alt: 사진 설명                  # image 를 넣으면 함께
```

### `_data/infrastructure.yml`

```yml
- title: 항목명
  type: 서버            # 스토리지 / 서버 등
  access: 내부 운영
  summary: 무엇에 쓰는지
  url: ""               # 비어 있으면 "접속 URL은 아직 공개되지 않았습니다"
  notes: 접근 조건       # 선택. 항목마다 다른 내용일 때만
```

`notes` 를 여러 항목에 똑같이 복사하지 않습니다. 같은 문장이 반복되면 지웁니다.

### `_data/site.yml`

연구 분야 3종입니다. 추상적인 목표 문장 대신 **구체적인 사실**을 씁니다.

```yml
research_areas:
  - title: 분야명
    description: 무엇을 실제로 하는지. 다룬 악성코드 이름, 맺은 협약, 참석한 워크숍 같은 것.
```

> 이전 사이트에는 "취약점 분석"이 세 번째 항목이었습니다. 현재 3종은 이후 발표자료 기준이라 그 항목이 빠져 있습니다. 지금도 수행 중인 분야라면 여기에 추가하세요.

---

## 4. 이미지와 첨부파일

| 종류 | 위치 | 비고 |
|---|---|---|
| 게시물 이미지 | `assets/uploads/posts/<연도-주제>/` | |
| 첨부 문서 | `assets/uploads/files/<연도-주제>/` | |
| 프로젝트 대표 이미지 | `assets/uploads/projects/` | 16:10 로 잘립니다 |
| 연혁 사진 | `assets/uploads/history/` | 200px 폭으로 표시 |
| 히어로 배경 | `assets/uploads/hero/` | 아래 5절 참조 |
| 로고·OG | `assets/branding/` | |

규칙:

- 파일명은 **영문·숫자·하이픈**만. macOS 시스템 Ruby(2.6)는 한글 파일명이 있으면 빌드 중 `Encoding::UndefinedConversionError` 로 죽습니다.
- 헤더 로고는 `center-logo-96.png`(9KB)를 씁니다. 원본 `center-logo.png`(96KB)는 OG·대형 표시용입니다. 헤더에서 원본을 쓰면 페이지 무게의 절반 이상을 로고가 차지합니다.
- 업로드해 놓고 아무 데서도 참조하지 않는 파일은 `verify.py` 가 경고합니다.

---

## 5. 히어로 배경을 교체할 때

첫 화면 배경은 `assets/uploads/hero/center-hero.jpg`(2400px)와 `center-hero-1200.jpg`(좁은 화면용)입니다. 두 판을 함께 교체하세요(`sips -Z 2400` / `sips -Z 1200`).

**교체하면 대비를 다시 계산해야 합니다.** 글자는 이미지 위 스크림(`.hero::before`) 위에 놓입니다. 현재 스크림은 텍스트 구간(좌측 56%)에서 0.93 이상을 유지하고, 그 기준에서 이미지가 최악의 경우(흰 픽셀)여도 다음이 성립합니다.

| 요소 | 대비 |
|---|---|
| 흰 제목 | 16:1 |
| `ink-2` 리드 문단 | 13:1 |
| `muted` 라벨 | 7:1 |
| `accent` 영문 라인 | 4.7:1 |

스크림을 0.90 으로 낮추면 `accent` 가 4.0:1 로 **AA 미달**입니다. 밝은 이미지로 바꿀 때는 스크림을 더 올리세요. 계산 근거는 DESIGN.md 의 "히어로 이미지" 절에 있습니다.

교체 원칙: 센터가 직접 만든 이미지(분석 화면, 행사 사진, 장비 사진)로 바꿉니다. 범용 스톡 사진으로 바꾸지 않습니다.

---

## 6. 디자인을 수정할 때

전체 원칙은 DESIGN.md 에 있습니다. 특히 다음은 **의식적으로 금지**한 것이라 되살리지 마세요.

- 가짜 코드 배경, 매트릭스 레인, 네온 글로우, 방패·자물쇠 아이콘
- 그라데이션 버튼·그라데이션 텍스트
- 두 번째 강조색
- 제목 위 kicker/eyebrow, 섹션 번호(01/02/03), 큰 숫자 지표 타일
- 아이콘+제목+문단이 같은 크기로 반복되는 카드 격자 (이미지를 뺀 텍스트 카드 격자도 같은 함정 → 하한선 목록으로)
- 모노스페이스를 "기술적 분위기"로 사용 (데이터·코드·계측에만)

기술적 함정 여섯 가지:

1. **`.site-shell` 과 같은 요소에 `padding` 축약형을 쓰지 않습니다.** 좌우 여백이 덮여서 그 섹션만 화면 끝에 붙습니다. `padding-block` 을 쓰세요.
2. **sticky 헤더의 높이·폭을 트랜지션하지 않습니다.** 헤더가 문서 흐름에 있어 매 프레임 전체 리플로우가 납니다. `transform` 과 `box-shadow` 만 씁니다.
3. **`requestAnimationFrame` 안에 상태 플래그를 두지 않습니다.** 탭이 백그라운드면 rAF 가 멈춰 플래그가 걸리고 상태가 영구히 정지합니다.
4. **측정폭에 `ch` 를 쓰지 않습니다.** `ch` 는 "0" 글자 너비 기준이라 전각인 한글에서 의도보다 훨씬 넓어집니다. `68ch` 가 실측 47자였습니다. `rem` 으로 고정하세요 — 값은 DESIGN.md 의 표에 있습니다.
5. **`td` 의 `max-width` 는 무시됩니다.** `table-layout: auto` 에서는 적용되지 않으니 표 전체 폭을 제한하세요.
6. **한글에 12px 미만을 쓰지 않습니다.** 라틴 전용 표기만 예외입니다.

색을 추가하면 `DESIGN.md` 의 `colors` 에도 등록하세요. 등록하지 않은 색은 Impeccable 검출기가 잡습니다.

```bash
node ~/.claude/skills/impeccable/scripts/detect.mjs --json assets/css/style.scss _site
```

---

## 7. 모션

세 층으로만 구성되어 있습니다. 자세한 내용은 DESIGN.md.

1. 첫 화면 정착 시퀀스 (약 1.8초, CSS 애니메이션)
2. 스크롤 지속 상태 — 헤더 압축, 히어로 시차 (`site.js`)
3. 목록 행 착지 — `animation-timeline: view()` 스크롤 구동 CSS

**섹션마다 같은 등장 효과를 추가하지 마세요.** 그리고 행 등장을 IntersectionObserver 로 바꾸지 마세요. 빠르게 스크롤하면 콜백 전에 행이 화면을 지나가 `opacity: 0` 으로 영구히 남습니다(실측: 맨 아래로 점프 시 24행 중 18행이 사라졌습니다).

`prefers-reduced-motion` 에서는 **등장 연출만** 끕니다. hover·focus 전환까지 끄면 무엇이 반응했는지 알 수 없게 됩니다.

---

## 8. 로컬 테스트

```bash
bundle install
LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 RUBYOPT="-E utf-8" bundle exec jekyll serve
```

빌드만 확인:

```bash
LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 RUBYOPT="-E utf-8" bundle exec jekyll build
```

로케일 지정은 저장소에 한글 경로가 남아 있을 때 필요합니다. 시스템 Ruby 2.6 기준입니다.

---

## 9. 릴리스 전 확인 순서

```bash
# 1. 빌드
LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 RUBYOPT="-E utf-8" bundle exec jekyll build

# 2. 자동 검사 (실패 0건이어야 합니다)
python3 tools/verify.py

# 3. 눈으로 확인
#    데스크톱 1280 이상 / 모바일 390 두 폭에서
```

`verify.py` 가 자동으로 잡는 것:

- 깨진 내부 링크, 존재하지 않는 첨부·이미지
- `h1` 개수, 헤딩 단계 건너뜀, `alt` 누락, `lang` 누락, 건너뛰기 링크 누락
- 빈 요소가 렌더되는 경우 (front matter 필드가 비었을 때)
- 편집자용 자리표시 문구 노출
- `researchers.yml` ↔ `_people` 기수·구분 불일치
- 프로젝트 필수 필드 누락, front matter 구분자 오류
- `_config.yml` 의 `url` 누락 (canonical·og:url 이 깨집니다)

**측정으로 확인한 것** (재현 방법은 DESIGN.md):

- 국문 본문 측정폭 전 항목 35~45자
- 전 페이지 대비 위반 0건, 24px 미달 클릭 영역 0건
- 모바일 390px 가로 넘침 0건, 본문 표 전 셀 한 줄

**사람이 봐야 하는 것** (자동화하지 않았습니다):

- 첫 화면에서 최신 보고서와 최근 소식이 스크롤 없이 읽히는지
- 모집 공고 마감 여부와 주 버튼 문구가 맞는지
- 새로 쓴 문장에 사실 오류가 없는지 (악성코드 이름, 분석가, 기수, 진로)
- 모바일에서 메뉴 토글, 표 가로 스크롤, 히어로 여백
- 민감 정보·개인정보·내부 계정 정보가 없는지

---

## 10. 배포

GitHub Pages 가 `main` 브랜치에서 빌드합니다.

- `_config.yml` 의 `url` 은 `https://schcrc.github.io` 입니다. 도메인이 바뀌면 여기도 바꿉니다. 비워 두면 `canonical` 과 `og:url` 이 `/` 로 깨집니다.
- `og:image` 는 `_config.yml` 의 `defaults` 에서 전 페이지에 내려줍니다. `logo` 는 JSON-LD 용입니다.
- `_site/` 는 빌드 산출물이라 커밋 대상이 아닙니다. `.gitignore` 에 있지만 과거에 커밋된 이력이 있어 `git rm -r --cached _site` 로 정리해야 완전히 빠집니다.
- 배포는 `.github/workflows/jekyll.yml` 이 처리합니다(Ruby 3.1, Actions 기반). 빌드 직후 `tools/verify.py` 가 실행되고 실패하면 배포되지 않습니다.
- 피드는 `_config.yml` 의 `feed.collections` 로 `/feed/blog.xml`, `/feed/news.xml` 을 만듭니다. `jekyll-feed` 는 기본으로 `site.posts` 만 보므로 이 설정이 없으면 빈 피드가 나갑니다. 컬렉션을 추가하면 여기도 추가하세요.
- **사이트맵은 아직 없습니다.** `jekyll-sitemap` gem 을 추가하면 됩니다(`Gemfile` + `_config.yml` plugins). 다만 `Gemfile.lock` 이 Bundler 1.17 로 생성돼 있어, gem 을 추가할 때는 로컬에서 `bundle install` 로 lock 을 갱신한 뒤 함께 커밋하세요.
- CSS 안의 이미지 경로는 `relative_url` 을 씁니다. 절대경로로 적으면 프로젝트 페이지(baseurl 이 있는 경우)로 배포할 때 히어로 배경이 깨집니다.

### 이전 사이트 URL

이전 사이트는 별도 도메인(`schcsrc.github.io`)이라 여기서 301 리다이렉트를 걸 수 없습니다. 이전 저장소를 유지하면 기존 링크가 살아 있고, 내리면 아래 형태의 링크가 끊깁니다.

```
https://schcsrc.github.io/report/Post/2022/06/13/2022-상반기-분석-보고서/
```

`404.html` 이 이전 사이트에서 온 방문자를 블로그·프로젝트로 안내합니다.

---

## 11. 빠른 참고

| 수정 대상 | 파일 |
|---|---|
| 메인 화면 구성 | `index.md` |
| 소식 추가 | `_news/` |
| 블로그·보고서 추가 | `_blog/` |
| 프로젝트 추가 | `_project_pages/` |
| 프로젝트 목록 행 모양 | `_includes/project-row.html` |
| 연구원 명단 | `_data/researchers.yml` |
| 연구원 상세 | `_people/` |
| 연혁 | `_data/history.yml` |
| 인프라 URL | `_data/infrastructure.yml` |
| 연구 분야 문구 | `_data/site.yml` |
| 헤더·푸터·메타 | `_layouts/default.html` |
| 스타일 | `assets/css/style.scss` |
| 스크립트 | `assets/js/site.js` |
| 로고 교체 | `assets/branding/` |
| 디자인 원칙 | `DESIGN.md` |
| 제품 맥락 | `PRODUCT.md` |
| 릴리스 검사 | `tools/verify.py` |
