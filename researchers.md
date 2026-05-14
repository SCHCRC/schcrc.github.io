---
title: 연구원 현황
permalink: /researchers/
---

<section class="page-hero">
  <div class="site-shell">
    <p class="eyebrow">Researchers</p>
    <h1>센터 연구원 현황</h1>
    <p>현재 활동 중인 연구원과 졸업 후 진학 및 취업으로 센터를 거쳐간 연구원을 구분해 소개합니다.</p>
  </div>
</section>

<section class="section">
  <div class="site-shell">
    <div class="section__heading">
      <h2>현재 연구원</h2>
      <p>운영 중인 기수 및 담당 분야를 한눈에 볼 수 있도록 정리했습니다.</p>
    </div>
    <div class="people-list">
      {% for person in site.data.researchers.current %}
      {% assign detail = site.people | where: "slug", person.slug | first %}
      <article class="person-row">
        <div class="person-row__head">
          <p class="meta">{{ person.generation }}기 · {{ person.role }}</p>
          <h3>
            {% if detail %}
            <a href="{{ detail.url | relative_url }}">{{ person.name }}</a>
            {% else %}
            {{ person.name }}
            {% endif %}
          </h3>
        </div>
        <div class="person-row__body">
          <p>{{ person.focus }}</p>
          <ul class="tag-list">
            {% for tag in person.tags %}
            <li>{{ tag }}</li>
            {% endfor %}
          </ul>
          {% if detail %}
          <p class="person-row__link"><a class="text-link" href="{{ detail.url | relative_url }}">상세 연구 이력 보기</a></p>
          {% endif %}
        </div>
      </article>
      {% endfor %}
    </div>
  </div>
</section>

<section class="section">
  <div class="site-shell">
    <div class="section__heading">
      <h2>졸업 및 진출 연구원</h2>
      <p>발표자료에 포함된 진학 및 취업 성과를 바탕으로 정리한 이력입니다.</p>
    </div>
    <div class="timeline">
      {% for person in site.data.researchers.alumni %}
      {% assign detail = site.people | where: "slug", person.slug | first %}
      <article class="timeline__item">
        <div class="timeline__year">{{ person.generation }}기</div>
        <div class="timeline__content">
          <h3>
            {% if detail %}
            <a href="{{ detail.url | relative_url }}">{{ person.name }}</a>
            {% else %}
            {{ person.name }}
            {% endif %}
          </h3>
          <p>{{ person.outcome }}</p>
          {% if detail %}
          <p class="person-row__link"><a class="text-link" href="{{ detail.url | relative_url }}">상세 연구 이력 보기</a></p>
          {% endif %}
        </div>
      </article>
      {% endfor %}
    </div>
  </div>
</section>
