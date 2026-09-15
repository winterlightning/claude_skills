#!/usr/bin/env python3
"""Fill the $icon-brief prompt template with each folder and save the prompts as JSON and TXT.

Usage:
  python3 icon_set/scripts/brief_prompts.py pictographic-primitives/work
  python3 icon_set/scripts/brief_prompts.py --folders-file folders.txt -o work/brief-prompts.json
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # claude_skills/

# {folder} is replaced with each folder path.
PROMPT = """[$icon-brief](/Applications/Workspaces/pictographic/claude_skills/.agents/skills/icon-brief/SKILL.md)
Using this skill, generate solo brief for these icon in folder {folder}, family: solo, if a folder contain more than 15 files, split, split them into chunk of 15 items, If less than 30, just split by half folder"""


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folders", nargs="*", help="reference folders (relative to claude_skills/)")
    ap.add_argument("--folders-file", help="text file with one folder per line (blank lines ignored)")
    ap.add_argument("-o", "--output", default="work/brief-prompts.json",
                    help="JSON file to write; a copy-paste .txt with the same name is written beside it")
    args = ap.parse_args()

    folders = list(args.folders)
    if args.folders_file:
        folders += [ln.strip() for ln in Path(args.folders_file).read_text().splitlines() if ln.strip()]
    if not folders:
        ap.error("give at least one folder or --folders-file")

    entries = []
    for folder in folders:
        folder = folder.rstrip("/")
        if not (ROOT / folder).is_dir():
            print(f"skip (not a folder): {folder}")
            continue
        entries.append({"folder": folder, "prompt": PROMPT.format(folder=folder)})

    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n")

    txt = output.with_suffix(".txt")
    txt.write_text("\n\n\n".join(
        f"==================== {n}/{len(entries)}  {e['folder']} ====================\n\n{e['prompt']}"
        for n, e in enumerate(entries, 1)
    ) + "\n")
    print(f"{len(entries)} prompt(s) -> {output.relative_to(ROOT)} and {txt.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
