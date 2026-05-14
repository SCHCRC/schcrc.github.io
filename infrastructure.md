---
title: 센터 인프라
permalink: /infrastructure/
---

<section class="page-hero">
  <div class="site-shell">
    <p class="eyebrow">Infrastructure</p>
    <h1>센터 인프라</h1>
    <p>센터에서 운영하는 NAS, 연구 서버, 공용 서비스, 내부 시스템 등 인프라 구성을 소개하고 관련 URL을 안내하는 공간입니다.</p>
  </div>
</section>

<section class="section">
  <div class="site-shell">
    <div class="section__heading">
      <h2>인프라 구성</h2>
      <p>외부 방문자는 센터가 어떤 인프라를 갖추고 있는지 확인할 수 있고, 연구원은 등록된 URL을 통해 필요한 서비스로 바로 이동할 수 있도록 구성했습니다.</p>
    </div>
    <div class="resource-list">
      {% for item in site.data.infrastructure %}
      <article class="resource-item">
        <div class="resource-item__head">
          <p class="meta">{{ item.type }}{% if item.access %} · {{ item.access }}{% endif %}</p>
          <h3>{{ item.title }}</h3>
        </div>
        <div class="resource-item__body">
          <p>{{ item.summary }}</p>
          {% if item.url %}
          <p><a href="{{ item.url }}">{{ item.url }}</a></p>
          {% endif %}
          {% if item.notes %}
          <p class="meta">{{ item.notes }}</p>
          {% endif %}
        </div>
      </article>
      {% endfor %}
    </div>
  </div>
</section>
