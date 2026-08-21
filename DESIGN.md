---
name: SCH사이버보안연구센터 공식 사이트
description: 네이비 계열 다크 지면에 로고 크림슨 하나를 강조색으로 쓰는 기술 지면 시스템. 모노스페이스는 실제 데이터에만.
colors:
  ground: "#0a0e17"
  ground-2: "#111725"
  ground-3: "#18202f"
  ground-deep: "#06090f"
  ink: "#eef2f8"
  ink-2: "#c2cad8"
  muted: "#8b95a8"
  rule: "#202836"
  rule-strong: "#334054"
  accent: "#e8646f"
  accent-strong: "#f0838c"
  accent-solid: "#c2242f"
  accent-solid-hover: "#d63744"
  accent-tint: "rgba(232, 100, 111, 0.13)"
  on-accent: "#ffffff"
  shadow: "rgba(2, 4, 8, 0.55)"
  shadow-strong: "rgba(2, 4, 8, 0.6)"
typography:
  display:
    fontFamily: "Pretendard Variable, Pretendard, -apple-system, Apple SD Gothic Neo, system-ui, sans-serif"
    fontSize: "clamp(2.125rem, 4.8vw, 3.75rem)"
    fontWeight: 800
    lineHeight: 1.12
    letterSpacing: "-0.042em"
  mono-data:
    fontFamily: "ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, monospace"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "normal"
  heading:
    fontFamily: "Pretendard Variable, Pretendard, -apple-system, Apple SD Gothic Neo, system-ui, sans-serif"
    fontSize: "clamp(1.5rem, 2.5vw, 1.9375rem)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.034em"
  subheading:
    fontFamily: "Pretendard Variable, Pretendard, -apple-system, Apple SD Gothic Neo, system-ui, sans-serif"
    fontSize: "1.1875rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.03em"
  body:
    fontFamily: "Pretendard Variable, Pretendard, -apple-system, Apple SD Gothic Neo, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: "-0.011em"
  prose:
    fontFamily: "Pretendard Variable, Pretendard, -apple-system, Apple SD Gothic Neo, system-ui, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.85
    letterSpacing: "-0.011em"
  meta:
    fontFamily: "Pretendard Variable, Pretendard, -apple-system, Apple SD Gothic Neo, system-ui, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: "normal"
  page-title:
    fontFamily: "Pretendard Variable, Pretendard, -apple-system, Apple SD Gothic Neo, system-ui, sans-serif"
    fontSize: "clamp(1.75rem, 3.2vw, 2.5rem)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.036em"
  section-title:
    fontFamily: "Pretendard Variable, Pretendard, -apple-system, Apple SD Gothic Neo, system-ui, sans-serif"
    fontSize: "1.5rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.032em"
  title:
    fontFamily: "Pretendard Variable, Pretendard, -apple-system, Apple SD Gothic Neo, system-ui, sans-serif"
    fontSize: "1.3125rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.032em"
  ui-lead:
    fontFamily: "Pretendard Variable, Pretendard, -apple-system, Apple SD Gothic Neo, system-ui, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.8
    letterSpacing: "-0.011em"
  ui:
    fontFamily: "Pretendard Variable, Pretendard, -apple-system, Apple SD Gothic Neo, system-ui, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 500
    lineHeight: 1.6
    letterSpacing: "-0.01em"
  ui-sm:
    fontFamily: "Pretendard Variable, Pretendard, -apple-system, Apple SD Gothic Neo, system-ui, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: "normal"
  label:
    fontFamily: "Pretendard Variable, Pretendard, -apple-system, Apple SD Gothic Neo, system-ui, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: "normal"
  micro:
    fontFamily: "Pretendard Variable, Pretendard, -apple-system, Apple SD Gothic Neo, system-ui, sans-serif"
    fontSize: "0.6875rem"
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.02em"
rounded:
  sm: "2px"
  md: "4px"
  pill: "999px"
spacing:
  xs: "6px"
  sm: "10px"
  md: "18px"
  lg: "28px"
  xl: "44px"
  section: "74px"
components:
  button-primary:
    backgroundColor: "{colors.accent-solid}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.md}"
    padding: "12px 20px"
  button-primary-hover:
    backgroundColor: "{colors.accent-solid-hover}"
    textColor: "{colors.on-accent}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "12px 20px"
  button-ghost-hover:
    backgroundColor: "{colors.ground-2}"
    textColor: "{colors.ink}"
  badge:
    backgroundColor: "{colors.accent-tint}"
    textColor: "{colors.accent}"
    rounded: "{rounded.pill}"
    padding: "2px 8px"
  badge-quiet:
    backgroundColor: "{colors.ground-2}"
    textColor: "{colors.muted}"
    rounded: "{rounded.pill}"
    padding: "2px 8px"
  tag:
    backgroundColor: "{colors.ground-2}"
    textColor: "{colors.ink-2}"
    rounded: "{rounded.pill}"
    padding: "3px 10px"
  panel:
    backgroundColor: "{colors.ground-2}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "20px"
  project-row:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "0"
    padding: "24px 0"
  nav-link:
    backgroundColor: "transparent"
    textColor: "{colors.ink-2}"
    rounded: "{rounded.sm}"
    padding: "8px 11px"
  nav-link-active:
    backgroundColor: "transparent"
    textColor: "{colors.accent}"
---

# Design System: SCH사이버보안연구센터 공식 사이트

## Overview

**다크 기술 지면 위의 분석 기록.** 네이비 계열 근검정 지면에 로고 크림슨 하나를 강조색으로 쓰고, 실제 데이터에는 모노스페이스를 쓴다. 화면의 주인공은 축적된 산출물이다 — 반기 분석 보고서 PDF, 기수별 프로젝트, 연구원 진로 기록.

### 어떻게 여기까지 왔는지 (같은 실수를 반복하지 않기 위해)

첫 방향 라운드에서 사용자는 "카테고리 표준"과 "기관·학술 신뢰형"을 택했고, 나는 그것을 **라이트 그라운드 기관 사이트**로 해석했다. 그 뒤 네 차례에 걸쳐 이전 사이트보다 못하다는 판정을 받았다. 매번 표면을 손질했다 — 이미지 복원, 밀도 증가, 모션 재작성, 명조 표제 추가. 전부 어긋났다.

세 버전(원래 다크 네이비 / 이전 블로그 / 라이트 재설계)을 실제로 나란히 띄워 물었을 때 답은 **원래 다크 방향**이었다. 즉 첫 해석이 틀렸고, 네 번의 손질은 잘못된 전제 위에서의 최적화였다.

**교훈**: 사용자가 고른 추상 라벨("기관 신뢰형")을 시각 언어로 번역할 때는, 번역 결과를 실물로 확인받아야 한다. 라벨이 같아도 번역은 여러 갈래다. 그리고 반복되는 부정 판정은 표면 결함이 아니라 전제 오류의 신호다.

동시에 원래 버전의 **싸구려 장식은 되돌리지 않았다**: 가짜 코드 레인 배경, 보라 그라데이션 버튼, 네온 글로우, Audiowide 로고체. 다크 방향을 유지하면서 그 자리를 실제 자산과 실제 데이터로 채운 것이 지금 상태다.

## Colors

색 전략은 **Restrained** — 다크 중성 지면 + 강조색 하나.

### Primary

`accent #e8646f` — 로고 크림슨을 다크 지면용으로 올린 값. 링크, 영문 표기, 육각 마커, 연혁 연도, 화살표. 지면 대비 6.0:1.
`accent-strong #f0838c` — 링크 hover.
`accent-solid #c2242f` — **버튼 배경 전용.** 흰 글자를 `#e8646f` 위에 올리면 3.4:1로 미달하므로 배경색을 따로 둔다. 흰 글자 대비 5.9:1.
`accent-solid-hover #d63744` — 흰 글자 대비 4.7:1.
`accent-tint rgba(232,100,111,.13)` — 활성 상태 배지 배경. 지면 위 합성 결과에서 `accent` 텍스트가 5.8:1.
`on-accent #ffffff` — `accent-solid` 위 글자와 선택 영역 글자에만. 다크 지면 본문에는 쓰지 않는다(`ink`를 쓴다).
`shadow rgba(2,4,8,.55)` / `shadow-strong rgba(2,4,8,.6)` — 부양 요소 그림자.

두 번째 강조색을 도입하지 않는다. 원래 버전은 블루·퍼플·시안을 동시에 썼고 그것이 "네온 다크" 클리셰의 정체다.

### Neutral

`ground #0a0e17` 기본 지면 · `ground-2 #111725` 교차 섹션·패널 · `ground-3 #18202f` hover·이미지 자리 · `ground-deep #06090f` 발간 보고서 밴드·코드 블록·푸터.

`ink #eef2f8` 제목·강조 데이터(17.2:1) · `ink-2 #c2cad8` 본문(11.8:1) · `muted #8b95a8` 메타·캡션(6.4:1).

`rule #202836` 기본 괘선 · `rule-strong #334054` 표 상단·고스트 버튼 테두리·부양 패널 경계.

### Named Rules

- 지면 단계는 넷뿐이고 그 순서를 지킨다: `ground-deep < ground < ground-2 < ground-3`. 다섯 번째 단계를 만들지 않는다.
- 강조색은 면적을 차지하지 않는다. 버튼, 링크, 1~2px 괘선, 배지, 육각 마커까지다. 크림슨 배경 블록이나 그라데이션을 만들지 않는다.
- **글로우 금지.** `box-shadow`로 색광을 뿌리거나 `text-shadow`로 발광시키지 않는다. 오프셋과 블러를 가진 실제 그림자만 쓴다(부양 패널 `0 20px 48px rgba(2,4,8,.55)`).
- 반투명 배경을 쓰면 대비를 **합성값으로** 계산한다. 눈으로는 통과처럼 보인다.

## Typography

단일 서체 **Pretendard Variable** (jsDelivr, dynamic-subset). 한글과 라틴 메트릭이 한 가족에서 나오므로 혼용 표기가 어긋나지 않는다. 폴백은 Apple SD Gothic Neo → 맑은 고딕 → system-ui.

다크 지면에서 성격은 **무게와 자간**이 만든다. 표제는 800 / `-0.042em`으로 조인다. 한글 명조를 표제에 쓰던 버전이 있었으나 다크 기술 지면과 어긋나 되돌렸다.

**모노스페이스는 실제 데이터에만.** 이 사이트에서 그것은: 악성코드명과 종류(보고서 본문 표), 발간 연월, 게시 날짜, 기수, 프로젝트 기간, 코드 블록이다. 보안 분석 맥락에서 데이터 열의 모노는 분위기용 코스튬이 아니라 올바른 조판이다. 라벨이나 소제목에는 쓰지 않는다.

### Hierarchy

램프는 10단계로 고정한다. 이 밖의 리터럴 크기를 새로 만들지 않는다.

| 토큰 | 크기 | 쓰임 |
|---|---|---|
| display | clamp(2.125rem, 4.8vw, 3.75rem) / 800 / -0.042em | 홈 히어로 h1 |
| page-title | clamp(1.75rem, 3.2vw, 2.5rem) / 800 | 하위 페이지 h1, 글 제목, 404 |
| heading | clamp(1.5rem, 2.5vw, 1.9375rem) / 800 | 섹션 h2 |
| section-title | 1.5rem / 800 | 상세 페이지 h2, 글 본문 h2 |
| title | 1.3125rem / 700 | 연구 분야 h3, 연구원 이름 |
| subheading | 1.1875rem / 700 | 목록 항목 h3, 글 본문 h3 |
| mono-data | 0.875~0.9375rem | 표 데이터, 날짜, 기수, 기간 |
| ui-lead / prose | 1.0625rem | 리드 문단, 글 본문 |
| body | 1rem / 1.75 | 기본 본문 |
| ui | 0.9375rem / 500 | 내비, 버튼, 링크 |
| ui-sm | 0.875rem | 밀도 높은 UI, 푸터, 요약 |
| meta | 0.8125rem / 600 | 분류 메타 |
| label | 0.75rem / 600 | dt 라벨, 태그 |
| micro | 0.6875rem / 600 | 브랜드 영문 표기, 배지 |

### Named Rules

- `word-break: keep-all` + `overflow-wrap: break-word` 를 전역으로 둔다. 한국어는 단어 중간에서 끊지 않고, 긴 라틴 토큰(악성코드명 등)은 넘치지 않게 끊는다.
- **측정폭은 `rem` 으로 고정한다. `ch` 를 쓰지 않는다.** `ch` 는 "0" 글자 너비 기준이라 전각인 한글에서 의도보다 훨씬 넓어진다. `68ch` 로 두었을 때 실측 47자, `74ch` 는 51자였다.
- 국문 본문 측정폭 목표는 **35~45자**다. 폰트 크기별 실측값:

| 용도 | max-width | 실측 한글 |
|---|---|---|
| 글 본문 (17px) | `38rem` | 45자 |
| 목록 설명 (16px) | `38rem` | 45자 |
| 작은 설명 (13~14px) | `36rem` | 42자 |
| 진로 표 (15px) | 표 전체 `50rem` | 44자 |
| 히어로 리드 (17px) | `28rem` | 33자 |

  측정 방법: 같은 폰트로 `가` 한 글자 폭을 재고 요소 폭을 나눈다. 라틴이 섞인 문장에서 "글자 수"를 세면 라틴이 좁아 왜곡된다.
- **`td` 의 `max-width` 는 `table-layout: auto` 에서 무시된다.** 표 열을 좁히려면 표 전체 폭을 제한한다.
- 숫자는 `font-variant-numeric: tabular-nums`.
- 제목 위 여백이 아래 여백보다 크다.
- **kicker·eyebrow 금지.** 제목 위에 소형 대문자 라벨을 얹지 않는다.
- **섹션 번호(01/02/03) 금지.** 순서 자체가 정보인 경우만 예외.
- **한글에는 12px 미만을 쓰지 않는다.** 한글은 획이 많아 같은 크기에서 라틴보다 불리하다. 배지가 11px 였는데 12px 로 올렸다. 라틴 전용 표기(`.brand__text small` 의 영문 센터명)는 11px 를 허용한다.
- 본문 표는 Markdown 출력이라 스크롤 래퍼를 넣을 수 없다. 좁은 화면에서 패딩·글자를 줄여 **3~4열까지** 한 줄로 들어가게 해 뒀다. 그보다 열이 많이 필요하면 표를 나누는 편이 낫다.

### 히어로 이미지 (출처 기록)

`assets/uploads/hero/center-hero.jpg` (2400×747, 231KB) — 이전 센터 홈페이지 `SCHCsRC.github.io`의 `img/header.jpg`(6942×2161, 2.25MB)를 리사이즈한 것이다. 센터가 실제로 쓰던 자산이며, 네이비 지면 + 붉은 네트워크 그래픽이라는 지금 팔레트의 근거이기도 하다. `center-hero-1200.jpg`는 좁은 화면용 예비본.

히어로 위 글자는 스크림이 **0.93 이상**인 구간에만 놓는다. 텍스트 컬럼은 좌측 54%까지, 스크림은 56%까지 0.93 이상을 유지하고 그 뒤로 0.3까지 떨어진다. 배경 이미지를 교체하면 이 계산을 다시 한다.

교체할 때: 센터가 직접 만든 이미지(분석 화면, 컨퍼런스 사진, 장비 사진)가 생기면 바꾼다. 범용 스톡 사진으로 교체하지는 않는다.

## Layout

셸 최대폭 1180px, 좌우 여백 28px(≤900px에서 20px). 섹션 상하 74px(≤900px에서 56px).

목록은 전부 **하한선 격자(hairline grid)** 다. 카드 대신 `border-bottom: 1px solid var(--rule)`로 나눈 행을 쓴다. 좌열은 고정 폭, 우열은 `minmax(0, 1fr)`.

프로젝트 행은 3열이다: `[상태 배지 + 기간] [제목 + 요약] [담당 · 핵심 주제]`. 한때 이미지 카드 격자였으나 대표 이미지가 센터 산출물이 아닌 범용 스톡 사진이어서 목록에서 걷어냈다. 이미지는 상세 페이지 사이드바에만 남긴다.

지면 리듬: `히어로(이미지+스크림) → ground → ground-deep 발간보고서 → ground 프로젝트 → ground-2 블로그 → ground 진로 → ground-2 센터현황 → ground-deep 푸터`. 같은 지면 단계를 연달아 두지 않는다.

반응형 분기: 1040px(히어로·상세 2열 → 1열), 900px(내비 → 토글 메뉴, 푸터 1열, 프로젝트 행 2열), 720px(모든 좌우 다열 목록 → 1열).

## Elevation & Depth

깊이는 지면 단계와 괘선으로 표현하고, 그림자는 실제로 떠 있는 것에만 쓴다.

- 히어로 우측 패널: `ground-2` 82% 반투명 + `blur(8px)` + `0 20px 48px rgba(2,4,8,.55)` + `rule-strong` 1px 경계. 다크 지면 위에서 카드가 떠 있음을 보이려면 그림자가 깊어야 한다 — 라이트 지면용 값(0.1 알파)은 보이지 않는다.
- 모바일 드롭다운 메뉴: `0 16px 34px rgba(2,4,8,.6)`.
- sticky 헤더 압축 시: `0 6px 22px rgba(2,4,8,.55)`.
- 카드 안의 카드를 만들지 않는다. `box-shadow: 4px 4px 0` 류의 오프셋 블록 섀도를 쓰지 않는다.

## Shapes

모서리는 거의 직각이다. `sm 2px`(포커스 링, 내비 링크), `md 4px`(버튼, 패널, 이미지 액자), `pill 999px`(배지, 태그)만 쓴다. 프로젝트 행은 반경 0.

**육각형 마커.** 센터 로고의 육각 큐브에서 온 형태를 `clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)`로 그려 연구 분야 제목과 성과 목록의 불릿에 쓴다. 원형 불릿 대신 브랜드 자체의 기하를 쓴다. 장식으로 크게 띄우거나 배경 패턴으로 반복하지 않는다.

강조색 세로 띠(`border-left: 3px+ solid accent`)를 쓰지 않는다. 인용문은 1px 크림슨 좌측선만 쓴다.

## Components

### Buttons

`button--primary`: `accent-solid` 배경 / 흰 글자 / 4px / 12·20px. 페이지당 한 개.
`button--ghost`: 투명 배경 / `rule-strong` 테두리 / hover에서 `ground-2` 배경 + `ink-2` 테두리.
`text-link`: `accent` 텍스트 + `→` 유사요소. hover에서 화살표가 3px 이동. `padding-block: 3px`로 클릭 영역을 24px 이상 확보한다.

### Chips

`badge`: 진행 중·예정·상시 운영은 크림슨 틴트. `badge--quiet`: 이전 기수·기록용은 중성. 상태를 색으로 구분하는 것이 유일한 목적이다.
`tag-list li`: 주제 태그. 중성색만.

### Cards / Containers

`hero__aside` — 첫 화면 우측 부양 패널. 최신 보고서(제목·분석 대상·PDF 링크)와 최근 소식 3건. 첫 화면이 장식이 아니라 실제 산출물로 채워지는 지점이다.
`hero__facts` — 센터장·설립·공개 보고서 수·배출 연구원 수. 라벨 스케일로만. **큰 숫자 + 작은 라벨 + 강조색의 지표 타일로 만들지 않는다.** 수치는 데이터 파일에서 계산한다.
**목록 행 링크 규칙** — `project-row` 와 `person-row` 가 공유한다. 행은 `<div>`이고 **제목(또는 이름)만 `<a>`** 다. 링크의 `::before` 가 행 전체를 덮어 클릭 영역은 행 전체지만 스크린리더가 읽는 이름은 제목뿐이다. 행 전체를 `<a>` 로 감쌌을 때 프로젝트 링크 이름이 146자였다. 대가로 요약문·태그 드래그 선택이 안 된다.

화살표 `→` 는 **링크 자신의 `::after`** 에 붙인다. 행이나 제목에 붙이면 상세 페이지가 없는 항목(링크가 없는 행)에도 화살표가 새므로, `:has()` 같은 조건 선택자가 필요해진다. 링크에 붙이면 링크가 없을 때 화살표도 없다 — 브라우저 지원과 무관하게 성립한다.

**한 행에 같은 목적지로 가는 링크를 두 개 두지 않는다.** 연구원 목록에는 이름 링크와 "상세 연구 이력 보기" 링크가 같은 URL 로 나란히 있었다. 스크린리더에서 같은 페이지가 두 번 읽히고, 게다가 현재 연구원 중 `research_history` 를 가진 사람이 없어 그 문구는 지키지 못할 약속이었다.
`researcher-meta` — 상세 페이지 사이드바. `ground-2`, sticky(top 100px).

### Navigation

기본 `ink-2`, hover `accent` + `ground-2`, 현재 페이지는 `accent` 600 + 하단 2px 밑선. 현재 페이지 판정은 `page.url` 또는 컬렉션 기본값 `section_path`.
900px 이하에서 `.nav-toggle`(`aria-expanded`, `aria-controls`)로 접히고 Esc·바깥 클릭·뷰포트 확대에서 닫힌다.

### 브라우저 표면

시스템 기본값을 그대로 내보내지 않는다. `::selection` `accent-solid`/흰색 · `caret-color` accent · `:focus-visible` 2px accent 아웃라인 + 3px 오프셋 · `scrollbar-color`와 `::-webkit-scrollbar-thumb` 팔레트 지정 · `text-underline-offset: 0.22em`.

### 접근성 규칙 (측정으로 확정된 것)

- **단독 링크의 클릭 영역은 최소 24px**(WCAG 2.5.8). 제목·표·브레드크럼 안의 링크는 글자 높이가 16~23px뿐이므로 `::before { inset: -5px -6px }`로 레이아웃을 건드리지 않고 히트 영역만 넓힌다.
- **같은 문구의 링크가 여러 개면 `aria-label`로 구분한다.** "PDF 내려받기"가 한 페이지에 4개 있었다.
- **건너뛰기 링크는 첫 번째 탭 대상**이며 `:focus`(`:focus-visible` 아님)에서 나타난다.
- **선택자 특이도를 확인한다.** 지면이 바뀌는 섹션에서 `.section__heading p`가 `.section--dark p`를 이겨 3.38:1까지 떨어진 적이 있다.
- **헤더 로고는 96px 판(`center-logo-96.png`)을 쓴다.** 600px 원본은 97KB로 페이지 무게의 67%였다.

### 모션

세 층으로만 구성한다. 섹션마다 같은 페이드를 반복하는 것은 모션이 아니라 소음이다.

**1. 첫 화면 정착 (연출된 한 순간, 약 1.8초).** 배경이 `scale 1.09 → 1`로 1700ms 가라앉는 동안, 제목 두 줄이 `overflow: hidden` 마스크 안에서 115% 아래에서 차례로 올라오고(120·240ms 지연), 영문 라인 → 리드 → 버튼 → 사실 목록이 520~820ms 지연으로 상승하고, 크림슨 규칙이 좌→우로 그려지고, 마지막에 패널이 올라온다. 전부 `cubic-bezier(.16,1,.3,1)`.

초기 버전은 620ms에 14px 이동 하나뿐이어서 "하나의 연출된 순간"이라는 규칙을 만족한다고 적어놓고도 **순간이 지각되지 않았다.** 절제와 부재는 다르다.

**2. 지속 상태.** 스크롤 120px을 넘으면 헤더에 그림자가 생기고 브랜드가 `scale(0.9)`로 조여든다. 히어로 배경은 스크롤의 0.14배로 밀린다.
**`min-height`·`width`·`height`를 트랜지션하지 않는다.** sticky 헤더는 문서 흐름에 있으므로 높이를 애니메이션하면 매 프레임 문서 전체가 리플로우된다. `transform`과 `box-shadow`만 쓴다.

**3. 목록 행 착지.** `animation-timeline: view()` 스크롤 구동 애니메이션. 진행도가 스크롤 위치에 묶여 있어 **이미 지나친 행은 항상 100%**다. IntersectionObserver로 하면 빠르게 스크롤할 때 콜백 전에 행이 지나가 `opacity: 0`으로 영구히 남는다(실측: 맨 아래로 점프하면 24행 중 18행이 안 보였다). 미지원 브라우저에서는 애니메이션 없이 그냥 보인다.

`requestAnimationFrame` 안에 상태 플래그를 두면 탭이 백그라운드일 때 rAF가 정지해 플래그가 걸리고 상태가 멈춘다. 헤더 토글처럼 값싼 갱신은 rAF 밖에 둔다.

`prefers-reduced-motion: reduce`에서는 **등장 연출만** 끈다. hover·focus 전환과 헤더 압축은 남긴다.

## Do's and Don'ts

### Do:

- 새 글·새 프로젝트는 Markdown 파일 하나로 끝낸다. `_project_pages/*.md`가 프로젝트의 유일한 원본이다.
- 없는 실적은 비워 둔다. `resource-empty` / `empty-state`로 "아직 없음"을 정직하게 표시한다.
- 표를 쓴다. 진로·분석 내용처럼 대조가 필요한 데이터는 카드가 아니라 표가 맞다.
- 실제 데이터에 모노를 쓴다. 악성코드명 표는 모노로 조판하는 것이 맞다.
- 첫 화면을 실제 산출물로 채운다. 카운터가 아니라 최신 보고서 제목과 분석 대상 이름 같은 실물이다.
- 연혁의 행사 사진처럼 진짜 증거는 해상도가 낮아도 싣는다. 200px 썸네일이 문장보다 강하다.
- 반투명이 끼면 대비를 합성값으로 계산한다.

### Don't:

- **가짜 코드 배경, 매트릭스 레인, 네온 글로우, 방패·자물쇠 아이콘을 쓰지 않는다.** 다크 지면을 쓴다는 것이 이 클리셰를 허가하는 것은 아니다. 이번 재설계가 걷어낸 것이 정확히 그것이다.
- 그라데이션 버튼과 그라데이션 텍스트를 쓰지 않는다. 강조는 무게와 색면으로 한다.
- 두 번째 강조색을 도입하지 않는다. 로고 크림슨 하나다.
- 제목 위 kicker/eyebrow, 섹션 번호, 큰 숫자 지표 타일을 만들지 않는다.
- 아이콘+제목+문단이 똑같은 크기로 반복되는 카드 격자를 페이지 구조로 쓰지 않는다. 이미지를 뺀 텍스트 카드 격자도 같은 함정이다 — 그때는 하한선 목록으로 간다.
- 이모지나 유니코드 글리프를 아이콘 대신 쓰지 않는다.
- 모노스페이스를 "기술적 분위기"로 쓰지 않는다. 데이터·코드·계측에만 쓴다.
- 라이트 지면용 그림자 알파(0.1 내외)를 다크에 그대로 쓰지 않는다. 보이지 않는다.
