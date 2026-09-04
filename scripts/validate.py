#!/usr/bin/env python3
"""Validate cognitive-bridge metadata and relative links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^]]*\]\(([^)]+)\)")


def main() -> int:
    errors: list[str] = []
    manifest = json.loads((REPO_ROOT / "skills-manifest.json").read_text())
    item = manifest["skills"][0]
    skill_file = REPO_ROOT / "SKILL.md"
    agent_file = REPO_ROOT / "agents" / "openai.yaml"
    text = skill_file.read_text()
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    frontmatter = match.group(1) if match else ""
    name = item["name"]
    if not re.search(rf"^name:\s*{re.escape(name)}\s*$", frontmatter, re.M):
        errors.append("frontmatter name does not match manifest")
    if not re.search(r"^description:\s*.+$", frontmatter, re.M):
        errors.append("frontmatter description is missing")
    if f"${name}" not in agent_file.read_text():
        errors.append("default prompt does not invoke $cognitive-bridge")
    for markdown in REPO_ROOT.rglob("*.md"):
        for raw in LINK_RE.findall(markdown.read_text()):
            link = raw.split("#", 1)[0]
            if not link or "{{" in link or "://" in link or link.startswith(("#", "/")):
                continue
            if not (markdown.parent / link).resolve().exists():
                errors.append(f"broken link: {markdown.relative_to(REPO_ROOT)} -> {raw}")
    if errors:
        print("\n".join(sorted(set(errors))), file=sys.stderr)
        return 1
    print("validated cognitive-bridge")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
