# SCH사이버보안연구센터 GitHub Pages 사이트

발표자료 기반으로 제작한 `github.io` 운영용 정적 사이트입니다.  
GitHub Pages에서 바로 쓰기 쉽도록 **Jekyll + Markdown** 구조로 구성했습니다.

실제 운영 중인 [schcsrc.github.io](https://schcsrc.github.io/)의 파비콘과 소개 문구 톤을 참고해, 현재 사이트에도 `SCH Cybersecurity Research Center` 표기와 핵심 방향성을 반영했습니다.

추가 유지보수 문서는 [UPDATE_GUIDELINES.md](/Users/yeopeva/Documents/codex_workspace/SCHCRC/UPDATE_GUIDELINES.md)에 정리되어 있습니다.
빠르게 수정할 때 보는 짧은 운영 문서는 [QUICK_START_FOR_RESEARCHERS.md](/Users/yeopeva/Documents/codex_workspace/SCHCRC/QUICK_START_FOR_RESEARCHERS.md)에 정리되어 있습니다.

## 현재 사이트 구조 요약

- 정적 사이트 엔진: Jekyll
- 주요 콘텐츠 작성 방식: Markdown, YAML 데이터 파일
- 공통 레이아웃: `_layouts/`
- 공통 스타일: `assets/css/style.scss`
- 공통 인터랙션: `assets/js/site.js`
- 브랜드 이미지: `assets/branding/센터.png`
- 파비콘: `assets/favicon/`

메인 화면에는 C/Assembly 코드 레인과 경량화된 스크롤 진입 애니메이션이 적용되어 있습니다. 성능 유지를 위해 hero 코드 컬럼과 반복 애니메이션을 과도하게 늘리지 않는 것을 권장합니다.

## 포함된 페이지

- 메인 페이지: 센터 소개, 연구 분야, 최근 소식, 최근 블로그 글
- `센터 소식`: 공지, 행사, 모집, 협약 등 공식 뉴스 게시
- `센터 블로그`: 연구 내용, 분석 사례, 기술 글 게시
- `센터 프로젝트`: 수행 중인 프로젝트, 산출물 URL, 관련 연구 링크 정리
- `센터 인프라`: NAS, 서버, 내부 서비스 URL 및 인프라 구성 안내
- `연구원 현황`: 현재 연구원 / 졸업 및 진출 연구원 소개
- `센터 연혁`: 연도별 활동과 성과를 타임라인으로 정리

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

## 프로젝트 수정

`_data/projects.yml` 파일을 수정하면 됩니다.

프로젝트 페이지는 외부 방문자가 센터에서 어떤 연구와 개발이 진행되는지 볼 수 있도록 구성되어 있습니다.

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

빌드만 확인하려면 아래 명령을 사용합니다.

```bash
bundle exec jekyll build --source /Users/yeopeva/Documents/codex_workspace/SCHCRC --destination /tmp/schcrc_site
```

## 릴리스 전 확인

- `bundle exec jekyll build`가 성공하는지 확인
- 메인, 센터 소식, 센터 블로그, 센터 프로젝트, 센터 인프라, 연구원 현황, 센터 연혁 페이지 확인
- 프로젝트 상세 페이지와 연구원 상세 페이지 연결 확인
- 이미지, 첨부파일, 외부 URL 링크 확인
- 모바일 화면에서 메뉴, hero, 목록, 타임라인 레이아웃 확인
- 공개 전 민감 정보, 개인정보, 내부 계정 정보가 없는지 확인

## 이번 초안에 반영한 발표자료 기반 내용

- 센터 소개 문구
- 연구 분야 3종
- 누리랩 MOU 체결
- KISTI-NICT 국제 공동 워크숍 참석
- 2024/2025 주요 성과 요약
- 26기 연구원 모집 안내

연구원 현황은 발표자료에서 확인 가능한 인물 중심으로 기본 입력했으며, 실제 운영 전 최신 인원 기준으로 보완하는 것을 권장합니다.
