#!/usr/bin/env python3
"""qa_overlays.py — render the review QA PNGs + gate metrics for finished SVGs.

Usage:  python3 qa_overlays.py icon.svg [more.svg ...] \
            [--png source.png --src-svg icon_final_raw.svg]

For each SVG (missing files are skipped) this writes, next to it:
  <base>_distance_debug.png   perpendicular-distance overlay
  <base>.metrics.json         lowest_distance / hole_score / hole counts /
                              path_count + gate verdicts

With --png + --src-svg the source-referenced precision/recall/IoU gates and
the hole-fidelity metrics are also computed and merged into each
metrics.json, plus a <base>_visual_comparison.png overlay. --src-svg must be
the SOURCE-COORDINATE SVG (same space as the PNG, e.g. <stem>_final_raw.svg)
— same approach as compare_pipelines.py, which scores that file against the
PNG on a 1024 canvas.

Hole metrics come from the png2svg family's own scorer (./holecmp): the
`hole_score` it reports on the source-coordinate SVG is the same `holes=`
number png2svg prints per shape in its merge log
(hole_score = 100·Σ min(P,R) / (n_src + extra), null when the icon has no
holes and no extras). n_src / n_render also feed the source_holes /
svg_holes count gate.

Distance + P/R/IoU still reuse the exact producers execute_pipeline uses
(svg_extraction/execution.py): calculate_distance_v2.
save_distance_visualization and compute_overlap. Gate thresholds match
lib/datamodel.js METRIC: precision >= 94, recall >= 80,
lowest_distance >= 102.4, hole_score >= 80 (no-holes icons pass); the
pipeline-level PASS is min(P, R, IoU) >= PASS_THRESHOLD (98) as in
execution.py.
"""
import argparse
import json
import os
import subprocess
import sys

import matplotlib
matplotlib.use("Agg")

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), "svg_extraction"))

from calculate_distance_v2 import save_distance_visualization  # noqa: E402
from test_visual_comparison_v2 import (  # noqa: E402
    PASS_THRESHOLD,
    compute_geometry_metrics,
    compute_overlap,
    match_svg_stroke_to_source,
    save_comparison,
)

DISTANCE_GATE = 102.4
HOLE_SCORE_GATE = 80
PRECISION_GATE = 94
RECALL_GATE = 80


def holecmp_metrics(png_path, src_svg_path):
    """Hole fidelity via ./holecmp on the SOURCE-COORDINATE SVG (identity
    align, real stroke widths) so the score matches png2svg's own `holes=`
    merge-log numbers. Returns the metrics.json fields to merge in."""
    exe = os.path.join(_HERE, "holecmp")
    proc = subprocess.run([exe, png_path, src_svg_path],
                          capture_output=True, text=True, timeout=120)
    if proc.returncode != 0:
        raise RuntimeError(
            f"holecmp exit {proc.returncode}: {proc.stderr.strip()[:200]}")
    d = json.loads(proc.stdout)
    hs = d.get("hole_score")
    return {
        "hole_score": round(float(hs), 2) if hs is not None else None,
        "hole_p_mean": d.get("hole_p_mean"),
        "hole_r_mean": d.get("hole_r_mean"),
        "source_holes": d.get("n_src"),
        "svg_holes": d.get("n_render"),
        "holes_missing": d.get("missing"),
        "holes_merged": d.get("merged"),
        "holes_extra": d.get("extra"),
    }


def source_metrics(png_path, src_svg_path, overlay_path):
    """Production-style source-referenced P/R/IoU: PNG ink vs the
    source-coordinate SVG, stroke auto-fitted (execution.py:360-374, with
    compare_pipelines' source-space alignment instead of the step1 CSV)."""
    import numpy as np
    from compare_pipelines import load_ink_mask

    ink = load_ink_mask(png_path)
    svg_mask, stroke_used, stroke_iters = match_svg_stroke_to_source(
        src_svg_path, ink, start_stroke=45)
    precision, recall, iou, f1, detail = compute_overlap(
        ink, svg_mask, align=False, detail=True)
    save_comparison(ink, svg_mask, overlay_path, align=False,
                    deviations=detail)
    score = min(precision, recall, iou)
    return {
        "precision": round(float(precision), 2),
        "recall": round(float(recall), 2),
        "iou": round(float(iou), 2),
        "f1": round(float(f1), 2),
        "score": round(float(score), 2),
        "passed": bool(score >= PASS_THRESHOLD),
        "pass_threshold": PASS_THRESHOLD,
        "precision_gate": PRECISION_GATE,
        "precision_passed": bool(precision >= PRECISION_GATE),
        "recall_gate": RECALL_GATE,
        "recall_passed": bool(recall >= RECALL_GATE),
        "tolerance": int(detail["tolerance"]),
        "source_pixels": int(np.count_nonzero(ink)),
        "svg_pixels": int(np.count_nonzero(svg_mask)),
        "stroke_used": stroke_used,
        "stroke_iterations": stroke_iters,
    }


def process(svg_path, src_metrics=None, hole_metrics=None):
    base = os.path.splitext(svg_path)[0]
    metrics = dict(src_metrics) if src_metrics else {}
    if hole_metrics:
        metrics.update(hole_metrics)

    geom = compute_geometry_metrics(svg_path)
    metrics["path_count"] = geom["path_count"]
    metrics["lowest_distance"] = (round(geom["lowest_distance"], 2)
                                  if geom["lowest_distance"] is not None else None)
    metrics["complexity_score"] = (round(geom["complexity_score"], 2)
                                   if geom["complexity_score"] is not None else None)
    try:
        save_distance_visualization(svg_path, base + "_distance_debug.png")
    except Exception as e:
        print(f"  distance overlay failed: {e}")

    hole_score = metrics.get("hole_score")

    ld = metrics["lowest_distance"]
    metrics["distance_gate"] = DISTANCE_GATE
    metrics["distance_passed"] = (ld >= DISTANCE_GATE) if ld is not None else None
    metrics["hole_gate"] = HOLE_SCORE_GATE
    # null hole_score = no holes and no extras — nothing to gate, passes
    metrics["hole_passed"] = (hole_score >= HOLE_SCORE_GATE
                              if hole_score is not None else True)

    with open(base + ".metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)
    line = (f"{os.path.basename(svg_path)}: "
            f"lowest_distance={ld} "
            f"({'PASS' if metrics['distance_passed'] else 'FAIL'}) "
            f"hole_score={hole_score} "
            f"({'PASS' if metrics['hole_passed'] else 'FAIL'}) "
            f"paths={metrics['path_count']}")
    if src_metrics:
        line += (f" P={src_metrics['precision']} "
                 f"({'PASS' if src_metrics['precision_passed'] else 'FAIL'}) "
                 f"R={src_metrics['recall']} "
                 f"({'PASS' if src_metrics['recall_passed'] else 'FAIL'}) "
                 f"IoU={src_metrics['iou']}")
    print(line)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("svgs", nargs="+", help="finished SVGs to measure")
    ap.add_argument("--png", help="source PNG (enables precision/recall gates)")
    ap.add_argument("--src-svg", help="source-coordinate SVG matching --png "
                                      "(e.g. <stem>_final_raw.svg)")
    args = ap.parse_args()

    svgs = [p for p in args.svgs if os.path.isfile(p)]
    if not svgs:
        print("error: none of the given SVGs exist", file=sys.stderr)
        sys.exit(2)

    src = holes = None
    if args.png and args.src_svg:
        if os.path.isfile(args.png) and os.path.isfile(args.src_svg):
            overlay = (os.path.splitext(svgs[0])[0]
                       + "_visual_comparison.png")
            try:
                src = source_metrics(args.png, args.src_svg, overlay)
            except Exception as e:
                print(f"warn: precision/recall failed: {e}", file=sys.stderr)
            try:
                holes = holecmp_metrics(args.png, args.src_svg)
            except Exception as e:
                print(f"warn: holecmp failed: {e}", file=sys.stderr)
        else:
            print("warn: --png/--src-svg not found — skipping "
                  "precision/recall + holes", file=sys.stderr)
    elif args.png or args.src_svg:
        print("warn: need BOTH --png and --src-svg for precision/recall "
              "+ holes", file=sys.stderr)

    for p in svgs:
        try:
            process(p, src_metrics=src, hole_metrics=holes)
        except Exception as e:
            print(f"warn: {os.path.basename(p)} — QA overlays failed: {e}",
                  file=sys.stderr)


if __name__ == "__main__":
    main()
