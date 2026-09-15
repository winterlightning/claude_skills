#!/usr/bin/env python3
"""qa_overlays.py — render the review QA PNGs + gate metrics for finished SVGs.

Usage:  python3 qa_overlays.py icon.svg|svg_dir [more ...] \
            [--out-dir DIR] [--gate N] [--jobs N] [--force] \
            [--png source.png --src-svg icon_final_raw.svg]

By default only SVGs whose output is missing or stale are measured: an SVG is
skipped when its metrics.json records the same svg_sha256, was measured at the
same --gate, and the debug PNGs it implies exist. --force re-measures
everything. Runs with --png/--src-svg always measure.

build.py reads icon_set/work/qa_overlays/<family folder>/ (e.g. solo48): an
icon whose saved result here failed distance or holes for the SVG it would
publish goes to dist/failed instead. Measure into that folder, then rebuild.

For each SVG (directories are expanded to their *.svg; missing files are
skipped) this writes, next to it or into --out-dir:
  <base>_distance_debug.png   perpendicular-distance overlay
  <base>_hole_debug.png       enclosed-hole / pinch overlay (canvas <= 256)
  <base>.metrics.json         lowest_distance / hole_score / hole counts /
                              negative_space holes+pinches / path_count +
                              gate verdicts
With --out-dir a qa_results.csv covering every SVG is written too.

Negative space (no source PNG needed) is icon_set.validation.library_qa's
measure_negative_space, the library-release hole gate: every enclosed opening
is measured with strokes narrowed to the 1u measurement stroke and needs an
inscribed radius >= minimum_enclosed_radius + retreat (2.5u on a 4u stroke);
the authored-stroke render is checked too, and pinches (regions closed only
by overlapping paint) fail. Rules come from negative-space.v1.json.

Canvas-aware: the distance metric's tunables were written for a 1024 canvas.
The canvas is read from each SVG's viewBox (else width) and every length
tunable is scaled by canvas/1024, so a 48x48 icon is measured in its own
units. The distance gate is per canvas (CANVAS_DISTANCE_GATES: 1024 -> 102.4;
the icon_set profiles' requiredCenterline 32 -> 6u, 48 -> 8u, 64 -> 6u; other
canvases scale 102.4 proportionally); --gate overrides it.

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
import csv
import hashlib
import json
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

import matplotlib
matplotlib.use("Agg")
import matplotlib.patches  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
# svg_extraction lives in the pg_app_utility repo; QA_SVG_EXTRACTION_DIR
# points at it when that checkout is not a sibling of claude_skills.
for _cand in (os.environ.get("QA_SVG_EXTRACTION_DIR", ""),
              os.path.join(os.path.dirname(_HERE), "svg_extraction"),
              os.path.join(os.path.dirname(_HERE), "pg_app_utility",
                           "svg_extraction")):
    if _cand and os.path.isdir(_cand):
        sys.path.insert(0, _cand)
        break

try:
    import calculate_distance_v2 as cd  # noqa: E402
except ImportError as _error:
    raise ImportError(
        "qa_overlays.py needs pg_app_utility/svg_extraction "
        "(calculate_distance_v2.py, count_paths.py): clone pg_app_utility "
        "next to claude_skills or set QA_SVG_EXTRACTION_DIR") from _error

BASE_CANVAS = 1024.0
DISTANCE_GATE = 102.4
# icon_set profile requiredCenterline: SUB32 6u, SOLO48 8u, CONTAINER64 6u
CANVAS_DISTANCE_GATES = {1024: 102.4, 32: 6.0, 48: 8.0, 64: 6.0}
HOLE_SCORE_GATE = 80
PRECISION_GATE = 94
RECALL_GATE = 80


def svg_canvas(svg_path):
    """Canvas size (max of width/height) from the viewBox, else width/height;
    falls back to the 1024 base when neither parses."""
    root = ET.parse(svg_path).getroot()
    vb = root.get("viewBox")
    if vb:
        nums = [float(n) for n in re.split(r"[\s,]+", vb.strip()) if n]
        if len(nums) == 4 and max(nums[2], nums[3]) > 0:
            return (nums[0], nums[1], nums[2], nums[3])
    try:
        w = float(re.sub(r"[^\d.]", "", root.get("width", "")))
        h = float(re.sub(r"[^\d.]", "", root.get("height", "")))
        return (0.0, 0.0, w, h)
    except ValueError:
        return (0.0, 0.0, BASE_CANVAS, BASE_CANVAS)


def distance_kwargs(canvas):
    """calculate_distance_v2 length tunables scaled from 1024 to `canvas`;
    angle/ratio tunables are scale-free and stay as-is."""
    s = canvas / BASE_CANVAS
    return dict(collinear_deg=cd.COLLINEAR_DEG,
                min_line_len=cd.MIN_LINE_LEN * s,
                parallel_deg=cd.PARALLEL_DEG,
                min_perp=cd.MIN_PERP * s,
                flat_tol=cd.FLAT_TOL * s)


def distance_gate(canvas):
    key = int(round(canvas))
    if key in CANVAS_DISTANCE_GATES:
        return CANVAS_DISTANCE_GATES[key]
    return DISTANCE_GATE * canvas / BASE_CANVAS


def analyze_distance(svg_path, gate=None):
    """Canvas-scaled analyze_svg. Returns (analysis, viewbox, kwargs, gate)."""
    vb = svg_canvas(svg_path)
    canvas = max(vb[2], vb[3])
    kw = distance_kwargs(canvas)
    s = canvas / BASE_CANVAS
    res = cd.analyze_svg(svg_path, min_circ_gap=cd.MIN_CIRC_GAP * s, **kw)
    return res, vb, kw, (gate if gate is not None else distance_gate(canvas))


def save_distance_debug(svg_path, out_png, res, vb, kw, gate, passed):
    """calculate_distance_v2's overlay drawn at the icon's own scale: axes
    locked to the viewBox, 2-decimal min distance and the gate verdict in the
    title (the stock renderer rounds 7.97 to "8.0")."""
    fig, ax = plt.subplots(figsize=(8, 8))
    try:
        cd.render_on_axes(ax, svg_path, title_fontsize=10, **kw)
        x0, y0, w, h = vb
        # The stock background draws every curve as its chord; swap it for
        # the actual rendered icon (real stroke width, real curves).
        for ln in list(ax.lines):
            if ln.get_zorder() == 1:
                ln.remove()
        try:
            import io
            import cairosvg
            from matplotlib.image import imread
            px = int(max(w, h) * max(1, round(768 / max(w, h))))
            png = cairosvg.svg2png(url=svg_path, output_width=px,
                                   output_height=int(px * h / w))
            img = imread(io.BytesIO(png), format="png")
            ax.imshow(img, extent=(x0, x0 + w, y0 + h, y0), alpha=0.16,
                      zorder=0, interpolation="bilinear")
        except Exception as e:
            print(f"  icon underlay skipped for {svg_path}: {e}")
        pad = max(w, h) * 0.02
        ax.set_xlim(x0 - pad, x0 + w + pad)
        ax.set_ylim(y0 + h + pad, y0 - pad)
        ax.add_patch(matplotlib.patches.Rectangle(
            (x0, y0), w, h, fill=False, edgecolor="0.6", lw=0.8, ls="--"))
        canvas = max(w, h)
        step = 4 if canvas <= 64 else (32 if canvas <= 256 else 128)
        ax.set_xticks([x0 + i for i in range(0, int(w) + 1, step)])
        ax.set_yticks([y0 + i for i in range(0, int(h) + 1, step)])
        ld = res["lowest_distance"]
        mg = res["min_gap"]
        measured = ld < cd.NO_DATA
        for t in list(ax.texts):  # replace the 1-decimal min-gap label
            t.remove()
        if mg is not None:
            o, p = mg["origin"], mg["point"]
            ax.text((o[0] + p[0]) / 2, (o[1] + p[1]) / 2, f" {ld:.2f}",
                    color="red", fontsize=11, fontweight="bold", zorder=5)
        verdict = "PASS" if passed else "FAIL"
        name = os.path.splitext(os.path.basename(svg_path))[0]
        md = f"{ld:.2f}" if measured else "no parallel pairs"
        kind = f" [{mg['kind']}]" if mg is not None else ""
        ax.set_title(
            f"{name}  —  {verdict}\n"
            f"min_d={md}{kind}  gate>={gate:g}  canvas={w:g}x{h:g}  "
            f"lines={len(res['lines'])} circles={len(res['circles'])}",
            fontsize=10, color=("black" if passed else "firebrick"))
        plt.tight_layout()
        plt.savefig(out_png, dpi=110, bbox_inches="tight")
    finally:
        plt.close(fig)


NEGATIVE_SPACE_MAX_CANVAS = 256  # render is canvas*32 px; skip pipeline 1024s
_NUM = r"-?\d*\.?\d+(?:[eE][-+]?\d+)?"
_CIRCLE_ARC_PATH = re.compile(
    rf"^\s*M\s*({_NUM})[\s,]+({_NUM})\s*"
    rf"((?:A\s*{_NUM}[\s,]+{_NUM}[\s,]+{_NUM}[\s,]+[01][\s,]*[01][\s,]*"
    rf"{_NUM}[\s,]+{_NUM}\s*)+)Z?\s*$")
_ARC = re.compile(rf"A\s*({_NUM})[\s,]+({_NUM})[\s,]+{_NUM}[\s,]+([01])[\s,]*"
                  rf"([01])[\s,]*({_NUM})[\s,]+({_NUM})")


def _circle_from_arc_path(d):
    """(cx, cy, r) when `d` is one closed circle drawn as equal-radius arcs
    (how the build bakes a circle into dist SVGs), else None. Conservative:
    every endpoint must lie on one circle of that radius, every arc must
    sweep the same way with a large-arc flag matching its angle, and the
    sweeps must total exactly one turn back to the start."""
    import math
    m = _CIRCLE_ARC_PATH.match(d or "")
    if not m:
        return None
    pts = [(float(m.group(1)), float(m.group(2)))]
    arcs = _ARC.findall(m.group(3))
    if len(arcs) < 2 or len({a[3] for a in arcs}) != 1:
        return None
    radii = {(float(a[0]), float(a[1])) for a in arcs}
    if len(radii) != 1:
        return None
    r, ry = radii.pop()
    if r <= 0 or abs(r - ry) > 1e-9:
        return None
    pts += [(float(a[4]), float(a[5])) for a in arcs]
    if math.dist(pts[0], pts[-1]) > 1e-9:
        return None
    ring = []
    for p in pts[:-1]:
        if all(math.dist(p, q) > 1e-9 for q in ring):
            ring.append(p)
    if len(ring) < 2:
        return None
    if len(ring) == 2:
        if abs(math.dist(*ring) - 2 * r) > 1e-6:
            return None
        cx, cy = (ring[0][0] + ring[1][0]) / 2, (ring[0][1] + ring[1][1]) / 2
    else:
        (ax, ay), (bx, by), (qx, qy) = ring[:3]
        den = 2 * (ax * (by - qy) + bx * (qy - ay) + qx * (ay - by))
        if abs(den) < 1e-12:
            return None
        cx = ((ax * ax + ay * ay) * (by - qy) + (bx * bx + by * by) * (qy - ay)
              + (qx * qx + qy * qy) * (ay - by)) / den
        cy = ((ax * ax + ay * ay) * (qx - bx) + (bx * bx + by * by) * (ax - qx)
              + (qx * qx + qy * qy) * (bx - ax)) / den
    if any(abs(math.dist(p, (cx, cy)) - r) > 1e-6 for p in pts):
        return None
    sweep = 1 if arcs[0][3] == "1" else -1  # SVG y-down: "1" = +angle
    total = 0.0
    for (_, _, large, _, _, _), p0, p1 in zip(arcs, pts, pts[1:]):
        a0 = math.atan2(p0[1] - cy, p0[0] - cx)
        a1 = math.atan2(p1[1] - cy, p1[0] - cx)
        delta = ((a1 - a0) * sweep) % (2 * math.pi)
        if delta < 1e-9:
            return None
        if (large == "1") != (delta > math.pi + 1e-9):
            return None
        total += delta
    if abs(total - 2 * math.pi) > 1e-6:
        return None
    return cx, cy, r


def _with_explicit_circles(document):
    """Rewrite baked circle paths as <circle> elements (identical stroke
    render) so measure_negative_space's small-circle exception sees them;
    the release build gets the same circles from the icon model instead."""
    ns = "http://www.w3.org/2000/svg"
    ET.register_namespace("", ns)
    root = ET.fromstring(document)
    changed = False
    for parent in root.iter():
        for i, el in enumerate(list(parent)):
            if el.tag.split("}")[-1] != "path" or el.get("transform"):
                continue
            fit = _circle_from_arc_path(el.get("d"))
            if fit is None:
                continue
            circle = ET.Element(f"{{{ns}}}circle", {
                k: v for k, v in el.attrib.items() if k != "d"})
            circle.set("cx", f"{fit[0]:g}")
            circle.set("cy", f"{fit[1]:g}")
            circle.set("r", f"{fit[2]:g}")
            parent.remove(el)
            parent.insert(i, circle)
            changed = True
    return ET.tostring(root, encoding="unicode") if changed else document


def negative_space_metrics(svg_path, vb, out_png):
    """Source-free hole/pinch gate: icon_set.validation.library_qa's
    measure_negative_space (the library-release check). Writes one combined
    <base>_hole_debug.png: measured at the 1u measurement stroke (left) and
    at the authored stroke (right). Returns the metrics.json fields."""
    import tempfile
    from pathlib import Path
    from matplotlib.image import imread
    from icon_set.validation.library_qa import measure_negative_space

    canvas = int(round(max(vb[2], vb[3])))
    with open(svg_path, encoding="utf-8") as f:
        document = _with_explicit_circles(f.read())
    with tempfile.TemporaryDirectory(prefix="qa-holes-") as tmp:
        thin_png = Path(tmp) / "holes.png"
        r = measure_negative_space(document, canvas, overlay=thin_png)
        thin = imread(thin_png)
        authored = imread(thin_png.with_name("authored-" + thin_png.name))

    def brief(h):
        return {"hole": h["hole"], "center": h["center_viewbox"],
                "inscribed_radius_u": h["inscribed_radius_design_u"],
                "minimum_radius_u": h["minimum_radius_design_u"],
                "status": h["status"],
                **({"exception": h["exception"]} if "exception" in h else {})}

    thin_holes = [h for h in r["holes"] if "measuring_stroke_width" not in h]
    extra = [h for h in r["holes"] if "measuring_stroke_width" in h]
    passed = r["status"] == "pass"
    out = {
        "negative_space_status": r["status"],
        "negative_space_passed": passed,
        "hole_count": r["hole_count"],
        "failed_hole_count": r["failed_hole_count"],
        "pinch_count": r["pinch_count"],
        "authored_hole_count": r["authored_hole_count"],
        "raster_artifact_count": r["raster_artifact_count"],
        "hole_exception_count": r["exception_count"],
        "measuring_stroke_width": r["measuring_stroke_width"],
        "minimum_measured_radius": r["minimum_measured_diameter"] / 2,
        "minimum_authored_radius": r["minimum_authored_diameter"] / 2,
        "holes": [brief(h) for h in r["holes"]],
        "pinches": [{"center": p["center_viewbox"],
                     "closure_margin_u": p["closure_margin_design_u"],
                     "trapped_radius_u": p["trapped_radius_design_u"]}
                    for p in r["pinches"]],
    }

    colors = {"pass": "#087f5b", "fail": "#d9480f",
              "raster-artifact": "0.45"}
    fig, axes = plt.subplots(1, 2, figsize=(14, 7.6))
    try:
        x0, y0, w, h = vb
        panels = (
            (axes[0], thin, thin_holes, r["pinches"],
             f"measured @ {r['measuring_stroke_width']:g}u stroke  "
             f"(inscribed r >= {r['minimum_measured_diameter'] / 2:g}u)"),
            (axes[1], authored, r["authored_holes"], [],
             f"authored stroke  (inscribed r >= "
             f"{r['minimum_authored_diameter'] / 2:g}u)"),
        )
        for ax, img, holes, pinches, subtitle in panels:
            ax.imshow(img, extent=(x0, x0 + w, y0 + h, y0),
                      interpolation="nearest")
            for hole in holes:
                cx, cy = hole["center_viewbox"]
                rad = hole["inscribed_radius_design_u"]
                col = ("#1c7ed6" if "exception" in hole
                       else colors.get(hole["status"], "black"))
                ax.add_patch(matplotlib.patches.Circle(
                    (cx, cy), rad, fill=False, edgecolor=col, lw=1.6,
                    ls="-" if hole["status"] != "raster-artifact" else ":"))
                ax.plot(cx, cy, "+", color=col, ms=6)
                tag = ("exc" if "exception" in hole
                       else "artifact" if hole["status"] == "raster-artifact"
                       else hole["status"].upper())
                ax.annotate(f"#{hole['hole']} r={rad:.2f} {tag}", (cx, cy),
                            xytext=(4, -6), textcoords="offset points",
                            fontsize=8, color=col, fontweight="bold",
                            bbox=dict(boxstyle="round,pad=0.15", fc="white",
                                      ec="none", alpha=0.75))
            for p in pinches:
                cx, cy = p["center_viewbox"]
                ax.annotate(f"pinch margin={p['closure_margin_design_u']:.2f}u",
                            (cx, cy), xytext=(8, 8), textcoords="offset points",
                            fontsize=8, color="#c92a2a", fontweight="bold",
                            bbox=dict(boxstyle="round,pad=0.15", fc="white",
                                      ec="none", alpha=0.75))
            ax.set_xlim(x0, x0 + w)
            ax.set_ylim(y0 + h, y0)
            step = 4 if max(w, h) <= 64 else 16
            ax.set_xticks([x0 + i for i in range(0, int(w) + 1, step)])
            ax.set_yticks([y0 + i for i in range(0, int(h) + 1, step)])
            ax.grid(True, linestyle=":", alpha=0.35)
            ax.set_title(subtitle, fontsize=9)
        failed_extra = f" (+{len(extra)} authored-only)" if extra else ""
        name = os.path.splitext(os.path.basename(svg_path))[0]
        fig.suptitle(
            f"{name}  —  holes {'PASS' if passed else 'FAIL'}\n"
            f"holes={r['hole_count']} failed={r['failed_hole_count']}"
            f"{failed_extra}  pinches={r['pinch_count']}  "
            f"exceptions={r['exception_count']}  "
            f"artifacts={r['raster_artifact_count']}  canvas={w:g}x{h:g}",
            fontsize=10, color=("black" if passed else "firebrick"))
        plt.tight_layout()
        plt.savefig(out_png, dpi=100, bbox_inches="tight")
    finally:
        plt.close(fig)
    return out


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
    # Only the source-PNG gates need the full png2svg comparison stack.
    from test_visual_comparison_v2 import (
        PASS_THRESHOLD,
        compute_overlap,
        match_svg_stroke_to_source,
        save_comparison,
    )

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


def process(svg_path, src_metrics=None, hole_metrics=None, out_dir=None,
            gate=None, quiet=False):
    base = _output_base(svg_path, out_dir)
    metrics = dict(src_metrics) if src_metrics else {}
    # Ties the result to this exact drawing: build.py only applies a verdict
    # whose hash matches the SVG it is publishing.
    metrics["svg_sha256"] = _file_sha256(svg_path)
    if hole_metrics:
        metrics.update(hole_metrics)

    try:
        from count_paths import count_path
        metrics["path_count"] = count_path(svg_path)
    except Exception as e:
        metrics["path_count"] = None
        print(f"  count_path failed for {svg_path}: {e}")

    res = None
    try:
        res, vb, kw, gate = analyze_distance(svg_path, gate)
    except Exception as e:
        # a failed parse is "no measurement" (None), never the NO_DATA
        # sentinel, which would falsely pass the gate
        print(f"  perpendicular analysis failed for {svg_path}: {e}")
        vb, gate = None, gate if gate is not None else DISTANCE_GATE
    ld = res["lowest_distance"] if res else None
    metrics["canvas"] = [vb[2], vb[3]] if vb else None
    metrics["lowest_distance"] = round(ld, 2) if ld is not None else None
    metrics["complexity_score"] = (round(res["complexity_score"], 2)
                                   if res else None)
    metrics["min_gap_kind"] = (res["min_gap"]["kind"]
                               if res and res["min_gap"] else None)

    hole_score = metrics.get("hole_score")

    ld = metrics["lowest_distance"]
    metrics["distance_gate"] = gate
    metrics["distance_measured"] = (ld is not None and ld < cd.NO_DATA)
    metrics["distance_passed"] = (ld >= gate) if ld is not None else None

    if res is not None:
        try:
            save_distance_debug(svg_path, base + "_distance_debug.png", res,
                                vb, kw, gate, metrics["distance_passed"])
        except Exception as e:
            print(f"  distance overlay failed: {e}")

    if vb is not None and max(vb[2], vb[3]) <= NEGATIVE_SPACE_MAX_CANVAS:
        try:
            metrics.update(negative_space_metrics(
                svg_path, vb, base + "_hole_debug.png"))
        except Exception as e:
            metrics["negative_space_status"] = "error"
            metrics["negative_space_passed"] = None
            print(f"  negative-space check failed for {svg_path}: {e}")
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
    if "negative_space_status" in metrics:
        line += (f" negative_space={metrics['negative_space_status'].upper()}"
                 f" (holes={metrics.get('hole_count')}"
                 f" failed={metrics.get('failed_hole_count')}"
                 f" pinches={metrics.get('pinch_count')})")
    if src_metrics:
        line += (f" P={src_metrics['precision']} "
                 f"({'PASS' if src_metrics['precision_passed'] else 'FAIL'}) "
                 f"R={src_metrics['recall']} "
                 f"({'PASS' if src_metrics['recall_passed'] else 'FAIL'}) "
                 f"IoU={src_metrics['iou']}")
    if not quiet:
        print(line)
    return metrics


def _file_sha256(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def _output_base(svg_path, out_dir):
    stem = os.path.splitext(os.path.basename(svg_path))[0]
    return (os.path.join(out_dir, stem) if out_dir
            else os.path.splitext(svg_path)[0])


def existing_metrics(svg_path, out_dir=None, gate=None):
    """The saved metrics when this SVG's debug output is complete and current,
    else None: metrics.json measured this exact SVG (svg_sha256) at the
    requested gate, and every debug PNG that metrics.json implies is on disk."""
    base = _output_base(svg_path, out_dir)
    try:
        with open(base + ".metrics.json", encoding="utf-8") as f:
            m = json.load(f)
        current = _file_sha256(svg_path)
    except (OSError, ValueError):
        return None
    if not isinstance(m, dict) or m.get("svg_sha256") != current:
        return None
    if gate is not None and m.get("distance_gate") != gate:
        return None
    needed = []
    if m.get("canvas") is not None:
        needed.append(base + "_distance_debug.png")
    if m.get("negative_space_status") not in (None, "error"):
        needed.append(base + "_hole_debug.png")
    return m if all(os.path.isfile(p) for p in needed) else None


def _process_batch_item(job):
    path, out_dir, gate = job
    try:
        m = process(path, out_dir=out_dir, gate=gate, quiet=True)
    except Exception as e:
        return {"icon": os.path.basename(path)[:-4], "status": "ERROR",
                "distance_status": "ERROR", "hole_status": "ERROR",
                "error": str(e)[:200]}
    return _summary_row(path, m)


def _summary_row(path, m):
    def verdict(v):
        return "ERROR" if v is None else "PASS" if v else "FAIL"

    dist = verdict(m["distance_passed"])
    hole = (verdict(m["negative_space_passed"])
            if "negative_space_passed" in m else "SKIP")
    parts = {dist, hole} - {"SKIP"}
    status = ("ERROR" if "ERROR" in parts
              else "FAIL" if "FAIL" in parts else "PASS")
    return {"icon": os.path.basename(path)[:-4], "status": status,
            "distance_status": dist, "hole_status": hole,
            "lowest_distance": (m["lowest_distance"]
                                if m["distance_measured"] else None),
            "gate": m["distance_gate"], "min_gap_kind": m["min_gap_kind"],
            "holes": m.get("hole_count"),
            "failed_holes": m.get("failed_hole_count"),
            "pinches": m.get("pinch_count"),
            "min_hole_radius": min(
                (h["inscribed_radius_u"] for h in m.get("holes", [])
                 if h["status"] != "raster-artifact"), default=None),
            "canvas": "x".join(f"{c:g}" for c in m["canvas"] or []),
            "error": ""}


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("svgs", nargs="+",
                    help="finished SVGs (or directories of SVGs) to measure")
    ap.add_argument("--out-dir", help="write debug PNGs + metrics.json here "
                                      "instead of next to each SVG")
    ap.add_argument("--gate", type=float,
                    help="distance gate override, in canvas units "
                         "(default: per canvas, 8 for 48x48)")
    ap.add_argument("--jobs", type=int, default=os.cpu_count() or 1,
                    help="parallel workers for multi-SVG runs without --png")
    ap.add_argument("--png", help="source PNG (enables precision/recall gates)")
    ap.add_argument("--src-svg", help="source-coordinate SVG matching --png "
                                      "(e.g. <stem>_final_raw.svg)")
    ap.add_argument("--force", action="store_true",
                    help="re-measure every SVG (default: only SVGs whose "
                         "debug PNGs/metrics.json are missing or were "
                         "measured on a different SVG)")
    args = ap.parse_args()

    svgs = []
    for p in args.svgs:
        if os.path.isdir(p):
            svgs.extend(sorted(os.path.join(p, n) for n in os.listdir(p)
                               if n.endswith(".svg")))
        elif os.path.isfile(p):
            svgs.append(p)
    if not svgs:
        print("error: none of the given SVGs exist", file=sys.stderr)
        sys.exit(2)
    if args.out_dir:
        os.makedirs(args.out_dir, exist_ok=True)

    if len(svgs) > 1 and not (args.png or args.src_svg):
        from multiprocessing import Pool
        rows_by_path = {}
        if not args.force:
            for p in svgs:
                m = existing_metrics(p, args.out_dir, args.gate)
                if m is not None:
                    rows_by_path[p] = _summary_row(p, m)
        jobs = [(p, args.out_dir, args.gate) for p in svgs
                if p not in rows_by_path]
        print(f"measuring {len(jobs)}/{len(svgs)} SVGs "
              f"({len(rows_by_path)} up to date"
              f"{'' if args.force else '; --force re-measures all'})",
              file=sys.stderr)
        if jobs:
            with Pool(max(1, min(args.jobs, len(jobs)))) as pool:
                for i, row in enumerate(pool.imap(_process_batch_item, jobs,
                                                  chunksize=8), 1):
                    rows_by_path[jobs[i - 1][0]] = row
                    if i % 500 == 0:
                        print(f"  ... {i}/{len(jobs)}", file=sys.stderr)
        # Report and write the CSV over every SVG, skipped ones included.
        rows = [rows_by_path[p] for p in svgs]
        for row in rows:
            if row["status"] != "PASS":
                print(f"{row['icon']}: distance={row['distance_status']}"
                      f" lowest_distance={row.get('lowest_distance')}"
                      f" holes={row['hole_status']}"
                      f" failed_holes={row.get('failed_holes')}"
                      f" pinches={row.get('pinches')} "
                      f"{row.get('error', '')}".rstrip())

        def tally(key):
            counts = {}
            for r in rows:
                counts[r[key]] = counts.get(r[key], 0) + 1
            return " ".join(f"{k}={v}" for k, v in sorted(counts.items()))

        unmeasured = sum(1 for r in rows if r["distance_status"] == "PASS"
                         and r.get("lowest_distance") is None)
        if args.out_dir:
            fields = ["icon", "status", "distance_status", "lowest_distance",
                      "gate", "min_gap_kind", "hole_status", "holes",
                      "failed_holes", "pinches", "min_hole_radius", "canvas",
                      "error"]
            with open(os.path.join(args.out_dir, "qa_results.csv"), "w",
                      newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
                w.writeheader()
                w.writerows(rows)
        print(f"total={len(rows)}  overall: {tally('status')}\n"
              f"  distance: {tally('distance_status')} "
              f"(unmeasured passes={unmeasured})\n"
              f"  holes:    {tally('hole_status')}")
        return

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
        # Source-referenced runs are not covered by the saved-output check.
        if not (args.force or args.png or args.src_svg) and \
                existing_metrics(p, args.out_dir, args.gate) is not None:
            print(f"{os.path.basename(p)}: up to date (--force to re-measure)")
            continue
        try:
            process(p, src_metrics=src, hole_metrics=holes,
                    out_dir=args.out_dir, gate=args.gate)
        except Exception as e:
            print(f"warn: {os.path.basename(p)} — QA overlays failed: {e}",
                  file=sys.stderr)


if __name__ == "__main__":
    main()
