#!/usr/bin/env python3
"""Render a flat SVG folder as a labeled true-size icon-family contact sheet."""

from __future__ import annotations

import argparse
import io
import math
from pathlib import Path

import cairosvg
from PIL import Image, ImageDraw, ImageFont


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--columns", type=int, default=10)
    parser.add_argument("--true-size", type=int, default=24)
    parser.add_argument("--preview-scale", type=int, default=3)
    args = parser.parse_args()
    files = sorted(args.input.glob("*.svg"))
    if not files:
        parser.error("no SVG files found")
    icon_size = args.true_size * args.preview_scale
    cell_w = max(132, icon_size + 24)
    cell_h = icon_size + 44
    rows = math.ceil(len(files) / args.columns)
    sheet = Image.new("RGB", (cell_w * args.columns, cell_h * rows), "white")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for index, path in enumerate(files):
        png = cairosvg.svg2png(bytestring=path.read_bytes(), output_width=args.true_size, output_height=args.true_size)
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
    print(f"rendered {len(files)} SVGs -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
