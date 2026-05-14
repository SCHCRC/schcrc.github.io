---
title: SCH사이버보안연구센터
permalink: /
---

<section class="hero">
  <div class="hero__code-rain" aria-hidden="true">
    <span>int main(void) {
  init_sensor();
  while (packet = recv()) {
    if (detect_ioc(packet)) alert();
  }
  return EXIT_SUCCESS;
}

static int detect_ioc(pkt_t *p) {
  return hash_match(p) || yara_hit(p);
}</span>
    <span>typedef struct {
  char hash[65];
  uint32_t pid;
  uint8_t risk;
} sample_t;

sample_t s = parse_sample(buf);
if (s.risk > 7) {
  isolate_host(s.pid);
}</span>
    <span>for (int i = 0; i < n; i++) {
  score += yara_scan(buf[i]);
  trace_actor(flow[i]);
  if (score > threshold) break;
}

fprintf(report, "%08x:%s", score, tag);
}</span>
    <span>push rbp
mov rbp, rsp
sub rsp, 0x40
mov rdi, [rbp-0x18]
call yara_scan
test eax, eax
jnz short loc_alert
xor eax, eax
leave
ret</span>
    <span>loc_unpack:
lea rcx, [rip+section]
mov edx, 0x200
call entropy_check
cmp eax, 7
jg loc_decrypt
nop
jmp loc_report

loc_decrypt:
xor byte ptr [rsi], 0x5A
inc rsi</span>
  </div>
  <div class="site-shell hero__inner">
    <div class="hero__content">
      <p class="hero__kicker">SCH Cybersecurity Research Center</p>
      <h1>SCH 사이버보안연구센터</h1>
      <p class="hero__lead">
        악성코드 분석 및 사이버 범죄 그룹 추적, 국내외 유관기관의 협력을 통해 <br>
        사이버 위협 및 사이버전 대응과 관련된 연구를 진행하고 있습니다.
      </p>
      <div class="hero__actions">
        <a class="button button--primary" href="{{ '/news/' | relative_url }}">센터 소식 보기</a>
        <a class="button button--ghost" href="{{ '/blog/' | relative_url }}">연구 블로그 보기</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--identity">
  <div class="site-shell">
    <div class="section__heading">
      <p class="eyebrow">Center Identity</p>
      <h2>센터 기본 정보</h2>
      <p>센터장 및 소속, 위치에 대한 정보입니다.</p>
    </div>
    <div class="identity-list">
      <article class="identity-item">
        <span>센터장</span>
        <strong>엄홍열 교수</strong>
      </article>
      <article class="identity-item">
        <span>소속</span>
        <strong>순천향대학교 산학협력단 산하</strong>
      </article>
      <article class="identity-item">
        <span>위치</span>
        <strong>공과대학 9332호</strong>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="site-shell">
    <div class="section__heading">
      <p class="eyebrow">About the Center</p>
      <h2>센터 소개</h2>
      <p>아래와 같은 활동을 중점으로 진행하고 있습니다.</p>
    </div>
    <div class="editorial-grid">
      <article class="editorial-block">
        <h3>실무 중심 연구</h3>
        <p>악성코드 샘플 수집부터 리버스 엔지니어링, 대응 방안 수립까지 실제 분석 흐름을 중심으로 연구합니다.</p>
      </article>
      <article class="editorial-block">
        <h3>사이버 범죄 추적</h3>
        <p>침해사고 발생 시 해커 그룹과 범죄 행위를 신속히 추적할 수 있는 분석 역량을 강화합니다.</p>
      </article>
      <article class="editorial-block">
        <h3>기관 협력 네트워크</h3>
        <p>국내외 유관기관과의 협력 및 정보 공유를 통해 실무 능력 향상과 공동 대응 기반을 구축합니다.</p>
      </article>
    </div>
  </div>
</section>

<section class="section section--band">
  <div class="site-shell">
    <div class="section__heading section__heading--split">
      <div>
        <p class="eyebrow">Core Research</p>
        <h2>주요 연구 분야</h2>
      </div>
      <p>다음과 같이 주요 연구 분야를 설정한 후, 다양한 연구를 진행하고 있습니다.</p>
    </div>
    <div class="focus-list">
      {% for area in site.data.site.research_areas %}
      <article class="focus-item">
        <span class="focus-item__index">0{{ forloop.index }}</span>
        <div>
          <h3>{{ area.title }}</h3>
          <p>{{ area.description }}</p>
        </div>
      </article>
      {% endfor %}
    </div>
  </div>
</section>

<section class="section">
  <div class="site-shell">
    <div class="section__heading section__heading--split">
      <div>
        <p class="eyebrow">Latest News</p>
        <h2>최근 센터 소식</h2>
      </div>
      <a class="text-link" href="{{ '/news/' | relative_url }}">전체 소식 보기</a>
    </div>
    <div class="archive-list">
      {% assign latest_news = site.news | sort: "date" | reverse | slice: 0, 2 %}
      {% for post in latest_news %}
      <article class="archive-item">
        <div class="archive-item__date">
          <span>{{ post.date | date: "%Y" }}</span>
          <strong>{{ post.date | date: "%m.%d" }}</strong>
        </div>
        <div class="archive-item__body">
          <p class="meta">{{ post.category }}</p>
          <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
          <p>{{ post.excerpt | strip_html | truncate: 140 }}</p>
        </div>
      </article>
      {% endfor %}
    </div>
  </div>
</section>

<section class="section">
  <div class="site-shell">
    <div class="section__heading section__heading--split">
      <div>
        <p class="eyebrow">CSRC Weblog</p>
        <h2>센터 블로그</h2>
      </div>
      <a class="text-link" href="{{ '/blog/' | relative_url }}">블로그 전체 보기</a>
    </div>
    <div class="blog-teasers">
      {% assign latest_blog = site.blog | sort: "date" | reverse | slice: 0, 2 %}
      {% for post in latest_blog %}
      <article class="blog-teaser">
        <p class="meta">{{ post.date | date: "%Y.%m.%d" }} · {{ post.topic }}</p>
        <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        <p>{{ post.excerpt | strip_html | truncate: 150 }}</p>
      </article>
      {% endfor %}
    </div>
  </div>
</section>

<section class="section">
  <div class="site-shell">
    <div class="section__heading">
      <p class="eyebrow">Center Overview</p>
      <h2>센터 현황</h2>
    </div>
    <div class="link-panels link-panels--wide">
      <article class="link-panel">
        <h3>센터 프로젝트</h3>
        <p>센터에서 수행 중인 프로젝트와 연구 결과, 산출물를 확인할 수 있습니다.</p>
        <a class="text-link" href="{{ '/projects/' | relative_url }}">프로젝트 페이지 이동</a>
      </article>
      <article class="link-panel">
        <h3>센터 인프라</h3>
        <p>센터가 운영 중인 NAS, 서버, 공용 서비스 등 연구 지원 인프라 구성을 소개합니다.</p>
        <a class="text-link" href="{{ '/infrastructure/' | relative_url }}">인프라 페이지 이동</a>
      </article>
      <article class="link-panel">
        <h3>연구원 현황</h3>
        <p>현재 활동 중인 연구원과 센터를 거쳐간 연구원의 진학 및 진출 현황을 소개합니다.</p>
        <a class="text-link" href="{{ '/researchers/' | relative_url }}">연구원 페이지 이동</a>
      </article>
      <article class="link-panel">
        <h3>센터 연혁</h3>
        <p>설립 배경과 주요 협약, 활동, 연도별 성과를 타임라인으로 확인하실 수 있습니다.</p>
        <a class="text-link" href="{{ '/history/' | relative_url }}">연혁 페이지 이동</a>
      </article>
    </div>
  </div>
</section>
