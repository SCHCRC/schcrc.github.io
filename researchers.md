---
description: SCH사이버보안연구센터의 현재 연구원과 졸업·진출 연구원 명단. 기수별 진학 및 진출 기록을 함께 정리했습니다.
title: 연구원 현황
permalink: /researchers/
---

<section class="page-hero">
  <div class="site-shell">
    <h1>연구원 현황</h1>
    <p>현재 연구원과, 센터를 거쳐 나간 연구원.</p>
  </div>
</section>

<section class="section">
  <div class="site-shell">
    <div class="section__heading">
      <h2>현재 연구원</h2>
    </div>
    {% assign current = site.data.researchers.current %}
    {% if current.size > 0 %}
    <div class="people-list">
      {% for person in current %}
      {% assign detail = site.people | where: "slug", person.slug | first %}
      <article class="person-row">
        <div class="person-row__head">
          <p class="meta">{{ person.generation }}기 · {{ person.role }}</p>
          <h3>
            {% if detail %}<a href="{{ detail.url | relative_url }}">{{ person.name }}</a>{% else %}{{ person.name }}{% endif %}
          </h3>
        </div>
        <div class="person-row__body">
          {% if person.focus %}<p>{{ person.focus }}</p>{% endif %}
          {% if person.tags %}
          <ul class="tag-list">
            {% for tag in person.tags %}<li>{{ tag }}</li>{% endfor %}
          </ul>
          {% endif %}
        </div>
      </article>
      {% endfor %}
    </div>
    {% else %}
    <p class="empty-state">현재 등록된 연구원이 없습니다.</p>
    {% endif %}
  </div>
</section>

<section class="section section--tinted">
  <div class="site-shell">
    <div class="section__heading">
      <h2>졸업 및 진출 연구원</h2>
      <p>진로 기록이 비어 있는 항목은 이전 홈페이지 명단에서 이관한 연구원입니다.</p>
    </div>
    {% assign alumni = site.data.researchers.alumni | sort: "generation" | reverse %}
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
          {% for person in alumni %}
          {% assign detail = site.people | where: "slug", person.slug | first %}
          <tr>
            <td>{{ person.generation }}기</td>
            <td>{% if detail %}<a href="{{ detail.url | relative_url }}">{{ person.name }}</a>{% else %}{{ person.name }}{% endif %}</td>
            <td>{{ person.outcome }}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
</section>
