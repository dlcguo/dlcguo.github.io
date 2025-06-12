---
layout: page
permalink: /summaries/
title: paper summaries
description: summaries of papers I've read
nav: true
nav_order: 4
---

This page contains summaries of papers I've read and find are interesting. Readers should have some familiarity with the papers.

The intent behind this is to document what I have read and provide others suggestions of papers to read.

{% include scripts/mathjax_macros.html %}

---

<ol>
    {% for summary in site.summaries reversed %}
    <li>
        <a href="{{ summary.url | relative_url }}">
            ({{ summary.date | date: '%b %-d, %Y' }})
            {{ summary.title }}
        </a>
    </li>
    {% endfor %}
</ol>
