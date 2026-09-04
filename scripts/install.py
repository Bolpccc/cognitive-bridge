#!/usr/bin/env python3
"""Install cognitive-bridge with delete-style parity."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target-root", type=Path, default=Path.home() / ".codex" / "skills")
    args = parser.parse_args()
    target_root = args.target_root.expanduser().resolve()
    if target_root == Path(target_root.anchor):
        parser.error("target root may not be a filesystem root")
    target_root.mkdir(parents=True, exist_ok=True)
    target = target_root / "cognitive-bridge"
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(
        REPO_ROOT,
        target,
        ignore=shutil.ignore_patterns(".git", "__pycache__", ".DS_Store"),
    )
    print(f"installed cognitive-bridge -> {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

