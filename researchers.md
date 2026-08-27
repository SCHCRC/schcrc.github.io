---
description: SCH사이버보안연구센터의 현재 연구원과 졸업·진출 연구원 명단. 기수별 진학 및 진출 기록을 함께 정리했습니다.
title: 연구원 현황
permalink: /researchers/
---

<section class="page-hero">
  <div class="site-shell">
    <h1>연구원 현황</h1>
    <p>현재 연구원과 센터를 거쳐 나간 연구원.</p>
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
      {% comment %} 센터는 1기부터인데 명단은 아직 그 전부를 담지 못했다.
         기수 숫자를 직접 적지 않고 데이터에서 계산해, 이전 기수를 채워 넣으면
         이 안내가 저절로 사라진다. {% endcomment %}
      {% assign first_gen = site.data.site.center.first_generation %}
      {% assign alu_known = site.data.researchers.alumni | where_exp: "p", "p.generation" | sort: "generation" %}
      {% assign alu_unknown = site.data.researchers.alumni | where_exp: "p", "p.generation == nil" %}
      {% assign alu_min = alu_known | first %}
      {% if alu_min.generation > first_gen %}
      <p>지금 정리된 것은 {{ alu_min.generation }}기 이후입니다. {{ first_gen }}기까지 거슬러 채우는 중입니다.</p>
      {% endif %}
    </div>
    {% assign alumni = alu_known | reverse %}
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
            <td>{% if person.generation %}{{ person.generation }}기{% else %}-{% endif %}</td>
            <td>{% if detail %}<a href="{{ detail.url | relative_url }}">{{ person.name }}</a>{% else %}{{ person.name }}{% endif %}</td>
            <td>{{ person.outcome }}</td>
          </tr>
          {% endfor %}
          {% comment %} 기수를 확인할 수 없는 연구원은 정렬 기준이 없으니 끝에 둔다. {% endcomment %}
          {% for person in alu_unknown %}
          {% assign detail = site.people | where: "slug", person.slug | first %}
          <tr>
            <td>-</td>
            <td>{% if detail %}<a href="{{ detail.url | relative_url }}">{{ person.name }}</a>{% else %}{{ person.name }}{% endif %}</td>
            <td>{{ person.outcome }}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
</section>
