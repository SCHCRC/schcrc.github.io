---
description: 순천향대학교 산학협력단 산하 SCH사이버보안연구센터. 학부 연구원이 랜섬웨어와 인포스틸러를 직접 분석해 반기마다 보고서를 공개합니다.
title: SCH사이버보안연구센터
permalink: /
---

{% assign recruit = site.news | where: "category", "모집" | sort: "date" | last %}
{% assign reports = site.blog | where: "topic", "분석 보고서" | sort: "date" | reverse %}
{% assign latest_news = site.news | sort: "date" | reverse %}
{% assign projects = site.project_pages | sort: "date" | reverse %}
{% assign latest_blog = site.blog | sort: "date" | reverse %}
{% assign alumni = site.data.researchers.alumni | sort: "generation" | reverse %}

<section class="hero">
  <div class="hero__bg" aria-hidden="true"></div>
  <div class="site-shell hero__inner">
    <div class="hero__content">
      <h1>
        <span class="hero__line"><span>악성코드를 분석하고,</span></span>
        <span class="hero__line"><span>분석한 것을 공개합니다</span></span>
        <span class="hero__en">SCH Cybersecurity Research Center</span>
      </h1>
      <p class="hero__lead">
        순천향대학교 산학협력단 산하 연구센터입니다. 학부 연구원이 악성코드를 직접 분석하고,
        그 결과를 반기 보고서로 공개합니다.
      </p>
      {% comment %} 마감된 뒤에도 '모집 안내'를 주 버튼에 두면 열려 있는 것처럼 읽힌다. {% endcomment %}
      {% assign today = 'now' | date: '%Y%m%d' | plus: 0 %}
      {% if recruit.closes %}
        {% assign recruit_closes = recruit.closes | date: '%Y%m%d' | plus: 0 %}
      {% else %}
        {% assign recruit_closes = recruit.date | date: '%Y%m%d' | plus: 0 %}
      {% endif %}
      <div class="hero__actions">
        {% if recruit and recruit_closes >= today %}
        <a class="button button--primary" href="{{ recruit.url | relative_url }}">{{ recruit.generation | default: 26 }}기 연구원 모집 중</a>
        {% else %}
        <a class="button button--primary" href="{{ '/blog/' | relative_url }}">분석 보고서 보기</a>
        {% endif %}
        <a class="button button--ghost" href="{{ '/projects/' | relative_url }}">수행 프로젝트 보기</a>
      </div>
      <dl class="hero__facts">
        <div>
          <dt>센터장</dt>
          <dd>염흥열 교수</dd>
        </div>
        <div>
          <dt>설립</dt>
          <dd>2013년 12월</dd>
        </div>
        <div>
          <dt>공개 보고서</dt>
          <dd>{{ reports.size }}권 · 반기 발간</dd>
        </div>
        <div>
          <dt>배출 연구원</dt>
          <dd>{{ alumni.size }}명 · 14기부터</dd>
        </div>
      </dl>
    </div>

    <div class="hero__aside">
      {% assign top_report = reports | first %}
      {% if top_report %}
      {% assign top_file = top_report.attachments | first %}
      <h2>
        최신 보고서
        <a href="{{ '/blog/' | relative_url }}" aria-label="보고서 전체 보기">전체 보기</a>
      </h2>
      <div class="hero__report">
        <p class="meta">{{ top_report.date | date: "%Y.%m" }} 발간</p>
        <h3><a href="{{ top_report.url | relative_url }}">{{ top_report.title }}</a></h3>
        {% if top_file.description %}<p>{{ top_file.description }}</p>{% endif %}
        {% if top_file %}
        <p><a class="text-link" href="{{ top_file.url | relative_url }}" download aria-label="{{ top_report.title }} PDF 내려받기">PDF 내려받기</a></p>
        {% endif %}
      </div>
      {% endif %}
      <h2>
        최근 소식
        <a href="{{ '/news/' | relative_url }}" aria-label="센터 소식 전체 보기">전체 보기</a>
      </h2>
      <ul class="mini-list">
        {% for post in latest_news limit: 3 %}
        <li>
          <a href="{{ post.url | relative_url }}">
            <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y.%m.%d" }} · {{ post.category }}</time>
            <strong>{{ post.title }}</strong>
          </a>
        </li>
        {% endfor %}
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="site-shell">
    <div class="section__heading">
      <h2>주요 연구 분야</h2>
    </div>
    <div class="focus-list">
      {% for area in site.data.site.research_areas %}
      <article class="focus-item">
        <h3>{{ area.title }}</h3>
        <p>{{ area.description }}</p>
      </article>
      {% endfor %}
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="site-shell">
    <div class="section__heading section__heading--split">
      <div>
        <h2>발간 보고서</h2>
        <p>2022년부터 반기마다 발간합니다. PDF 원문을 그대로 올립니다.</p>
      </div>
      <a class="text-link" href="{{ '/blog/' | relative_url }}">보고서 전체 보기</a>
    </div>
    {% if reports.size > 0 %}
    <div class="report-list">
      {% for post in reports %}
      {% assign file = post.attachments | first %}
      <article class="report-item">
        <p class="report-item__year"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y.%m" }}</time> 발간</p>
        <div class="report-item__body">
          <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
          <p>{% if file.description %}{{ file.description }}{% else %}{{ post.excerpt | strip_html | truncate: 150 }}{% endif %}</p>
        </div>
        <p class="report-item__action">
          {% if file %}
          <a class="text-link" href="{{ file.url | relative_url }}" download aria-label="{{ post.title }} PDF 내려받기">PDF 내려받기</a>
          {% else %}
          <a class="text-link" href="{{ post.url | relative_url }}">본문 보기</a>
          {% endif %}
        </p>
      </article>
      {% endfor %}
    </div>
    {% else %}
    <p class="empty-state">아직 공개된 보고서가 없습니다.</p>
    {% endif %}
  </div>
</section>

<section class="section">
  <div class="site-shell">
    <div class="section__heading section__heading--split">
      <div>
        <h2>수행 프로젝트</h2>
        <p>기수별 분석 도구와 탐지 모델, 그리고 매년 운영하는 신입 교육 과정.</p>
      </div>
      <a class="text-link" href="{{ '/projects/' | relative_url }}">프로젝트 전체 보기</a>
    </div>
    <div class="project-list">
      {% for item in projects limit: 6 %}
      {% include project-row.html item=item %}
      {% endfor %}
    </div>
  </div>
</section>

<section class="section section--tinted">
  <div class="site-shell">
    <div class="section__heading section__heading--split">
      <div>
        <h2>센터 블로그</h2>
      </div>
      <a class="text-link" href="{{ '/blog/' | relative_url }}">블로그 전체 보기</a>
    </div>
    {% comment %} 3열 격자였을 때 국문 줄당 18자로 끊겨 읽기 리듬이 깨졌다.
       사이트의 다른 목록과 같은 하한선 행으로 통일한다. {% endcomment %}
    <div class="archive-list">
      {% for post in latest_blog limit: 3 %}
      <article class="archive-item">
        <div class="archive-item__date">
          <span>{{ post.date | date: "%Y" }}</span>
          <strong>{{ post.date | date: "%m.%d" }}</strong>
        </div>
        <div class="archive-item__body">
          <p class="meta">{{ post.topic }}</p>
          <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
          <p>{{ post.excerpt | strip_html | truncate: 150 }}</p>
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
        <h2>연구원 진로</h2>
        <p>14기부터 22기까지, 센터를 거쳐 나간 연구원이 어디로 갔는지입니다.</p>
      </div>
      <a class="text-link" href="{{ '/researchers/' | relative_url }}">연구원 현황 보기</a>
    </div>
    <div class="table-scroll">
      <table class="outcome-table">
        <caption class="visually-hidden">기수별 졸업 및 진출 연구원 기록</caption>
        <thead>
          <tr>
            <th scope="col">기수</th>
            <th scope="col">이름</th>
            <th scope="col">진학 및 진출</th>
          </tr>
        </thead>
        <tbody>
          {% for person in alumni limit: 6 %}
          {% assign detail = site.people | where: "slug", person.slug | first %}
          <tr>
            <td>{{ person.generation }}기</td>
            <td>
              {% if detail %}<a href="{{ detail.url | relative_url }}">{{ person.name }}</a>{% else %}{{ person.name }}{% endif %}
            </td>
            <td>{{ person.outcome }}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section section--tinted">
  <div class="site-shell">
    <div class="section__heading">
      <h2>센터 현황</h2>
    </div>
    <div class="link-panels">
      <article class="link-panel">
        <h3>센터 인프라</h3>
        <p>NAS, 분석 서버, 내부 Wiki.</p>
        <a class="text-link" href="{{ '/infrastructure/' | relative_url }}">인프라 보기</a>
      </article>
      <article class="link-panel">
        <h3>연구원 현황</h3>
        <p>현재 연구원 {{ site.data.researchers.current | size }}명, 졸업·진출 연구원 {{ alumni | size }}명.</p>
        <a class="text-link" href="{{ '/researchers/' | relative_url }}">연구원 보기</a>
      </article>
      <article class="link-panel">
        <h3>센터 연혁</h3>
        <p>2013년 설립부터 지금까지.</p>
        <a class="text-link" href="{{ '/history/' | relative_url }}">연혁 보기</a>
      </article>
    </div>
  </div>
</section>
