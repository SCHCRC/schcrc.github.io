---
description: SCH사이버보안연구센터의 공지, 협약, 활동, 연구원 모집 소식.
title: 센터 소식
permalink: /news/
---

<section class="page-hero">
  <div class="site-shell">
    <h1>센터 소식</h1>
    <p>공지 · 협약 · 행사 참여 · 연구원 모집.</p>
  </div>
</section>

<section class="section">
  <div class="site-shell">
    {% assign posts = site.news | sort: "date" | reverse %}
    {% if posts.size > 0 %}
    <div class="archive-list">
      {% for post in posts %}
      <article class="archive-item">
        <div class="archive-item__date">
          <span>{{ post.date | date: "%Y" }}</span>
          <strong>{{ post.date | date: "%m.%d" }}</strong>
        </div>
        <div class="archive-item__body">
          <p class="meta">{{ post.category }}</p>
          <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
          <p>{{ post.excerpt | strip_html | truncate: 180 }}</p>
        </div>
      </article>
      {% endfor %}
    </div>
    {% else %}
    <p class="empty-state">등록된 소식이 없습니다.</p>
    {% endif %}
  </div>
</section>
