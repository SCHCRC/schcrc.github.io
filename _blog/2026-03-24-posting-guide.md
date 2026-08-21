---
title: 센터 게시물 작성 가이드
date: 2026-03-24
author: SCH사이버보안연구센터
topic: 운영 가이드
# 편집자용 안내라 공개 블로그에서 내렸습니다. 같은 내용이 UPDATE_GUIDELINES.md 에 있습니다.
# 다시 공개하려면 아래 줄을 지우세요.
published: false
---

센터 블로그와 센터 소식은 Markdown 글 작성만으로 운영할 수 있습니다.

## 이미지 넣기

본문 안에서는 아래 형식으로 이미지를 삽입합니다.

```md
![대체 텍스트](/assets/uploads/posts/example-post/detail-image.png)
```

## 대표 이미지 넣기

글 상단에 대표 이미지를 넣으려면 front matter에 아래 세 줄을 추가합니다. 실제로 업로드한 파일 경로를 넣어야 합니다.

```yml
cover_image: /assets/uploads/posts/2026-example/cover.png
cover_image_alt: 대표 이미지 설명
cover_image_caption: 이미지 아래에 붙는 캡션입니다.
```

## 첨부파일 넣기

본문 하단에 별도 다운로드 영역을 만들고 싶다면 front matter의 `attachments`를 사용합니다.

```yml
attachments:
  - label: 분석 보고서 PDF
    url: /assets/uploads/files/2026-example/report.pdf
    description: 첨부파일 목록에 표시되는 설명입니다.
    download: true
```

이 방식은 공지 PDF, 지원서 양식, 발표자료, 연구 요약본 등을 정리할 때 특히 편합니다. 경로에 실제로 파일이 없으면 링크가 깨지므로, 파일을 먼저 올린 뒤 front matter에 적어 주세요.

## 권장 운영 방식

- 게시글마다 전용 폴더를 하나 만들어 관련 이미지와 첨부파일을 함께 보관합니다.
- 게시글 제목은 한글로 작성해도 되지만, 업로드 파일명은 영문 기준으로 관리하는 것을 권장합니다.
- 외부 링크 문서가 사라지는 상황을 피하려면 공개 가능한 파일은 저장소 내부에 함께 보관하는 편이 좋습니다.
