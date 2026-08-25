# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

- **외부 방문자 (1차)**: 순천향대학교 정보보호학과 학부생·수험생, 타 기관 연구자, 협력 기관 담당자. 센터가 무엇을 연구하고 어떤 성과를 냈는지 짧은 시간에 판단하려는 상황. 신입 연구원 모집 시기에는 "여기 지원할 만한가"를 확인하는 것이 핵심 작업.
- **센터 소속 연구원 (2차)**: 공지·모집 안내 확인, 분석 보고서 및 프로젝트 기록 열람, 센터 인프라(NAS, 분석 서버, Wiki) 진입점 사용.
- **운영 담당 연구원 (3차)**: Markdown/YAML만 수정해 소식·블로그·프로젝트·연구원 현황을 갱신하는 역할. 디자인 파일을 만지지 않고 콘텐츠만 추가할 수 있어야 한다.

## Product Purpose

순천향대학교 SCH사이버보안연구센터의 공식 웹사이트. 센터의 연구 방향, 활동 기록, 산출물, 연구원 진로 성과를 공개적으로 축적하고, 신입 연구원 모집과 기관 협력의 근거 자료로 쓰인다. 성공은 "센터의 실제 역량이 문서로 증명되는 것" — 즉 보고서·프로젝트·성과가 계속 쌓이고 외부에서 그것을 확인할 수 있는 상태다.

## Positioning

학생 연구센터이면서 실제 악성코드 분석 보고서를 반기 단위로 발간하고, 배출 연구원의 진로(S2W, AhnLab ASEC, 고려대 정보보호대학원, BoB 등)를 실명으로 공개한다. 홍보 문구가 아니라 축적된 산출물과 진로 기록이 증거다.

## Operating Context

- Jekyll 4.3 정적 사이트, GitHub Pages(`SCHCRC/schcrc.github.io`)로 배포.
- 콘텐츠 저작 = `_news/`, `_blog/`, `_project_pages/` Markdown + `_data/*.yml`.
- 첨부물은 저장소 내부 정적 파일(`assets/uploads/`) 기준으로 운영. 외부 링크는 장기 안정성이 낮아 지양.
- 이전 사이트 `SCHCsRC.github.io`(Bootstrap 원페이지 템플릿)의 콘텐츠를 이전 중.
- 로컬 확인은 `bundle exec jekyll build` / `jekyll serve`.

## Capabilities and Constraints

- 컬렉션: `news`(센터 소식), `blog`(센터 블로그), `people`(연구원 상세), `project_pages`(프로젝트 상세).
- 데이터 파일: `researchers.yml`, `history.yml`, `infrastructure.yml`, `site.yml`. 프로젝트는 `_project_pages/*.md` 가 유일한 원본이며 별도 데이터 파일을 두지 않는다.
- 게시글 front matter 지원: `cover_image`, `cover_image_alt`, `cover_image_caption`, `attachments[]`(label/url/description/download).
- 플러그인은 GitHub Pages 호환 범위(`jekyll-feed`, `jekyll-seo-tag`, `jekyll-sitemap`)로 제한. 커스텀 Ruby 플러그인 불가.
- 빌드 툴체인 없음(번들러/PostCSS 없음). SCSS는 Jekyll 내장 sass-embedded로만 컴파일.
- 언어는 한국어 단일(`ko-KR`). i18n 요구 없음.
- 인프라 페이지의 실제 URL은 아직 비어 있음(`url: ""`). 접근 권한은 각 서비스가 처리한다는 전제.

## Brand Commitments

- 정식 명칭: `SCH사이버보안연구센터` / 영문 `SCH Cybersecurity Research Center`.
- 기존 자산: `assets/branding/center-logo.png`, `assets/branding/logo.png`, `assets/favicon/`.
- 소속 표기: 순천향대학교 산학협력단 산하, 공과대학 9332호. 센터장 순천향대학교 정보보호학과 염흥열 교수.
- 주소: [31538] 충남 아산시 순천향로 22-3 공과대학 9332 (이전 사이트 기재값).
- 톤: 기관·학술 신뢰형. 절제되고 정확한 어조. 과장된 마케팅 문구 금지.
- **시각 방향 (2026-08-21 확정, 지속 선호)**: 다크 기술 지면. 네이비 계열 근검정 + 로고 크림슨 하나 + 실제 데이터에만 모노스페이스. 비유적 세계관이나 아이러니는 쓰지 않는다.
  최초에 "카테고리 표준 / 기관·학술 신뢰형"을 선택받아 라이트 그라운드로 해석했으나 네 차례 부정 판정을 받았다. 세 후보(원래 다크 / 이전 블로그 / 라이트)를 나란히 띄워 확인한 결과 **다크 방향**이 기준이다. 자세한 경위와 금지 사항은 DESIGN.md 참조.
- **동시에 금지**: 이전 버전이 쓰던 가짜 코드 레인 배경, 보라 그라데이션 버튼, 네온 글로우, Audiowide 로고체. 다크를 쓴다는 것이 이 클리셰를 허가하는 것은 아니다.

## Evidence on Hand

- 반기 악성코드 분석 보고서 PDF 3종: `assets/uploads/files/old-reports/` (2022 상반기/하반기, 2023 상반기).
- 이전 사이트 프로젝트 이미지 13종: `old-site/img/portfolio/`.
- 연구원 진로 실적: `_data/researchers.yml` alumni 항목(실명 + 진출처).
- 연혁 8건: `_data/history.yml` (2013 설립 ~ 2026 26기 모집).
- 협약/행사: 누리랩 MOU, 제9회 KISTI-NICT 국제 공동 워크숍.
- **없는 것 — 만들어내지 말 것**: 논문 목록, 수치화된 벤치마크, 외부 인용/추천사, 예산·과제 수주 규모, 재학생 수, 실제 인프라 URL.

## Product Principles

1. **산출물이 주인공.** 보고서·프로젝트·진로 기록이 첫 화면에서부터 증거로 읽혀야 한다.
2. **모집을 상시 고려한다.** 학부생 지원자가 "무엇을 배우고 어디로 가는가"를 3분 안에 파악할 수 있어야 한다.
3. **Markdown만으로 운영된다.** 새 글·새 프로젝트 추가가 템플릿 수정 없이 끝나야 한다.
4. **과장하지 않는다.** 없는 실적을 시각적 장식으로 대체하지 않는다.
5. **기록은 사라지지 않는다.** 이전 사이트의 글·프로젝트·첨부물은 링크가 끊기지 않게 옮긴다.

## Accessibility & Inclusion

한국어 본문 기준 가독성 우선. 공공·대학 기관 사이트 성격상 키보드 접근과 명도 대비를 기본으로 만족해야 한다. 모션은 `prefers-reduced-motion` 존중(현재 `site.js`가 이미 처리).
