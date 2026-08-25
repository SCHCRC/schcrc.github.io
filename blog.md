---
description: SCH사이버보안연구센터가 발간한 반기 악성코드 분석 보고서와 연구 기록. PDF 원문을 그대로 공개합니다.
title: 센터 블로그
permalink: /blog/
---

<section class="page-hero">
  <div class="site-shell">
    <h1>센터 블로그</h1>
    <p>반기 분석 보고서와 분석 사례, 센터 운영 기록.</p>
  </div>
</section>

<section class="section">
  <div class="site-shell">
    {% assign posts = site.blog | sort: "date" | reverse %}
    {% if posts.size > 0 %}
    <div class="archive-list">
      {% for post in posts %}
      <article class="archive-item">
        <div class="archive-item__date">
          <span>{{ post.date | date: "%Y" }}</span>
          <strong>{{ post.date | date: "%m.%d" }}</strong>
        </div>
        <div class="archive-item__body">
          <p class="meta">{{ post.topic }}{% if post.attachments %} · 첨부 {{ post.attachments | size }}건{% endif %}</p>
          <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
          <p>{{ post.excerpt | strip_html | truncate: 190 }}</p>
          <p class="archive-item__link"><a class="text-link" href="{{ post.url | relative_url }}">글 읽기</a></p>
        </div>
      </article>
      {% endfor %}
    </div>
    {% else %}
    <p class="empty-state">등록된 글이 없습니다.</p>
    {% endif %}
  </div>
</section>
