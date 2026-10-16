---
layout: default
title: Home
lang: en
lang_url: /zh/
---

# DevOps × AI Agents

Cerostep is a learning and engineering blog about building, delivering, and operating AI-powered systems. It brings together DevOps practices and AI agent engineering, with an emphasis on practical experiments, clear trade-offs, and lessons worth reusing.

## Topics

- **DevOps and platform engineering** — automation, CI/CD, cloud-native practices, observability, reliability, and developer experience.
- **AI agent engineering** — retrieval and tool use, agent orchestration, context management, evaluation, and safety guardrails.
- **AI application delivery and operations** — integrating AI into existing systems while improving quality, cost, latency, and reliability.
- **Learning through practice** — documenting experiments, technical decisions, troubleshooting, and lessons learned.

## Latest article

{% assign localized_posts = site.posts | where: "lang", page.lang %}
{% for post in localized_posts limit: 5 %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.excerpt | strip_html | strip }}
{% endfor %}

The blog is written in English and Chinese. Use the language switch in the header to view the corresponding translation.
