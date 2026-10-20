---
name: markdown-post-formatting
description: "Format and validate Markdown articles in any language. Use when standardizing icons, diagrams, mathematical formulas, or matching a post to an existing style reference."
---

# Markdown Post Formatting

## When to Use

- Normalize a Markdown article to match an existing post's visual conventions, regardless of its language.
- Fix mathematical notation, diagrams, or decorative symbols in technical and general articles.
- Review article formatting without rewriting its technical meaning or translating its content.

## Procedure

1. Read the full target article and the supplied reference article. Treat the reference as the source of formatting conventions, not as content to copy.
2. Preserve the article's language, front matter, meaning, examples, code, tables, links, and citations. Do not translate or localize content unless explicitly requested. Make only formatting changes requested or required for consistency.
3. Match the reference's math delimiters:
   - Use `$...$` for inline math.
   - Put display math between `$$` delimiters on their own lines.
   - Do not use `\(...\)` or `\[...\]` when the reference uses dollar delimiters.
   - Keep math inside fenced examples untouched when it is sample input or literal code.
4. Match the reference's diagram style:
   - Use fenced `mermaid` flowcharts for processes and architecture diagrams when supported by the site.
   - Use Markdown lists for simple hierarchies.
   - Avoid drawing diagrams with Unicode box characters or arrow glyphs in fenced `text` blocks.
   - Keep code fences for actual code, data, prompts, and literal examples.
5. Follow the reference's icon and emoji use. Do not add decorative emoji or symbols when the reference uses none; preserve meaningful symbols in technical examples.
6. Validate the result:
   - Check that each math block has matching delimiters and that inline math is consistently delimited.
   - Check Mermaid syntax and fence closure.
   - Confirm headings, front matter, links, tables, and code examples remain intact.
   - Review the diff to ensure prose and technical claims were not changed unintentionally.
