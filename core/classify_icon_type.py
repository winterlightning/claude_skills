#!/usr/bin/env python3
"""Write a size-based `icon_type.txt` (sub or normal) beside every pack prototype.

The classifier measures each `sym_*/<sid>_prototype.svg` with `bbox_zones.measure`
and compares the longer side of its painted bounding box, in prototype units,
against `--sub-max` (default 12, half of the 24u art box used by symbol-library
prototypes). At or below that size the symbol is `sub`; above it, `normal`.

It never writes `container`: that is a later agent decision made by the generate
skill for `normal` symbols. An existing `container` verdict is preserved unless
`--overwrite` is passed, so re-running the classifier does not undo review work.

    python3 core/classify_icon_type.py <pack-root-or-batch> [...]
    python3 core/classify_icon_type.py <batch> --dry-run --json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from bbox_zones import measure

FILENAME = "icon_type.txt"
SUB_MAX = 12.0
CLASSIFIER_TYPES = ("sub", "normal")
PRESERVED_TYPES = ("container",)


def classify(size: float, sub_max: float = SUB_MAX) -> str:
    return "sub" if size <= sub_max else "normal"


def prototypes(inputs: list[str]) -> list[Path]:
    """Collect every `sym_*/<sid>_prototype.svg` under the given folders or files."""
    found: set[Path] = set()
    for raw in inputs:
        path = Path(raw).expanduser().resolve()
        if path.is_file():
            if path.suffix.lower() == ".svg" and path.stem.endswith("_prototype"):
                found.add(path)
            else:
                print(f"warn: not a prototype SVG: {path}", file=sys.stderr)
        elif path.is_dir():
            if path.name.startswith("sym_"):
                found.update(item for item in path.glob(f"{path.name}_prototype.svg") if item.is_file())
            else:
                found.update(item for item in path.glob("**/sym_*/sym_*_prototype.svg") if item.is_file())
        else:
            print(f"warn: skipping missing input: {path}", file=sys.stderr)
    return sorted(item for item in found if item.parent.name == item.stem.removesuffix("_prototype"))


def existing_type(path: Path) -> str | None:
    if not path.is_file():
        return None
    first = path.read_text(encoding="utf-8").strip().splitlines()
    return first[0].strip() if first else None


def classify_prototype(prototype: Path, sub_max: float, include_stroke: bool,
                       overwrite: bool, dry_run: bool) -> dict:
    result = measure(prototype, include_stroke=include_stroke)
    size = max(result["bbox"]["width"], result["bbox"]["height"])
    target = prototype.parent / FILENAME
    previous = existing_type(target)
    kind = classify(size, sub_max)
    action = "write"
    if previous in PRESERVED_TYPES and not overwrite:
        kind, action = previous, "preserve"
    elif previous == kind:
        action = "unchanged"
    if action == "write" and not dry_run:
        target.write_text(kind + "\n", encoding="utf-8")
    return {
        "sid": prototype.parent.name,
        "prototype": str(prototype),
        "file": str(target),
        "size": round(size, 4),
        "width": round(result["bbox"]["width"], 4),
        "height": round(result["bbox"]["height"], 4),
        "type": kind,
        "previous": previous,
        "action": action if not dry_run or action != "write" else "would-write",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("inputs", nargs="+", help="pack roots, batch folders, sym_* folders, or prototype SVGs")
    parser.add_argument("--sub-max", type=float, default=SUB_MAX,
                        help=f"longest painted side (prototype units) at or below which a symbol is sub (default {SUB_MAX:g})")
    parser.add_argument("--no-stroke", action="store_true", help="measure centerline geometry only, ignoring stroke width")
    parser.add_argument("--overwrite", action="store_true", help="replace an existing container verdict with the size result")
    parser.add_argument("--dry-run", action="store_true", help="report only; write no icon_type.txt")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = parser.parse_args()

    files = prototypes(args.inputs)
    if not files:
        print("error: no sym_*/<sid>_prototype.svg found", file=sys.stderr)
        return 2

    rows, failures = [], []
    for prototype in files:
        try:
            rows.append(classify_prototype(prototype, args.sub_max, not args.no_stroke, args.overwrite, args.dry_run))
        except Exception as error:  # noqa: BLE001 - one bad prototype must not stop the batch
            failures.append({"prototype": str(prototype), "error": str(error)})
            print(f"error: {prototype}: {error}", file=sys.stderr)

    counts = {kind: sum(1 for row in rows if row["type"] == kind) for kind in CLASSIFIER_TYPES + PRESERVED_TYPES}
    counts = {kind: count for kind, count in counts.items() if count}
    if args.json:
        print(json.dumps({"subMax": args.sub_max, "dryRun": args.dry_run, "counts": counts,
                          "symbols": rows, "failures": failures}, indent=2))
    else:
        for row in rows:
            print(f"{row['sid']}  {row['size']:6.2f}u  {row['type']:<9}  {row['action']}")
        summary = ", ".join(f"{count} {kind}" for kind, count in counts.items())
        print(f"{len(rows)} classified ({summary}); {len(failures)} failed"
              + ("; dry run, nothing written" if args.dry_run else ""))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
