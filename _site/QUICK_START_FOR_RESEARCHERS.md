# SCHCRC 사이트 빠른 운영 매뉴얼

이 문서는 다른 연구원들이 사이트를 빠르게 수정하고 운영할 수 있도록 만든 **짧은 실무용 안내서**입니다.  
더 자세한 내용은 [UPDATE_GUIDELINES.md](/Users/yeopeva/Documents/codex_workspace/SCHCRC/UPDATE_GUIDELINES.md)를 참고하면 됩니다.

## 1. 가장 자주 수정하는 파일

- 메인 페이지: `index.md`
- 센터 소식 글 추가: `_news/`
- 센터 블로그 글 추가: `_blog/`
- 프로젝트 목록 수정: `_data/projects.yml`
- 프로젝트 상세 수정: `_project_pages/`
- 인프라 목록 수정: `_data/infrastructure.yml`
- 연구원 목록 수정: `_data/researchers.yml`
- 연구원 상세 수정: `_people/`
- 연혁 수정: `_data/history.yml`
- 공통 디자인 수정: `assets/css/style.scss`
- 스크롤 애니메이션 수정: `assets/js/site.js`

## 2. 글 추가 방법

### 센터 소식

`_news` 폴더에 새 Markdown 파일 추가

```md
---
title: 새 공지 제목
date: 2026-03-24
author: SCH사이버보안연구센터
category: 공지
---

공지 본문 작성
```

### 센터 블로그

`_blog` 폴더에 새 Markdown 파일 추가

```md
---
title: 연구 글 제목
date: 2026-03-24
author: SCH사이버보안연구센터
topic: 악성코드 분석
---

연구 내용 작성
```

## 3. 프로젝트 수정 방법

### 목록에 보이는 정보 수정

`_data/projects.yml` 수정

예시:

```yml
- title: 프로젝트 이름
  slug: project-slug
  status: 진행 중
  period: 2026
  summary: 프로젝트 한 줄 설명
  links:
    - label: 결과 보고서
      url: https://example.com
```

### 상세 페이지 수정

`_project_pages/project-slug.md` 수정 또는 새 파일 추가

중요:

- `slug` 값은 `_data/projects.yml`과 같아야 함
- 그래야 프로젝트 목록에서 상세 페이지로 연결됨

## 4. 연구원 수정 방법

### 목록에 보이는 정보 수정

`_data/researchers.yml` 수정

### 상세 페이지 수정

`_people/slug.md` 수정 또는 새 파일 추가

중요:

- `slug` 값은 `_data/researchers.yml`과 같아야 함
- 그래야 연구원 목록에서 상세 페이지로 연결됨

## 5. 인프라 수정 방법

`_data/infrastructure.yml` 수정

예시:

```yml
- title: 연구원 공용 NAS
  type: 스토리지
  access: 등록 연구원 대상
  summary: 공용 자료 저장용 NAS
  url: https://nas.example.org
  notes: 서비스 정책에 따라 별도 인증 필요
```

주의:

- 인프라 URL은 외부 공개 가능한 것만 입력
- 실제 권한 처리는 각 서비스에서 별도로 진행

## 6. 이미지와 첨부파일

- 게시글 이미지: `assets/uploads/posts/`
- 첨부파일: `assets/uploads/files/`

본문 예시:

```md
![설명](/assets/uploads/posts/2026-sample/image.png)
```

## 7. 수정할 때 꼭 지킬 것

- 외부 공개용 사이트라는 점을 항상 기억
- 내부 문체보다 대외 안내 문체 사용
- 개인정보, 계정정보, 민감한 내부 정보는 올리지 않기
- 파일명은 가능하면 영문/숫자/하이픈 사용
- 메인 화면의 C/Assembly 코드 레인 효과는 성능을 위해 과하게 늘리지 않기
- 새 애니메이션을 추가할 때는 모바일과 `prefers-reduced-motion` 환경을 함께 고려하기

## 8. 로컬에서 확인 방법

```bash
cd /Users/yeopeva/Documents/codex_workspace/SCHCRC
bundle exec jekyll serve
```

브라우저 주소:

- `http://127.0.0.1:4000`

## 9. 배포 전 최소 체크

- 오탈자 확인
- 링크 동작 확인
- 이미지/첨부파일 경로 확인
- 공개 가능한 정보만 올렸는지 확인
- 프로젝트/연구원 상세 연결이 되는지 확인
- 메인 화면에서 텍스트가 코드 레인에 가리지 않는지 확인
- 모바일에서 메뉴, 목록, 타임라인이 깨지지 않는지 확인
- 아래 빌드 명령이 성공하는지 확인

```bash
bundle exec jekyll build --source /Users/yeopeva/Documents/codex_workspace/SCHCRC --destination /tmp/schcrc_site
```

## 10. 문제 생기면 먼저 볼 것

- 프로젝트 상세 안 열림: `_data/projects.yml`의 `slug`와 `_project_pages/*.md`의 `slug`가 같은지 확인
- 연구원 상세 안 열림: `_data/researchers.yml`의 `slug`와 `_people/*.md`의 `slug`가 같은지 확인
- 이미지 안 뜸: `assets/uploads/...` 경로가 맞는지 확인
- 버튼/스타일 이상함: `assets/css/style.scss` 확인
- 스크롤 애니메이션 이상함: `assets/js/site.js` 확인
- 메인 화면이 버벅임: `index.md`의 `hero__code-rain` 코드 컬럼 수와 `assets/css/style.scss`의 hero 애니메이션 확인
