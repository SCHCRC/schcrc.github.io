---
title: 센터 게시물 작성 가이드
date: 2026-03-24
author: SCH사이버보안연구센터
topic: 운영 가이드
cover_image: /assets/uploads/posts/example-post/cover-example.png
cover_image_alt: 예시 대표 이미지
cover_image_caption: 실제 운영 시에는 업로드한 대표 이미지를 지정해 사용할 수 있습니다.
attachments:
  - label: 예시 보고서 PDF
    url: /assets/uploads/files/example-post/example-report.pdf
    description: 첨부파일 목록에 표시되는 문서 예시입니다.
    download: true
---

센터 블로그와 센터 소식은 Markdown 글 작성만으로 운영할 수 있습니다.

## 이미지 넣기

본문 안에서는 아래 형식으로 이미지를 삽입합니다.

```md
![대체 텍스트](/assets/uploads/posts/example-post/detail-image.png)
```

## 첨부파일 넣기

본문 하단에 별도 다운로드 영역을 만들고 싶다면 front matter의 `attachments`를 사용합니다.

이 방식은 공지 PDF, 지원서 양식, 발표자료, 연구 요약본 등을 정리할 때 특히 편합니다.

## 권장 운영 방식

- 게시글마다 전용 폴더를 하나 만들어 관련 이미지와 첨부파일을 함께 보관합니다.
- 게시글 제목은 한글로 작성해도 되지만, 업로드 파일명은 영문 기준으로 관리하는 것을 권장합니다.
- 외부 링크 문서가 사라지는 상황을 피하려면 공개 가능한 파일은 저장소 내부에 함께 보관하는 편이 좋습니다.
