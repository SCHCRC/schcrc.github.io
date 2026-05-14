---
title: 센터 블로그
permalink: /blog/
---

<section class="page-hero">
  <div class="site-shell">
    <p class="eyebrow">Research Blog</p>
    <h1>센터 블로그</h1>
    <p>연구 주제, 분석 사례, 기술 보고서를 공개하는 공간입니다. 마크다운 기반으로 새 글 작성과 수정이 쉽도록 구성했습니다.</p>
  </div>
</section>

<section class="section">
  <div class="site-shell">
    <div class="archive-list archive-list--page">
      {% assign posts = site.blog | sort: "date" | reverse %}
      {% for post in posts %}
      <article class="archive-item archive-item--blog">
        <div class="archive-item__date">
          <span>{{ post.date | date: "%Y" }}</span>
          <strong>{{ post.date | date: "%m.%d" }}</strong>
        </div>
        <div class="archive-item__body">
          <p class="meta">{{ post.topic }}</p>
          <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
          <p>{{ post.excerpt | strip_html | truncate: 190 }}</p>
          <p class="archive-item__link"><a class="text-link" href="{{ post.url | relative_url }}">글 읽기</a></p>
        </div>
      </article>
      {% endfor %}
    </div>
  </div>
</section>
