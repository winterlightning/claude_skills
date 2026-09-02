#!/usr/bin/env python3
"""Validate finished SVG paint against the selected profile's keyshapes.

The keyshape is the painted padding boundary: circle-44, square-40,
portrait-36x44, or landscape-44x36. Stroke paint is included.

When editable metadata does not declare a target, circle inference requires a
large, nearly constant-radius outer silhouette. All other icons fall back by
whole painted orientation: near-equal to square, tall to portrait, wide to
landscape. Inference is diagnostic and does not replace visual declaration.
"""

from __future__ import annotations

import argparse
import csv
import html
import io
import json
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
from urllib.parse import quote

import cairosvg
import numpy as np
from PIL import Image, ImageDraw

PROJECT_ROOT = next(
    (parent for parent in Path(__file__).resolve().parents if (parent / "core" / "keyfit.py").is_file()),
    None,
)
if PROJECT_ROOT is None:
    raise RuntimeError("cannot locate project core/keyfit.py from the keyfit checker")
sys.path.insert(0, str(PROJECT_ROOT / "core"))
from icon_profiles import DEFAULT_ICON_TYPE,document_icon_type,get_profile,profile_names
from keyfit import DESIGN_CANVAS,CIRCLE_DIAMETER,SHIP_CANVAS,assign,canonical_tokens,max_box,token_box,token_named

DEFAULT_SAMPLES_PER_UNIT = 32
CIRCLE_ANGULAR_BINS = 180
CIRCLE_RADIAL_STEP = 0.25
CIRCLE_BAND_HALF_WIDTH = 1.25
CIRCLE_MIN_RADIUS = 14.0
CIRCLE_MIN_ANGULAR_COVERAGE = 0.72
CIRCLE_MIN_ENVELOPE_COVERAGE = 0.90
CIRCLE_MAX_ENVELOPE_SPREAD = 1.0
RECTANGULAR_ORIENTATION_RATIO = 1.10


def _number(value: str | None, fallback: float) -> float:
    if not value:
        return fallback
    token = "".join(ch for ch in value.strip() if ch in "0123456789+-.eE")
    try:
        return float(token)
    except ValueError:
        return fallback


def svg_canvas(svg_path: Path, fallback_canvas: float=SHIP_CANVAS) -> tuple[float, float, float, float]:
    root = ET.parse(svg_path).getroot()
    raw = root.get("viewBox")
    if raw:
        values = [float(item) for item in raw.replace(",", " ").split()]
        if len(values) == 4 and values[2] > 0 and values[3] > 0:
            return tuple(values)  # type: ignore[return-value]
    return (
        0.0,
        0.0,
        _number(root.get("width"), fallback_canvas),
        _number(root.get("height"), fallback_canvas),
    )


def render_mask(
    svg_path: Path, view_width: float, view_height: float, samples_per_unit: int
) -> tuple[np.ndarray, Image.Image]:
    width = max(1, int(round(view_width * samples_per_unit)))
    height = max(1, int(round(view_height * samples_per_unit)))
    png = cairosvg.svg2png(
        url=str(svg_path), output_width=width, output_height=height
    )
    rgba = Image.open(io.BytesIO(png)).convert("RGBA")
    alpha = np.asarray(rgba)[:, :, 3]
    return alpha >= 128, rgba


def painted_bounds(
    mask: np.ndarray, view_box: tuple[float, float, float, float],design_canvas: float=DESIGN_CANVAS
) -> tuple[float, float, float, float] | None:
    ys, xs = np.where(mask)
    if not len(xs):
        return None
    _, _, view_width, view_height = view_box
    raster_h, raster_w = mask.shape
    scale_x = design_canvas / raster_w
    scale_y = design_canvas / raster_h
    left = xs.min() * scale_x
    top = ys.min() * scale_y
    right = (xs.max() + 1) * scale_x
    bottom = (ys.max() + 1) * scale_y
    return left, top, right, bottom


def painted_circle_overflow(mask: np.ndarray,icon_type: str=DEFAULT_ICON_TYPE) -> float:
    """Maximum painted-sample overflow beyond the profile's circle."""
    ys, xs = np.where(mask)
    if not len(xs):
        return 0.0
    profile=get_profile(icon_type); design_canvas=float(profile["designCanvas"]); center=profile["center"]
    circle=next(item for item in canonical_tokens(icon_type) if item["shape"]=="circle")
    scale_x = design_canvas / mask.shape[1]
    scale_y = design_canvas / mask.shape[0]
    dx = (xs + 0.5) * scale_x - center["x"]
    dy = (ys + 0.5) * scale_y - center["y"]
    return float(np.hypot(dx, dy).max() - circle["diameter"] / 2.0)


def dominant_circle_evidence(
    mask: np.ndarray,
    bounds: tuple[float, float, float, float] | None,
    icon_type: str=DEFAULT_ICON_TYPE,
) -> dict:
    """Detect a large, continuous circular form in rendered paint.

    A near-square painted box is not circle evidence. The detector bins paint
    in polar coordinates and requires most angles to carry paint in one narrow,
    large-radius band. This admits a dominant outer ring/disc while rejecting
    houses, boxes, and other rectilinear or peaked silhouettes.
    """
    profile=get_profile(icon_type); design_canvas=float(profile["designCanvas"]); center=profile["center"]
    circle=next(item for item in canonical_tokens(icon_type) if item["shape"]=="circle")
    minimum_profile_radius=CIRCLE_MIN_RADIUS*design_canvas/DESIGN_CANVAS
    if bounds is None:
        return {
            "isDominantLargeCircle": False,
            "angularCoverage": 0.0,
            "radiusDesignU": None,
            "minimumAngularCoverage": CIRCLE_MIN_ANGULAR_COVERAGE,
            "minimumRadiusDesignU": minimum_profile_radius,
            "radialEnvelopeCoverage": 0.0,
            "radialEnvelopeSpreadDesignU": None,
            "maximumEnvelopeSpreadDesignU": CIRCLE_MAX_ENVELOPE_SPREAD,
        }
    ys, xs = np.where(mask)
    if not len(xs):
        return {
            "isDominantLargeCircle": False,
            "angularCoverage": 0.0,
            "radiusDesignU": None,
            "minimumAngularCoverage": CIRCLE_MIN_ANGULAR_COVERAGE,
            "minimumRadiusDesignU": minimum_profile_radius,
            "radialEnvelopeCoverage": 0.0,
            "radialEnvelopeSpreadDesignU": None,
            "maximumEnvelopeSpreadDesignU": CIRCLE_MAX_ENVELOPE_SPREAD,
        }

    scale_x = design_canvas / mask.shape[1]
    scale_y = design_canvas / mask.shape[0]
    dx = (xs + 0.5) * scale_x - center["x"]
    dy = (ys + 0.5) * scale_y - center["y"]
    radii = np.hypot(dx, dy)
    angles = np.mod(np.arctan2(dy, dx), 2.0 * np.pi)
    angle_bins = np.minimum(
        (angles * CIRCLE_ANGULAR_BINS / (2.0 * np.pi)).astype(int),
        CIRCLE_ANGULAR_BINS - 1,
    )
    radial_bins = np.maximum((radii / CIRCLE_RADIAL_STEP).astype(int), 0)
    radial_count = int(np.ceil((circle["diameter"] / 2.0 + CIRCLE_BAND_HALF_WIDTH) / CIRCLE_RADIAL_STEP)) + 2
    polar = np.zeros((radial_count, CIRCLE_ANGULAR_BINS), dtype=bool)
    valid = radial_bins < radial_count
    polar[radial_bins[valid], angle_bins[valid]] = True

    painted_width = bounds[2] - bounds[0]
    painted_height = bounds[3] - bounds[1]
    minimum_radius = max(minimum_profile_radius, 0.34 * min(painted_width, painted_height))
    start = int(np.floor(minimum_radius / CIRCLE_RADIAL_STEP))
    stop = int(np.ceil((circle["diameter"] / 2.0) / CIRCLE_RADIAL_STEP))
    half_window = max(1, int(np.ceil(CIRCLE_BAND_HALF_WIDTH / CIRCLE_RADIAL_STEP)))
    best_coverage = 0.0
    best_radius = None
    for radial_index in range(start, min(stop + 1, radial_count)):
        low = max(0, radial_index - half_window)
        high = min(radial_count, radial_index + half_window + 1)
        coverage = float(np.any(polar[low:high], axis=0).mean())
        if coverage > best_coverage:
            best_coverage = coverage
            best_radius = radial_index * CIRCLE_RADIAL_STEP

    radial_envelope = np.full(CIRCLE_ANGULAR_BINS, -np.inf)
    np.maximum.at(radial_envelope, angle_bins, radii)
    valid_envelope = radial_envelope[np.isfinite(radial_envelope)]
    envelope_coverage = len(valid_envelope) / CIRCLE_ANGULAR_BINS
    envelope_spread = (
        float(np.percentile(valid_envelope, 90) - np.percentile(valid_envelope, 10))
        if len(valid_envelope)
        else float("inf")
    )
    is_dominant = (
        best_coverage >= CIRCLE_MIN_ANGULAR_COVERAGE
        and envelope_coverage >= CIRCLE_MIN_ENVELOPE_COVERAGE
        and envelope_spread <= CIRCLE_MAX_ENVELOPE_SPREAD
    )

    return {
        "isDominantLargeCircle": is_dominant,
        "angularCoverage": round(best_coverage, 4),
        "radiusDesignU": round(best_radius, 4) if best_radius is not None else None,
        "minimumAngularCoverage": CIRCLE_MIN_ANGULAR_COVERAGE,
        "minimumRadiusDesignU": round(minimum_radius, 4),
        "radialEnvelopeCoverage": round(envelope_coverage, 4),
        "radialEnvelopeSpreadDesignU": round(envelope_spread, 4),
        "maximumEnvelopeSpreadDesignU": CIRCLE_MAX_ENVELOPE_SPREAD,
    }


def inferred_visual_target(
    bounds: tuple[float, float, float, float], allow_circle: bool,icon_type: str=DEFAULT_ICON_TYPE
) -> dict:
    """Choose circle only from raster evidence; otherwise use whole-box orientation."""
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    by_orientation={item["orientation"]:item for item in canonical_tokens(icon_type)}
    if allow_circle:
        token = by_orientation["circle"]
    elif width / max(height, 1e-9) >= RECTANGULAR_ORIENTATION_RATIO:
        token = by_orientation["landscape"]
    elif height / max(width, 1e-9) >= RECTANGULAR_ORIENTATION_RATIO:
        token = by_orientation["portrait"]
    else:
        token = by_orientation["square"]
    box = token_box(token["width"], token["height"],icon_type)
    return {
        **token,
        "bounds": list(box),
        "edgeDeltaToTarget": {
            "left": bounds[0] - box[0],
            "top": bounds[1] - box[1],
            "right": box[2] - bounds[2],
            "bottom": box[3] - bounds[3],
        },
    }


def classify_keyfit(
    bounds: tuple[float, float, float, float] | None,
    tolerance: float,
    expected_token_name: str | None = None,
    circle_radial_overflow: float = 0.0,
    circle_evidence: dict | None = None,
    icon_type: str=DEFAULT_ICON_TYPE,
) -> dict:
    if bounds is None:
        return {
            "status": "fail",
            "reason": "no-painted-geometry",
            "assignedToken": None,
            "paintedBoundsDesign": None,
        }

    profile=get_profile(icon_type); design_canvas=float(profile["designCanvas"])
    circle_evidence = circle_evidence or {"isDominantLargeCircle": False}
    expected=token_named(expected_token_name,icon_type) if expected_token_name else None
    if expected_token_name and expected is None:
        raise ValueError(f"unknown {icon_type} expected keyshape token: {expected_token_name}")
    allow_circle = (
        expected["shape"] == "circle"
        if expected_token_name is not None
        else bool(circle_evidence.get("isDominantLargeCircle"))
    )
    assigned = assign(bounds, tolerance, allow_circle=allow_circle,icon_type=icon_type)
    if expected_token_name:
        assert expected is not None
        box = token_box(expected["width"], expected["height"],icon_type)
        target = {
            **expected,
            "bounds": list(box),
            "edgeDeltaToTarget": {
                "left": bounds[0] - box[0],
                "top": bounds[1] - box[1],
                "right": box[2] - bounds[2],
                "bottom": box[3] - bounds[3],
            },
        }
    else:
        target = assigned or inferred_visual_target(bounds, allow_circle,icon_type)
    selected = expected if expected_token_name else assigned
    radial_overflow = circle_radial_overflow if selected and selected["shape"] == "circle" else 0.0
    matches_expected = bool(assigned) and radial_overflow <= tolerance and (
        expected_token_name is None or assigned["name"] == expected_token_name
    )
    maximum = max_box(icon_type)
    overflow = {
        "left": max(0.0, maximum[0] - bounds[0]),
        "top": max(0.0, maximum[1] - bounds[1]),
        "right": max(0.0, bounds[2] - maximum[2]),
        "bottom": max(0.0, bounds[3] - maximum[3]),
    }
    return {
        "status": "pass" if matches_expected else "fail",
        "reason": (
            None if matches_expected
            else "paint-crosses-circle-keyshape" if selected and selected["shape"] == "circle" and radial_overflow > tolerance
            else "paint-does-not-match-declared-keyshape-target" if expected_token_name
            else "paint-does-not-match-canonical-keyshape-target"
        ),
        "expectedTokenName": expected_token_name,
        "assignedToken": assigned,
        "targetToken": target,
        "paintedBoundsDesign": [round(value, 4) for value in bounds],
        "paintedSizeDesign": [
            round(bounds[2] - bounds[0], 4),
            round(bounds[3] - bounds[1], 4),
        ],
        "paintedPaddingDesign": {
            "left": round(bounds[0], 4),
            "top": round(bounds[1], 4),
            "right": round(design_canvas - bounds[2], 4),
            "bottom": round(design_canvas - bounds[3], 4),
        },
        "overflowBeyondAbsolute44Bounds": {
            key: round(value, 4) for key, value in overflow.items()
        },
        "overflowBeyondAbsoluteKeyfitBounds": {
            key: round(value, 4) for key, value in overflow.items()
        },
        "circleOverflowDesignU": round(max(0.0, radial_overflow), 4),
        "circleDetection": circle_evidence,
        "edgeDeltaToTarget": {
            key: round(value, 4)
            for key, value in target.get("edgeDeltaToTarget", {}).items()
        },
    }


def save_overlay(
    rgba: Image.Image,
    bounds: tuple[float, float, float, float] | None,
    result: dict,
    output_path: Path,
) -> None:
    canvas = Image.new("RGB", rgba.size, "white")
    ink = Image.new("RGB", rgba.size, (28, 30, 34))
    canvas.paste(ink, mask=rgba.getchannel("A"))
    draw = ImageDraw.Draw(canvas)
    design_canvas=float(result.get("designCanvas",DESIGN_CANVAS)); icon_type=result.get("iconType",DEFAULT_ICON_TYPE)
    scale_x = canvas.width / design_canvas
    scale_y = canvas.height / design_canvas

    selected = result.get("targetToken") or result.get("assignedToken")
    box = selected["bounds"] if selected else list(max_box(icon_type))
    color = (24, 151, 84) if result["status"] == "pass" else (210, 47, 47)
    outline = tuple(int(round(value * (scale_x if index % 2 == 0 else scale_y))) for index, value in enumerate(box))
    if selected and selected.get("shape") == "circle":
        draw.ellipse(outline, outline=color, width=max(2, canvas.width // 384))
    else:
        draw.rectangle(outline, outline=color, width=max(2, canvas.width // 384))
    if bounds:
        draw.rectangle(
            (
                int(round(bounds[0] * scale_x)),
                int(round(bounds[1] * scale_y)),
                int(round(bounds[2] * scale_x)),
                int(round(bounds[3] * scale_y)),
            ),
            outline=(24, 94, 210),
            width=max(2, canvas.width // 512),
        )
    canvas.save(output_path)


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
    tolerance: float,
    expected_token_name: str | None = None,
    icon_type: str=DEFAULT_ICON_TYPE,
) -> dict:
    profile=get_profile(icon_type); design_canvas=float(profile["designCanvas"])
    view_box = svg_canvas(svg_path,float(profile["shipCanvas"]))
    mask, rgba = render_mask(svg_path, view_box[2], view_box[3], samples_per_unit)
    bounds = painted_bounds(mask, view_box,design_canvas)
    circle_evidence = dominant_circle_evidence(mask, bounds,icon_type)
    check = classify_keyfit(
        bounds,
        tolerance,
        expected_token_name,
        painted_circle_overflow(mask,icon_type),
        circle_evidence,
        icon_type,
    )
    result = {
        "file": svg_path.name,
        "source": str(svg_path),
        "viewBox": list(view_box),
        "iconType": icon_type,
        "designCanvas": profile["designCanvas"],
        "shipCanvas": profile["shipCanvas"],
        "toleranceDesignUnits": tolerance,
        **check,
    }
    (output_dir / f"{svg_path.stem}.keyfit.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    save_overlay(
        rgba,
        bounds,
        result,
        output_dir / f"{svg_path.stem}_keyfit.png",
    )
    return result


def write_csv(results: list[dict], output_dir: Path) -> None:
    fields = [
        "file",
        "status",
        "reason",
        "assigned_token",
        "target_token",
        "painted_width_design_u",
        "painted_height_design_u",
        "padding_left_design_u",
        "padding_top_design_u",
        "padding_right_design_u",
        "padding_bottom_design_u",
        "overflow_left_design_u",
        "overflow_top_design_u",
        "overflow_right_design_u",
        "overflow_bottom_design_u",
        "target_delta_left_design_u",
        "target_delta_top_design_u",
        "target_delta_right_design_u",
        "target_delta_bottom_design_u",
    ]
    with (output_dir / "keyfit-results.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for result in results:
            size = result.get("paintedSizeDesign") or [None, None]
            padding = result.get("paintedPaddingDesign") or {}
            overflow = result.get("overflowBeyondAbsolute44Bounds") or {}
            delta = result.get("edgeDeltaToTarget") or {}
            writer.writerow(
                {
                    "file": result["file"],
                    "status": result["status"],
                    "reason": result.get("reason"),
                    "assigned_token": (result.get("assignedToken") or {}).get("name"),
                    "target_token": (result.get("targetToken") or {}).get("name"),
                    "painted_width_design_u": size[0],
                    "painted_height_design_u": size[1],
                    "padding_left_design_u": padding.get("left"),
                    "padding_top_design_u": padding.get("top"),
                    "padding_right_design_u": padding.get("right"),
                    "padding_bottom_design_u": padding.get("bottom"),
                    "overflow_left_design_u": overflow.get("left"),
                    "overflow_top_design_u": overflow.get("top"),
                    "overflow_right_design_u": overflow.get("right"),
                    "overflow_bottom_design_u": overflow.get("bottom"),
                    "target_delta_left_design_u": delta.get("left"),
                    "target_delta_top_design_u": delta.get("top"),
                    "target_delta_right_design_u": delta.get("right"),
                    "target_delta_bottom_design_u": delta.get("bottom"),
                }
            )


def write_html(results: list[dict], output_dir: Path) -> None:
    failed = [result for result in results if result["status"] == "fail"]
    passing = [result for result in results if result["status"] == "pass"]
    declared_count = sum(bool(result.get("expectedTokenName")) for result in results)
    inferred_count = len(results) - declared_count
    rows = []
    for result in failed:
        padding = result.get("paintedPaddingDesign") or {}
        size = result.get("paintedSizeDesign") or [None, None]
        delta = result.get("edgeDeltaToTarget") or {}
        target_token = result.get("targetToken") or {}
        target = target_token.get("name", "unknown")
        delta_text = ", ".join(
            f"{side} {amount:+g}u" for side, amount in delta.items() if abs(amount) > 1e-6
        ) or "no edge adjustment measured"
        if result.get("expectedTokenName"):
            basis = "declared"
        elif target_token.get("shape") == "circle":
            basis = "inferred: dominant large circle"
        else:
            basis = "inferred: rectangular fallback"
        reason = (result.get("reason") or "unknown").replace("-", " ")
        stem = Path(result["file"]).stem
        icon_type=result.get("iconType",DEFAULT_ICON_TYPE); canvas=result.get("designCanvas",DESIGN_CANVAS)
        target_bounds = target_token.get("bounds") or list(max_box(icon_type))
        if target_token.get("shape") == "circle":
            left,top,right,bottom=target_bounds
            keyshape_markup = (
                f'<circle class="keyshape-boundary" cx="{(left+right)/2:g}" cy="{(top+bottom)/2:g}" r="{(right-left)/2:g}"/>'
            )
        else:
            left, top, right, bottom = target_bounds
            keyshape_markup = (
                f'<rect class="keyshape-boundary" x="{left:g}" y="{top:g}" '
                f'width="{right - left:g}" height="{bottom - top:g}"/>'
            )
        painted = result.get("paintedBoundsDesign")
        painted_markup = ""
        if painted:
            left, top, right, bottom = painted
            painted_markup = (
                f'<rect class="painted-boundary" x="{left:g}" y="{top:g}" '
                f'width="{right - left:g}" height="{bottom - top:g}"/>'
            )
        source_href = quote(f"../../final/{result['file']}")
        preview = (
            f'<div class="preview" style="--grid-major:{canvas/4:g};--grid-canvas:{canvas:g}">'
            f'<img src="{source_href}" alt="Rendered {html.escape(result["file"])}">'
            f'<svg class="inspection-overlay" viewBox="0 0 {canvas:g} {canvas:g}" aria-hidden="true">'
            f'{keyshape_markup}{painted_markup}</svg>'
            '</div>'
        )
        rows.append(
            "<tr>"
            f"<td>{preview}</td>"
            f"<td><code>{html.escape(result['file'])}</code></td>"
            f"<td>{size[0]:g}×{size[1]:g}u</td>"
            f"<td>{html.escape(target)}<br><small>{html.escape(basis)}</small></td>"
            f"<td>{html.escape(reason)}</td>"
            f"<td>{html.escape(delta_text)}</td>"
            f"<td>L {padding.get('left', 0):g} · T {padding.get('top', 0):g} · "
            f"R {padding.get('right', 0):g} · B {padding.get('bottom', 0):g}</td>"
            f"<td><a href=\"{quote(stem + '_keyfit.png')}\">overlay</a> · "
            f"<a href=\"{quote(stem + '.keyfit.json')}\">metrics</a></td>"
            "</tr>"
        )
    body = "\n".join(rows) if rows else (
        '<tr><td colspan="8" class="empty">No files failed.</td></tr>'
    )
    passing_text = ", ".join(result["file"] for result in passing) or "None"
    document = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Unlimited Shapes keyshape QA</title>
<style>
body{{margin:0;background:#f4f5f7;color:#17191e;font-family:Inter,system-ui,sans-serif}}
main{{max-width:1680px;margin:auto;padding:40px 24px}}h1{{margin:0 0 8px}}
.lede{{color:#5b616c;margin:0 0 24px}}.cards{{display:flex;gap:12px;margin-bottom:24px}}
.card{{background:#fff;border:1px solid #dde1e7;border-radius:12px;padding:18px;min-width:170px}}
.value{{display:block;font-size:28px;font-weight:750}}.label{{font-size:13px;color:#69707c}}
.bad{{color:#b42318}}.legend{{display:flex;gap:18px;flex-wrap:wrap;margin:0 0 20px;font-size:13px;color:#59606a}}
.swatch{{display:inline-block;width:24px;height:0;margin-right:7px;vertical-align:middle;border-top:3px solid}}
.swatch.keyshape{{border-color:#dc2626}}.swatch.paint{{border-color:#2563eb;border-top-style:dashed}}
table{{width:100%;border-collapse:collapse;background:#fff}}
th,td{{padding:12px 14px;text-align:left;border-bottom:1px solid #e6e9ed;vertical-align:top}}
th{{position:sticky;top:0;z-index:10;font-size:12px;text-transform:uppercase;color:#59606a;background:#f9fafb}}a{{color:#155eef}}
.empty{{color:#247a3d;text-align:center;padding:32px}}code{{font-size:13px}}
.preview{{position:relative;width:220px;aspect-ratio:1;background-color:#fff;
background-image:linear-gradient(to right,rgba(30,64,175,.28) 1px,transparent 1px),linear-gradient(to bottom,rgba(30,64,175,.28) 1px,transparent 1px),linear-gradient(to right,rgba(71,85,105,.09) 1px,transparent 1px),linear-gradient(to bottom,rgba(71,85,105,.09) 1px,transparent 1px);
background-size:calc(100% / var(--grid-major)) 100%,100% calc(100% / var(--grid-major)),calc(100% / var(--grid-canvas)) 100%,100% calc(100% / var(--grid-canvas));
border:1px solid #cbd5e1;border-radius:8px;overflow:hidden}}
.preview img,.inspection-overlay{{position:absolute;inset:0;width:100%;height:100%;display:block}}
.preview img{{z-index:1}}.inspection-overlay{{z-index:2;pointer-events:none;fill:none}}
.keyshape-boundary{{stroke:#dc2626;stroke-width:.55}}
.painted-boundary{{stroke:#2563eb;stroke-width:.45;stroke-dasharray:1.2 1}}
small{{color:#6b7280}}@media(max-width:900px){{.preview{{width:180px}}th,td{{padding:10px}}}}
</style></head><body><main><h1>Centered keyshape QA</h1>
<p class="lede">Paint must exactly reach and remain inside one centered keyshape from the selected icon profile. Stroke paint is included.</p>
<p class="lede"><strong>Evidence basis:</strong> {declared_count} declared target(s), {inferred_count} target(s)
inferred from rendered paint. Circle inference requires a dominant large-radius form with at least
{CIRCLE_MIN_ANGULAR_COVERAGE:.0%} angular coverage and no more than {CIRCLE_MAX_ENVELOPE_SPREAD:g}u
of robust outer-radius variation; other silhouettes use a rectangular fallback. Visual confirmation remains required;
geometric failure still means the paint fits none of the canonical boundaries.</p>
<p class="lede"><strong>Passing files:</strong> {html.escape(passing_text)}</p>
<div class="cards"><div class="card"><span class="value">{len(results)}</span><span class="label">SVGs checked</span></div>
<div class="card"><span class="value bad">{len(failed)}</span><span class="label">failed files</span></div>
<div class="card"><span class="value">{inferred_count}</span><span class="label">inferred targets</span></div></div>
<div class="legend"><span><i class="swatch keyshape"></i>selected keyshape</span><span><i class="swatch paint"></i>measured painted bounds</span><span>Grid: 1u minor / 4u major</span></div>
<table><thead><tr><th>SVG + grid</th><th>File</th><th>Painted size</th><th>Target / basis</th><th>Failure</th><th>Required edge adjustment</th><th>Canvas padding</th><th>Evidence</th></tr></thead>
<tbody>{body}</tbody></table></main></body></html>"""
    (output_dir / "keyfit-report.html").write_text(document, encoding="utf-8")


def write_aggregate(results: list[dict], output_dir: Path) -> None:
    (output_dir / "keyfit-results.json").write_text(
        json.dumps(results, indent=2) + "\n", encoding="utf-8"
    )
    write_csv(results, output_dir)
    write_html(results, output_dir)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("inputs", nargs="+", help="SVG files or flat SVG folders")
    parser.add_argument("--output-dir", required=True, help="QA output folder")
    parser.add_argument(
        "--icon-type",
        choices=profile_names(),
        default=None,
        help="icon profile when editable metadata is unavailable (default: normal)",
    )
    parser.add_argument(
        "--expected-editable-dir",
        type=Path,
        help="editable JSON folder whose keyfitCheck.targetToken is authoritative",
    )
    parser.add_argument(
        "--samples-per-unit",
        type=int,
        default=DEFAULT_SAMPLES_PER_UNIT,
        help="raster samples per SVG viewBox unit (default: 32)",
    )
    parser.add_argument(
        "--tolerance-design-u",
        type=float,
        default=None,
        help="edge tolerance in design units (default: one raster sample)",
    )
    args = parser.parse_args()
    if args.samples_per_unit < 4:
        parser.error("--samples-per-unit must be at least 4")
    tolerance = (
        args.tolerance_design_u
        if args.tolerance_design_u is not None
        else 2.0 / args.samples_per_unit
    )
    if tolerance < 0:
        parser.error("--tolerance-design-u cannot be negative")

    svgs = collect_svgs(args.inputs)
    if not svgs:
        parser.error("no SVG files found")
    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    expected_tokens: dict[str, str] = {}
    icon_types: dict[str,str] = {}
    if args.expected_editable_dir:
        for svg_path in svgs:
            editable = args.expected_editable_dir / f"{svg_path.stem}.json"
            if not editable.is_file():
                parser.error(f"missing expected editable source: {editable}")
            document = json.loads(editable.read_text(encoding="utf-8"))
            editable_icon_type=document_icon_type(document)
            if args.icon_type and args.icon_type!=editable_icon_type:
                parser.error(f"--icon-type {args.icon_type!r} conflicts with iconType {editable_icon_type!r} in {editable}")
            icon_types[svg_path.stem]=editable_icon_type
            token = (document.get("keyfitCheck") or {}).get("targetToken")
            if not token:
                parser.error(f"missing keyfitCheck.targetToken in {editable}")
            expected_tokens[svg_path.stem] = token

    results = []
    processing_errors = 0
    for svg_path in svgs:
        try:
            result = process(
                svg_path,
                output_dir,
                args.samples_per_unit,
                tolerance,
                expected_tokens.get(svg_path.stem),
                icon_types.get(svg_path.stem,args.icon_type or DEFAULT_ICON_TYPE),
            )
            results.append(result)
            token = (result.get("assignedToken") or {}).get("name", "none")
            print(f"{svg_path.name}: {result['status'].upper()} ({token})")
        except Exception as exc:
            processing_errors += 1
            print(f"warn: {svg_path.name}: {exc}", file=sys.stderr)
    write_aggregate(results, output_dir)
    print(f"wrote {len(results)} keyshape reports to {output_dir}")
    return 1 if processing_errors or any(result["status"] == "fail" for result in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
