---
description: SCH사이버보안연구센터가 기수별로 수행한 악성코드 분석 도구, 탐지 모델, 침해대응 연구와 신입 교육 과정.
title: 센터 프로젝트
permalink: /projects/
---

<section class="page-hero">
  <div class="site-shell">
    <h1>센터 프로젝트</h1>
    <p>기수별 분석 도구와 탐지 모델, 신입 교육 과정.</p>
  </div>
</section>

<section class="section">
  <div class="site-shell">
    {% assign projects = site.project_pages | sort: "date" | reverse %}
    <div class="section__heading">
      <h2>전체 프로젝트 {{ projects.size }}건</h2>
    </div>
    {% if projects.size > 0 %}
    <div class="project-list">
      {% for item in projects %}
      {% include project-row.html item=item %}
      {% endfor %}
    </div>
    {% else %}
    <p class="empty-state">등록된 프로젝트가 없습니다.</p>
    {% endif %}
  </div>
</section>
