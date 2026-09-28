#!/usr/bin/env python3
"""Combine png2svg per-object SVGs onto one canvas, then apply the
production finishing steps: step-8 normalization (content bbox ->
uniform scale -> centered on a 1024x1024 canvas, 4px padding) followed
by the stretch-to-fit keyshape snap (deform onto the nearest of the 12
grid shapes, stroke normalized to 51.2).

png2svg emits one SVG per connected component, each with a tight
data-fitted viewBox but coordinates in source-image pixels — so merging
is just re-parenting every child element under a single full-canvas svg.
Both finishing steps reuse the production code verbatim
(svg_extraction/pipeline_steps/step8_scale_svg.py process_icon() and
snap_icon_into_keyshapes/stretch_to_fit.py snap_svg_text()), so the
output matches execute_pipeline's final shipped SVG exactly. As in
production, the pre-snap SVG is kept beside the output as
<output>.pre_snap.svg, and a snap failure falls back to it.

Usage:
    python3 combine_svgs.py obj0.svg obj1.svg ... -o combined.svg
        [--size 1024]        raw-combine canvas (pre-fit), default 1024
        [--no-fit]           skip step-8 normalization (raw combine only)
        [--no-snap]          skip the stretch-to-fit keyshape snap
        [--stroke-width W]   force every stroke-width to W after the
                             step-8 fit; default: keep real widths,
                             scaled proportionally (the snap normalizes
                             to 51.2 regardless)
"""
import argparse
import os
import re
import sys

INNER_RE = re.compile(r"<svg\b[^>]*>(.*)</svg>", re.DOTALL)

_HERE = os.path.dirname(os.path.abspath(__file__))
_STEP8_DIR = os.path.join(_HERE, "step8")
_SNAP_DIR = os.path.join(_HERE, "keyshapes")


def inner_content(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = INNER_RE.search(text)
    if not m:
        sys.exit(f"error: {path}: no <svg>...</svg> element found")
    return m.group(1).strip("\n")


def combine(svg_paths, out_path, size):
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" '
             f'viewBox="0 0 {size:g} {size:g}">']
    for path in svg_paths:
        parts.append(f"  <!-- {path} -->")
        parts.append(inner_content(path))
    parts.append("</svg>\n")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("svgs", nargs="+", help="object SVG files (png2svg output)")
    ap.add_argument("-o", "--output", required=True, help="combined SVG path")
    ap.add_argument("--size", type=float, default=1024,
                    help="raw-combine canvas size in source pixels (default 1024)")
    ap.add_argument("--no-fit", dest="fit", action="store_false",
                    help="skip the step-8 bbox/scale normalization")
    ap.add_argument("--no-snap", dest="snap", action="store_false",
                    help="skip the stretch-to-fit keyshape snap")
    ap.add_argument("--stroke-width", type=float, default=None,
                    help="force all stroke-widths to this value after fitting")
    args = ap.parse_args()

    if not args.fit:
        combine(args.svgs, args.output, args.size)
        print(f"{args.output}: combined {len(args.svgs)} object(s), no fit")
        return

    sys.path.insert(0, _STEP8_DIR)
    from step8_scale_svg import process_icon  # noqa: E402

    # keep the source-coordinate combine beside the output — it's the
    # new-algo analog of the old pipeline's pre_step8.svg (used for scoring)
    raw_path = os.path.splitext(args.output)[0] + "_raw.svg"
    combine(args.svgs, raw_path, args.size)
    # bbox of all content (+half max stroke-width) -> uniform scale,
    # centered on 0 0 1024 1024 with 4px padding — same as execute_pipeline
    process_icon(raw_path, args.output, stroke_width=args.stroke_width)

    snapped = False
    if args.snap:
        sys.path.insert(0, _SNAP_DIR)
        from stretch_to_fit import snap_svg_text  # noqa: E402

        with open(args.output, encoding="utf-8") as f:
            src_text = f.read()
        _, snapped_text, _, snap_meta = snap_svg_text(src_text)
        if snap_meta.get("status") == "ok" and snapped_text is not None:
            pre_snap = os.path.splitext(args.output)[0] + ".pre_snap.svg"
            os.replace(args.output, pre_snap)
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(snapped_text)
            snapped = True
            print(f"stretch-to-fit snap: {snap_meta['label']} "
                  f"(pre-snap kept as {pre_snap})")
        else:
            print(f"snap skipped (status={snap_meta.get('status')}) — "
                  f"keeping step-8 output")

    print(f"{args.output}: combined {len(args.svgs)} object(s), "
          f"step-8 fit to 1024x1024"
          + (", keyshape-snapped" if snapped else ""))


if __name__ == "__main__":
    main()
