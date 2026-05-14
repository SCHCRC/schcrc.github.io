---
title: 센터 프로젝트
permalink: /projects/
---

<section class="page-hero">
  <div class="site-shell">
    <p class="eyebrow">Projects</p>
    <h1>센터 프로젝트</h1>
    <p>센터에서 수행 중인 프로젝트와 연구 주제, 관련 산출물 및 참고 URL을 외부에서도 확인할 수 있도록 정리하는 공간입니다.</p>
  </div>
</section>

<section class="section">
  <div class="site-shell">
    <div class="section__heading">
      <h2>프로젝트 현황</h2>
      <p>프로젝트별 목적, 진행 상태, 결과물 링크를 정리해 센터에서 어떤 연구와 개발이 진행되는지 보여줄 수 있도록 구성했습니다.</p>
    </div>
    <div class="resource-list">
      {% for item in site.data.projects %}
      {% assign detail = site.project_pages | where: "slug", item.slug | first %}
      <article class="resource-item">
        <div class="resource-item__head">
          <p class="meta">{{ item.status }}{% if item.period %} · {{ item.period }}{% endif %}</p>
          <h3>{{ item.title }}</h3>
          {% if detail %}
          <p class="resource-item__head-action">
            <a class="resource-item__button" href="{{ detail.url | relative_url }}">프로젝트 상세 페이지</a>
          </p>
          {% endif %}
        </div>
        <div class="resource-item__body">
          <p>{{ item.summary }}</p>
          {% if item.links %}
          <ul class="resource-links">
            {% for link in item.links %}
            <li><a href="{{ link.url }}">{{ link.label }}</a></li>
            {% endfor %}
          </ul>
          {% endif %}
        </div>
      </article>
      {% endfor %}
    </div>
  </div>
</section>
