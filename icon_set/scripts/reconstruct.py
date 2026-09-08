#!/usr/bin/env python3
"""Trace a batch of reference icons, then measure the reconstructions against them.

    python3 icon_set/scripts/reconstruct.py trace container_icons/svg
    python3 icon_set/scripts/reconstruct.py compare --family container
    python3 icon_set/scripts/reconstruct.py status  --family container

`prepare_references.py` gets a batch ready to *look* at. This gets it ready to
*build*, and then tells you whether what you built is the same icon.

Both halves work on the raster, never on the source's path data. An SVG's
coordinates describe an exporter's decisions -- its fragmentation, its stroke
ratio, its accidents -- and none of that survives re-authoring on a fixed grid
with a fixed 4-unit stroke. The picture is the thing being reproduced, so the
picture is what gets measured.

**trace** renders each source at the target family's canvas and reports what is
actually in the image, in that canvas's units: painted bounds, the aspect ratio
and the keyshape it points at, every full-width rule and full-height rule with
its position, every small detached mark with its centre, and the corner
rounding. That is the brief an author needs before drawing a window with a
title bar at y 22 and three dashes at y 14 -- facts about the subject, on this
system's grid, with no coordinates copied.

**compare** pairs each authored icon with its source, renders both at native
size, and reports the intersection-over-union of their ink. Validity says the
rules were followed; IoU says whether it is the same picture. A reconstruction
that validates at 0.55 is a different icon and the ledger sorts it to the top.

Sources are matched to icons by slug: `web-browser-window-<uuid>.svg` matches
the icon whose `icon_id` or `aliases` contains `web-browser-window`. Anything
unmatched is listed as pending, which is what makes this a worklist for 182
icons rather than a report on the handful already done.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import deque
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.model.icons.registry import icons_in  # noqa: E402
from icon_set.model.keyshapes import Keyshape  # noqa: E402
from icon_set.model.profiles import Profile  # noqa: E402

#: Measurement raster. Big enough that a 4-unit stroke is ~16px wide, so a rule
#: is unambiguous, and small enough that labelling is instant.
WORK = 256
#: A row counts as a rule when this much of the painted width is inked.
RULE_COVERAGE = 0.72
#: A component this small, relative to canvas area, is a detached mark.
MARK_AREA = 0.02
#: How far a stroke may move and still count as the same stroke, in canvas units.
TOLERANCE = 2.0

UUID = re.compile(r"-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")


def slug_of(path: Path) -> str:
    return UUID.sub("", path.stem)


def _mask(svg_text: str, size: int):
    """Ink coverage as a boolean array, rendered from the picture."""
    import cairosvg
    import numpy as np
    from PIL import Image
    import io

    png = cairosvg.svg2png(
        bytestring=svg_text.encode("utf-8"), output_width=size, output_height=size,
        background_color="#ffffff",
    )
    grey = np.asarray(Image.open(io.BytesIO(png)).convert("L"), dtype=float)
    return grey < 128


def _components(mask):
    """Connected ink components, 4-connected, as (area, top, left, bottom, right)."""
    import numpy as np

    seen = np.zeros(mask.shape, dtype=bool)
    out = []
    height, width = mask.shape
    for y in range(height):
        for x in range(width):
            if not mask[y, x] or seen[y, x]:
                continue
            queue = deque([(y, x)])
            seen[y, x] = True
            area = 0
            top = bottom = y
            left = right = x
            while queue:
                cy, cx = queue.popleft()
                area += 1
                top, bottom = min(top, cy), max(bottom, cy)
                left, right = min(left, cx), max(right, cx)
                for ny, nx in ((cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)):
                    if 0 <= ny < height and 0 <= nx < width and mask[ny, nx] and not seen[ny, nx]:
                        seen[ny, nx] = True
                        queue.append((ny, nx))
            out.append((area, top, left, bottom, right))
    return sorted(out, reverse=True)


def _num(value) -> float:
    """Plain Python float: numpy scalars repr as `np.float64(...)` in briefs."""
    return round(float(value), 1)


def _bands(flags: list[bool], scale: float, canvas: int) -> list[dict]:
    """Maximal runs of True, reported as centre and thickness in canvas units."""
    bands, start = [], None
    for index, flag in enumerate(list(flags) + [False]):
        if flag and start is None:
            start = index
        elif not flag and start is not None:
            bands.append({
                "centre": _num(((start + index - 1) / 2) / scale),
                "thickness": _num((index - start) / scale),
            })
            start = None
    return [b for b in bands if b["thickness"] * scale >= 1]


def trace_one(svg_text: str, canvas: int) -> dict:
    """Everything measurable about the picture, in the target canvas's units."""
    import numpy as np

    mask = _mask(svg_text, WORK)
    scale = WORK / canvas
    if not mask.any():
        return {"empty": True}

    ys, xs = np.nonzero(mask)
    top, bottom, left, right = ys.min(), ys.max(), xs.min(), xs.max()
    height, width = bottom - top + 1, right - left + 1

    inner = mask[top:bottom + 1, left:right + 1]
    rules_h = _bands([row.sum() / width >= RULE_COVERAGE for row in inner], scale, canvas)
    rules_v = _bands([col.sum() / height >= RULE_COVERAGE for col in inner.T], scale, canvas)
    for band in rules_h:
        band["centre"] = _num(band["centre"] + top / scale)
    for band in rules_v:
        band["centre"] = _num(band["centre"] + left / scale)

    components = _components(mask)
    limit = MARK_AREA * WORK * WORK
    marks = [
        {
            "centre": [_num((c[2] + c[4]) / 2 / scale), _num((c[1] + c[3]) / 2 / scale)],
            "size": [_num((c[4] - c[2] + 1) / scale), _num((c[3] - c[1] + 1) / scale)],
        }
        for c in components[1:] if c[0] <= limit
    ]

    # Corner rounding, read off the top edge of the largest component: how far
    # in from the left the topmost inked row starts.
    corner = 0.0
    if components:
        _, ctop, cleft, _, cright = components[0]
        row = np.nonzero(mask[ctop])[0]
        if row.size:
            corner = _num(max(row.min() - cleft, cright - row.max()) / scale)

    aspect = float(width) / float(height)
    return {
        "bounds": [_num(left / scale), _num(top / scale),
                   _num((right + 1) / scale), _num((bottom + 1) / scale)],
        "aspect": round(float(aspect), 3),
        "keyshape_hint": _keyshape_hint(aspect, canvas),
        "parts": len(components),
        "rules_horizontal": rules_h,
        "rules_vertical": rules_v,
        "marks": marks,
        "corner_radius": corner,
    }


def _keyshape_hint(aspect: float, canvas: int) -> str:
    """The rectangle keyshape whose proportions are closest to the picture's."""
    profile = next(p for p in Profile if p.spec.canvas_size == canvas)
    best, gap = "FREE", float("inf")
    for token in Keyshape:
        if token is Keyshape.FREE or token.is_radial:
            continue
        left, top, right, bottom = token.bounds_for(profile)
        ratio = (right - left) / (bottom - top)
        if abs(ratio - aspect) < gap:
            best, gap = token.name, abs(ratio - aspect)
    if abs(aspect - 1.0) < 0.04:
        return f"{best} (or CIRCLE -- the picture is square)"
    return best


def _brief(slug: str, concept: str, tags: str, trace: dict, canvas: int) -> str:
    lines = [f"# {concept or slug}", "", f"- slug: `{slug}`", f"- tags: {tags or '--'}", ""]
    if trace.get("empty"):
        return "\n".join(lines + ["The source renders empty. Nothing to trace."])
    lines += [
        "## Traced from the render, in "
        f"{canvas}-unit terms",
        "",
        f"- painted bounds: {tuple(trace['bounds'])}",
        f"- aspect: {trace['aspect']} -> keyshape hint **{trace['keyshape_hint']}**",
        f"- separate parts: {trace['parts']}",
        f"- corner rounding: ~{trace['corner_radius']} units",
    ]
    if trace["rules_horizontal"]:
        rules = ", ".join(f"y {b['centre']} ({b['thickness']} thick)"
                          for b in trace["rules_horizontal"])
        lines.append(f"- full-width rules: {rules}")
    if trace["rules_vertical"]:
        rules = ", ".join(f"x {b['centre']} ({b['thickness']} thick)"
                          for b in trace["rules_vertical"])
        lines.append(f"- full-height rules: {rules}")
    if trace["marks"]:
        marks = ", ".join(f"{tuple(m['centre'])} sized {tuple(m['size'])}"
                          for m in trace["marks"])
        lines.append(f"- detached marks: {marks}")
    lines += [
        "",
        "These are measurements of the picture, not coordinates to copy. Recompose "
        "on the profile: choose the keyshape, write down its four extremes, and "
        "place the rules and marks at the nearest legal grid positions that keep "
        "the proportions the trace reports.",
    ]
    return "\n".join(lines) + "\n"


def _concepts(folder: Path) -> dict[str, tuple[str, str]]:
    index = folder.parent / "index.csv"
    if not index.is_file():
        return {}
    out = {}
    with index.open(newline="") as handle:
        for row in csv.DictReader(handle):
            out[slug_of(Path(row["file"]))] = (row.get("concept", ""), row.get("tags", ""))
    return out


def cmd_trace(args: argparse.Namespace) -> int:
    folder = Path(args.folder)
    sources = sorted(folder.glob("*.svg"))
    if not sources:
        print(f"no SVGs in {folder}", file=sys.stderr)
        return 1
    canvas = Profile.for_family(args.family).spec.canvas_size
    out = Path(args.out or folder.parent / "work")
    (out / "traces").mkdir(parents=True, exist_ok=True)
    concepts = _concepts(folder)

    traces = {}
    for source in sources:
        slug = slug_of(source)
        trace = trace_one(source.read_text(), canvas)
        traces[slug] = trace
        concept, tags = concepts.get(slug, ("", ""))
        (out / "traces" / f"{slug}.md").write_text(_brief(slug, concept, tags, trace, canvas))
    (out / "traces.json").write_text(json.dumps(traces, indent=2) + "\n")
    print(f"traced {len(traces)} sources at {canvas} units -> {out}/traces/")
    return 0


def _sources(folder: Path) -> dict[str, Path]:
    """Every source file, keyed uniquely.

    A concept can appear more than once in a batch -- three
    `vertical-admission-ticket` files, three `desktop-computer-monitor` -- so
    repeats are suffixed rather than collapsed. `_base_slug` recovers the
    concept for matching.
    """
    out: dict[str, Path] = {}
    seen: dict[str, int] = {}
    for path in sorted(folder.glob("*.svg")):
        slug = slug_of(path)
        seen[slug] = seen.get(slug, 0) + 1
        out[slug if seen[slug] == 1 else f"{slug}#{seen[slug]}"] = path
    return out


def _base_slug(key: str) -> str:
    return key.split("#", 1)[0]


def _match(sources: dict[str, Path], family: str) -> tuple[dict, list[str]]:
    """Pair each authored icon with the source slug it reconstructs."""
    pairs, unmatched = {}, []
    names = {}
    for icon in icons_in(family):
        for name in (icon.icon_id,) + tuple(icon.aliases):
            names[name] = icon
    for key in sources:
        icon = names.get(_base_slug(key))
        if icon is not None:
            pairs[key] = icon
    matched = {icon.icon_id for icon in pairs.values()}
    for icon in icons_in(family):
        if icon.icon_id not in matched:
            unmatched.append(icon.icon_id)
    return pairs, unmatched


def _dilate(mask, radius_px: int):
    """Grow ink by `radius_px`, so nearby strokes count as the same stroke."""
    import numpy as np
    from PIL import Image, ImageFilter

    image = Image.fromarray((mask * 255).astype("uint8"), mode="L")
    grown = image.filter(ImageFilter.MaxFilter(radius_px * 2 + 1))
    return np.asarray(grown) > 127


def _fidelity(source_svg: str, icon, canvas: int) -> dict:
    """How much of the same picture the reconstruction is.

    Raw IoU is unusable on line art: two 4-unit strokes drawn 3 units apart are
    the same feature to a reader and barely overlap to a pixel counter, so a
    faithful redraw scores like a wrong one. What is wanted is whether every
    stroke of the source has a stroke of the reconstruction near it, and the
    other way round, so each mask is compared against the other dilated by
    ``TOLERANCE`` canvas units. Recall is the fraction of the source that is
    accounted for, precision the fraction of the reconstruction that belongs,
    and `fidelity` is their harmonic mean. Raw IoU is kept alongside because it
    is what shifts when proportions move.
    """
    import numpy as np

    a = _mask(source_svg, WORK)
    b = _mask(icon.to_svg(), WORK)
    union = (a | b).sum()
    iou = round(float((a & b).sum() / union), 3) if union else 0.0
    if not a.any() or not b.any():
        return {"iou": iou, "fidelity": 0.0, "recall": 0.0, "precision": 0.0}
    radius = max(1, round(TOLERANCE * WORK / canvas))
    recall = float((a & _dilate(b, radius)).sum() / a.sum())
    precision = float((b & _dilate(a, radius)).sum() / b.sum())
    both = recall + precision
    fidelity = (2 * recall * precision / both) if both else 0.0
    return {"iou": iou, "fidelity": round(fidelity, 3),
            "recall": round(recall, 3), "precision": round(precision, 3)}


def cmd_compare(args: argparse.Namespace) -> int:
    import cairosvg

    folder = Path(args.folder)
    canvas = Profile.for_family(args.family).spec.canvas_size
    out = Path(args.out or folder.parent / "work")
    (out / "compare").mkdir(parents=True, exist_ok=True)
    sources = _sources(folder)
    pairs, unmatched = _match(sources, args.family)
    concepts = _concepts(folder)

    rows = []
    for slug, icon in sorted(pairs.items()):
        source_svg = sources[slug].read_text()
        report = icon.validate_icon()
        scores = _fidelity(source_svg, icon, canvas)
        rows.append({
            "slug": slug, "icon_id": icon.icon_id,
            "concept": concepts.get(_base_slug(slug), ("", ""))[0],
            "status": report.status, "warnings": len(report.warnings), **scores,
        })
        panel = _panel(source_svg, icon.to_svg(), canvas)
        cairosvg.svg2png(bytestring=panel.encode(), write_to=str(out / "compare" / f"{slug}.png"),
                         scale=args.scale)

    rows.sort(key=lambda r: r["fidelity"])
    ledger = {
        "family": args.family, "sources": len(sources), "reconstructed": len(rows),
        "pending": len(sources) - len(rows),
        "icons_without_a_source": unmatched, "rows": rows,
    }
    (out / "ledger.json").write_text(json.dumps(ledger, indent=2) + "\n")
    (out / "ledger.md").write_text(_ledger_md(ledger, sources, pairs, concepts))
    for row in rows:
        print(f"  fidelity {row['fidelity']:.3f}  iou {row['iou']:.3f}  "
              f"{row['status']:<8} {row['icon_id']}")
    print(f"{len(rows)}/{len(sources)} reconstructed -> {out}/ledger.md")
    return 0


def _panel(source_svg: str, icon_svg: str, canvas: int) -> str:
    """Source, reconstruction, and the two overlaid, all at native size.

    Each drawing is embedded as a nested ``<svg>`` carrying its own viewBox, so
    a 1024-unit source and a 64-unit icon are both scaled to the same cell
    without touching either one's coordinates.
    """
    def parts(svg: str) -> tuple[str, str]:
        match = re.search(r"<svg([^>]*)>(.*)</svg>", svg, re.S)
        if match is None:
            return "0 0 1 1", ""
        box = re.search(r'viewBox="([^"]+)"', match.group(1))
        return (box.group(1) if box else f"0 0 {canvas} {canvas}"), match.group(2)

    src_box, src = parts(source_svg)
    got_box, got = parts(icon_svg)
    style = ('fill="none" stroke-width="4" stroke-linecap="round" '
             'stroke-linejoin="round"')
    step = canvas + 8

    def cell(x: int, box: str, body: str, extra: str = "") -> str:
        return (f'<svg x="{x}" y="4" width="{canvas}" height="{canvas}" '
                f'viewBox="{box}" {extra}>{body}</svg>')

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{step * 3 + 4}" '
        f'height="{canvas + 14}">'
        f'<rect width="100%" height="100%" fill="#ffffff"/>'
        + cell(4, src_box, src)
        + cell(step + 4, got_box, got, f'stroke="#000000" {style}')
        + f'<g opacity="0.5">{cell(step * 2 + 4, src_box, src)}</g>'
        + f'<g opacity="0.6">{cell(step * 2 + 4, got_box, got, f'stroke="#d33333" {style}')}</g>'
        + f'<text x="4" y="{canvas + 11}" font-family="monospace" font-size="5" '
        f'fill="#666">source / authored / overlay</text></svg>'
    )


def _ledger_md(ledger: dict, sources: dict, pairs: dict, concepts: dict) -> str:
    lines = [
        f"# Reconstruction ledger — {ledger['family']}", "",
        f"{ledger['reconstructed']} of {ledger['sources']} sources reconstructed; "
        f"{ledger['pending']} pending.", "",
        "**fidelity** compares the source render with the authored icon at native size,",
        f"allowing each stroke {TOLERANCE:g} units of movement: 1.0 means every stroke of the",
        "source has a stroke of the reconstruction near it and nothing was invented.",
        "Under about 0.75 the drawing has lost or gained a feature. **iou** is the raw",
        "pixel overlap, with no tolerance -- it drops when proportions shift even though",
        "the icon is still right, so read it as a proportions signal, not a verdict.",
        "Sorted worst first, because that is the work queue.", "",
        "| fidelity | iou | status | icon | source |", "|---|---|---|---|---|",
    ]
    for row in ledger["rows"]:
        warn = f" ({row['warnings']} warn)" if row["warnings"] else ""
        lines.append(
            f"| {row['fidelity']:.3f} | {row['iou']:.3f} | {row['status']}{warn} "
            f"| `{row['icon_id']}` | `{row['slug']}` |"
        )
    pending = [s for s in sorted(sources) if s not in pairs]
    if pending:
        lines += ["", "## Pending", ""]
        lines += [f"- `{slug}` — {concepts.get(_base_slug(slug), ('', ''))[0]}" for slug in pending]
    if ledger["icons_without_a_source"]:
        lines += ["", "## Authored without a source in this batch", ""]
        lines += [f"- `{name}`" for name in ledger["icons_without_a_source"]]
    return "\n".join(lines) + "\n"


def cmd_status(args: argparse.Namespace) -> int:
    folder = Path(args.folder)
    sources = _sources(folder)
    pairs, unmatched = _match(sources, args.family)
    print(f"{args.family}: {len(pairs)}/{len(sources)} sources reconstructed, "
          f"{len(sources) - len(pairs)} pending")
    if unmatched:
        print("authored without a source in this batch: " + ", ".join(sorted(unmatched)))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)

    common = {"folder": dict(nargs="?", default="container_icons/svg")}
    for name, handler, helptext in (
        ("trace", cmd_trace, "measure every source and write an authoring brief"),
        ("compare", cmd_compare, "score each reconstruction against its source"),
        ("status", cmd_status, "how much of the batch is done"),
    ):
        node = sub.add_parser(name, help=helptext)
        node.add_argument("folder", **common["folder"])
        node.add_argument("--family", default="container",
                          choices=("sub", "solo", "container"))
        node.add_argument("--out", default=None)
        if name == "compare":
            node.add_argument("--scale", type=int, default=4)
        node.set_defaults(handler=handler)

    args = parser.parse_args(argv)
    return args.handler(args)


if __name__ == "__main__":
    raise SystemExit(main())
