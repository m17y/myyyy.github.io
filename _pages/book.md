---
layout: page
permalink: /book/
title: 愫读
description: 读万卷书.
book-classification: [洞见,哲学,人文,科幻,经济,小说,心理学,社会科学]
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
