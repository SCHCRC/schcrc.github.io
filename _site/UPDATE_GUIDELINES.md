# SCH사이버보안연구센터 사이트 업데이트 가이드라인

이 문서는 `/Users/yeopeva/Documents/codex_workspace/SCHCRC` 사이트를 향후 수정하거나 운영할 때 참고하는 내부 작업 가이드입니다.

사이트는 GitHub Pages 배포를 전제로 한 **Jekyll 기반 정적 사이트**입니다.  
대부분의 업데이트는 Markdown 파일 또는 `_data` 파일 수정만으로 처리할 수 있습니다.

## 1. 기본 원칙

- 이 사이트는 **외부 공개용 공식 홈페이지**입니다.
- 문구는 내부 운영 문체보다 **대외 안내 문체**를 우선합니다.
- URL, 연락처, 연구원 정보, 프로젝트 정보는 공개 가능 여부를 확인한 뒤 반영합니다.
- 인프라 페이지에 URL을 등록하더라도, 실제 접근 권한 확인은 각 서비스에서 별도로 처리된다는 전제를 유지합니다.
- 파일명은 가능하면 영문, 숫자, 하이픈(`-`) 기준으로 관리합니다.

## 2. 주요 수정 위치

### 공통 설정

- 사이트 기본 설정: `_config.yml`
- 공통 레이아웃: `_layouts/default.html`
- 게시글 상세 레이아웃: `_layouts/post.html`
- 연구원 상세 레이아웃: `_layouts/researcher.html`
- 프로젝트 상세 레이아웃: `_layouts/project.html`
- 공통 스타일: `assets/css/style.scss`
- 공통 인터랙션 스크립트: `assets/js/site.js`
- 헤더 로고: `assets/branding/센터.png`
- 파비콘: `assets/favicon/`

### 메인 페이지

- 메인 페이지 내용: `index.md`

### 센터 소식

- 목록/소개 페이지: `news.md`
- 실제 게시글: `_news/*.md`

### 센터 블로그

- 목록/소개 페이지: `blog.md`
- 실제 게시글: `_blog/*.md`

### 센터 프로젝트

- 소개 페이지: `projects.md`
- 프로젝트 데이터: `_data/projects.yml`
- 상세 페이지 컬렉션: `_project_pages/*.md`

### 센터 인프라

- 소개 페이지: `infrastructure.md`
- 인프라 데이터: `_data/infrastructure.yml`

### 연구원 현황

- 페이지: `researchers.md`
- 데이터: `_data/researchers.yml`
- 상세 페이지 컬렉션: `_people/*.md`

### 센터 연혁

- 페이지: `history.md`
- 데이터: `_data/history.yml`

## 3. 콘텐츠별 업데이트 방법

### 3-1. 센터 소식 추가

`_news` 폴더에 새 Markdown 파일을 추가합니다.

예시:

```md
---
title: 새 공지 제목
date: 2026-03-24
author: SCH사이버보안연구센터
category: 공지
---

공지 본문을 작성합니다.
```

권장 카테고리 예시:

- 공지
- 활동
- 협약
- 모집
- 수상

### 3-2. 센터 블로그 추가

`_blog` 폴더에 새 Markdown 파일을 추가합니다.

예시:

```md
---
title: 연구 글 제목
date: 2026-03-24
author: SCH사이버보안연구센터
topic: 악성코드 분석
---

연구 내용을 작성합니다.
```

권장 토픽 예시:

- 악성코드 분석
- 디지털 포렌식
- 침해대응
- 연구 소개
- 운영 가이드

### 3-3. 프로젝트 업데이트

`_data/projects.yml`에서 항목을 추가/수정합니다.

예시:

```yml
- title: 악성코드 자동 분류 프로젝트
  status: 진행 중
  period: 2026
  summary: 악성코드 샘플 분류 자동화를 목표로 하는 연구 프로젝트입니다.
  links:
    - label: 결과 보고서
      url: https://example.com/report
    - label: 시연 페이지
      url: https://example.com/demo
```

외부 공개용이므로 요약문은 다음 기준을 권장합니다.

- 프로젝트 목적이 한 문장에 드러날 것
- 외부인이 봐도 이해 가능한 표현일 것
- 비공개 정보는 포함하지 않을 것

### 3-3-1. 프로젝트 상세 페이지 업데이트

프로젝트 상세 페이지는 `_project_pages` 폴더의 Markdown 파일로 관리합니다.

예시:

```md
---
title: 악성코드 자동 분류 프로젝트
slug: malware-auto-classification
status: 진행 중
period: 2026
summary: 한 줄 요약
overview: 프로젝트 상세 개요
owner: SCH사이버보안연구센터
topics:
  - 악성코드 분석
  - 자동 분류
activities:
  - period: 2026
    title: 진행 단계
    description: 세부 설명
outputs:
  - type: 보고서
    title: 결과 보고서
    description: 산출물 설명
    url: https://example.com
highlights:
  - 요약 포인트 1
  - 요약 포인트 2
---
```

그리고 `_data/projects.yml`의 해당 항목에도 같은 `slug`를 넣어야 목록 페이지에서 상세 페이지로 연결됩니다.

### 3-4. 인프라 업데이트

`_data/infrastructure.yml`에서 항목을 추가/수정합니다.

예시:

```yml
- title: 연구원 공용 NAS
  type: 스토리지
  access: 등록 연구원 대상
  summary: 공용 자료 저장 및 산출물 백업을 위한 NAS입니다.
  url: https://nas.example.org
  notes: 접속 시 서비스 정책에 따라 별도 인증이 필요합니다.
```

인프라 항목 작성 기준:

- `title`: 서비스 이름
- `type`: 스토리지 / 서버 / 내부시스템 / 협업도구 등
- `access`: 공개 여부 또는 이용 대상
- `summary`: 외부인이 이해할 수 있는 서비스 설명
- `url`: 실제 서비스 주소
- `notes`: 인증 방식, 이용 조건, 주의사항

### 3-5. 연구원 현황 업데이트

`_data/researchers.yml`에서 수정합니다.

- `current`: 현재 연구원
- `alumni`: 졸업 및 진출 연구원

공개 사이트이므로 다음 항목은 신중히 반영합니다.

- 실명 공개 여부
- 소속/진학/취업 정보 공개 가능 여부
- 개인 연락처 비공개 유지

### 3-5-1. 연구원 상세 페이지 업데이트

연구원 상세 페이지는 `_people` 폴더의 Markdown 파일로 관리합니다.

예시:

```md
---
name: 홍길동
slug: gildong-hong
generation: 26
status: 현재 연구원
role: 연구원
summary: 한 줄 소개
bio: 상세 소개
current_focus: 현재 연구 주제
current_affiliation: 현재 소속 또는 진출 현황
specialties:
  - 악성코드 분석
  - 침해대응
research_history:
  - period: 2026
    title: 연구 이력 제목
    description: 상세 설명
projects:
  - status: 진행 중
    title: 프로젝트명
    description: 프로젝트 설명
    url: https://example.com
achievements:
  - 주요 성과 1
  - 주요 성과 2
---
```

그리고 `_data/researchers.yml`의 해당 인물 항목에 같은 `slug`를 넣어야 목록 페이지에서 상세 페이지로 연결됩니다.

### 3-6. 연혁 업데이트

`_data/history.yml`에서 연도별 항목을 추가합니다.

예시:

```yml
- year: 2026
  label: 주요 활동
  title: 신규 연구 프로젝트 공개
  description: 센터의 신규 연구 프로젝트와 공개 산출물을 외부에 소개했습니다.
```

## 4. 이미지 및 첨부파일 관리

### 업로드 권장 위치

- 게시글 이미지: `assets/uploads/posts/연도-주제명/`
- 첨부 문서: `assets/uploads/files/연도-주제명/`

예시:

- `assets/uploads/posts/2026-malware-report/cover.png`
- `assets/uploads/files/2026-malware-report/report.pdf`

### 게시글에서 이미지 사용

```md
![분석 화면](/assets/uploads/posts/2026-malware-report/sample-1.png)
```

### 게시글에서 대표 이미지 및 첨부파일 사용

```md
---
cover_image: /assets/uploads/posts/2026-malware-report/cover.png
cover_image_alt: 분석 대표 이미지
cover_image_caption: 실습 환경에서 확인한 화면
attachments:
  - label: 분석 보고서 PDF
    url: /assets/uploads/files/2026-malware-report/report.pdf
    description: 외부 공개용 보고서
    download: true
---
```

## 5. 디자인 수정 시 원칙

- 현재 사이트는 `/Users/yeopeva/Downloads/SKILL.md`의 **Cosmic Design System**을 반영한 어두운 보안 관제/연구소 분위기입니다.
- 주요 폰트는 `Audiowide`, 보조 고정폭 폰트는 `JetBrains Mono`, 한글 본문은 `Noto Sans KR`을 사용합니다.
- 색상은 `assets/css/style.scss`의 토큰을 기준으로 수정합니다. 주요 토큰은 `--color-primary: #3b82f6`, `--color-secondary: #8b5cf6`, `--color-bg: #070b14`입니다.
- 메인 화면은 브랜드가 가장 먼저 보이도록 유지합니다. 첫 화면에 불필요한 통계, 긴 목록, 운영 정보, 카드형 패널을 추가하지 않습니다.
- 새 컴포넌트를 추가할 때는 카드 반경을 `8px` 이하로 유지하고, 선/그리드/타이포그래피로 정보 구조를 먼저 잡습니다.
- 버튼, 링크, 메뉴는 반드시 `hover`와 `focus-visible` 상태가 보여야 합니다.
- 외부 공개용 사이트이므로 내부 시스템처럼 보이는 모호한 라벨보다 `프로젝트 상세 페이지`, `상세 연구 이력 보기`처럼 행동이 분명한 문구를 사용합니다.
- 배경 효과를 추가할 때는 과한 장식보다 텍스트 대비와 가독성을 우선합니다.
- 메인 hero에는 C/Assembly 코드 레인 효과가 적용되어 있습니다. 성능을 위해 코드 컬럼 수는 기본 `5개` 수준을 유지하고, 무한 반복되는 큰 blur, filter, drop-shadow, mix-blend 효과를 추가하지 않는 것을 권장합니다.
- 스크롤 진입 애니메이션은 `assets/js/site.js`의 `IntersectionObserver`가 담당합니다. 새 섹션을 추가할 때 모든 요소에 reveal을 남발하지 말고, 섹션 제목이나 주요 목록 단위에만 적용합니다.
- `prefers-reduced-motion` 사용자는 애니메이션이 최소화되어야 합니다. 새 애니메이션을 추가하면 해당 미디어 쿼리에서 무력화되는지 확인합니다.

## 6. 배포 전 점검 체크리스트

- 오탈자가 없는지 확인
- 날짜, 이름, 링크가 정확한지 확인
- 외부 공개가 가능한 내용인지 확인
- 인프라 URL이 공개 가능한지 확인
- 게시글 이미지/첨부파일 경로가 실제로 존재하는지 확인
- 로고와 파비콘이 정상 표시되는지 확인
- 메인 hero의 코드 레인 효과가 텍스트를 가리지 않는지 확인
- 스크롤 애니메이션이 과하게 느리거나 버벅이지 않는지 확인
- 모바일 화면에서도 레이아웃이 무너지지 않는지 확인
- `bundle exec jekyll build`가 오류 없이 완료되는지 확인
- 배포 후 GitHub Pages 실제 URL에서 주요 메뉴와 상세 페이지 링크가 정상 동작하는지 확인

## 7. 로컬 테스트 방법

작업 폴더에서 아래 명령을 실행합니다.

```bash
cd /Users/yeopeva/Documents/codex_workspace/SCHCRC
bundle exec jekyll serve
```

브라우저에서 아래 주소로 확인합니다.

- `http://127.0.0.1:4000`
- `http://localhost:4000`

빌드만 확인하려면:

```bash
bundle exec jekyll build --source /Users/yeopeva/Documents/codex_workspace/SCHCRC --destination /tmp/schcrc_site
```

## 8. 권장 운영 흐름

1. 수정할 페이지 또는 데이터 파일을 먼저 결정합니다.
2. 공개 가능한 문구인지 검토합니다.
3. 로컬에서 미리보기 또는 빌드 확인을 합니다.
4. GitHub 저장소에 반영합니다.
5. 배포 후 실제 사이트에서 링크와 레이아웃을 다시 확인합니다.

## 9. 릴리스 전 최종 확인 순서

1. `bundle exec jekyll build --source /Users/yeopeva/Documents/codex_workspace/SCHCRC --destination /tmp/schcrc_site`로 빌드합니다.
2. `bundle exec jekyll serve`로 로컬 서버를 실행합니다.
3. 메인, 센터 소식, 센터 블로그, 센터 프로젝트, 센터 인프라, 연구원 현황, 센터 연혁을 차례대로 확인합니다.
4. 프로젝트 상세 페이지와 연구원 상세 페이지가 목록에서 정상 연결되는지 확인합니다.
5. 이미지, 첨부파일, 외부 URL이 404 또는 권한 오류 없이 의도대로 동작하는지 확인합니다.
6. 모바일 폭에서 메뉴, hero, 목록, 타임라인, 상세 페이지가 깨지지 않는지 확인합니다.
7. GitHub Pages 배포 후 실제 공개 URL에서 다시 한 번 주요 링크를 확인합니다.

## 10. 빠른 참고

- 메인 소개 수정: `index.md`
- 소식 추가: `_news/`
- 블로그 추가: `_blog/`
- 프로젝트 갱신: `_data/projects.yml`
- 프로젝트 상세 갱신: `_project_pages/`
- 인프라 URL 갱신: `_data/infrastructure.yml`
- 연구원 정보 갱신: `_data/researchers.yml`
- 연구원 상세 이력 갱신: `_people/`
- 연혁 갱신: `_data/history.yml`
- 로고 교체: `assets/branding/센터.png`
- 공통 스타일 수정: `assets/css/style.scss`
- 공통 애니메이션 수정: `assets/js/site.js`
