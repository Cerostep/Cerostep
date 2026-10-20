#!/usr/bin/env python3

from datetime import datetime, timezone
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
POSTS = ROOT / "_posts"
LANGUAGE_LABELS = {"zh": "中文", "en": "English"}
START_MARKER = "<!-- latest-articles:start -->"
END_MARKER = "<!-- latest-articles:end -->"


def read_post(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---(?:\s*\n|\Z)", text, re.DOTALL)
    if not match:
        raise ValueError(f"Missing YAML front matter in {path.relative_to(ROOT)}")

    front_matter = match.group(1)
    fields = {}
    for field in ("title", "date", "lang"):
        value = re.search(rf"^{field}:\s*(.*?)\s*$", front_matter, re.MULTILINE)
        if not value:
            raise ValueError(f"Missing `{field}` in {path.relative_to(ROOT)}")
        fields[field] = value.group(1)

    title = fields["title"]
    if len(title) >= 2 and title[0] == title[-1] and title[0] in "\"'":
        title = title[1:-1]

    date_value = fields["date"]
    if len(date_value) >= 2 and date_value[0] == date_value[-1] and date_value[0] in "\"'":
        date_value = date_value[1:-1]
    published_at = datetime.fromisoformat(date_value.replace("Z", "+00:00"))
    if published_at.tzinfo is None:
        published_at = published_at.replace(tzinfo=timezone.utc)

    return {
        "title": title,
        "date": published_at,
        "lang": fields["lang"],
        "path": path,
    }


def main():
    latest_by_language = {}
    for path in POSTS.glob("*.md"):
        post = read_post(path)
        if post["lang"] in LANGUAGE_LABELS:
            current = latest_by_language.get(post["lang"])
            if current is None or post["date"] > current["date"]:
                latest_by_language[post["lang"]] = post

    missing_languages = set(LANGUAGE_LABELS) - latest_by_language.keys()
    if missing_languages:
        raise ValueError(f"No posts found for: {', '.join(sorted(missing_languages))}")

    lines = []
    for language, label in LANGUAGE_LABELS.items():
        post = latest_by_language[language]
        relative_path = post["path"].relative_to(ROOT).as_posix()
        lines.append(f"- {label}: [{post['title']}]({relative_path})")

    readme = README.read_text(encoding="utf-8")
    if readme.count(START_MARKER) != 1 or readme.count(END_MARKER) != 1:
        raise ValueError("README must contain exactly one pair of latest-articles markers")

    start = readme.index(START_MARKER) + len(START_MARKER)
    end = readme.index(END_MARKER)
    if start > end:
        raise ValueError("README latest-articles markers are out of order")

    updated = f"{readme[:start]}\n" + "\n".join(lines) + f"\n{readme[end:]}"
    if updated != readme:
        README.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
