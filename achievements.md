---
description: SCH사이버보안연구센터 연구원의 수상, 프로그램 선발, 진출과 진학 기록. 발표자료에 정리된 24~25년도 실적입니다.
title: 센터 실적
permalink: /achievements/
---

{% assign records = site.data.achievements %}
{% assign years = records | map: "year" | uniq | sort | reverse %}
{% assign awards = records | where: "kind", "수상" %}
{% assign picks = records | where: "kind", "선발" %}
{% assign jobs = records | where: "kind", "진출" %}
{% assign grads = records | where: "kind", "진학" %}

<section class="page-hero">
  <div class="site-shell">
    <h1>센터 실적</h1>
    {% comment %} 요약을 별도 섹션으로 두면 한 문장이 밴드 하나를 다 쓴다. 리드에 붙인다. {% endcomment %}
    <p>수상 {{ awards.size }}건, 프로그램 선발 {{ picks.size }}건, 진출 {{ jobs.size }}건, 진학 {{ grads.size }}건.</p>
  </div>
</section>

{% for year in years %}
{% assign items = records | where: "year", year %}
<section class="section{% cycle 'band': '', ' section--tinted' %}">
  <div class="site-shell">
    <div class="section__heading">
      <h2>{{ year }}년</h2>
      <p>{{ items.size }}건</p>
    </div>
    <div class="report-list">
      {% for record in items %}
      <article class="report-item">
        <p class="report-item__year">{{ record.kind }}</p>
        <div class="report-item__body">
          <h3>{{ record.title }}</h3>
          {% if record.org %}{% unless record.title contains record.org %}<p>{{ record.org }}</p>{% endunless %}{% endif %}
        </div>
        <p class="report-item__action">
          {% for member in record.members %}
            {% assign detail = site.people | where: "slug", member.slug | first %}
            {% if detail %}<a href="{{ detail.url | relative_url }}">{{ member.generation }}기 {{ member.name }}</a>{% else %}{{ member.generation }}기 {{ member.name }}{% endif %}{% unless forloop.last %} · {% endunless %}
          {% endfor %}
        </p>
      </article>
      {% endfor %}
    </div>
  </div>
</section>
{% endfor %}
