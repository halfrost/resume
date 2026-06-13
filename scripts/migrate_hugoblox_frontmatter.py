#!/usr/bin/env python3
"""Migrate deprecated HugoBlox front matter fields without reformatting files."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"

LEGACY_LINK_FIELDS = {
    "external_link": "site",
    "url_pdf": "pdf",
    "url_preprint": "preprint",
    "url_code": "code",
    "url_dataset": "dataset",
    "url_poster": "poster",
    "url_project": "project",
    "url_slides": "slides",
    "url_source": "source",
    "url_video": "video",
}

PUBLICATION_TYPE_MAP = {
    "0": "article",
    "1": "paper-conference",
    "2": "article-journal",
    "3": "article",
    "4": "report",
    "5": "book",
    "6": "chapter",
    "7": "thesis",
    "8": "patent",
}

FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)


def quote(value: object) -> str:
    return "'" + str(value).replace("'", "''") + "'"


def replace_scalar_line(front_matter: str, key: str, replacement: str = "") -> str:
    pattern = re.compile(rf"(?m)^{re.escape(key)}:[^\n]*(?:\n|\Z)")
    return pattern.sub(replacement, front_matter, count=1)


def append_links(front_matter: str, links: list[tuple[str, str]]) -> str:
    if not links:
        return front_matter

    lines = front_matter.splitlines(keepends=True)
    links_index = next(
        (index for index, line in enumerate(lines) if re.match(r"^links:\s*$", line)),
        None,
    )

    if links_index is None:
        rendered = "".join(
            f"- type: {link_type}\n  url: {quote(url)}\n"
            for link_type, url in links
        )
        return front_matter.rstrip() + "\n\nlinks:\n" + rendered.rstrip() + "\n"

    end = len(lines)
    item_indent = "  "
    for index in range(links_index + 1, len(lines)):
        item_match = re.match(r"^(\s*)-", lines[index])
        if item_match:
            item_indent = item_match.group(1)
            break

    rendered = "".join(
        f"{item_indent}- type: {link_type}\n"
        f"{item_indent}  url: {quote(url)}\n"
        for link_type, url in links
    )
    for index in range(links_index + 1, len(lines)):
        if re.match(r"^[A-Za-z0-9_-]+:", lines[index]):
            end = index
            break

    lines.insert(end, rendered)
    return "".join(lines)


def migrate(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER.match(text)
    if not match:
        return False

    front_matter = match.group(1) + "\n"
    data = yaml.safe_load(front_matter) or {}
    migrated = front_matter

    current_links = {
        (str(item.get("type", "")), str(item.get("url", "")))
        for item in data.get("links", []) or []
        if isinstance(item, dict)
    }
    new_links: list[tuple[str, str]] = []
    for field, link_type in LEGACY_LINK_FIELDS.items():
        value = data.get(field)
        if value and (link_type, str(value)) not in current_links:
            new_links.append((link_type, str(value)))
        migrated = replace_scalar_line(migrated, field)

    if "publication" in data and not isinstance(data["publication"], dict):
        publication = data.get("publication") or ""
        short_name = data.get("publication_short") or ""
        replacement = "publication:\n"
        if publication:
            replacement += f"  name: {quote(publication)}\n"
        if short_name:
            replacement += f"  short_name: {quote(short_name)}\n"
        migrated = replace_scalar_line(migrated, "publication", replacement)
        migrated = replace_scalar_line(migrated, "publication_short")

    publication_types = data.get("publication_types")
    if isinstance(publication_types, list):
        converted = [
            PUBLICATION_TYPE_MAP.get(str(value), str(value))
            for value in publication_types
        ]
        if converted != [str(value) for value in publication_types]:
            rendered = ", ".join(quote(value) for value in converted)
            migrated = replace_scalar_line(
                migrated, "publication_types", f"publication_types: [{rendered}]\n"
            )

    doi = data.get("doi")
    if doi:
        raise ValueError(f"{path}: non-empty legacy doi needs manual migration")
    migrated = replace_scalar_line(migrated, "doi")

    migrated = append_links(migrated, new_links)
    migrated = re.sub(r"\n{3,}", "\n\n", migrated).rstrip() + "\n"

    yaml.safe_load(migrated)
    if migrated == front_matter:
        return False

    updated = text[: match.start(1)] + migrated.rstrip("\n") + text[match.end(1) :]
    path.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    changed = []
    for path in sorted(CONTENT.rglob("*.md")):
        if migrate(path):
            changed.append(path.relative_to(ROOT))

    for path in changed:
        print(path)
    print(f"Migrated {len(changed)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
