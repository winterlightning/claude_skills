#!/usr/bin/env python3
"""Measure enclosed negative space in finished Unlimited Shapes SVGs.

This core validator is adapted from the supplied ``qa_overlays.py`` utility.
The original tool's source-PNG fidelity gates were tied to a 1024px png2svg
pipeline and did not measure hole diameter.  This version renders finished
SVGs directly and reports two related defects on the selected icon profile:

* **Undersized holes** — a background region enclosed by ink whose largest
  inscribed radius is below the design minimum.
* **Pinched junctions** — a region that is *not* a hole only because two
  parts were pushed into each other until their paint merged.  These are
  found by retreating every painted edge inward and reporting any pocket
  that opens up.  A junction that survives only a hair of overlap is a
  squeeze, not a connection, and it muds over at ship size exactly like an
  undersized hole.

Both defects are resolved the same way, and never by moving parts closer:

1. Enlarge the opening (grow the enclosing shape, or move the parts apart).
2. Rebalance the composition (shrink the dominant part so the detail can
   carry a legal opening).
3. Remove the whole part when it is not identity-bearing.

Examples:
  python3 core/qa_overlays.py path/to/icon.svg --output-dir results
  python3 core/qa_overlays.py path/to/final_svg --output-dir results

Outputs:
  <output-dir>/<icon>.metrics.json
  <output-dir>/<icon>_holes.png
  <output-dir>/hole-diameters.csv
  <output-dir>/hole-diameters.json
  <output-dir>/hole-radius-report.html
"""

from __future__ import annotations

import argparse
import csv
import html
import io
import json
import math
import os
import re
import shutil
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
from urllib.parse import quote

import cairosvg
import cv2
import numpy as np
from PIL import Image
from icon_profiles import DEFAULT_ICON_TYPE,get_profile,profile_names


_NORMAL_PROFILE=get_profile(DEFAULT_ICON_TYPE)
DESIGN_CANVAS = float(_NORMAL_PROFILE["designCanvas"])
SHIP_CANVAS = float(_NORMAL_PROFILE["shipCanvas"])
DEFAULT_SAMPLES_PER_UNIT = 32
REGULAR_STROKE_SHIP = 2.0
DEFAULT_MIN_RADIUS_DESIGN_U = 1.0
DEFAULT_MIN_FILL_DEPTH_DESIGN_U = 1.0
DEFAULT_MEASURE_STROKE_DESIGN_U = 1.0
REMEDIATION = (
    "enlarge the opening, rebalance the composition so the detail can carry a "
    "legal opening, or remove the whole part - never merge parts to close it"
)


def _number(value: str | None, fallback: float) -> float:
    if not value:
        return fallback
    token = "".join(ch for ch in value.strip() if ch in "0123456789+-.eE")
    try:
        return float(token)
    except ValueError:
        return fallback


def svg_canvas(svg_path: Path,fallback_canvas: float=SHIP_CANVAS) -> tuple[float, float, float, float]:
    root = ET.parse(svg_path).getroot()
    raw = root.get("viewBox")
    if raw:
        values = [float(item) for item in raw.replace(",", " ").split()]
        if len(values) == 4 and values[2] > 0 and values[3] > 0:
            return tuple(values)  # type: ignore[return-value]
    width = _number(root.get("width"), fallback_canvas)
    height = _number(root.get("height"), fallback_canvas)
    return 0.0, 0.0, width, height


def render_ink_mask(
    svg_path: Path,
    view_width: float,
    view_height: float,
    samples_per_unit: int,
    retreat_view_units: float = 0.0,
) -> np.ndarray:
    width = max(1, int(round(view_width * samples_per_unit)))
    height = max(1, int(round(view_height * samples_per_unit)))
    png = cairosvg.svg2png(
        bytestring=_thinned_svg(svg_path, retreat_view_units),
        output_width=width,
        output_height=height,
    )
    rgba = np.asarray(Image.open(io.BytesIO(png)).convert("RGBA"))
    return rgba[:, :, 3] >= 128


def enclosed_components(ink: np.ndarray) -> tuple[np.ndarray, list[int]]:
    background = (~ink).astype(np.uint8)
    count, labels, stats, _ = cv2.connectedComponentsWithStats(
        background, connectivity=4
    )
    border_labels = set(np.unique(labels[0, :]))
    border_labels.update(np.unique(labels[-1, :]))
    border_labels.update(np.unique(labels[:, 0]))
    border_labels.update(np.unique(labels[:, -1]))
    holes = [
        label
        for label in range(1, count)
        if label not in border_labels and stats[label, cv2.CC_STAT_AREA] > 0
    ]
    return labels, holes


def measure_holes(
    labels: np.ndarray,
    hole_labels: list[int],
    view_box: tuple[float, float, float, float],
    samples_per_unit: int,
    min_radius_design_u: float,
    design_canvas: float=DESIGN_CANVAS,
    ship_canvas: float=SHIP_CANVAS,
) -> list[dict]:
    min_x, min_y, view_width, view_height = view_box
    ship_scale_x = ship_canvas / view_width
    ship_scale_y = ship_canvas / view_height
    design_scale_x = design_canvas / view_width
    design_scale_y = design_canvas / view_height
    pixel_area_in_view_units = 1.0 / (samples_per_unit**2)
    measured = []

    for index, label in enumerate(hole_labels, start=1):
        ys, xs = np.where(labels == label)
        x0, x1 = int(xs.min()), int(xs.max()) + 1
        y0, y1 = int(ys.min()), int(ys.max()) + 1
        component = (labels[y0:y1, x0:x1] == label).astype(np.uint8)
        # A component exactly fills its tight crop, so pad it with known
        # non-hole pixels before computing the largest inscribed circle.
        padded = np.pad(component, 1, mode="constant", constant_values=0)
        distance = cv2.distanceTransform(padded, cv2.DIST_L2, 5)
        _, radius_samples, _, center = cv2.minMaxLoc(distance)
        center_x = min_x + (x0 + center[0] - 0.5) / samples_per_unit
        center_y = min_y + (y0 + center[1] - 0.5) / samples_per_unit
        width_view = (x1 - x0) / samples_per_unit
        height_view = (y1 - y0) / samples_per_unit
        area_view = len(xs) * pixel_area_in_view_units
        equivalent_view = math.sqrt(4.0 * area_view / math.pi)
        inscribed_view = 2.0 * radius_samples / samples_per_unit

        inscribed_diameter_design = (
            inscribed_view * min(design_scale_x, design_scale_y)
        )
        inscribed_radius_design = inscribed_diameter_design / 2.0
        status = (
            "pass" if inscribed_radius_design >= min_radius_design_u else "fail"
        )
        measured.append(
            {
                "hole": index,
                "center_viewbox": [round(center_x, 4), round(center_y, 4)],
                "bbox_viewbox": [
                    round(min_x + x0 / samples_per_unit, 4),
                    round(min_y + y0 / samples_per_unit, 4),
                    round(width_view, 4),
                    round(height_view, 4),
                ],
                "bbox_ship_px": [
                    round(width_view * ship_scale_x, 4),
                    round(height_view * ship_scale_y, 4),
                ],
                "bbox_design_u": [
                    round(width_view * design_scale_x, 4),
                    round(height_view * design_scale_y, 4),
                ],
                "area_ship_px2": round(
                    area_view * ship_scale_x * ship_scale_y, 4
                ),
                "equivalent_diameter_ship_px": round(
                    equivalent_view * math.sqrt(ship_scale_x * ship_scale_y), 4
                ),
                "equivalent_diameter_design_u": round(
                    equivalent_view * math.sqrt(design_scale_x * design_scale_y), 4
                ),
                "inscribed_diameter_ship_px": round(
                    inscribed_view * min(ship_scale_x, ship_scale_y), 4
                ),
                "inscribed_diameter_design_u": round(
                    inscribed_diameter_design, 4
                ),
                "inscribed_radius_ship_px": round(
                    inscribed_view * min(ship_scale_x, ship_scale_y) / 2.0, 4
                ),
                "inscribed_radius_design_u": round(inscribed_radius_design, 4),
                "minimum_radius_design_u": min_radius_design_u,
                "status": status,
            }
        )
    return measured


def authored_stroke_design_u(svg_path, view_box,design_canvas: float=DESIGN_CANVAS):
    root = ET.parse(svg_path).getroot()
    m = re.search(r"stroke-width\s*:\s*([0-9.eE+-]+)", root.get("style") or "")
    width = _number(m.group(1) if m else root.get("stroke-width"), REGULAR_STROKE_SHIP)
    return width * min(design_canvas / view_box[2], design_canvas / view_box[3])


def _thinned_svg(svg_path: Path, retreat_view_units: float) -> bytes:
    """Return the same SVG with every stroke narrowed by 2x the retreat.

    Narrowing the strokes pulls each painted edge back by ``retreat`` without
    touching centerlines, which is exactly how a region that was closed by
    overlapping paint reopens.
    """
    ET.register_namespace("", "http://www.w3.org/2000/svg")
    root = ET.parse(svg_path).getroot()
    style_pattern = re.compile(r"stroke-width\s*:\s*([0-9.eE+-]+)")

    def rewrite(element: ET.Element, inherited: float) -> None:
        width = inherited
        style = element.get("style") or ""
        match = style_pattern.search(style)
        if match:
            width = _number(match.group(1), inherited)
        elif element.get("stroke-width") is not None:
            width = _number(element.get("stroke-width"), inherited)
        narrowed = max(width - 2.0 * retreat_view_units, 1e-4)
        if match:
            element.set(
                "style", style_pattern.sub(f"stroke-width:{narrowed:.6g}", style)
            )
        if element.get("stroke-width") is not None or element is root:
            element.set("stroke-width", f"{narrowed:.6g}")
        for child in element:
            rewrite(child, width)

    rewrite(root, 1.0)
    return ET.tostring(root, encoding="utf-8")


def _pocket_mask(
    svg_path: Path,
    background: np.ndarray,
    view_box: tuple[float, float, float, float],
    samples_per_unit: int,
    retreat_view_units: float,
) -> np.ndarray:
    """Enclosed regions that exist only because strokes overlap.

    Renders the icon with narrowed strokes and keeps the enclosed background
    components that do not contain any real negative space, so genuine holes
    (which simply grow) are excluded.
    """
    width = max(1, int(round(view_box[2] * samples_per_unit)))
    height = max(1, int(round(view_box[3] * samples_per_unit)))
    png = cairosvg.svg2png(
        bytestring=_thinned_svg(svg_path, retreat_view_units),
        output_width=width,
        output_height=height,
    )
    thin_ink = np.asarray(Image.open(io.BytesIO(png)).convert("RGBA"))[:, :, 3] >= 128
    labels, pocket_labels = enclosed_components(thin_ink)
    pockets = np.zeros_like(thin_ink)
    for label in pocket_labels:
        mask = labels == label
        if background[mask].any():
            continue
        pockets |= mask
    return pockets


def find_pinches(
    svg_path: Path,
    ink: np.ndarray,
    view_box: tuple[float, float, float, float],
    samples_per_unit: int,
    min_fill_depth_design_u: float,
    base_retreat_view_units: float = 0.0,
    design_canvas: float=DESIGN_CANVAS,
) -> list[dict]:
    """Report regions that are solid only because parts were squeezed together.

    A real connection stays solid when the paint is trimmed back; a squeezed
    junction reopens into an enclosed pocket. Each pocket is bisected to report
    how little paint was actually holding it closed.
    """
    if min_fill_depth_design_u <= 0:
        return []
    min_x, min_y, view_width, view_height = view_box
    design_scale = min(design_canvas / view_width, design_canvas / view_height)
    retreat = min_fill_depth_design_u / design_scale
    background = ~ink
    cache: dict[float, np.ndarray] = {}

    def pockets_at(value: float) -> np.ndarray:
        key = round(value, 6)
        if key not in cache:
            cache[key] = _pocket_mask(
                svg_path, background, view_box, samples_per_unit,
                base_retreat_view_units + key
            )
        return cache[key]

    pockets = pockets_at(retreat)
    if not pockets.any():
        return []

    count, labels, _, _ = cv2.connectedComponentsWithStats(
        pockets.astype(np.uint8), connectivity=4
    )
    pixel_area_in_view_units = 1.0 / (samples_per_unit**2)
    found = []
    for label in range(1, count):
        mask = labels == label
        ys, xs = np.where(mask)
        component = mask[ys.min(): ys.max() + 1, xs.min(): xs.max() + 1]
        padded = np.pad(component.astype(np.uint8), 1, constant_values=0)
        distance = cv2.distanceTransform(padded, cv2.DIST_L2, 5)
        _, radius_samples, _, peak = cv2.minMaxLoc(distance)
        cx = int(xs.min() + peak[0] - 1)
        cy = int(ys.min() + peak[1] - 1)

        # Bisect the paint retreat to report how thin the closure really is.
        low, high = 0.0, retreat
        for _ in range(7):
            mid = (low + high) / 2.0
            if pockets_at(mid)[cy, cx]:
                high = mid
            else:
                low = mid

        x0, x1 = int(xs.min()), int(xs.max()) + 1
        y0, y1 = int(ys.min()), int(ys.max()) + 1
        found.append(
            {
                "pinch": len(found) + 1,
                "center_viewbox": [
                    round(min_x + (cx + 0.5) / samples_per_unit, 4),
                    round(min_y + (cy + 0.5) / samples_per_unit, 4),
                ],
                "bbox_viewbox": [
                    round(min_x + x0 / samples_per_unit, 4),
                    round(min_y + y0 / samples_per_unit, 4),
                    round((x1 - x0) / samples_per_unit, 4),
                    round((y1 - y0) / samples_per_unit, 4),
                ],
                "trapped_area_design_u2": round(
                    len(xs) * pixel_area_in_view_units * design_scale**2, 4
                ),
                "trapped_radius_design_u": round(
                    radius_samples / samples_per_unit * design_scale, 4
                ),
                "closure_margin_design_u": round(high * design_scale, 4),
                "minimum_fill_depth_design_u": min_fill_depth_design_u,
                "status": "fail",
            }
        )
    return found


def save_overlay(
    ink: np.ndarray,
    labels: np.ndarray,
    hole_labels: list[int],
    holes: list[dict],
    pinches: list[dict],
    output_path: Path,
    view_box: tuple[float, float, float, float],
    samples_per_unit: int,
) -> None:
    canvas = np.full((*ink.shape, 3), 255, dtype=np.uint8)
    canvas[ink] = (25, 25, 25)
    palette = [
        (255, 208, 94),
        (106, 202, 255),
        (255, 139, 170),
        (150, 226, 143),
        (196, 157, 255),
    ]
    for index, label in enumerate(hole_labels):
        canvas[labels == label] = palette[index % len(palette)]
        center_x, center_y = holes[index]["center_viewbox"]
        min_x, min_y, _, _ = view_box
        px = int(round((center_x - min_x) * samples_per_unit))
        py = int(round((center_y - min_y) * samples_per_unit))
        cv2.putText(
            canvas,
            str(index + 1),
            (px, py),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (20, 20, 20),
            1,
            cv2.LINE_AA,
        )
    min_x, min_y, _, _ = view_box
    for pinch in pinches:
        center_x, center_y = pinch["center_viewbox"]
        px = int(round((center_x - min_x) * samples_per_unit))
        py = int(round((center_y - min_y) * samples_per_unit))
        reach = max(6, samples_per_unit // 2)
        cv2.circle(canvas, (px, py), reach, (232, 62, 40), 2, cv2.LINE_AA)
        cv2.line(
            canvas,
            (px - reach, py - reach),
            (px + reach, py + reach),
            (232, 62, 40),
            2,
            cv2.LINE_AA,
        )
        cv2.line(
            canvas,
            (px - reach, py + reach),
            (px + reach, py - reach),
            (232, 62, 40),
            2,
            cv2.LINE_AA,
        )
    Image.fromarray(canvas).save(output_path)


def collect_svgs(inputs: list[str]) -> list[Path]:
    files: set[Path] = set()
    for raw in inputs:
        path = Path(raw).expanduser().resolve()
        if path.is_dir():
            files.update(item for item in path.glob("*.svg") if item.is_file())
        elif path.is_file() and path.suffix.lower() == ".svg":
            files.add(path)
        else:
            print(f"warn: skipping missing/non-SVG input: {path}", file=sys.stderr)
    return sorted(files)


def process(
    svg_path: Path,
    output_dir: Path,
    samples_per_unit: int,
    min_radius_design_u: float,
    min_fill_depth_design_u: float,
    icon_type: str=DEFAULT_ICON_TYPE,
) -> dict:
    profile=get_profile(icon_type); design_canvas=float(profile["designCanvas"]); ship_canvas=float(profile["shipCanvas"])
    view_box = svg_canvas(svg_path,ship_canvas)
    design_scale = min(design_canvas / view_box[2], design_canvas / view_box[3])
    authored = authored_stroke_design_u(svg_path, view_box,design_canvas)
    measure = min(DEFAULT_MEASURE_STROKE_DESIGN_U, authored)
    retreat_design = (authored - measure) / 2.0
    retreat_view = retreat_design / design_scale
    min_radius_design_u = min_radius_design_u + retreat_design
    min_fill_depth_design_u = max(0.0, min_fill_depth_design_u - retreat_design)
    ink = render_ink_mask(svg_path, view_box[2], view_box[3], samples_per_unit, retreat_view)
    labels, hole_labels = enclosed_components(ink)
    holes = measure_holes(
        labels,
        hole_labels,
        view_box,
        samples_per_unit,
        min_radius_design_u,
        design_canvas,
        ship_canvas,
    )
    pinches = find_pinches(
        svg_path, ink, view_box, samples_per_unit, min_fill_depth_design_u, retreat_view,design_canvas
    )
    for _h in holes:
        _h["equivalent_radius_at_authored_stroke_design_u"] = round(
            _h["inscribed_radius_design_u"] - retreat_design, 4)
    failed_holes = [hole for hole in holes if hole["status"] == "fail"]
    result = {
        "file": svg_path.name,
        "source": str(svg_path),
        "iconType": icon_type,
        "viewBox": list(view_box),
        "normalizedCanvases": {"designUnits": design_canvas, "shipPixels": ship_canvas},
        "samplesPerViewBoxUnit": samples_per_unit,
        "minimumRadiusDesignUnits": min_radius_design_u,
        "minimumFillDepthDesignUnits": min_fill_depth_design_u,
        "hole_count": len(holes),
        "failed_hole_count": len(failed_holes),
        "pinch_count": len(pinches),
        "status": "fail" if failed_holes or pinches else "pass",
        "remediation": REMEDIATION,
        "holes": holes,
        "pinches": pinches,
    }
    metrics_path = output_dir / f"{svg_path.stem}.metrics.json"
    metrics_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    save_overlay(
        ink,
        labels,
        hole_labels,
        holes,
        pinches,
        output_dir / f"{svg_path.stem}_holes.png",
        view_box,
        samples_per_unit,
    )
    return result


def write_html_report(
    results: list[dict],
    output_dir: Path,
    min_radius_design_u: float,
    min_fill_depth_design_u: float,
) -> None:
    failed = [result for result in results if result["status"] == "fail"]
    failed_hole_count = sum(result["failed_hole_count"] for result in failed)
    pinch_count = sum(result["pinch_count"] for result in failed)
    rows = []
    for result in failed:
        failed_holes = [hole for hole in result["holes"] if hole["status"] == "fail"]
        measurements = [
            f"Hole {hole['hole']}: {hole['inscribed_radius_design_u']:.4g}u radius "
            f"({hole['inscribed_diameter_design_u']:.4g}u diameter) "
            f"at {hole['center_viewbox'][0]:g},{hole['center_viewbox'][1]:g}"
            for hole in failed_holes
        ]
        measurements += [
            f"<span class=\"pinch\">Pinch {pinch['pinch']}</span>: junction held closed by "
            f"only {pinch['closure_margin_design_u']:.4g}u of overlapping paint "
            f"at {pinch['center_viewbox'][0]:g},{pinch['center_viewbox'][1]:g}"
            for pinch in result["pinches"]
        ]
        stem = Path(result["file"]).stem
        overlay = quote(f"{stem}_holes.png")
        metrics = quote(f"{stem}.metrics.json")
        rows.append(
            "<tr>"
            f"<td><code>{html.escape(result['file'])}</code></td>"
            f"<td>{len(failed_holes)}</td>"
            f"<td>{result['pinch_count']}</td>"
            f"<td>{'<br>'.join(measurements)}</td>"
            f"<td><a href=\"{overlay}\">overlay</a> · "
            f"<a href=\"{metrics}\">metrics</a></td>"
            "</tr>"
        )
    body = "\n".join(rows) if rows else (
        '<tr><td colspan="5" class="empty">No files failed.</td></tr>'
    )
    document = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Unlimited Shapes hole-radius QA</title>
  <style>
    :root {{ color-scheme: light; font-family: Inter, ui-sans-serif, system-ui, sans-serif; }}
    body {{ margin: 0; background: #f4f5f7; color: #16181d; }}
    main {{ max-width: 1100px; margin: 0 auto; padding: 40px 24px; }}
    h1 {{ margin: 0 0 8px; font-size: 30px; }}
    .lede {{ margin: 0 0 24px; color: #565c66; }}
    .cards {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; margin-bottom: 24px; }}
    .card {{ background: white; border: 1px solid #dde0e5; border-radius: 12px; padding: 18px; }}
    .value {{ display: block; font-size: 28px; font-weight: 750; }}
    .label {{ color: #666d78; font-size: 13px; }}
    .fail {{ color: #b42318; }}
    table {{ width: 100%; border-collapse: collapse; background: white; border: 1px solid #dde0e5; }}
    th, td {{ padding: 12px 14px; text-align: left; border-bottom: 1px solid #e7e9ed; vertical-align: top; }}
    th {{ background: #f8f9fa; color: #4e5560; font-size: 12px; text-transform: uppercase; letter-spacing: .04em; }}
    td:nth-child(2), td:nth-child(3) {{ text-align: center; }}
    .pinch {{ color: #b42318; font-weight: 650; }}
    .policy {{ background: white; border: 1px solid #dde0e5; border-radius: 12px; padding: 18px 22px; margin-bottom: 24px; }}
    .policy li {{ margin: 4px 0; }}
    a {{ color: #155eef; }}
    code {{ font-size: 13px; }}
    .empty {{ color: #247a3d; text-align: center; padding: 32px; }}
    @media (max-width: 700px) {{ .cards {{ grid-template-columns: 1fr; }} table {{ font-size: 13px; }} }}
  </style>
</head>
<body>
<main>
  <h1>Hole-radius QA</h1>
  <p class="lede">A file fails when any enclosed region has an inscribed radius below
    {min_radius_design_u:g} design unit ({min_radius_design_u / 2:g}px at ship size),
    or when a junction is solid only because parts were squeezed together — paint
    filling it less than {min_fill_depth_design_u:g}u deep. Equality passes.</p>
  <section class="cards">
    <div class="card"><span class="value">{len(results)}</span><span class="label">SVG files checked</span></div>
    <div class="card"><span class="value fail">{len(failed)}</span><span class="label">failed files</span></div>
    <div class="card"><span class="value fail">{failed_hole_count}</span><span class="label">failed holes</span></div>
    <div class="card"><span class="value fail">{pinch_count}</span><span class="label">pinched junctions</span></div>
  </section>
  <section class="policy">
    <strong>How to fix a failing zone</strong> — give the geometry more room, in this order:
    <ol>
      <li>Enlarge the opening: grow the enclosing shape, or move the parts apart.</li>
      <li>Rebalance the composition: shrink the dominant part so the detail can carry a legal opening.</li>
      <li>Remove the whole part when it is not identity-bearing. Never clip a fragment.</li>
    </ol>
    Never close a failing region by pushing parts into each other until the paint merges.
    That trades a measurable hole for an unmeasurable mud spot, and the pinch check fails it.
  </section>
  <table>
    <thead><tr><th>File</th><th>Failed holes</th><th>Pinches</th><th>Measurement</th><th>Evidence</th></tr></thead>
    <tbody>{body}</tbody>
  </table>
</main>
</body>
</html>
"""
    (output_dir / "hole-radius-report.html").write_text(document, encoding="utf-8")


def write_aggregate(
    results: list[dict],
    output_dir: Path,
    min_radius_design_u: float,
    min_fill_depth_design_u: float,
) -> None:
    (output_dir / "hole-diameters.json").write_text(
        json.dumps(results, indent=2) + "\n", encoding="utf-8"
    )
    columns = [
        "file",
        "region_type",
        "region_index",
        "center_x_viewbox",
        "center_y_viewbox",
        "bbox_width_ship_px",
        "bbox_height_ship_px",
        "equivalent_diameter_ship_px",
        "inscribed_diameter_ship_px",
        "bbox_width_design_u",
        "bbox_height_design_u",
        "equivalent_diameter_design_u",
        "inscribed_diameter_design_u",
        "inscribed_radius_ship_px",
        "inscribed_radius_design_u",
        "minimum_radius_design_u",
        "closure_margin_design_u",
        "trapped_radius_design_u",
        "minimum_fill_depth_design_u",
        "status",
    ]
    with (output_dir / "hole-diameters.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for result in results:
            for hole in result["holes"]:
                writer.writerow(
                    {
                        "file": result["file"],
                        "region_type": "hole",
                        "region_index": hole["hole"],
                        "center_x_viewbox": hole["center_viewbox"][0],
                        "center_y_viewbox": hole["center_viewbox"][1],
                        "bbox_width_ship_px": hole["bbox_ship_px"][0],
                        "bbox_height_ship_px": hole["bbox_ship_px"][1],
                        "equivalent_diameter_ship_px": hole[
                            "equivalent_diameter_ship_px"
                        ],
                        "inscribed_diameter_ship_px": hole[
                            "inscribed_diameter_ship_px"
                        ],
                        "bbox_width_design_u": hole["bbox_design_u"][0],
                        "bbox_height_design_u": hole["bbox_design_u"][1],
                        "equivalent_diameter_design_u": hole[
                            "equivalent_diameter_design_u"
                        ],
                        "inscribed_diameter_design_u": hole[
                            "inscribed_diameter_design_u"
                        ],
                        "inscribed_radius_ship_px": hole[
                            "inscribed_radius_ship_px"
                        ],
                        "inscribed_radius_design_u": hole[
                            "inscribed_radius_design_u"
                        ],
                        "minimum_radius_design_u": hole[
                            "minimum_radius_design_u"
                        ],
                        "status": hole["status"],
                    }
                )
            for pinch in result["pinches"]:
                writer.writerow(
                    {
                        "file": result["file"],
                        "region_type": "pinch",
                        "region_index": pinch["pinch"],
                        "center_x_viewbox": pinch["center_viewbox"][0],
                        "center_y_viewbox": pinch["center_viewbox"][1],
                        "closure_margin_design_u": pinch[
                            "closure_margin_design_u"
                        ],
                        "trapped_radius_design_u": pinch[
                            "trapped_radius_design_u"
                        ],
                        "minimum_fill_depth_design_u": pinch[
                            "minimum_fill_depth_design_u"
                        ],
                        "status": pinch["status"],
                    }
                )
    write_html_report(
        results, output_dir, min_radius_design_u, min_fill_depth_design_u
    )


DEFAULT_ERROR_DIRNAME = "hole_error"

#: File patterns this tool owns inside the error folder, cleared on every run so
#: a fixed icon never lingers there and gets re-reported as still failing.
ERROR_DIR_OWNED = ("*.svg", "*_holes.png", "*.metrics.json", "README.md")


def collect_failures(
    results: list[dict],
    output_dir: Path,
    error_dir: Path,
    min_radius_design_u: float,
    min_fill_depth_design_u: float,
) -> list[dict]:
    """Copy every failing icon into `error_dir` with its overlay and metrics.

    The folder is a ready-to-work queue: the SVG to edit, the overlay showing
    where it fails, the numbers behind the call, and a README naming each zone.
    """
    failed = [item for item in results if item["status"] == "fail"]
    error_dir.mkdir(parents=True, exist_ok=True)
    for pattern in ERROR_DIR_OWNED:
        for stale in error_dir.glob(pattern):
            stale.unlink()
    if not failed:
        return failed

    lines = [
        "# Hole-gate failures",
        "",
        f"{len(failed)} of {len(results)} icons failed. Gate: enclosed regions need an",
        f"inscribed radius of at least {min_radius_design_u:g}u on the design canvas, and a solid",
        f"junction must be filled at least {min_fill_depth_design_u:g}u deep or it counts as a pinch.",
        "",
        "Each icon is copied here with its `_holes.png` overlay and `.metrics.json`.",
        "Repair in place, then rerun the gate on this folder.",
        "",
        "Ladder (stop at the first rung that keeps the icon recognisable):",
        "enlarge the opening, rebalance the composition, or remove the whole part.",
        "Never merge parts to close a region, and recheck keyfit afterwards — every",
        "rung moves paint, and the token is measured from painted bounds.",
        "",
    ]
    for item in failed:
        source = Path(item["source"])
        shutil.copy2(source, error_dir / source.name)
        for extra in (f"{source.stem}_holes.png", f"{source.stem}.metrics.json"):
            candidate = output_dir / extra
            if candidate.is_file():
                shutil.copy2(candidate, error_dir / extra)

        lines.append(f"## {item['file']}")
        lines.append("")
        lines.append(
            f"{item['failed_hole_count']} undersized hole(s), "
            f"{item['pinch_count']} pinched junction(s)."
        )
        lines.append("")
        lines.append("| zone | centre (design u) | measured | gate |")
        lines.append("| --- | --- | --- | --- |")
        for hole in item["holes"]:
            if hole["status"] != "fail":
                continue
            cx, cy = hole["center_viewbox"]
            lines.append(
                f"| hole {hole['hole']} | ({cx:g}, {cy:g}) | "
                f"inscribed r {hole['inscribed_radius_design_u']:g}u | "
                f"{min_radius_design_u:g}u |"
            )
        for pinch in item.get("pinches", []):
            cx, cy = pinch["center_viewbox"]
            lines.append(
                f"| pinch {pinch['pinch']} | ({cx:g}, {cy:g}) | "
                f"trapped r {pinch['trapped_radius_design_u']:g}u | "
                f"fill depth {min_fill_depth_design_u:g}u |"
            )
        lines.append("")
    (error_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")
    return failed



def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("inputs", nargs="+", help="SVG files or flat SVG folders")
    parser.add_argument(
        "--icon-type",choices=profile_names(),default=DEFAULT_ICON_TYPE,
        help="icon profile to normalize against (default: normal)",
    )
    parser.add_argument(
        "--output-dir", required=True, help="folder for reports and overlays"
    )
    parser.add_argument(
        "--error-dir",
        default=None,
        help=(
            "folder to copy failing icons into, with their overlays and metrics "
            f"(default: <output-dir>/{DEFAULT_ERROR_DIRNAME})"
        ),
    )
    parser.add_argument(
        "--samples-per-unit",
        type=int,
        default=DEFAULT_SAMPLES_PER_UNIT,
        help="raster supersampling per SVG viewBox unit (default: 32)",
    )
    parser.add_argument(
        "--min-radius-design-u",
        type=float,
        default=DEFAULT_MIN_RADIUS_DESIGN_U,
        help="minimum passing inscribed hole radius in profile design units (default: 1)",
    )
    parser.add_argument(
        "--min-fill-depth-design-u",
        type=float,
        default=DEFAULT_MIN_FILL_DEPTH_DESIGN_U,
        help=(
            "minimum paint depth, in profile design units, that must fill a solid "
            "junction before it counts as a connection instead of a squeeze; "
            "0 disables the pinch check (default: 1)"
        ),
    )
    args = parser.parse_args()
    if args.samples_per_unit < 4:
        parser.error("--samples-per-unit must be at least 4")
    if args.min_radius_design_u <= 0:
        parser.error("--min-radius-design-u must be greater than zero")
    if args.min_fill_depth_design_u < 0:
        parser.error("--min-fill-depth-design-u must not be negative")

    svgs = collect_svgs(args.inputs)
    if not svgs:
        parser.error("no SVG files found")
    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    results = []
    for svg_path in svgs:
        try:
            result = process(
                svg_path,
                output_dir,
                args.samples_per_unit,
                args.min_radius_design_u,
                args.min_fill_depth_design_u,
                args.icon_type,
            )
            results.append(result)
            print(
                f"{svg_path.name}: {result['hole_count']} enclosed hole(s), "
                f"{result['failed_hole_count']} undersized, "
                f"{result['pinch_count']} pinched junction(s), "
                f"{result['status'].upper()}"
            )
        except Exception as exc:
            print(f"warn: {svg_path.name}: {exc}", file=sys.stderr)
    write_aggregate(
        results,
        output_dir,
        args.min_radius_design_u,
        args.min_fill_depth_design_u,
    )
    print(f"wrote {len(results)} icon reports to {output_dir}")

    error_dir = (
        Path(args.error_dir).expanduser().resolve()
        if args.error_dir
        else output_dir / DEFAULT_ERROR_DIRNAME
    )
    failed = collect_failures(
        results,
        output_dir,
        error_dir,
        args.min_radius_design_u,
        args.min_fill_depth_design_u,
    )
    if failed:
        print(f"copied {len(failed)} failing icon(s) to {error_dir}")
        print(f"fix a failing zone by: {REMEDIATION}.", file=sys.stderr)


if __name__ == "__main__":
    main()
