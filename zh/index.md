---
layout: default
title: 首页
lang: zh
lang_url: /
permalink: /zh/
description: 记录 DevOps 与 AI Agent 的学习、实践和工程经验。
---

# DevOps × AI Agent

Cerostep 是一个关于 DevOps 与 AI Agent 学习和工程实践的博客，关注如何构建、交付和运行 AI 应用，并持续总结实践经验、技术取舍与可复用的方法。

## 关注主题

- **DevOps 与平台工程**：自动化、CI/CD、云原生、可观测性、可靠性及开发者体验。
- **AI Agent 工程**：检索与工具使用、Agent 编排、上下文管理、评估与安全护栏。
- **AI 应用交付与运维**：将 AI 能力融入现有系统，并持续改进质量、成本、延迟与可靠性。
- **通过实践学习**：记录实验、技术决策、问题排查和经验总结。

## 最新文章

{% assign localized_posts = site.posts | where: "lang", page.lang %}
{% for post in localized_posts limit: 5 %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.excerpt | strip_html | strip }}
{% endfor %}

博客提供英文和中文内容，可使用页面顶部的语言切换查看对应译文。
