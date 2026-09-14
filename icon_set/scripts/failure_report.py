#!/usr/bin/env python3
"""Render every icon that failed the build, grouped by the rule it breaks.

Reads the failed build the last ``build.py`` run wrote under ``dist/failed/`` --
nothing is re-validated -- and writes one self-contained ``failures.html``. Each
finding is classified into a rule and a specific violation kind, and drawn over
the icon: the keyshape envelope against the ink box, the gap between two parts
that sit too close, the undersized hole. The build stages it into the gallery,
where it is the Failed build tab.

    python3 icon_set/scripts/failure_report.py
    python3 icon_set/scripts/failure_report.py --dist icon_set/dist --output /tmp/failures.html
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ElementTree
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DIST = REPO_ROOT / "icon_set" / "dist"
# Families the Failed build tab lists while the team works through them. Failed
# icons of other families are still written to dist/failed; they are only left
# out of this view. Add "container" / "sub" back when it is their turn.
FOCUS_FAMILIES = ("solo",)

RULES = {
    "bounds": {
        "title": "Keyshape bounds",
        "summary": "The visible ink must land exactly on the keyshape envelope: every side touches, none overshoots.",
        "fix": "Move the outermost strokes so the ink box equals the dashed envelope, or pick the keyshape the drawing really fits.",
    },
    "spacing": {
        "title": "Spacing (MIC)",
        "summary": "Separate strokes need 8u between centerlines (4u of clear ink) unless their contact is declared.",
        "fix": "Push the marked parts apart to the minimum, join them into one contour, or declare a scoped `connect` if they truly touch.",
    },
    "holes": {
        "title": "Holes & pinches",
        "summary": "Enclosed counters must stay open at ship size; tiny holes fill in and read as blobs.",
        "fix": "Enlarge the marked counter, or close it completely so it is not a hole.",
    },
    "broken": {
        "title": "Broken geometry",
        "summary": "The drawing cannot be emitted, so there is nothing to render. The Python model itself is inconsistent.",
        "fix": "Fix the contour order, the arc endpoints, or the element names reported below.",
    },
    "other": {
        "title": "Other",
        "summary": "Findings that do not fit a known rule group.",
        "fix": "Read the message; it names the element and the check.",
    },
}

NUMBER = r"-?\d+(?:\.\d+)?(?:e[-+]?\d+)?"
BOX = re.compile(rf"visible ink \(({NUMBER}), ({NUMBER}), ({NUMBER}), ({NUMBER})\) does not match the (\w+) envelope "
                 rf"\(({NUMBER}), ({NUMBER}), ({NUMBER}), ({NUMBER})\)")
CIRCLE_SHORT = re.compile(rf"reaches only radius ({NUMBER}) about \(({NUMBER}), ({NUMBER})\); (\w+) requires at least ({NUMBER})")
CIRCLE_OVER = re.compile(rf"reaches radius ({NUMBER}) about \(({NUMBER}), ({NUMBER})\), outside the (\w+) radius ({NUMBER})")
PAIR = re.compile(rf"^mic \[[^\]]*\]: (\S+) and (\S+) are ({NUMBER}) apart on centerlines nearest "
                  rf"\(({NUMBER}), ({NUMBER})\)<->\(({NUMBER}), ({NUMBER})\); \S+ requires at least ({NUMBER})")
PARALLEL = re.compile(rf"^mic \[([^\]]*)\]: parallel straight edges (.+?) are ({NUMBER}) apart on centerlines"
                      rf".*?requires at least ({NUMBER}) centerline")
HOLES = re.compile(r"holes/pinches: (\d+) undersized holes?; (\d+) pinch")
BROKEN = [("not contiguous", "Contour not contiguous"),
          ("does not return to its start", "Closed contour does not close"),
          ("coincident endpoints", "Degenerate arc (zero length)"),
          ("references unknown element", "Names an unknown element"),
          ("duplicate element ids", "Duplicate element ids"),
          ("only; this icon is", "Wrong family for its folder"),
          ("export:", "Export failed")]
EPSILON = 1e-3


def _floats(match, *groups):
    return [round(float(match.group(g)), 4) for g in groups]


def _box_kind(ink, env):
    """Say how an ink box misses its envelope, in the words a fix starts from."""
    if any(abs(value - round(value)) > EPSILON for value in ink):
        return "Curve extreme off the grid"
    width = (ink[2] - ink[0]) - (env[2] - env[0])
    height = (ink[3] - ink[1]) - (env[3] - env[1])
    parts = []
    if abs(width) > EPSILON:
        parts.append("too wide" if width > 0 else "too narrow")
    if abs(height) > EPSILON:
        parts.append("too tall" if height > 0 else "too short")
    return "Ink box " + " & ".join(parts or ["right size, shifted"])


def classify(message: str) -> dict:
    """One finding -> rule, violation kind, and what to draw for it."""
    issue = {"text": message, "rule": "other", "kind": message.split(":", 1)[0].strip() or "Unlabelled"}
    if message.startswith("canvas/keyshape bounds") and "cannot measure" not in message:
        issue["rule"] = "bounds"
        if match := BOX.search(message):
            ink, env = _floats(match, 1, 2, 3, 4), _floats(match, 6, 7, 8, 9)
            issue.update(kind=_box_kind(ink, env), keyshape=match.group(5),
                         overlay={"type": "box", "ink": ink, "env": env})
        elif match := CIRCLE_SHORT.search(message):
            radius, cx, cy, required = _floats(match, 1, 2, 3, 5)
            issue.update(kind="Circle ink does not reach the envelope", keyshape=match.group(4),
                         overlay={"type": "circle", "c": [cx, cy], "ink": radius, "env": required})
        elif match := CIRCLE_OVER.search(message):
            radius, cx, cy, allowed = _floats(match, 1, 2, 3, 5)
            issue.update(kind="Circle ink overshoots the envelope", keyshape=match.group(4),
                         overlay={"type": "circle", "c": [cx, cy], "ink": radius, "env": allowed})
        else:
            issue["kind"] = "Bounds (unparsed)"
    elif message.startswith("mic"):
        issue["rule"] = "spacing"
        if match := PAIR.search(message):
            distance, ax, ay, bx, by, required = _floats(match, 3, 4, 5, 6, 7, 8)
            issue.update(kind="Separate parts too close", distance=distance, required=required,
                         elements=[match.group(1), match.group(2)],
                         overlay={"type": "gap", "a": [ax, ay], "b": [bx, by]})
        elif match := PARALLEL.search(message):
            issue.update(kind="Parallel straight edges too close", distance=float(match.group(3)),
                         required=float(match.group(4)),
                         elements=[match.group(1)] + re.split(r",\s*|\s+and\s+", match.group(2)))
        else:
            issue["kind"] = "Spacing (unparsed)"
    elif message.startswith("holes/pinches"):
        issue["rule"] = "holes"
        match = HOLES.search(message)
        holes, pinches = (int(match.group(1)), int(match.group(2))) if match else (0, 0)
        issue["kind"] = "Undersized holes & pinches" if holes and pinches else "Pinch" if pinches else "Undersized hole"
    else:
        for needle, kind in BROKEN:
            if needle in message:
                issue.update(rule="broken", kind=kind)
                break
        else:
            if message.startswith(("style/grid", "schema/profile")) or re.match(r"^\w+Error:", message):
                issue["rule"] = "broken"
    return issue


def _svg_paths(document: str | None) -> tuple[list[dict] | None, dict | None]:
    if not document:
        return None, None
    try:
        root = ElementTree.fromstring(document)
    except ElementTree.ParseError:
        return None, None
    attributes = {name: root.get(name) for name in ("stroke-width", "viewBox") if root.get(name)}
    paths = [{"id": element.get("id", ""), "d": element.get("d", "")}
             for element in root.iter() if element.tag.rsplit("}", 1)[-1] == "path" and element.get("d")]
    return paths, attributes


def collect(failed_manifests: list[tuple[Path, str]], *, total: int | None = None,
            families: tuple[str, ...] | None = FOCUS_FAMILIES) -> dict:
    """Build the report data from ``(manifest path, svg url prefix)`` pairs, keeping ``families``."""
    icons = []
    for manifest, url_prefix in failed_manifests:
        try:
            records = json.loads(manifest.read_text(encoding="utf-8"))["icons"]
        except (OSError, ValueError, KeyError):
            continue
        for record in records:
            if families is not None and record.get("family") not in families:
                continue
            issues, seen = [], []
            for message in record.get("errors") or record.get("warnings") or []:
                # "ValueError: X" repeats the "style/grid: X" that reported the same fault,
                # and the bounds check re-reports a degenerate arc inside its own message.
                tail = message.split(":", 1)[-1].strip()
                if any(tail.endswith(other) or other.endswith(tail) for other in seen):
                    continue
                seen.append(tail)
                issues.append(classify(message))
            document = None
            if record.get("svg"):
                try:
                    document = (manifest.parent / record["svg"]).read_text(encoding="utf-8")
                except OSError:
                    document = None
            paths, attributes = _svg_paths(document)
            icons.append({
                "id": record["icon_id"], "family": record["family"], "profile": record.get("profile"),
                "status": record.get("status"), "canvas": record.get("canvas_size") or 48,
                "paths": paths, "svg": attributes, "issues": issues,
                "svgUrl": url_prefix + record["svg"] if record.get("svg") and paths is not None else None,
                "spacingPairs": record.get("spacing_pairs") or [], "holes": record.get("holes") or [],
                "file": record.get("source_path"),
            })
    icons.sort(key=lambda icon: (len(icon["issues"]), icon["family"], icon["id"]))
    kinds = Counter((issue["rule"], issue["kind"]) for icon in icons for issue in icon["issues"])
    return {"total": total, "failed": len(icons), "families": list(families) if families else None, "rules": RULES,
            "kinds": [{"rule": rule, "kind": kind, "count": count} for (rule, kind), count in kinds.most_common()],
            "icons": icons}


def write_report(data: dict, output: Path) -> Path:
    template = (Path(__file__).with_name("templates") / "failures.html").read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    output.write_text(template.replace("__FAILURE_DATA__", payload), encoding="utf-8")
    return output


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dist", type=Path, default=DEFAULT_DIST, help="build output folder")
    parser.add_argument("--output", type=Path, help="default: <dist>/gallery/failures.html")
    parser.add_argument("--family", action="append",
                        help=f"family to list (repeatable); default {', '.join(FOCUS_FAMILIES)}")
    parser.add_argument("--all-families", action="store_true", help="list every family's failed icons")
    args = parser.parse_args(argv)
    families = None if args.all_families else tuple(args.family or FOCUS_FAMILIES)
    manifests = sorted((args.dist / "failed").glob("*/manifest.json"))
    if not manifests:
        print(f"error: no failed build in {args.dist / 'failed'}; run icon_set/scripts/build.py first", file=sys.stderr)
        return 2
    output = args.output or args.dist / "gallery" / "failures.html"
    output.parent.mkdir(parents=True, exist_ok=True)
    pairs = [(path, f"../failed/{path.parent.name}/") for path in manifests]
    data = collect(pairs, families=families)
    passed = 0
    for path in manifests:
        try:
            release = json.loads((args.dist / path.parent.name / "manifest.json").read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if families is None or release.get("family") in families:
            passed += release.get("count", 0)
    data["total"] = passed + data["failed"]
    print(f"Failure report -> {write_report(data, output)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
