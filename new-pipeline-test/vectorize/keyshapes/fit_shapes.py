#!/usr/bin/env python3
"""
Catalog of the reference container shapes in grid_system/.

Reads every grid_system/shape-*.svg, extracts its <rect>/<circle> geometry, and
builds a dimension table (name, category, width, height, aspect, grid cells).
This is the up-to-date replacement for the old 4-shape FIT_DIMENSIONS table in
stretch_to_fit.py -- there are now 12 shapes (5 horizontal, 5 vertical, square,
circle) at finer aspect-ratio steps.

Run directly to print the table:   python3 fit_shapes.py
Import FIT_SHAPES / fit_dimensions() / nearest_shape() to reuse it.
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent
GRID_DIR = ROOT / "grid_system"
CANVAS = 1024.0
CELL = CANVAS / 20.0          # 51.2 px per grid cell

RECT_RE = re.compile(
    r'<rect[^>]*\bwidth="([\d.]+)"[^>]*\bheight="([\d.]+)"', re.I)
RECT_XYR_RE = re.compile(
    r'<rect[^>]*\bx="([\d.]+)"[^>]*\by="([\d.]+)"[^>]*\brx="([\d.]+)"', re.I)
CIRCLE_RE = re.compile(r'<circle[^>]*\br="([\d.]+)"', re.I)


def _category(stem: str) -> str:
    s = stem.replace("shape-", "")
    if s.startswith("horizontal-rect"):
        return "horizontal-rect"
    if s.startswith("vertical-rect"):
        return "vertical-rect"
    return s  # 'square' or 'circle'


def _parse(svg: Path):
    """Return a shape dict for one grid_system SVG, or None if no shape found."""
    text = svg.read_text()
    cat = _category(svg.stem)

    circ = CIRCLE_RE.search(text)
    if cat == "circle" and circ:
        r = float(circ.group(1))
        w = h = 2 * r
        return dict(name=svg.stem, category="circle", width=w, height=h,
                    x=CANVAS / 2 - r, y=CANVAS / 2 - r, rx=None, radius=r)

    # the container rect is the one with stroke-width="6" (skip the white bg)
    for m in re.finditer(r'<rect[^>]*?/>', text, re.I):
        tag = m.group(0)
        if 'stroke-width="6"' not in tag:
            continue
        wm = RECT_RE.search(tag)
        xyr = RECT_XYR_RE.search(tag)
        if not wm:
            continue
        w, h = float(wm.group(1)), float(wm.group(2))
        x = y = None
        rx = None
        if xyr:
            x, y, rx = float(xyr.group(1)), float(xyr.group(2)), float(xyr.group(3))
        return dict(name=svg.stem, category=cat, width=w, height=h,
                    x=x, y=y, rx=rx, radius=None)
    return None


def _load():
    shapes = []
    for svg in sorted(GRID_DIR.glob("shape-*.svg")):
        s = _parse(svg)
        if s:
            s["aspect"] = s["width"] / s["height"]
            s["cols"] = round(s["width"] / CELL)
            s["rows"] = round(s["height"] / CELL)
            shapes.append(s)
    # order: widest -> tallest (by aspect, descending)
    shapes.sort(key=lambda s: -s["aspect"])
    return shapes


FIT_SHAPES = _load()


def fit_dimensions(include_circle: bool = False):
    """{name: (width, height)} for use as a stretch target table."""
    return {s["name"]: (s["width"], s["height"])
            for s in FIT_SHAPES if include_circle or s["category"] != "circle"}


def nearest_shape(width: float, height: float, include_circle: bool = False):
    """Pick the shape whose aspect ratio is closest (in log space) to w/h."""
    import math
    la = math.log(width / height)
    cands = [s for s in FIT_SHAPES if include_circle or s["category"] != "circle"]
    return min(cands, key=lambda s: abs(math.log(s["aspect"]) - la))


def main():
    print(f"grid cell = {CELL:g} px   ({len(FIT_SHAPES)} shapes)\n")
    hdr = f'{"name":<28}{"category":<16}{"W x H":>13}  {"cells":>7}  {"aspect":>6}  {"rx":>6}'
    print(hdr)
    print("-" * len(hdr))
    for s in FIT_SHAPES:
        rx = f'{s["rx"]:.1f}' if s["rx"] is not None else "-"
        wh = f'{s["width"]:.1f} x {s["height"]:.1f}'
        cells = f'{s["cols"]}x{s["rows"]}'
        print(f'{s["name"]:<28}{s["category"]:<16}{wh:>13}  {cells:>7}  '
              f'{s["aspect"]:>6.3f}  {rx:>6}')


if __name__ == "__main__":
    main()
