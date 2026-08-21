---
title: 센터 연혁
permalink: /history/
---

<section class="page-hero">
  <div class="site-shell">
    <h1>센터 연혁</h1>
    <p>2013년 설립부터 지금까지.</p>
  </div>
</section>

<section class="section">
  <div class="site-shell">
    <div class="timeline">
      {% for item in site.data.history %}
      <article class="timeline__item">
        <p class="timeline__year">{{ item.year }}</p>
        <div class="timeline__content">
          <p class="meta">{{ item.label }}</p>
          <h2>{{ item.title }}</h2>
          <p>{{ item.description }}</p>
          {% if item.image %}
          <figure class="timeline__figure">
            <img src="{{ item.image | relative_url }}" alt="{{ item.image_alt | default: item.title }}" width="200" height="200" loading="lazy">
          </figure>
          {% endif %}
        </div>
      </article>
      {% endfor %}
    </div>
  </div>
</section>
