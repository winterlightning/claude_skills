"""Rendered hole/pinch measurement, vendored from claude_skills/core/qa_overlays.py.

See PROVENANCE.md for the source hash and adaptation boundary. Measurement
functions are retained; profile selection and artifact writing belong to library_qa.
Dependencies are imported lazily by the build's QA adapter.
"""
from __future__ import annotations
import io
import math
from pathlib import Path
import re
import xml.etree.ElementTree as ET

import cairosvg
import cv2
import numpy as np
from PIL import Image

# Legacy function defaults only. The adapter always passes the resolved canvas.
DESIGN_CANVAS = SHIP_CANVAS = 48.0
SVG_DEFAULT_STROKE_WIDTH = 1.0

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
    """Find enclosed background using edge and diagonal pixel neighbours.

    Diagonal edges at sharp tips can leave background samples that touch their
    region only at a corner. Four-connectivity incorrectly counts these as new
    holes. Eight-connectivity preserves that region without dropping genuinely
    isolated small holes by an area threshold.
    """
    background = (~ink).astype(np.uint8)
    count, labels, stats, _ = cv2.connectedComponentsWithStats(
        background, connectivity=8
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
        pockets.astype(np.uint8), connectivity=8
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

