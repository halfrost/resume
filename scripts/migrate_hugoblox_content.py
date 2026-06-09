#!/usr/bin/env python3
"""Convert this site's 2020 Wowchemy profile widgets to HugoBlox Kit data."""

from pathlib import Path
import re
import tomli

import yaml


ROOT = Path(__file__).resolve().parents[1]


def toml_frontmatter(path):
    text = path.read_text()
    _, frontmatter, _ = text.split("+++", 2)
    return tomli.loads(frontmatter)


def yaml_page(path):
    text = path.read_text()
    _, frontmatter, body = text.split("---", 2)
    return yaml.safe_load(frontmatter), body.strip()


def clean_summary(value):
    value = re.sub(r"<img[^>]*>\s*", "", value or "", flags=re.I)
    return value.strip()


def extract_image(value):
    match = re.search(
        r"<img[^>]+(?:data-src|src)=[\"']([^\"']+)[\"']",
        value or "",
        flags=re.I,
    )
    return match.group(1) if match else ""


profile, bio = yaml_page(ROOT / "content/authors/admin/_index.md")
experience = toml_frontmatter(ROOT / "content/home/experience.md")["experience"]
awards = toml_frontmatter(ROOT / "content/home/accomplishments.md")["item"]
features = toml_frontmatter(ROOT / "content/home/skills.md")["feature"]

author = {
    "schema": "hugoblox/author/v1",
    "slug": "me",
    "is_owner": True,
    "name": {
        "display": profile["title"],
        "given": "Dezhi",
        "family": "Yu",
    },
    "role": profile["role"],
    "bio": bio,
    "affiliations": [
        {
            "name": item["name"],
            **({"url": item["url"]} if item.get("url") else {}),
        }
        for item in profile.get("organizations", [])
    ],
    "links": [
        {"icon": "at-symbol", "url": "/#contact", "label": "Email"},
        {"icon": "brands/linkedin", "url": "https://www.linkedin.com/in/halffrost/"},
        {"icon": "brands/github", "url": "https://github.com/halfrost"},
        {"icon": "brands/twitter", "url": "https://twitter.com/halffrost"},
        {"icon": "brands/weixin", "url": "https://img.halfrost.com/wechat-qr-code.png"},
        {"icon": "hero/globe-alt", "url": "https://halfrost.com"},
    ],
    "interests": profile.get("interests", []),
    "education": [
        {
            "degree": item["course"],
            "institution": item["institution"],
            **({"badge": item["schoolbadge"]} if item.get("schoolbadge") else {}),
        }
        for item in profile.get("education", {}).get("courses", [])
    ],
    "experience": [
        {
            "role": item["title"],
            "org": item["company"],
            **({"url": item["company_url"]} if item.get("company_url") else {}),
            **({"location": item["location"]} if item.get("location") else {}),
            "start": str(item["date_start"]),
            **({"end": str(item["date_end"])} if item.get("date_end") else {}),
            **(
                {"image": extract_image(item.get("description"))}
                if extract_image(item.get("description"))
                else {}
            ),
            **(
                {"summary": clean_summary(item.get("description"))}
                if clean_summary(item.get("description"))
                else {}
            ),
        }
        for item in experience
    ],
    "skills": [
        {
            "name": "Technical Skills",
            "items": [
                {
                    "label": item["name"],
                    **({"icon": item["icon"]} if item.get("icon") else {}),
                    "level": max(
                        1,
                        min(
                            5,
                            round(int(item.get("description", "60%").rstrip("%")) / 20),
                        ),
                    ),
                }
                for item in features
            ],
        }
    ],
    "awards": [
        {
            "title": item["title"],
            "awarder": item["organization"],
            "date": str(item["date_start"]),
            **(
                {"url": item.get("certificate_url") or item.get("url")}
                if item.get("certificate_url") or item.get("url")
                else {}
            ),
            **(
                {"summary": clean_summary(item.get("description"))}
                if clean_summary(item.get("description"))
                else {}
            ),
            "icon": "hero/trophy",
        }
        for item in awards
    ],
}

output = ROOT / "data/authors/me.yaml"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(
    yaml.safe_dump(author, sort_keys=False, allow_unicode=True, width=1000)
)
