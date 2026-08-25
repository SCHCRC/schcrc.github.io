---
description: SCH사이버보안연구센터가 연구에 쓰는 공용 NAS, 악성코드 분석 서버, 내부 Wiki 등 인프라 현황.
title: 센터 인프라
permalink: /infrastructure/
---

<section class="page-hero">
  <div class="site-shell">
    <h1>센터 인프라</h1>
    <p>NAS, 연구 서버, 내부 Wiki. 접근 권한은 각 서비스에서 확인합니다.</p>
  </div>
</section>

<section class="section">
  <div class="site-shell">
    <div class="section__heading">
      <h2>운영 구성</h2>
      <p>센터 연구에 쓰는 공용 자원입니다.</p>
    </div>
    {% if site.data.infrastructure.size > 0 %}
    <div class="resource-list">
      {% for item in site.data.infrastructure %}
      <article class="resource-item">
        <div class="resource-item__head">
          <p class="meta">{{ item.type }}{% if item.access %} · {{ item.access }}{% endif %}</p>
          <h3>{{ item.title }}</h3>
        </div>
        <div class="resource-item__body">
          <p>{{ item.summary }}</p>
          {% if item.url and item.url != "" %}
          <div class="resource-links"><a href="{{ item.url }}">{{ item.url }}</a></div>
          {% else %}
          <p class="resource-empty">접속 URL은 아직 공개되지 않았습니다.</p>
          {% endif %}
          {% if item.notes %}
          <p class="meta">{{ item.notes }}</p>
          {% endif %}
        </div>
      </article>
      {% endfor %}
    </div>
    {% else %}
    <p class="empty-state">등록된 인프라 정보가 없습니다.</p>
    {% endif %}
  </div>
</section>
