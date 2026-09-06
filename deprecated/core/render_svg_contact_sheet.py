#!/usr/bin/env python3
"""Render a flat SVG folder as a labeled true-size icon-family contact sheet."""

from __future__ import annotations

import argparse
import io
import math
from pathlib import Path
import xml.etree.ElementTree as ET

import cairosvg
from PIL import Image, ImageDraw, ImageFont
from icon_profiles import DEFAULT_ICON_TYPE, get_profile, profile_names, svg_native_size_issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--columns", type=int, default=10)
    parser.add_argument("--icon-type", choices=profile_names(), default=DEFAULT_ICON_TYPE)
    parser.add_argument("--true-size", type=int, help="compatibility option; must equal the selected native profile size")
    parser.add_argument("--preview-scale", type=int, default=1, help="optional integer magnification of the native raster (default: 1)")
    args = parser.parse_args()
    native_size = get_profile(args.icon_type)["designCanvas"]
    if args.true_size is not None and args.true_size != native_size:
        parser.error(f"{args.icon_type} reviews use native {native_size}×{native_size}; reduced or cross-profile sizes are not supported")
    if args.columns < 1 or args.preview_scale < 1:
        parser.error("--columns and --preview-scale must be positive integers")
    files = sorted(args.input.glob("*.svg"))
    if not files:
        parser.error("no SVG files found")
    canonical_files = []
    for path in files:
        if path.stem.endswith("-design"):
            canonical = path.with_name(path.stem[:-7] + ".svg")
            if canonical in files:
                if path.read_bytes() != canonical.read_bytes():
                    parser.error(f"{path.name} differs from its native canonical file {canonical.name}; re-emit both files")
                continue
        canonical_files.append(path)
    files = canonical_files
    for path in files:
        issues = svg_native_size_issues(ET.parse(path).getroot().attrib, args.icon_type)
        if issues:
            parser.error(f"{path.name}: " + "; ".join(issue["detail"] for issue in issues))
    icon_size = native_size * args.preview_scale
    cell_w = max(132, icon_size + 24)
    cell_h = icon_size + 44
    rows = math.ceil(len(files) / args.columns)
    sheet = Image.new("RGB", (cell_w * args.columns, cell_h * rows), "white")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for index, path in enumerate(files):
        png = cairosvg.svg2png(bytestring=path.read_bytes(), output_width=native_size, output_height=native_size)
        icon = Image.open(io.BytesIO(png)).convert("RGBA").resize((icon_size, icon_size), Image.Resampling.NEAREST)
        col, row = index % args.columns, index // args.columns
        x0, y0 = col * cell_w, row * cell_h
        sheet.paste(icon, (x0 + (cell_w - icon_size) // 2, y0 + 8), icon)
        label = path.stem
        if len(label) > 20:
            label = label[:19] + "…"
        box = draw.textbbox((0, 0), label, font=font)
        draw.text((x0 + (cell_w - (box[2] - box[0])) // 2, y0 + icon_size + 16), label, fill="#222", font=font)
        draw.rectangle((x0, y0, x0 + cell_w - 1, y0 + cell_h - 1), outline="#e2e5e9")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(args.output)
    print(f"rendered {len(files)} SVGs at native {native_size}×{native_size} ({args.preview_scale}× display) -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
