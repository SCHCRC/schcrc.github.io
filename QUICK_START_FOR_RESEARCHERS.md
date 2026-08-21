# SCHCRC 사이트 빠른 운영 매뉴얼

연구원이 자주 하는 작업만 모았습니다. 자세한 규칙은 [UPDATE_GUIDELINES.md](UPDATE_GUIDELINES.md), 디자인 원칙은 [DESIGN.md](DESIGN.md)에 있습니다.

**센터 소개 문구를 고칠 때**: 센터장 이름, 연구 분야, 연구원 수상 내역 같은 사실은 그 학기 센터 소개 발표자료가 기준입니다. 자료에 없는 내용은 추측해서 채우지 마세요. 대조할 항목은 [UPDATE_GUIDELINES.md 1-1 절](UPDATE_GUIDELINES.md)에 표로 있습니다.

**핵심 원칙 하나**: 내용이 없으면 그 줄을 **지웁니다.** "추가 예정" 같은 문구를 채워 넣으면 방문자 화면에 그대로 찍힙니다. 비어 있으면 그 영역이 아예 나오지 않게 만들어 뒀습니다.

---

## 1. 자주 만지는 파일

| 하고 싶은 일 | 파일 |
|---|---|
| 소식·공지 올리기 | `_news/` 에 `.md` 새로 만들기 |
| 보고서·분석 글 올리기 | `_blog/` 에 `.md` 새로 만들기 |
| 프로젝트 추가·수정 | `_project_pages/` 에 `.md` 새로 만들기 |
| 연구원 명단 수정 | `_data/researchers.yml` |
| 연구원 상세 페이지 | `_people/<slug>.md` |
| 연혁 추가 | `_data/history.yml` |
| 인프라 URL 등록 | `_data/infrastructure.yml` |
| 연구 분야 문구 | `_data/site.yml` |

---

## 2. 소식 올리기

`_news/2026-09-01-something.md`

```md
---
title: 소식 제목
date: 2026-09-01
author: SCH사이버보안연구센터
category: 공지
---

본문을 씁니다.
```

`category` 는 `공지` · `협약` · `활동` · `모집` 중에서 씁니다. 홈 화면 우측 "최근 소식"에 자동으로 올라갑니다.

### 연구원 모집 공고는 두 줄을 더 넣습니다

```md
category: 모집
generation: 27
closes: 2027-03-20
```

`closes` 가 **오늘 이후**면 홈 첫 화면 주 버튼이 "27기 연구원 모집 중"으로 바뀌고, 마감이 지나면 "분석 보고서 보기"로 돌아갑니다. 이 두 줄을 빼면 마감된 공고가 계속 모집 중으로 보입니다.

---

## 3. 블로그 글 올리기

`_blog/2026-09-10-report.md`

```md
---
title: 2026 상반기 분석 보고서
date: 2026-09-10
author: 담당 연구원 이름
topic: 분석 보고서
attachments:
  - label: 2026년 상반기 악성코드 분석 보고서 PDF
    url: /assets/uploads/files/2026-first-half/report.pdf
    description: 다룬 악성코드 이름을 여기에 적습니다.
    download: true
---

본문.

## 분석 내용

| 악성코드 | 종류 | 분석가 |
|:---:|:---:|:---:|
| 예시 | Ransomware | 이름 |
```

- `topic: 분석 보고서` 로 적으면 **홈 화면 "발간 보고서" 섹션과 첫 화면 "최신 보고서" 카드에 자동으로 올라갑니다.** 다른 값이면 블로그 목록에만 나옵니다.
- `attachments` 의 `description` 은 홈 화면에 그대로 보입니다. 다룬 악성코드 이름을 적어 두면 방문자가 목록에서 바로 판단할 수 있습니다.
- PDF 는 **먼저 업로드하고** 그다음 경로를 적습니다. 파일이 없으면 검사기가 배포를 막습니다.
- 글을 내리고 싶으면 지우지 말고 `published: false` 한 줄을 넣습니다.

---

## 4. 프로젝트 추가

`_project_pages/` 에 파일 하나만 만들면 목록과 상세 페이지가 함께 생깁니다. 별도 데이터 파일은 없습니다.

```md
---
title: 프로젝트 제목
date: 2026-09-01
slug: project-slug
status: 진행 중
period: 2026
owner: 담당 연구원
summary: 목록에 한 줄로 나오는 요약.
overview: 상세 페이지 첫 문단.
cover_image: /assets/uploads/projects/project-slug.png
cover_image_alt: 이미지 설명
topics:
  - 주제1
  - 주제2
highlights:
  - 사이드바 요약 포인트
---
```

- **`---` 로 시작하고 `---` 로 닫아야 합니다.** 닫는 줄을 빼면 제목이 파일명(영문)으로 나옵니다.
- `status` 를 `진행 중` · `진행 예정` · `상시 운영` 로 적으면 배지가 크림슨, 그 외(`이전 기수 프로젝트` 등)는 회색입니다.
- 정렬은 `date` 역순입니다.
- `activities`, `outputs` 는 실제 내용이 있을 때만 넣습니다. 없으면 그 영역이 나오지 않습니다.

---

## 5. 연구원 수정

### 명단 (`_data/researchers.yml`)

```yml
current:
  - name: 이름
    slug: yeongmun-slug
    generation: 27
    role: 연구원
    tags:
      - 악성코드 분석

alumni:
  - name: 이름
    slug: yeongmun-slug
    generation: 22
    outcome: 어디로 갔는지 한 문장.
```

진로 기록이 없으면 `outcome: "-"` 로 씁니다. YAML 에서 맨앞 하이픈은 인용부호로 감싸야 합니다.

### 상세 페이지 (`_people/<slug>.md`)

```md
---
title: 이름
name: 이름
slug: yeongmun-slug
generation: 27
status: 현재 연구원
role: 연구원
summary: 27기 연구원. 무엇을 맡고 있는지 한 문장.
current_focus: 악성코드 분석
specialties:
  - 악성코드 분석
achievements:
  - 실제 수상·선발 내역
---
```

- `title` 과 `name` 을 **둘 다** 넣습니다. `title` 이 없으면 브라우저 탭 제목이 영문 슬러그로 나옵니다.
- `status` 는 `현재 연구원` 또는 `졸업 및 진출 연구원` 이며, `researchers.yml` 의 어느 섹션에 있는지와 **일치해야 합니다.** 어긋나면 검사기가 잡습니다.
- `generation` 도 `researchers.yml` 값과 같아야 합니다.
- 실적이 없으면 `achievements` 를 아예 빼세요.

---

## 6. 연혁 추가 (`_data/history.yml`)

```yml
  - year: 2026
    label: 센터 활동
    title: 한 줄 제목
    description: 무슨 일이 있었는지.
    image: /assets/uploads/history/2026-something.jpg
    image_alt: 사진 설명
```

`image` 는 선택입니다. 행사 사진이 있으면 넣는 편이 문장보다 강합니다. 200px 정도의 작은 사진도 괜찮습니다.

---

## 7. 이미지와 첨부파일

| 종류 | 위치 |
|---|---|
| 글 본문·대표 이미지 | `assets/uploads/posts/<연도-주제>/` |
| 첨부 문서(PDF 등) | `assets/uploads/files/<연도-주제>/` |
| 프로젝트 대표 이미지 | `assets/uploads/projects/` |
| 연혁 사진 | `assets/uploads/history/` |

파일명은 **영문·숫자·하이픈**으로만 씁니다. 한글 파일명은 macOS 시스템 Ruby 에서 빌드가 깨집니다.

본문에 이미지 넣기:

```md
![설명](/assets/uploads/posts/2026-example/screen.png)
```

---

## 8. 로컬에서 확인

```bash
bundle install
LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 RUBYOPT="-E utf-8" bundle exec jekyll serve
```

http://localhost:4000 에서 열립니다. 로케일 지정은 한글이 섞인 경로 때문에 필요합니다.

---

## 9. 올리기 전 필수 검사

```bash
bundle exec jekyll build && python3 tools/verify.py
```

`실패 0건` 이 나와야 올립니다. 이 검사가 잡는 것:

- 깨진 내부 링크, 없는 첨부파일·이미지
- 헤딩 단계 건너뜀, `h1` 개수, `alt` 없는 이미지, 빈 요소
- **"추가 예정" 같은 편집자용 문구가 방문자 화면에 노출**
- `researchers.yml` 과 `_people` 의 기수·구분 불일치
- 프로젝트 필수 필드 누락, front matter 구분자 오류

---

## 10. 문제가 생기면

| 증상 | 원인 |
|---|---|
| 제목이 영문 파일명으로 나옴 | front matter 닫는 `---` 누락, 또는 `_people` 에 `title` 없음 |
| 목록에서 상세로 안 넘어감 | `slug` 불일치 |
| 보고서가 홈에 안 뜸 | `topic: 분석 보고서` 가 아님 |
| 마감된 모집이 계속 뜸 | `closes` 없음 |
| 빌드가 `Encoding::UndefinedConversionError` | 한글 파일명. 8번의 로케일 지정으로 실행 |
| 화면이 예전 그대로 | 브라우저 캐시. `⌘⇧R` |
