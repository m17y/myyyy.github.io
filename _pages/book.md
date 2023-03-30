---
layout: page
permalink: /book/
title: 愫读
description: 读万卷书.
book-classification: [经济,科幻,人文,心理学,社会科学,小说,社会科学,洞见]
nav: true
nav_order: 2
---
<!-- _pages/publications.md -->

<div class="publications">
{%- for y in page.book-classification %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[book-classification={{y}}]* %}
{% endfor %}
</div>
