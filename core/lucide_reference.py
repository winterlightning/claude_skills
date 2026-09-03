#!/usr/bin/env python3
"""Search and inspect the local, paired Lucide construction-reference snapshot."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

REFERENCE_ROOT = Path(__file__).resolve().parent.parent / "references" / "lucide"
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
ALIASES = {
    "phone": ["handset", "telephone", "call", "receiver"],
    "smartphone": ["mobile", "device", "telephone"],
    "mail": ["envelope", "flap", "message"],
    "ellipsis": ["dots", "more", "horizontal"],
    "user-round": ["person", "bust", "head", "shoulders"],
    "user": ["person", "bust", "head", "shoulders"],
    "hard-hat": ["helmet", "construction", "brim"],
    "drafting-compass": ["hinge", "legs", "drawing"],
    "database": ["cylinder", "tiers", "storage"],
    "scroll": ["rolled", "paper", "blueprint"],
    "scroll-text": ["rolled", "paper", "blueprint"],
    "rectangle-horizontal": ["wide", "frame", "rounded", "container"],
    "rectangle-vertical": ["tall", "frame", "rounded", "container"],
    "square": ["frame", "rounded", "container"],
    "message-square": ["comment", "chat", "speech", "container"],
    "file": ["document", "paper", "fold", "container"],
    "settings": ["cog", "gear", "teeth"],
    "zap": ["lightning", "bolt", "electric"],
    "list-checks": ["checklist", "bullets", "tasks"],
    "corner-up-left": ["reply", "bent", "arrow"],
    "hand": ["holding", "fingers", "grip"],
    "minus": ["line", "divider"],
    "type": ["letter", "glyph", "text"],
}


def reference_paths(name: str, root: Path = REFERENCE_ROOT) -> tuple[Path, Path]:
    if not NAME.fullmatch(name):
        raise ValueError("reference name must be an exact lower-kebab-case icon name")
    paths = (root / "original" / f"{name}.svg", root / "atomic-debug" / f"{name}.svg")
    for path in paths:
        if not path.is_file() or path.is_symlink():
            raise ValueError(f"missing regular reference file: {path}")
    return paths


def build_index(root: Path = REFERENCE_ROOT) -> dict:
    originals = sorted((root / "original").glob("*.svg"))
    if not originals:
        raise ValueError("no original SVG references found")
    names = {p.stem for p in originals}
    if names != {p.stem for p in (root / "atomic-debug").glob("*.svg")}:
        raise ValueError("original and atomic-debug reference names do not match")
    entries = []
    totals = Counter()
    for original in originals:
        original, debug = reference_paths(original.stem, root)
        source_tree = ET.parse(original).getroot()
        debug_tree = ET.parse(debug).getroot()
        kinds = Counter(el.get("data-kind") for el in debug_tree if el.get("data-kind"))
        totals.update(kinds)
        entries.append({
            "name": original.stem,
            "original": original.relative_to(root).as_posix(),
            "debug": debug.relative_to(root).as_posix(),
            "keywords": sorted(set(original.stem.split("-") + ALIASES.get(original.stem, []))),
            "sourceElementCount": len(source_tree),
            "segmentCount": sum(kinds.values()),
            "segmentKinds": dict(sorted(kinds.items())),
            "originalSha256": hashlib.sha256(original.read_bytes()).hexdigest(),
            "debugSha256": hashlib.sha256(debug.read_bytes()).hexdigest(),
        })
    return {
        "schemaVersion": 1,
        "snapshot": "local analyze_lucide corpus imported 2026-09-03; upstream commit unknown",
        "purpose": "Construction evidence, not a mandatory shape catalog or production output.",
        "iconCount": len(entries),
        "segmentCounts": dict(sorted(totals.items())),
        "icons": entries,
    }


def search(query: str, index: dict, limit: int = 6, kind: str | None = None) -> list[dict]:
    tokens = re.findall(r"[a-z0-9]+", query.lower())
    if not tokens and not kind:
        return []
    ranked = []
    for entry in index["icons"]:
        if kind and kind not in entry["segmentKinds"]:
            continue
        words = set(entry["keywords"])
        matched = sum(token in words for token in tokens)
        if tokens and not matched:
            continue
        exact = query.lower().strip().replace(" ", "-") == entry["name"]
        score = (100 if exact else 0) + 10 * matched + (5 if matched == len(tokens) else 0)
        ranked.append((score, entry))
    ranked.sort(key=lambda pair: (-pair[0], len(pair[1]["name"]), pair[1]["name"]))
    return [dict(entry, score=score) for score, entry in ranked[:max(0, limit)]]


def inspect_reference(name: str, root: Path = REFERENCE_ROOT) -> dict:
    original, debug = reference_paths(name, root)
    source_tree = ET.parse(original).getroot()
    debug_tree = ET.parse(debug).getroot()
    return {
        "name": name,
        "original": str(original),
        "debug": str(debug),
        "viewBox": source_tree.get("viewBox"),
        "originalSha256": hashlib.sha256(original.read_bytes()).hexdigest(),
        "sourceElements": [{"index": i, "tag": el.tag.split("}")[-1], "attrs": dict(el.attrib)}
                           for i, el in enumerate(source_tree)],
        "segments": [{"sourceAtom": el.get("data-atom"), "kind": el.get("data-kind"), "d": el.get("d")}
                     for el in debug_tree if el.get("data-atom")],
        "caution": "Debug colors are per-icon segment labels, not semantic categories. Keep source path grouping when authoring.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("index", help="rebuild index.json from the paired snapshot (does not modify SVGs)")
    find = commands.add_parser("search", help="retrieve a few original/debug reference pairs")
    find.add_argument("query")
    find.add_argument("--limit", type=int, default=6)
    find.add_argument("--kind", help="optional debug segment kind, e.g. arc/circular")
    find.add_argument("--json", action="store_true")
    show = commands.add_parser("inspect", help="show original geometry and absolute debug segment paths")
    show.add_argument("name")
    show.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "index":
            data = build_index()
            output = REFERENCE_ROOT / "index.json"
            output.write_text(json.dumps(data, indent=2) + "\n")
            print(f"Indexed {data['iconCount']} paired references -> {output}")
        elif args.command == "inspect":
            data = inspect_reference(args.name)
            if args.json:
                print(json.dumps(data, indent=2))
            else:
                print(f"{data['name']}\nOriginal: {data['original']}\nDebug: {data['debug']}")
                print("Original SVG elements:")
                for element in data["sourceElements"]:
                    print(f"  {element['index']}: {element['tag']} {json.dumps(element['attrs'])}")
                print("Atomic construction:")
                for element in data["segments"]:
                    print(f"  {element['sourceAtom']} {element['kind']}: {element['d']}")
                print(data["caution"])
        else:
            data = json.loads((REFERENCE_ROOT / "index.json").read_text())
            results = search(args.query, data, args.limit, args.kind)
            if args.json:
                print(json.dumps(results, indent=2))
            else:
                for entry in results:
                    print(f"{entry['name']} — {entry['sourceElementCount']} source elements / {entry['segmentCount']} debug segments")
                    print(f"  {REFERENCE_ROOT / entry['original']}\n  {REFERENCE_ROOT / entry['debug']}")
                if not results:
                    print("No matches. Try a simpler subject, synonym, or a construction term.")
    except (OSError, ValueError, ET.ParseError) as error:
        parser.exit(1, f"reference error: {error}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
