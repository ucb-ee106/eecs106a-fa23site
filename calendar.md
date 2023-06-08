---
layout: page
title: Semester Calendar
nav_order: 3
description: An embedded Google Calendar displaying the weekly event schedule.
---

# Course Calendar
Lecture recordings can be found <a href="https://bcourses.berkeley.edu/courses/1518829/external_tools/78985">here</a>

{% for module in site.modules %}
{{ module }}
{% endfor %}

---
