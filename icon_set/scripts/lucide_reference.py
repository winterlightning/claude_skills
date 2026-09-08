#!/usr/bin/env python3
"""Search and inspect the local Lucide construction references.

Lucide is **construction evidence**, not a shape catalog and not permission to
substitute a subject. Retrieve the few icons that answer a real design question,
read how their contours flow, then recompose on the selected profile.

Two numbers matter before reading any of it:

* Lucide draws stroke 2 on a 24 canvas; this system draws stroke 4 on 32/48/64.
  Relative to its canvas a Lucide stroke is 1/12 wide and ours is 1/8 — a
  reference is about **1.5x lighter**, so detail that separates cleanly there
  can close up here.
* Lucide coordinates are frequently fractional. Every coordinate in this system
  is an integer on grid 1. A reference proportion is a target to re-derive, not
  a number to copy.

``inspect`` reports an original in this system's terms: normalized commands, the
painted bounding box, the aspect ratio, and which ``Keyshape`` the subject's
proportions actually point at on a chosen profile. It also reports the icon's
**atoms**, read from ``atomic-debug/``: the original's geometry split into one
segment per primitive, each classified as a line, an arc or a curve.

That is the half of a construction reference the outline cannot show you. A
Lucide heart is one ``d`` string; its atoms say it is three circular arcs, two
cubics and two diagonals joined in a ring, which is the shape of the
``add_arc`` / ``add_line`` / ``add_contour`` calls that would rebuild it here.
Read it as an inventory of what the construction is made of -- never as a part
count to match. The decomposition is analyzer output: it splits a native circle
into four quarter-arcs and numbers its colours sequentially, so its segment
count is a property of the analysis, not of the drawing.

    python3 icon_set/scripts/lucide_reference.py search 'cloud' --limit 6
    python3 icon_set/scripts/lucide_reference.py inspect heart --profile SUB32
    python3 icon_set/scripts/lucide_reference.py inspect heart --json
    python3 icon_set/scripts/lucide_reference.py atoms heart
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.model.keyshapes import Keyshape  # noqa: E402
from icon_set.model.profiles import STROKE_WIDTH, Profile  # noqa: E402
from icon_set.validation.envelope import centerline_bounds  # noqa: E402
from icon_set.model.primitives import Arc, Line, Point  # noqa: E402

REFERENCE_ROOT = REPO_ROOT / "icon_set" / "references" / "lucide"
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
NUMBER = re.compile(r"[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?")
PARAMS = {"M": 2, "L": 2, "H": 1, "V": 1, "C": 6, "S": 4, "Q": 4, "T": 2, "A": 7, "Z": 0}

LUCIDE_CANVAS = 24.0
LUCIDE_STROKE = 2.0


# -- index -------------------------------------------------------------------

def load_index(root: Path = REFERENCE_ROOT) -> dict:
    path = root / "index.json"
    if not path.is_file():
        raise ValueError(f"missing reference index: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def debug_path(name: str, root: Path = REFERENCE_ROOT) -> Path:
    """The per-segment view of one reference, with the same name checks."""
    if not NAME.fullmatch(name):
        raise ValueError(f"not a reference name: {name!r}")
    path = root / "atomic-debug" / f"{name}.svg"
    if not path.is_file():
        raise ValueError(f"no atomic-debug view for {name!r}: {path}")
    return path


def read_atoms(name: str, root: Path = REFERENCE_ROOT) -> list[dict]:
    """One row per segment: its index, the element it came from, its kind, its `d`.

    Straight from ``atomic-debug/<name>.svg``, in document order. ``atom`` is
    ``<element>.<segment>``, so the leading number groups segments that came
    out of the same source element and the ring structure survives.
    """
    root_element = ET.parse(debug_path(name, root)).getroot()
    atoms = []
    for element in root_element.iter():
        if _strip(element.tag) != "path":
            continue
        atoms.append({
            "atom": element.get("data-atom", ""),
            "source": element.get("data-src", ""),
            "kind": element.get("data-kind", ""),
            "d": element.get("d", ""),
        })
    return atoms


def original_path(name: str, root: Path = REFERENCE_ROOT) -> Path:
    if not NAME.fullmatch(name):
        raise ValueError("reference name must be an exact lower-kebab-case icon name")
    path = root / "original" / f"{name}.svg"
    if not path.is_file() or path.is_symlink():
        raise ValueError(f"missing regular reference file: {path}")
    return path


def search(query: str, index: dict, limit: int = 6, kind: str | None = None) -> list[dict]:
    """Rank index entries by keyword overlap. Ported unchanged in behaviour."""
    tokens = re.findall(r"[a-z0-9]+", query.lower())
    if not tokens and not kind:
        return []
    ranked = []
    for entry in index["icons"]:
        if kind and kind not in entry.get("segmentKinds", {}):
            continue
        words = set(entry["keywords"])
        matched = sum(token in words for token in tokens)
        if tokens and not matched:
            continue
        exact = query.lower().strip().replace(" ", "-") == entry["name"]
        score = (100 if exact else 0) + 10 * matched + (5 if matched == len(tokens) else 0)
        ranked.append((score, entry))
    ranked.sort(key=lambda pair: (-pair[0], len(pair[1]["name"]), pair[1]["name"]))
    return [dict(entry, score=score) for score, entry in ranked[: max(0, limit)]]


# -- geometry ----------------------------------------------------------------

def _scan(data: str) -> list[tuple[str, list[float]]]:
    """Split path data into (command, numbers) pairs, absolute and relative."""
    out: list[tuple[str, list[float]]] = []
    index = 0
    current = ""
    while index < len(data):
        char = data[index]
        if char.isalpha():
            current = char
            index += 1
            continue
        if char in " ,\t\r\n":
            index += 1
            continue
        if not current:
            raise ValueError("path data starts without a command")
        expected = PARAMS[current.upper()]
        numbers: list[float] = []
        while len(numbers) < expected:
            match = NUMBER.match(data, index)
            if match is None:
                raise ValueError(f"expected a number at offset {index}")
            numbers.append(float(match.group()))
            index = match.end()
            while index < len(data) and data[index] in " ,\t\r\n":
                index += 1
        out.append((current, numbers))
        if current == "M":
            current = "L"
        elif current == "m":
            current = "l"
    return out


def _element_points(tag: str, attrs: dict) -> list[tuple[float, float]]:
    """Sample enough points to bound one element. Curves use their control hull,
    which is conservative: a Bezier never leaves it."""
    def number(key: str, default: float = 0.0) -> float:
        return float(attrs.get(key, default))

    if tag == "circle":
        cx, cy, r = number("cx"), number("cy"), number("r")
        return [(cx - r, cy - r), (cx + r, cy + r)]
    if tag == "ellipse":
        cx, cy = number("cx"), number("cy")
        rx, ry = number("rx"), number("ry")
        return [(cx - rx, cy - ry), (cx + rx, cy + ry)]
    if tag == "rect":
        x, y = number("x"), number("y")
        return [(x, y), (x + number("width"), y + number("height"))]
    if tag == "line":
        return [(number("x1"), number("y1")), (number("x2"), number("y2"))]
    if tag in ("polyline", "polygon"):
        values = [float(v) for v in NUMBER.findall(attrs.get("points", ""))]
        return list(zip(values[0::2], values[1::2]))
    if tag == "path":
        points: list[tuple[float, float]] = []
        x = y = 0.0
        start = (0.0, 0.0)
        for command, numbers in _scan(attrs.get("d", "")):
            upper = command.upper()
            relative = command.islower()
            if upper == "Z":
                x, y = start
                continue
            if upper == "H":
                x = x + numbers[0] if relative else numbers[0]
            elif upper == "V":
                y = y + numbers[0] if relative else numbers[0]
            elif upper == "A":
                x = x + numbers[5] if relative else numbers[5]
                y = y + numbers[6] if relative else numbers[6]
                # An arc can bulge past its endpoints by at most its radii.
                points.append((x - abs(numbers[0]), y - abs(numbers[1])))
                points.append((x + abs(numbers[0]), y + abs(numbers[1])))
            else:
                pairs = list(zip(numbers[0::2], numbers[1::2]))
                for dx, dy in pairs:
                    px, py = (x + dx, y + dy) if relative else (dx, dy)
                    points.append((px, py))
                x, y = points[-1] if pairs else (x, y)
            points.append((x, y))
            if upper == "M":
                start = (x, y)
        return points
    return []


def _tally(atoms: list[dict]) -> dict[str, int]:
    tally: dict[str, int] = {}
    for atom in atoms:
        tally[atom["kind"]] = tally.get(atom["kind"], 0) + 1
    return dict(sorted(tally.items()))


def _strip(tag: str) -> str:
    return tag.split("}", 1)[-1]


def _nearest_keyshape(width: float, height: float, profile: Profile) -> list[dict]:
    """Which locked keyshape do these proportions actually point at?"""
    if width <= 0 or height <= 0:
        return []
    ratio = width / height
    scored = []
    for shape in Keyshape:
        if shape is Keyshape.FREE:
            continue
        size = shape.size_for(profile)
        scored.append((abs(math.log(ratio / (size.width / size.height))), shape, size))
    scored.sort(key=lambda row: row[0])
    return [
        {
            "keyshape": shape.name,
            "size": f"{size.width}x{size.height}",
            "visible_bounds": list(shape.bounds_for(profile)),
            "aspect": round(size.width / size.height, 4),
            "log_ratio_error": round(error, 4),
        }
        for error, shape, size in scored[:3]
    ]


def inspect_reference(
    name: str,
    profile: Profile = Profile.SUB32,
    root: Path = REFERENCE_ROOT,
) -> dict:
    path = original_path(name, root)
    root_element = ET.parse(path).getroot()
    elements = []
    points: list[tuple[float, float]] = []
    for element in root_element.iter():
        tag = _strip(element.tag)
        if tag == "svg":
            continue
        attrs = dict(element.attrib)
        element_points = _element_points(tag, attrs)
        points.extend(element_points)
        elements.append({"tag": tag, "attrs": attrs, "pointCount": len(element_points)})

    canvas = profile.spec.canvas_size
    try:
        atoms = read_atoms(name, root)
    except ValueError:
        atoms = []
    report: dict = {
        "name": name,
        "original": str(path),
        "originalSha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "atoms": atoms,
        "atomKinds": _tally(atoms),
        "viewBox": root_element.get("viewBox"),
        "sourceElements": elements,
        "target": {
            "profile": profile.name,
            "canvas": canvas,
            "stroke": STROKE_WIDTH,
            "reference_canvas": LUCIDE_CANVAS,
            "reference_stroke": LUCIDE_STROKE,
            "relative_weight_note": (
                f"Lucide stroke is {LUCIDE_STROKE / LUCIDE_CANVAS:.4f} of its canvas; "
                f"this profile's is {STROKE_WIDTH / canvas:.4f}. Ours is "
                f"{(STROKE_WIDTH / canvas) / (LUCIDE_STROKE / LUCIDE_CANVAS):.2f}x heavier, "
                "so gaps and interior detail need re-deriving, not copying."
            ),
        },
    }
    if points:
        left = min(p[0] for p in points)
        top = min(p[1] for p in points)
        right = max(p[0] for p in points)
        bottom = max(p[1] for p in points)
        width, height = right - left, bottom - top
        scale = (canvas - 2 * (STROKE_WIDTH / 2)) / LUCIDE_CANVAS
        report["referenceBounds"] = {
            "centerline": [round(v, 3) for v in (left, top, right, bottom)],
            "size": [round(width, 3), round(height, 3)],
            "aspect": round(width / height, 4) if height else None,
            "note": "Curve bounds use the control hull and arc radii, so this is an outer bound.",
        }
        report["suggestedKeyshapes"] = _nearest_keyshape(width, height, profile)
        report["rescaleHint"] = {
            "linear_factor": round(scale, 4),
            "note": (
                f"A {round(width, 2)}x{round(height, 2)} reference maps to roughly "
                f"{round(width * scale, 1)}x{round(height * scale, 1)} on {profile.name}. "
                "Re-derive integer coordinates from the chosen keyshape's four extreme "
                "values; do not multiply the reference's coordinates through."
            ),
        }
    return report


# -- cli ---------------------------------------------------------------------

def _print_search(rows: list[dict]) -> None:
    if not rows:
        print("no matches")
        return
    for row in rows:
        kinds = ", ".join(f"{k}x{v}" for k, v in sorted(row.get("segmentKinds", {}).items()))
        print(f"{row['name']:28s} score {row['score']:4d}  elements {row.get('sourceElementCount', '?'):>2}  {kinds}")


def _print_inspect(report: dict) -> None:
    print(f"{report['name']}  viewBox {report['viewBox']}")
    print(f"  file: {report['original']}")
    bounds = report.get("referenceBounds")
    if bounds:
        print(f"  reference bounds {bounds['centerline']}  size {bounds['size']}  aspect {bounds['aspect']}")
    print(f"  {report['target']['relative_weight_note']}")
    for row in report.get("suggestedKeyshapes", []):
        print(f"    {row['keyshape']:9s} {row['size']:>7s}  visible {row['visible_bounds']}  aspect {row['aspect']}")
    if "rescaleHint" in report:
        print(f"  {report['rescaleHint']['note']}")
    if report.get("atomKinds"):
        kinds = ", ".join(f"{kind} x{count}" for kind, count in report["atomKinds"].items())
        print(f"  atoms ({len(report['atoms'])}): {kinds}")
        print("  -- an inventory of the construction, not a part count to match;")
        print("     the analyser splits a native circle into four quarter-arcs.")
    print("  source elements:")
    for element in report["sourceElements"]:
        attrs = {k: v for k, v in element["attrs"].items() if k != "d"}
        data = element["attrs"].get("d")
        print(f"    <{element['tag']}> {attrs if attrs else ''}")
        if data:
            print(f"      d={data}")


def _print_atoms(name: str, rows: list[dict]) -> None:
    print(f"{name}  {len(rows)} segments  ({debug_path(name)})")
    for row in rows:
        print(f"  {row['atom']:>6s}  {row['kind']:<20s} from <{row['source']}>  d={row['d']}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    find = sub.add_parser("search", help="rank references by keyword")
    find.add_argument("query")
    find.add_argument("--limit", type=int, default=6)
    find.add_argument("--kind", help="filter by recorded segment kind, e.g. arc/circular")
    find.add_argument("--json", action="store_true")

    show = sub.add_parser("inspect", help="read one reference in this system's terms")
    show.add_argument("name")
    show.add_argument("--profile", default="SUB32", choices=[p.name for p in Profile])
    show.add_argument("--json", action="store_true")

    parts = sub.add_parser("atoms", help="list one reference's segments, in document order")
    parts.add_argument("name")
    parts.add_argument("--kind", help="show only this segment kind, e.g. arc/circular")
    parts.add_argument("--json", action="store_true")

    args = parser.parse_args(argv)
    try:
        if args.command == "search":
            rows = search(args.query, load_index(), args.limit, args.kind)
            print(json.dumps(rows, indent=2)) if args.json else _print_search(rows)
        elif args.command == "atoms":
            rows = read_atoms(args.name)
            if args.kind:
                rows = [row for row in rows if row["kind"] == args.kind]
            print(json.dumps(rows, indent=2)) if args.json else _print_atoms(args.name, rows)
        else:
            report = inspect_reference(args.name, Profile[args.profile])
            print(json.dumps(report, indent=2)) if args.json else _print_inspect(report)
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
