#!/usr/bin/env python3
"""Validate cognitive-bridge metadata and relative links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^]]*\]\(([^)]+)\)")
SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")


def metadata_version(frontmatter: str) -> str | None:
    lines = frontmatter.splitlines()
    for index, line in enumerate(lines):
        if line.strip() != "metadata:":
            continue
        for child in lines[index + 1 :]:
            if child and not child[0].isspace():
                break
            match = re.match(r"^\s+version:\s*([^\s]+)\s*$", child)
            if match:
                return match.group(1)
    return None


def main() -> int:
    errors: list[str] = []
    manifest = json.loads((REPO_ROOT / "skills-manifest.json").read_text())
    item = manifest["skills"][0]
    repo_version = (REPO_ROOT / "VERSION").read_text().strip()
    if manifest.get("schema_version") != 1:
        errors.append("unsupported manifest schema_version")
    if not SEMVER_RE.fullmatch(repo_version):
        errors.append("VERSION is not stable SemVer")
    if manifest.get("repository_version") != repo_version:
        errors.append("repository_version does not match VERSION")
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
    skill_version = item.get("version")
    if not isinstance(skill_version, str) or not SEMVER_RE.fullmatch(skill_version):
        errors.append("manifest Skill version is not stable SemVer")
    if metadata_version(frontmatter) != skill_version:
        errors.append("SKILL.md metadata.version does not match manifest")
    if f"## [{repo_version}]" not in (REPO_ROOT / "CHANGELOG.md").read_text():
        errors.append("CHANGELOG.md has no entry for VERSION")
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
