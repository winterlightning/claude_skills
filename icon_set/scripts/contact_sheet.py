#!/usr/bin/env python3
"""Render a QA contact sheet for visual review.

Visual review at native size is the real gate; the validators only prove the
rules were followed. Each cell shows the icon at its native canvas next to a
browser-size render, over the selected keyshape and the canvas edge, so a
technically valid but optically wrong icon is obvious.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.model import contracts  # noqa: E402
from icon_set.model.icons.registry import all_icons, icons_in  # noqa: E402
from icon_set.model.keyshapes import Keyshape  # noqa: E402
from icon_set.renderers.svg import build_paths  # noqa: E402

# The cell must hold an enlarged render and, beside it, an unscaled native one.
# The native render is as large as the widest profile canvas (CONTAINER64), so
# sizing the cell for 32 pixels makes container icons overflow their cell.
CELL = 170
COLUMNS = 8
LABEL_HEIGHT = 20
ENLARGED = 80
MARGIN = 10

THEMES = {
    "light": {"page": "#ffffff", "cell": "#fbfbfa", "ink": "#141413",
              "guide": "#d8d5cd", "keyshape": "#c96442", "label": "#6b6963"},
    "dark": {"page": "#1c1c19", "cell": "#232320", "ink": "#f5f4ef",
             "guide": "#3a3a35", "keyshape": "#d9795c", "label": "#a3a19a"},
}


def _keyshape_overlay(icon, scale: float, offset: tuple[float, float], colour: str) -> str:
    left, top, right, bottom = icon.keyshape_bounds()
    ox, oy = offset
    common = f'fill="none" stroke="{colour}" stroke-width="1" stroke-dasharray="3 3" opacity="0.9"'
    if icon.keyshape is Keyshape.CIRCLE:
        radius = icon.keyshape.visible_radius_for(icon.profile) * scale
        cx = ox + icon.profile.spec.center[0] * scale
        cy = oy + icon.profile.spec.center[1] * scale
        return f'<circle cx="{cx:g}" cy="{cy:g}" r="{radius:g}" {common}/>'
    return (
        f'<rect x="{ox + left * scale:g}" y="{oy + top * scale:g}" '
        f'width="{(right - left) * scale:g}" height="{(bottom - top) * scale:g}" {common}/>'
    )


def _cell(icon, column: int, row: int, theme: dict) -> str:
    x0, y0 = column * CELL, row * (CELL + LABEL_HEIGHT)
    canvas = icon.profile.spec.canvas_size
    big = ENLARGED
    scale = big / canvas
    ox, oy = x0 + MARGIN, y0 + MARGIN
    parts = [
        f'<rect x="{x0 + 2}" y="{y0 + 2}" width="{CELL - 4}" height="{CELL - 4}" '
        f'fill="{theme["cell"]}" stroke="{theme["guide"]}" stroke-width="1" rx="6"/>',
        # canvas edge
        f'<rect x="{ox}" y="{oy}" width="{big}" height="{big}" fill="none" '
        f'stroke="{theme["guide"]}" stroke-width="1"/>',
        _keyshape_overlay(icon, scale, (ox, oy), theme["keyshape"]),
    ]
    group = (
        f'<g transform="translate({ox} {oy}) scale({scale:g})" fill="none" '
        f'stroke="{theme["ink"]}" stroke-width="4" stroke-linecap="round" '
        f'stroke-linejoin="round">'
    )
    paths = "".join(f'<path d="{path["d"]}"/>' for path in build_paths(icon.draw()))
    parts.append(group + paths + "</g>")
    # Native-size render, unscaled, beside the enlarged one. Anchored to the
    # cell's bottom-right corner so every profile lands inside its own cell.
    native_x, native_y = x0 + CELL - canvas - MARGIN, y0 + CELL - canvas - MARGIN
    parts.append(
        f'<g transform="translate({native_x} {native_y})" fill="none" '
        f'stroke="{theme["ink"]}" stroke-width="4" stroke-linecap="round" '
        f'stroke-linejoin="round">{paths}</g>'
    )
    parts.append(
        f'<text x="{x0 + CELL / 2:g}" y="{y0 + CELL + 13}" text-anchor="middle" '
        f'font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" '
        f'fill="{theme["label"]}">{icon.icon_id}</text>'
    )
    return "".join(parts)


def render_sheet(
    theme_name: str = "light", columns: int = COLUMNS, family: str | None = None
) -> str:
    theme = THEMES[theme_name]
    icons = list(icons_in(family)) if family else list(all_icons())
    rows = (len(icons) + columns - 1) // columns
    width = columns * CELL
    height = rows * (CELL + LABEL_HEIGHT)
    cells = "".join(
        _cell(icon, index % columns, index // columns, theme)
        for index, icon in enumerate(icons)
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">'
        f'<rect width="{width}" height="{height}" fill="{theme["page"]}"/>'
        f"{cells}</svg>"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--theme", choices=sorted(THEMES), default="light")
    parser.add_argument("--columns", type=int, default=COLUMNS)
    parser.add_argument(
        "--family", choices=list(contracts.families()), default=None,
        help="render one family only; default is every family, sub first",
    )
    parser.add_argument(
        "--out", type=Path,
        default=REPO_ROOT / "icon_set" / "assets" / "previews-svg" / "contact-sheet.svg",
    )
    parser.add_argument("--png", type=Path, default=None)
    args = parser.parse_args(argv)

    document = render_sheet(args.theme, args.columns, args.family)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(document, encoding="utf-8")
    print(f"contact sheet -> {args.out}")
    if args.png is not None:
        import cairosvg

        args.png.parent.mkdir(parents=True, exist_ok=True)
        cairosvg.svg2png(bytestring=document.encode("utf-8"), write_to=str(args.png), scale=2)
        print(f"png -> {args.png}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
