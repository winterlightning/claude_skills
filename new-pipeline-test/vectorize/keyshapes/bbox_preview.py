#!/usr/bin/env python3
"""
Shared SVG render/measure helpers for the snap pipeline.

This module is import-only -- it provides the rasterize + ink-bbox primitives
used by stretch_to_fit.py, generate_report.py and report_common.py:
    render_rgba(path), render_rgba_text(markup)  -> (H,W,4) RGBA + size
    ink_bbox(mask)                               -> (x0,y0,x1,y1) of content
plus the canvas/threshold constants (VIEWBOX, RENDER_W, ALPHA_THRESHOLD) and the
INPUT_DIR / OUTPUT_DIR locations.

Shape classification lives in fit_shapes.nearest_shape() -- the source of truth
for which grid shape an icon snaps to.

Requires:
    pip install cairosvg numpy pillow
"""

import io
from pathlib import Path

import cairosvg
import numpy as np
from PIL import Image

# ---------------------------------------------------------------------------
ROOT = Path(__file__).parent
INPUT_DIR = ROOT / "inputs"
OUTPUT_DIR = ROOT / "outputs"
VIEWBOX = 1024.0          # canvas size in SVG user units (all inputs are 1024x1024)
RENDER_W = 1024           # raster size used for measuring (px)
ALPHA_THRESHOLD = 10      # a pixel counts as "ink" if alpha > this
# ---------------------------------------------------------------------------


def render_rgba(svg_path: Path, width: int):
    """Rasterize an SVG to an (H, W, 4) uint8 RGBA array on a transparent bg."""
    png_bytes = cairosvg.svg2png(
        url=str(svg_path),
        output_width=width,
        background_color="transparent",
    )
    img = Image.open(io.BytesIO(png_bytes)).convert("RGBA")
    return np.asarray(img), img.size  # (array, (w, h))


def render_rgba_text(svg_text: str, width: int):
    """Like render_rgba but rasterizes SVG markup from a string."""
    png_bytes = cairosvg.svg2png(
        bytestring=svg_text.encode("utf-8"),
        output_width=width,
        background_color="transparent",
    )
    img = Image.open(io.BytesIO(png_bytes)).convert("RGBA")
    return np.asarray(img), img.size


def ink_bbox(mask: np.ndarray):
    """Return (x0, y0, x1, y1) in pixel coords of True content, or None."""
    ys, xs = np.where(mask)
    if xs.size == 0:
        return None
    return xs.min(), ys.min(), xs.max() + 1, ys.max() + 1
