# SCH사이버보안연구센터 GitHub Pages 사이트

발표자료 기반으로 제작한 `github.io` 운영용 정적 사이트입니다.  
GitHub Pages에서 바로 쓰기 쉽도록 **Jekyll + Markdown** 구조로 구성했습니다.

실제 운영 중인 [schcsrc.github.io](https://schcsrc.github.io/)의 파비콘과 소개 문구 톤을 참고해, 현재 사이트에도 `SCH Cybersecurity Research Center` 표기와 핵심 방향성을 반영했습니다.

추가 유지보수 문서는 [UPDATE_GUIDELINES.md](UPDATE_GUIDELINES.md)에 정리되어 있습니다.
빠르게 수정할 때 보는 짧은 운영 문서는 [QUICK_START_FOR_RESEARCHERS.md](QUICK_START_FOR_RESEARCHERS.md)에 정리되어 있습니다.

## 현재 사이트 구조 요약

- 정적 사이트 엔진: Jekyll 4.3 (GitHub Pages 호환 플러그인만: `jekyll-feed`, `jekyll-seo-tag`, `jekyll-sitemap`)
- 콘텐츠: Markdown + YAML 데이터 파일. 빌드 툴체인 없음
- 공통 레이아웃: `_layouts/` (default / post / project / researcher)
- 공통 파셜: `_includes/project-row.html`
- 스타일: `assets/css/style.scss` — 다크 지면, 강조색은 로고 크림슨 하나
- 스크립트: `assets/js/site.js` — 모바일 메뉴 + 스크롤 상태 (2.6KB)
- 릴리스 검사기: `tools/verify.py` (의존성 없음, CI 에서도 실행)
- 피드: `/feed/blog.xml`, `/feed/news.xml` (`jekyll-feed` 의 `feed.collections` 설정)
- 사이트맵: `/sitemap.xml`, `/robots.txt` (`jekyll-sitemap` 이 자동 생성)

문서 세 개가 서로 다른 층을 담당합니다.

| 문서 | 무엇 |
|---|---|
| [QUICK_START_FOR_RESEARCHERS.md](QUICK_START_FOR_RESEARCHERS.md) | 글·프로젝트·연구원 추가하는 방법 |
| [UPDATE_GUIDELINES.md](UPDATE_GUIDELINES.md) | 구조·디자인을 손볼 때의 규칙과 함정 |
| [DESIGN.md](DESIGN.md) | 색·타이포·컴포넌트 토큰과 금지 사항 |
| [PRODUCT.md](PRODUCT.md) | 사용자·목적·제약, 그리고 발명하면 안 되는 것 |

## 포함된 페이지

- 메인 페이지: 센터 소개, 연구 분야, 최근 소식, 최근 블로그 글
- `센터 소식`: 공지, 행사, 모집, 협약 등 공식 뉴스 게시
- `센터 블로그`: 연구 내용, 분석 사례, 기술 글 게시
- `센터 프로젝트`: 수행 중인 프로젝트, 산출물 URL, 관련 연구 링크 정리
- `센터 인프라`: NAS, 서버, 내부 서비스 URL 및 인프라 구성 안내
- `연구원 현황`: 현재 연구원 / 졸업 및 진출 연구원 소개
- `센터 연혁`: 연도별 활동과 성과를 타임라인으로 정리
- `404`: 이전 사이트 링크로 들어온 방문자를 블로그/프로젝트로 안내

## 글 작성 방법

### 1. 센터 소식 작성

`_news` 폴더에 아래 형식의 Markdown 파일을 추가하면 됩니다.

```md
---
title: 새 공지 제목
date: 2026-03-24
author: SCH사이버보안연구센터
category: 공지
---

공지 본문을 작성합니다.
```

### 2. 센터 블로그 작성

`_blog` 폴더에 아래 형식의 Markdown 파일을 추가하면 됩니다.

```md
---
title: 연구 글 제목
date: 2026-03-24
author: SCH사이버보안연구센터
topic: 악성코드 분석
---

연구 내용을 Markdown으로 작성합니다.
```

## 이미지와 첨부파일 운영 방법

이미지와 외부 첨부파일도 GitHub Pages에서 문제 없이 배포되도록 정적 파일 기준으로 운영하는 방식을 반영했습니다.

### 권장 업로드 위치

- 게시물 이미지: `assets/uploads/posts/연도-주제명/`
- 첨부 문서: `assets/uploads/files/연도-주제명/`

예시:

- `assets/uploads/posts/2026-malware-report/sample-1.png`
- `assets/uploads/files/2026-malware-report/report.pdf`

### 본문 이미지 삽입

Markdown 본문에 아래처럼 루트 기준 경로로 넣으면 됩니다.

```md
![분석 화면](/assets/uploads/posts/2026-malware-report/sample-1.png)
```

### 대표 이미지와 첨부파일 등록

글 상단 front matter에서 아래 속성을 사용할 수 있습니다.

```md
---
title: 악성코드 분석 보고서 공개
date: 2026-03-24
author: SCH사이버보안연구센터
topic: 악성코드 분석
cover_image: /assets/uploads/posts/2026-malware-report/cover.png
cover_image_alt: 분석 대표 이미지
cover_image_caption: 실습 환경에서 확인한 악성 행위 화면
attachments:
  - label: 분석 보고서 PDF
    url: /assets/uploads/files/2026-malware-report/report.pdf
    description: 외부 공개용 요약 보고서입니다.
    download: true
  - label: IoC 목록 CSV
    url: /assets/uploads/files/2026-malware-report/ioc.csv
    description: 침해지표 정리 파일입니다.
    download: true
---
```

### 운영 시 주의사항

- 파일명은 가능하면 영문, 숫자, 하이픈(`-`) 위주로 관리하는 편이 안전합니다.
- 파일 경로에 공백과 특수문자를 많이 넣지 않는 것을 권장합니다.
- 이미지와 PDF는 업로드 전에 용량을 줄여 GitHub 저장소 부담을 낮추는 것이 좋습니다.
- 외부 링크 첨부도 가능하지만, 장기 운영 안정성은 저장소 내부 정적 파일이 가장 좋습니다.
- 게시글 삭제 시 연결된 이미지와 첨부파일도 함께 정리하면 관리가 쉬워집니다.

## 연구원 현황 수정

`_data/researchers.yml` 파일을 수정하면 됩니다.

- `current`: 현재 연구원
- `alumni`: 졸업 및 진학/취업 연구원

## 연혁 수정

`_data/history.yml` 파일을 수정하면 됩니다.

## 프로젝트 추가 및 수정

프로젝트는 `_project_pages/` 폴더의 Markdown 파일 **하나**가 원본입니다. 별도 데이터 파일은 없습니다.
(이전에 있던 `_data/projects.yml`은 같은 내용을 두 곳에 적어야 해서 삭제했습니다.)

```md
---
title: 프로젝트 제목
date: 2026-03-01          # 목록 정렬 기준. 최신순으로 표시됩니다.
slug: project-slug        # URL: /projects/project-slug/
status: 진행 중            # 배지로 표시됩니다.
period: 2026
owner: 담당 연구원
summary: 목록 카드에 나오는 한두 문장 요약입니다.
overview: 상세 페이지 개요 문단입니다.
cover_image: /assets/uploads/projects/project-slug.png
cover_image_alt: 대표 이미지 설명
topics:
  - 주제1
  - 주제2
highlights:
  - 사이드바 요약 포인트
outputs:                  # 없으면 생략하세요. 빈 상태 문구가 자동 표시됩니다.
  - type: 보고서
    title: 산출물 제목
    description: 설명
    url: https://example.com
archived_from: SCHCsRC.github.io   # 이전 사이트에서 이관한 경우만
---
```

- `cover_image`가 없으면 목록 카드에 "대표 이미지 준비 중"이 표시됩니다.
- 메인 화면의 프로젝트 격자에는 대표 이미지가 있는 프로젝트만 최신 6건이 노출됩니다. 전체 목록은 `/projects/`에서 볼 수 있습니다.
- `activities`, `outputs`, `topics`, `highlights`는 비어 있으면 해당 섹션이 아예 출력되지 않거나 빈 상태 문구로 대체됩니다.

## 인프라 수정

`_data/infrastructure.yml` 파일을 수정하면 됩니다.

인프라 페이지는 외부 방문자에게 센터 인프라 구성을 보여주고, 연구원은 등록된 URL을 통해 필요한 서비스로 바로 이동할 수 있도록 구성되어 있습니다. 실제 접근 권한은 각 서비스 측에서 별도로 처리하는 전제를 두고 있습니다.

## GitHub Pages 배포 방법

1. 이 폴더를 GitHub 저장소에 업로드합니다.
2. 저장소 이름을 `사용자이름.github.io`로 만들면 루트 도메인으로 배포할 수 있습니다.
3. GitHub 저장소의 `Settings > Pages`에서 배포 브랜치를 `main`으로 설정합니다.
4. 몇 분 뒤 `https://사용자이름.github.io`에서 사이트가 열립니다.

## 로컬 미리보기

Ruby와 Bundler가 준비되어 있다면 아래 명령으로 확인할 수 있습니다.

```bash
bundle install
bundle exec jekyll serve
```

macOS 시스템 Ruby(2.6)에서 빌드할 때 한글 파일명이 있으면 `Encoding::UndefinedConversionError`가 날 수 있습니다. 그럴 때는 로케일을 UTF-8로 지정해 실행합니다.

```bash
LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 RUBYOPT="-E utf-8" bundle exec jekyll serve
```

업로드 파일명은 영문·숫자·하이픈으로 관리하는 것이 안전합니다.

빌드만 확인하려면 아래 명령을 사용합니다.

```bash
bundle exec jekyll build
```

## 릴리스 전 확인

```bash
LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 RUBYOPT="-E utf-8" bundle exec jekyll build
python3 tools/verify.py
```

`실패 0건` 이 나와야 배포합니다. 검사기가 잡는 항목과 사람이 직접 봐야 하는 항목은 [UPDATE_GUIDELINES.md 9절](UPDATE_GUIDELINES.md#9-릴리스-전-확인-순서)에 정리되어 있습니다.

## 이번 초안에 반영한 발표자료 기반 내용

- 센터 소개 문구
- 연구 분야 3종
- 누리랩 MOU 체결
- KISTI-NICT 국제 공동 워크숍 참석
- 2024/2025 주요 성과 요약
- 26기 연구원 모집 안내

연구원 현황은 발표자료에서 확인 가능한 인물 중심으로 기본 입력했으며, 실제 운영 전 최신 인원 기준으로 보완하는 것을 권장합니다.

## 이전 사이트(SCHCsRC.github.io) 이관 내역

전수 대조 결과입니다. 바이너리는 SHA-256으로 원본과 비교했습니다.

| 이전 사이트 항목 | 수량 | 이관 결과 |
|---|---|---|
| 반기 분석 보고서 글 | 3 | `_blog/` 3건. 분석 표(악성코드·종류·분석가) 13행 전부 일치 |
| 보고서 PDF | 3 | `assets/uploads/files/old-reports/` — SHA-256 동일 |
| 프로젝트 글 | 7 | `_project_pages/` 7건. 담당 연구원 전부 일치 |
| 프로젝트 대표 이미지 | 7 | `assets/uploads/projects/` — SHA-256 동일 (영문 파일명) |
| 연구원 명단 | 11 | `_data/researchers.yml` alumni — 기수 전부 일치 |
| 연혁 항목 | 4 | `_data/history.yml` (2013·2014·2017·2021) |
| 연혁 사진 | 4 | `assets/uploads/history/` — SHA-256 동일 |
| 히어로 배경 | 1 | `assets/uploads/hero/` — 2400px·1200px로 리사이즈 (2.25MB → 230KB/83KB) |
| OG 이미지 | 1 | `assets/branding/og-image.jpg` — SHA-256 동일 |
| 주소 · 이메일 | — | 푸터 "찾아오는 길" |

### 이관하지 않은 것

- **"취약점 분석"** — 이전 사이트 "주요 활동" 3항목 중 하나였으나, 현재 `_data/site.yml`의 연구 분야 3종(악성코드 분석 / 사이버 범죄 그룹 추적 / 국내외 유관기관 협력)은 이후 발표자료 기준입니다. 지금도 수행 중인 분야라면 `_data/site.yml`에 항목을 추가하면 됩니다.
- `img/portfolio/` 미사용 이미지 6건(`DFCAT`, `DynamicAnalysis`, `darkweb`, `firmware`, `honeypot`, `web`). 이전 사이트에서도 어떤 글에도 연결되어 있지 않았습니다. 해당 프로젝트가 실제로 있었다면 `_project_pages/`에 추가하면서 함께 옮기면 됩니다.
- `img/map-image.png`(위치 지도). 주소를 푸터에 텍스트로 넣었고, 이전 사이트에서도 어떤 섹션에도 연결되어 있지 않았습니다.
- `img/team/1.jpg`. 연구원 7명 전원에게 같은 파일이 쓰인 자리표시 아바타입니다.
- 새로 추가한 연구원 6명(15·16·17·18·21기)의 진로 정보. 이전 사이트에 기록이 없어 비워 뒀습니다.

### 표기 변경 1건

`Cryptbot` → `CryptBot` (2022 하반기 보고서 분석 표). 업계 표준 표기로 맞췄습니다. 원문 유지가 맞다면 `_blog/2022-12-29-second-half-report.md`에서 되돌리면 됩니다.

### 이전 URL

이전 사이트는 별도 도메인(`schcsrc.github.io`)이라 신규 사이트에서 301 리다이렉트를 걸 수 없습니다. 이전 저장소를 그대로 두면 기존 링크는 계속 살아 있고, 내리면 아래 형태의 링크가 끊깁니다.

```
https://schcsrc.github.io/report/Post/2022/06/13/2022-상반기-분석-보고서/
https://schcsrc.github.io/report/Project/2023/04/03/윈도우-EDR-솔루션/
```

`404.html`에서 이전 사이트에서 온 방문자를 블로그/프로젝트로 안내하고 있습니다.
