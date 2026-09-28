#!/usr/bin/env python3
"""pre_process_input.py — normalize a source PNG before png2svg.

Inputs like avatar_combine/head_2x2/output/*.png carry the icon on a
TRANSPARENT background (and the transparent pixels still hold junk RGB, e.g.
(24,23,23,0)). png2svg wants an opaque black-ink-on-white image, so this step:

  * flattens onto a white background (alpha is the ink coverage, so the junk
    RGB under transparent pixels can never leak in as grey), and
  * collapses every ink colour to black, keeping the anti-aliased edge as a
    grey ramp instead of a hard 1-bit cut.

Two regimes, picked automatically from the source:

  transparent source  ink = alpha x (pixel is not near-white)
      Anti-aliasing lives in the alpha channel, so the colour test only has to
      separate "some colour" from "white background", and any colour -- red,
      pastel, mid-grey -- becomes full black.

  fully opaque source  ink = 1 - min(r,g,b)/255
      Anti-aliasing lives in the greys, so the grey ramp is preserved.
      Saturated colours still go black (min channel is low for any strong hue);
      white stays white. An already-processed black-on-white PNG round-trips
      through this branch unchanged, so re-running the step is harmless.

Usage:
    ./pre_process_input.py input.png                 # -> input.prepped.png
    ./pre_process_input.py input.png -o out.png
    ./pre_process_input.py in1.png in2.png --out-dir DIR
    ./pre_process_input.py input.png --threshold 0.5 # hard 1-bit cut instead

Exit code is non-zero if any input fails; the remaining inputs are still
processed.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image

# A source counts as "transparent" once this fraction of pixels is not fully
# opaque -- one stray soft pixel in an otherwise opaque icon must not flip the
# regime and crush its anti-aliasing.
TRANSPARENT_FRACTION = 0.005
# Near-white cut used in the transparent regime (min-channel, 0-255): >= WHITE
# is background, <= INK is full ink, in between ramps linearly.
WHITE_CUT = 250.0
INK_CUT = 230.0


def _ink_coverage(img: Image.Image) -> np.ndarray:
    """Ink coverage in [0,1] per pixel: 1 = solid black, 0 = background."""
    rgba = np.asarray(img.convert("RGBA"), dtype=np.float32)
    rgb, alpha = rgba[..., :3], rgba[..., 3] / 255.0
    # min channel: 255 only for white, low for black AND for any saturated hue
    darkest = rgb.min(axis=2)

    transparent = float((alpha < 1.0).mean())
    if transparent >= TRANSPARENT_FRACTION:
        colour = np.clip((WHITE_CUT - darkest) / (WHITE_CUT - INK_CUT), 0.0, 1.0)
        return alpha * colour
    return 1.0 - darkest / 255.0


def prep(src: Path, dst: Path, threshold: float | None = None) -> None:
    with Image.open(src) as img:
        coverage = _ink_coverage(img)
    if threshold is not None:
        coverage = (coverage >= threshold).astype(np.float32)
    grey = np.rint((1.0 - coverage) * 255.0).astype(np.uint8)
    dst.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(grey, mode="L").convert("RGB").save(dst)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("inputs", nargs="+", type=Path, help="source PNG(s)")
    ap.add_argument("-o", "--output", type=Path,
                    help="destination PNG (single input only)")
    ap.add_argument("--out-dir", type=Path,
                    help="write <stem>.prepped.png into this directory")
    ap.add_argument("--threshold", type=float, metavar="T",
                    help="hard-binarize: coverage >= T becomes black, "
                         "everything else white (default: keep the grey ramp)")
    args = ap.parse_args(argv)

    if args.output and len(args.inputs) > 1:
        ap.error("-o/--output takes a single input; use --out-dir for many")

    failed = 0
    for src in args.inputs:
        if args.output:
            dst = args.output
        elif args.out_dir:
            dst = args.out_dir / f"{src.stem}.prepped.png"
        else:
            dst = src.with_suffix(".prepped.png")
        try:
            prep(src, dst, args.threshold)
        except Exception as exc:  # keep going, report at the end
            print(f"error: {src} — {exc}", file=sys.stderr)
            failed += 1
            continue
        print(dst)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
