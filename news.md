---
title: 센터 소식
permalink: /news/
---

<section class="page-hero">
  <div class="site-shell">
    <p class="eyebrow">Newsroom</p>
    <h1>센터 소식</h1>
    <p>공지, 행사 참여, 협약 체결, 모집 안내 등 센터 내부에서 직접 올리는 공식 소식 페이지입니다.</p>
  </div>
</section>

<section class="section">
  <div class="site-shell">
    <div class="archive-list archive-list--page">
      {% assign posts = site.news | sort: "date" | reverse %}
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
  </div>
</section>
