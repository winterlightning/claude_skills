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
  <error-dir>/README.md links the current run-specific diagnostic evidence

Exit 0: all selected inputs pass. Exit 1: any failed hole, pinch, input,
processing, or report error. Exit 2: invalid arguments or an empty selection.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import io
import json
import math
import os
import re
import shutil
from pathlib import Path
import sys
import tempfile
import xml.etree.ElementTree as ET
from urllib.parse import quote

import cairosvg
import cv2
import numpy as np
from PIL import Image
from icon_profiles import DEFAULT_ICON_TYPE,get_profile,profile_names,svg_native_size_issues


_NORMAL_PROFILE=get_profile(DEFAULT_ICON_TYPE)
DESIGN_CANVAS = float(_NORMAL_PROFILE["designCanvas"])
SHIP_CANVAS = float(_NORMAL_PROFILE["shipCanvas"])
DEFAULT_SAMPLES_PER_UNIT = 32
# SVG itself defaults an omitted stroke-width to 1. Canonical native output
# explicitly declares profile stroke4, so this is only a diagnostic fallback.
SVG_DEFAULT_STROKE_WIDTH = 1.0
DEFAULT_MIN_RADIUS_DESIGN_U = _NORMAL_PROFILE["validation"]["minimumEnclosedRadius"]
DEFAULT_MIN_FILL_DEPTH_DESIGN_U = _NORMAL_PROFILE["validation"]["minimumSolidFillDepth"]
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
    width = _number(m.group(1) if m else root.get("stroke-width"), SVG_DEFAULT_STROKE_WIDTH)
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

    rewrite(root, SVG_DEFAULT_STROKE_WIDTH)
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


def _collect_svg_inputs(inputs: list[str]) -> tuple[list[Path], list[tuple[Path, str]]]:
    files: set[Path] = set()
    errors: dict[Path, str] = {}
    for raw in inputs:
        path = Path(raw).expanduser().absolute()
        try:
            path = path.resolve()
            if path.is_dir():
                selected = [item.resolve() for item in path.iterdir() if item.suffix.lower() == ".svg"]
                if selected:
                    files.update(selected)
                else:
                    errors[path] = "folder contains no immediate SVG files"
            elif path.suffix.lower() == ".svg":
                files.add(path)
            else:
                errors[path] = "input must be an SVG file or flat SVG folder"
        except (OSError, RuntimeError) as error:
            errors[path] = str(error)
    return sorted(files), sorted(errors.items())


def collect_svgs(inputs: list[str]) -> list[Path]:
    """Collect SVG candidates; malformed selections raise, missing SVGs stay visible."""
    files, errors = _collect_svg_inputs(inputs)
    if errors:
        raise ValueError("; ".join(f"{path}: {error}" for path, error in errors))
    return files


def _safe_target(path: Path, protected=()) -> None:
    if path.is_symlink() or path.exists() and not path.is_file():
        raise ValueError(f"unsafe report target: {path}")
    for source in protected:
        source = Path(source)
        if path.resolve() == source.resolve() or (path.exists() and source.exists() and path.samefile(source)):
            raise ValueError(f"report target would overwrite a selected input: {path}")


def _write_text(path: Path, text: str, protected=()) -> None:
    _safe_target(path, protected)
    staged = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                         prefix=".hole-qa-", delete=False) as handle:
            staged = Path(handle.name)
            handle.write(text)
        os.replace(staged, path)
    finally:
        if staged is not None and staged.exists():
            staged.unlink()


def _validate_directories(output_dir: Path, error_dir: Path, protected) -> None:
    for directory in (output_dir, error_dir):
        if directory.is_symlink() or directory.exists() and not directory.is_dir():
            raise ValueError(f"unsafe QA directory: {directory}")
        for source in protected:
            if Path(source).resolve().is_relative_to(directory.resolve()):
                raise ValueError(f"QA/error directory contains a selected input: {directory}")
    if output_dir.resolve().is_relative_to(error_dir.resolve()):
        raise ValueError("error directory cannot equal or contain the QA output directory")


def _error_result(path: Path, error: object, icon_type: str, radius: float, fill: float) -> dict:
    return {"file": path.name, "source": str(path), "iconType": icon_type,
            "validation": get_profile(icon_type)["validation"],
            "configuredMinimumRadiusDesignUnits": radius,
            "configuredMinimumFillDepthDesignUnits": fill,
            "hole_count": 0, "failed_hole_count": 0, "pinch_count": 0,
            "status": "fail", "holes": [], "pinches": [], "nativeSizeIssues": [],
            "svgSha256": None, "profileSha256": None,
            "processingErrors": [str(error)], "remediation": REMEDIATION}


def process(
    svg_path: Path,
    output_dir: Path,
    samples_per_unit: int,
    min_radius_design_u: float | None = None,
    min_fill_depth_design_u: float | None = None,
    icon_type: str=DEFAULT_ICON_TYPE,
) -> dict:
    profile=get_profile(icon_type); design_canvas=float(profile["designCanvas"]); ship_canvas=float(profile["shipCanvas"])
    source_bytes = svg_path.read_bytes()
    svg_sha256 = hashlib.sha256(source_bytes).hexdigest()
    profile_sha256 = hashlib.sha256(json.dumps(profile, sort_keys=True, separators=(",", ":"),
                                               ensure_ascii=False, allow_nan=False).encode("utf-8")).hexdigest()
    min_radius_design_u=profile["validation"]["minimumEnclosedRadius"] if min_radius_design_u is None else min_radius_design_u
    min_fill_depth_design_u=profile["validation"]["minimumSolidFillDepth"] if min_fill_depth_design_u is None else min_fill_depth_design_u
    if not math.isfinite(min_radius_design_u) or min_radius_design_u <= 0:
        raise ValueError("minimum enclosed radius must be finite and positive")
    if not math.isfinite(min_fill_depth_design_u) or min_fill_depth_design_u < 0:
        raise ValueError("minimum solid fill depth must be finite and nonnegative")
    configured_radius, configured_fill = min_radius_design_u, min_fill_depth_design_u
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
    size_issues = svg_native_size_issues(ET.parse(svg_path).getroot().attrib, icon_type)
    result = {
        "file": svg_path.name,
        "source": str(svg_path),
        "svgSha256": svg_sha256,
        "profileSha256": profile_sha256,
        "iconType": icon_type,
        "viewBox": list(view_box),
        "normalizedCanvases": {"designUnits": design_canvas, "shipPixels": ship_canvas},
        "validation": profile["validation"],
        "configuredMinimumRadiusDesignUnits": configured_radius,
        "configuredMinimumFillDepthDesignUnits": configured_fill,
        "samplesPerViewBoxUnit": samples_per_unit,
        "minimumRadiusDesignUnits": min_radius_design_u,
        "minimumFillDepthDesignUnits": min_fill_depth_design_u,
        "hole_count": len(holes),
        "failed_hole_count": len(failed_holes),
        "pinch_count": len(pinches),
        "status": "fail" if failed_holes or pinches or size_issues else "pass",
        "nativeSizeIssues": size_issues,
        "remediation": REMEDIATION,
        "holes": holes,
        "pinches": pinches,
    }
    try:
        if svg_path.read_bytes() != source_bytes:
            result.update(status="fail", processingErrors=["SVG changed during hole/pinch measurement; regenerate and rerun all verification gates"])
    except OSError as error:
        result.update(status="fail", processingErrors=[f"SVG became unreadable during hole/pinch measurement: {error}"])
    metrics_path = output_dir / f"{svg_path.stem}.metrics.json"
    overlay_path = output_dir / f"{svg_path.stem}_holes.png"
    _safe_target(metrics_path, [svg_path])
    _safe_target(overlay_path, [svg_path])
    save_overlay(
        ink,
        labels,
        hole_labels,
        holes,
        pinches,
        overlay_path,
        view_box,
        samples_per_unit,
    )
    _write_text(metrics_path, json.dumps(result, indent=2, allow_nan=False) + "\n", [svg_path])
    return result


def write_html_report(
    results: list[dict],
    output_dir: Path,
    min_radius_design_u: float | None = None,
    min_fill_depth_design_u: float | None = None,
) -> None:
    radius_text = f"{min_radius_design_u:g} design unit ({min_radius_design_u:g}px at native size)" if min_radius_design_u is not None else "the configured minimum for that icon's profile (native units equal pixels)"
    fill_text = f"{min_fill_depth_design_u:g}u" if min_fill_depth_design_u is not None else "that profile's configured minimum solid fill depth"
    policies = set()
    for result in results:
        icon_type = result.get("iconType", DEFAULT_ICON_TYPE)
        validation = result.get("validation") or get_profile(icon_type)["validation"]
        radius = result.get("configuredMinimumRadiusDesignUnits", min_radius_design_u if min_radius_design_u is not None else validation["minimumEnclosedRadius"])
        fill = result.get("configuredMinimumFillDepthDesignUnits", min_fill_depth_design_u if min_fill_depth_design_u is not None else validation["minimumSolidFillDepth"])
        policies.add(f"{icon_type}: enclosed radius ≥{radius:g}u; solid fill depth ≥{fill:g}u")
    policy_text = "; ".join(html.escape(policy) for policy in sorted(policies)) or "No icons checked."
    failed = [result for result in results if result["status"] == "fail"]
    failed_hole_count = sum(result["failed_hole_count"] for result in failed)
    pinch_count = sum(result["pinch_count"] for result in failed)
    rows = []
    for result in failed:
        failed_holes = [hole for hole in result["holes"] if hole["status"] == "fail"]
        measurements = [html.escape(str(error)) for error in result.get("processingErrors", [])]
        measurements += [html.escape(issue["detail"]) for issue in result.get("nativeSizeIssues", [])] + [
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
        evidence = "Processing failed; see aggregate JSON" if result.get("processingErrors") else (
            f'<a href="{overlay}">overlay</a> · <a href="{metrics}">metrics</a>'
        )
        rows.append(
            "<tr>"
            f"<td><code>{html.escape(result['file'])}</code></td>"
            f"<td>{len(failed_holes)}</td>"
            f"<td>{result['pinch_count']}</td>"
            f"<td>{'<br>'.join(measurements)}</td>"
            f"<td>{evidence}</td>"
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
    {radius_text},
    or when a junction is solid only because parts were squeezed together — paint
    filling it less than {fill_text} deep. Equality passes. Per-file JSON records the effective settings and explicit overrides.</p>
  <p class="lede">Effective settings: {policy_text}</p>
  <p class="lede">Invalid or unreadable inputs and processing errors also fail the gate; they are never skipped.</p>
  <section class="cards">
    <div class="card"><span class="value">{len(results)}</span><span class="label">selected inputs</span></div>
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
    _write_text(output_dir / "hole-radius-report.html", document, [item["source"] for item in results])


def write_aggregate(
    results: list[dict],
    output_dir: Path,
    min_radius_design_u: float | None = None,
    min_fill_depth_design_u: float | None = None,
) -> None:
    protected = [item["source"] for item in results]
    _write_text(output_dir / "hole-diameters.json", json.dumps(results, indent=2, allow_nan=False) + "\n", protected)
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
        "processing_error",
    ]
    with io.StringIO(newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for result in results:
            for error in result.get("processingErrors", []):
                writer.writerow({"file": result["file"], "region_type": "processing-error", "status": "fail", "processing_error": str(error)})
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
        _write_text(output_dir / "hole-diameters.csv", handle.getvalue(), protected)
    write_html_report(
        results, output_dir, min_radius_design_u, min_fill_depth_design_u
    )


DEFAULT_ERROR_DIRNAME = "hole_error"

def collect_failures(
    results: list[dict],
    output_dir: Path,
    error_dir: Path,
    min_radius_design_u: float,
    min_fill_depth_design_u: float,
) -> list[dict]:
    """Save current failure evidence in a fresh run; never delete user SVGs.

    Copies are diagnostic references, not editable source or production output.
    The root README identifies the current run; older runs remain historical.
    """
    failed = [item for item in results if item["status"] == "fail"]
    protected = [Path(item["source"]) for item in results]
    _validate_directories(output_dir, error_dir, protected)
    error_dir.mkdir(parents=True, exist_ok=True)
    _safe_target(error_dir / "README.md", protected)
    if not failed:
        _write_text(error_dir / "README.md", "# Hole-gate results\n\nNo inputs failed in the current run.\n\nOlder run folders are historical diagnostic evidence, not current approval.\n", protected)
        return failed

    run_dir = Path(tempfile.mkdtemp(prefix="run-", dir=error_dir))

    lines = [
        "# Hole-gate failures",
        "",
        f"{len(failed)} of {len(results)} inputs failed. Gate: enclosed regions need an",
        f"inscribed radius of at least {min_radius_design_u:g}u on the design canvas, and a solid",
        f"junction must be filled at least {min_fill_depth_design_u:g}u deep or it counts as a pinch.",
        "",
        "Each available SVG is copied into a numbered evidence folder with its overlay and metrics when processing succeeded.",
        "These copies are diagnostic references only. Repair the authoritative editable JSON,",
        "regenerate both canonical SVG aliases, then rerun distance → holes/pinches → keyshape verification on those outputs.",
        "Do not edit or validate these report copies as production output, and do not change thresholds to conceal failures.",
        "",
        "Ladder (stop at the first rung that keeps the icon recognisable):",
        "enlarge the opening, rebalance the composition, or remove the whole part.",
        "Never merge parts to close a region, and recheck keyfit afterwards — every",
        "rung moves paint, and the token is measured from painted bounds.",
        "",
    ]
    for index, item in enumerate(failed, start=1):
        source = Path(item["source"])
        evidence = run_dir / str(index)
        evidence.mkdir()
        if source.is_file() and source.suffix.lower() == ".svg":
            shutil.copy2(source, evidence / source.name)
        if not item.get("processingErrors"):
            for extra in (f"{source.stem}_holes.png", f"{source.stem}.metrics.json"):
                candidate = output_dir / extra
                if candidate.is_file():
                    shutil.copy2(candidate, evidence / extra)

        lines.append(f"## {item['file']}")
        lines.append("")
        lines.append(f"Authoritative generated SVG: `{source}`. Diagnostic evidence: `{index}/`.")
        lines.append("")
        for error in item.get("processingErrors", []):
            lines.append(f"Processing failure: {error}")
            lines.append("")
        for issue in item.get("nativeSizeIssues", []):
            lines.append(f"Native-size failure: {issue['detail']}")
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
    _write_text(run_dir / "README.md", "\n".join(lines), protected)
    _write_text(error_dir / "README.md",
                f"# Hole-gate results\n\nCurrent run: [{run_dir.name}]({run_dir.name}/README.md) — {len(failed)} of {len(results)} inputs failed.\n\n"
                "Repair the authoritative editable JSON and regenerate both canonical SVGs; report copies are diagnostic only.\n\n"
                "Older run folders are historical diagnostic evidence, not current approval.\n", protected)
    return failed



def main(argv=None) -> int:
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
            "folder for run-specific failure evidence; SVG copies are diagnostic only "
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
        default=None,
        help="minimum passing enclosed radius (default: profile validation.minimumEnclosedRadius)",
    )
    parser.add_argument(
        "--min-fill-depth-design-u",
        type=float,
        default=None,
        help=(
            "minimum paint depth, in profile design units, that must fill a solid "
            "junction before it counts as a connection instead of a squeeze; "
            "0 disables the pinch check (default: profile validation.minimumSolidFillDepth)"
        ),
    )
    args = parser.parse_args(argv)
    validation = get_profile(args.icon_type)["validation"]
    if args.min_radius_design_u is None:
        args.min_radius_design_u = validation["minimumEnclosedRadius"]
    if args.min_fill_depth_design_u is None:
        args.min_fill_depth_design_u = validation["minimumSolidFillDepth"]
    if args.samples_per_unit < 4:
        parser.error("--samples-per-unit must be at least 4")
    if not math.isfinite(args.min_radius_design_u) or args.min_radius_design_u <= 0:
        parser.error("--min-radius-design-u must be greater than zero")
    if not math.isfinite(args.min_fill_depth_design_u) or args.min_fill_depth_design_u < 0:
        parser.error("--min-fill-depth-design-u must not be negative")

    svgs, selection_errors = _collect_svg_inputs(args.inputs)
    if not svgs and selection_errors and all(path.is_dir() and error == "folder contains no immediate SVG files" for path, error in selection_errors):
        parser.error("no SVG files found")
    output_dir = Path(args.output_dir).expanduser().absolute()
    error_dir = Path(args.error_dir).expanduser().absolute() if args.error_dir else output_dir / DEFAULT_ERROR_DIRNAME
    protected = [*svgs, *(path for path, _ in selection_errors)]
    try:
        _validate_directories(output_dir, error_dir, protected)
        output_dir.mkdir(parents=True, exist_ok=True)
        for name in ("hole-diameters.json", "hole-diameters.csv", "hole-radius-report.html"):
            _safe_target(output_dir / name, protected)
        for svg_path in svgs:
            for name in (f"{svg_path.stem}.metrics.json", f"{svg_path.stem}_holes.png"):
                _safe_target(output_dir / name, protected)
    except (OSError, ValueError) as error:
        print(f"FAIL unsafe or unavailable QA destination: {error}", file=sys.stderr)
        return 1

    results = [_error_result(path, error, args.icon_type, args.min_radius_design_u, args.min_fill_depth_design_u)
               for path, error in selection_errors]
    stems = {}
    for path in svgs:
        stems.setdefault(path.stem.casefold(), []).append(path)
    for svg_path in svgs:
        try:
            if not svg_path.is_file() or svg_path.suffix.lower() != ".svg":
                raise ValueError("selected input is missing or is not a regular SVG file")
            if len(stems[svg_path.stem.casefold()]) > 1:
                raise ValueError("selected SVGs have duplicate stems; use unique names so QA artifacts cannot overwrite each other")
            result = process(
                svg_path,
                output_dir,
                args.samples_per_unit,
                args.min_radius_design_u,
                args.min_fill_depth_design_u,
                args.icon_type,
            )
            if not isinstance(result, dict) or result.get("status") not in ("pass", "fail"):
                raise ValueError("hole/pinch checker returned a malformed result")
            for field in ("hole_count", "failed_hole_count", "pinch_count"):
                if type(result.get(field)) is not int or result[field] < 0:
                    raise ValueError(f"hole/pinch checker returned an invalid {field}")
            if result.get("file") != svg_path.name or result.get("source") != str(svg_path):
                raise ValueError("hole/pinch checker returned a report for a different input")
            if not isinstance(result.get("holes"), list) or not isinstance(result.get("pinches"), list):
                raise ValueError("hole/pinch checker returned missing region measurements")
            if any(not isinstance(region, dict) or region.get("status") not in ("pass", "fail")
                   for region in [*result["holes"], *result["pinches"]]):
                raise ValueError("hole/pinch checker returned invalid region verdicts")
            if (result["hole_count"] != len(result["holes"]) or result["pinch_count"] != len(result["pinches"])
                    or result["failed_hole_count"] != sum(hole["status"] == "fail" for hole in result["holes"])):
                raise ValueError("hole/pinch checker returned inconsistent region counts")
            if result["failed_hole_count"] or result["pinch_count"] or result.get("nativeSizeIssues") or result.get("processingErrors"):
                result["status"] = "fail"
            print(
                f"{svg_path.name}: {result['hole_count']} enclosed hole(s), "
                f"{result['failed_hole_count']} undersized, "
                f"{result['pinch_count']} pinched junction(s), "
                f"{result['status'].upper()}"
            )
        except Exception as exc:
            result = _error_result(svg_path, f"{type(exc).__name__}: {exc}", args.icon_type, args.min_radius_design_u, args.min_fill_depth_design_u)
            print(f"FAIL {svg_path.name}: {exc}", file=sys.stderr)
            if len(stems[svg_path.stem.casefold()]) == 1:
                try:
                    _write_text(output_dir / f"{svg_path.stem}.metrics.json", json.dumps(result, indent=2) + "\n", protected)
                except (OSError, ValueError) as error:
                    result["processingErrors"].append(f"error report could not be written: {error}")
        results.append(result)
    report_failed = False
    try:
        write_aggregate(results, output_dir, args.min_radius_design_u, args.min_fill_depth_design_u)
        print(f"wrote {len(results)} input reports to {output_dir}")
    except Exception as error:
        report_failed = True
        print(f"FAIL writing aggregate reports: {error}", file=sys.stderr)
    failed = [item for item in results if item["status"] != "pass"]
    try:
        collect_failures(results, output_dir, error_dir, args.min_radius_design_u, args.min_fill_depth_design_u)
    except Exception as error:
        report_failed = True
        print(f"FAIL collecting failure evidence: {error}", file=sys.stderr)
    if failed:
        print(f"{len(failed)} input(s) failed; diagnostic evidence directory: {error_dir}")
        print(f"fix a failing zone by: {REMEDIATION}.", file=sys.stderr)
    return 1 if report_failed or failed or not results else 0


if __name__ == "__main__":
    raise SystemExit(main())
