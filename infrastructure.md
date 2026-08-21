---
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
      <p>접속 URL은 확정된 항목부터 등록합니다.</p>
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
