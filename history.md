---
title: 센터 연혁
permalink: /history/
---

<section class="page-hero">
  <div class="site-shell">
    <p class="eyebrow">History</p>
    <h1>센터 연혁</h1>
    <p>센터 설립 배경부터 주요 협약, 활동, 연도별 성과를 시간순으로 정리했습니다.</p>
  </div>
</section>

<section class="section">
  <div class="site-shell">
    <div class="timeline">
      {% for item in site.data.history %}
      <article class="timeline__item">
        <div class="timeline__year">{{ item.year }}</div>
        <div class="timeline__content">
          <p class="meta">{{ item.label }}</p>
          <h2>{{ item.title }}</h2>
          <p>{{ item.description }}</p>
        </div>
      </article>
      {% endfor %}
    </div>
  </div>
</section>
