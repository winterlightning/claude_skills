#!/usr/bin/env python3
"""Detect SVG primitives and propose Unlimited Shapes atoms before icon making."""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
import tempfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

NUMBER_PATTERN = r"[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?"
NUMBER_RE = re.compile(NUMBER_PATTERN)
PATH_TOKEN_RE = re.compile(rf"[AaCcHhLlMmQqSsTtVvZz]|{NUMBER_PATTERN}")
COMMAND_PARAMS = {"M": 2, "L": 2, "H": 1, "V": 1, "C": 6, "S": 4, "Q": 4, "T": 2, "A": 7, "Z": 0}
SHAPE_TAGS = {"circle", "ellipse", "rect", "line", "polyline", "polygon", "path"}
EPSILON = 1e-6
# Widest sweep still read as a corner ``quarter-arc`` rather than an ``arc``
# half-ellipse; 135° is the midpoint between the 90° and 180° families.
QUARTER_ARC_MAX_SWEEP = 135.0


@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def as_dict(self) -> dict[str, float]:
        return {"x": self.x, "y": self.y}


@dataclass(frozen=True)
class Bounds:
    x: float
    y: float
    width: float
    height: float

    def rounded(self) -> dict[str, float]:
        return {"x": clean(self.x), "y": clean(self.y), "width": clean(self.width), "height": clean(self.height)}


def clean(value: float, digits: int = 3) -> float | int:
    rounded = round(float(value), digits)
    return int(rounded) if rounded == int(rounded) else rounded


def near(a: float, b: float, tolerance: float) -> bool:
    return abs(a - b) <= tolerance


def vector(a: Point, b: Point) -> Point:
    return Point(b.x - a.x, b.y - a.y)


def dot(a: Point, b: Point) -> float:
    return a.x * b.x + a.y * b.y


def cross(a: Point, b: Point) -> float:
    return a.x * b.y - a.y * b.x


def magnitude(value: Point) -> float:
    return math.hypot(value.x, value.y)


def distance(a: Point, b: Point) -> float:
    return math.hypot(a.x - b.x, a.y - b.y)


def numeric(value: str | None, default: float | None = None) -> float | None:
    if value is None:
        return default
    match = NUMBER_RE.search(str(value))
    return float(match.group(0)) if match else default


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].split(":")[-1].lower()


def parse_view_box(root: ET.Element) -> Bounds:
    values = [float(value) for value in re.findall(NUMBER_PATTERN, root.attrib.get("viewBox", ""))]
    if len(values) == 4 and values[2] > 0 and values[3] > 0:
        return Bounds(*values)
    width = numeric(root.attrib.get("width"), 24) or 24
    height = numeric(root.attrib.get("height"), 24) or 24
    return Bounds(0, 0, width if width > 0 else 24, height if height > 0 else 24)


def parse_points(source: str = "") -> list[Point]:
    values = [float(value) for value in NUMBER_RE.findall(source)]
    return [Point(values[index], values[index + 1]) for index in range(0, len(values) - 1, 2)]


def parse_path(data: str) -> list[dict[str, Any]]:
    tokens = PATH_TOKEN_RE.findall(data or "")
    segments: list[dict[str, Any]] = []
    index = 0
    command: str | None = None
    current = Point(0, 0)
    start = Point(0, 0)
    previous_control: Point | None = None

    def make_point(x: float, y: float, relative: bool) -> Point:
        return Point(current.x + x, current.y + y) if relative else Point(x, y)

    while index < len(tokens):
        if tokens[index].isalpha():
            command = tokens[index]
            index += 1
        if command is None:
            raise ValueError("Path data must begin with a command")
        upper = command.upper()
        relative = command != upper
        count = COMMAND_PARAMS.get(upper)
        if count is None:
            raise ValueError(f"Unsupported path command {command}")
        if upper == "Z":
            segments.append({"type": "Z", "from": current, "to": start})
            current, previous_control, command = start, None, None
            continue
        if index + count > len(tokens) or tokens[index].isalpha():
            raise ValueError(f"Path command {command} has incomplete parameters")
        values = [float(value) for value in tokens[index : index + count]]
        origin = current

        if upper in {"M", "L", "T"}:
            target = make_point(values[0], values[1], relative)
            segment: dict[str, Any] = {"type": upper, "from": origin, "to": target}
            if upper == "T":
                control = Point(2 * origin.x - previous_control.x, 2 * origin.y - previous_control.y) if previous_control else origin
                segment["control"] = control
                previous_control = control
            else:
                previous_control = None
            current = target
            if upper == "M":
                start = target
                command = "l" if relative else "L"
        elif upper == "H":
            target = Point(current.x + values[0] if relative else values[0], current.y)
            segment = {"type": "L", "from": origin, "to": target, "sourceType": "H"}
            current, previous_control = target, None
        elif upper == "V":
            target = Point(current.x, current.y + values[0] if relative else values[0])
            segment = {"type": "L", "from": origin, "to": target, "sourceType": "V"}
            current, previous_control = target, None
        elif upper == "C":
            control1 = make_point(values[0], values[1], relative)
            control2 = make_point(values[2], values[3], relative)
            target = make_point(values[4], values[5], relative)
            segment = {"type": "C", "from": origin, "control1": control1, "control2": control2, "to": target}
            current, previous_control = target, control2
        elif upper == "S":
            control1 = Point(2 * origin.x - previous_control.x, 2 * origin.y - previous_control.y) if previous_control else origin
            control2 = make_point(values[0], values[1], relative)
            target = make_point(values[2], values[3], relative)
            segment = {"type": "C", "from": origin, "control1": control1, "control2": control2, "to": target, "sourceType": "S"}
            current, previous_control = target, control2
        elif upper == "Q":
            control = make_point(values[0], values[1], relative)
            target = make_point(values[2], values[3], relative)
            segment = {"type": "Q", "from": origin, "control": control, "to": target}
            current, previous_control = target, control
        else:  # A
            target = make_point(values[5], values[6], relative)
            segment = {
                "type": "A", "from": origin, "rx": abs(values[0]), "ry": abs(values[1]),
                "rotation": values[2], "largeArc": bool(values[3]), "sweep": bool(values[4]), "to": target,
            }
            current, previous_control = target, None
        segments.append(segment)
        index += count
    return segments


def bounds_from_points(points: Iterable[Point]) -> Bounds | None:
    values = list(points)
    if not values:
        return None
    xs, ys = [point.x for point in values], [point.y for point in values]
    return Bounds(min(xs), min(ys), max(xs) - min(xs), max(ys) - min(ys))


def sample_arc(segment: dict[str, Any], steps: int = 64) -> list[Point]:
    start, end = segment["from"], segment["to"]
    rx, ry = abs(segment["rx"]), abs(segment["ry"])
    if rx <= EPSILON or ry <= EPSILON or distance(start, end) <= EPSILON:
        return [start, end]
    phi = math.radians(segment["rotation"])
    cos_phi, sin_phi = math.cos(phi), math.sin(phi)
    dx, dy = (start.x - end.x) / 2, (start.y - end.y) / 2
    x1p, y1p = cos_phi * dx + sin_phi * dy, -sin_phi * dx + cos_phi * dy
    scale = x1p * x1p / (rx * rx) + y1p * y1p / (ry * ry)
    if scale > 1:
        factor = math.sqrt(scale)
        rx, ry = rx * factor, ry * factor
    numerator = max(0.0, rx * rx * ry * ry - rx * rx * y1p * y1p - ry * ry * x1p * x1p)
    denominator = rx * rx * y1p * y1p + ry * ry * x1p * x1p
    sign = -1 if segment["largeArc"] == segment["sweep"] else 1
    coefficient = 0 if denominator <= EPSILON else sign * math.sqrt(numerator / denominator)
    cxp, cyp = coefficient * rx * y1p / ry, coefficient * -ry * x1p / rx
    cx = cos_phi * cxp - sin_phi * cyp + (start.x + end.x) / 2
    cy = sin_phi * cxp + cos_phi * cyp + (start.y + end.y) / 2
    u = Point((x1p - cxp) / rx, (y1p - cyp) / ry)
    v = Point((-x1p - cxp) / rx, (-y1p - cyp) / ry)
    start_angle = math.atan2(u.y, u.x)
    delta = math.atan2(cross(u, v), dot(u, v))
    if not segment["sweep"] and delta > 0:
        delta -= math.tau
    if segment["sweep"] and delta < 0:
        delta += math.tau
    count = max(4, math.ceil(abs(delta) / math.tau * steps))
    return [
        Point(
            cx + cos_phi * rx * math.cos(start_angle + delta * index / count) - sin_phi * ry * math.sin(start_angle + delta * index / count),
            cy + sin_phi * rx * math.cos(start_angle + delta * index / count) + cos_phi * ry * math.sin(start_angle + delta * index / count),
        )
        for index in range(count + 1)
    ]


Affine = tuple[float, float, float, float, float, float]
IDENTITY: Affine = (1, 0, 0, 1, 0, 0)


def multiply_affine(left: Affine, right: Affine) -> Affine:
    """Return the SVG affine transform left ∘ right."""
    a1, b1, c1, d1, e1, f1 = left
    a2, b2, c2, d2, e2, f2 = right
    return (
        a1 * a2 + c1 * b2,
        b1 * a2 + d1 * b2,
        a1 * c2 + c1 * d2,
        b1 * c2 + d1 * d2,
        a1 * e2 + c1 * f2 + e1,
        b1 * e2 + d1 * f2 + f1,
    )


def apply_affine(matrix: Affine, point: Point) -> Point:
    a, b, c, d, e, f = matrix
    return Point(a * point.x + c * point.y + e, b * point.x + d * point.y + f)


def parse_transform(source: str | None) -> Affine:
    matrix = IDENTITY
    for match in re.finditer(r"([A-Za-z]+)\s*\(([^)]*)\)", source or ""):
        name = match.group(1).lower()
        values = [float(value) for value in NUMBER_RE.findall(match.group(2))]
        operation = IDENTITY
        if name == "matrix" and len(values) == 6:
            operation = tuple(values)  # type: ignore[assignment]
        elif name == "translate" and values:
            operation = (1, 0, 0, 1, values[0], values[1] if len(values) > 1 else 0)
        elif name == "scale" and values:
            operation = (values[0], 0, 0, values[1] if len(values) > 1 else values[0], 0, 0)
        elif name == "rotate" and values:
            radians = math.radians(values[0])
            rotation = (math.cos(radians), math.sin(radians), -math.sin(radians), math.cos(radians), 0, 0)
            if len(values) >= 3:
                cx, cy = values[1], values[2]
                operation = multiply_affine((1, 0, 0, 1, cx, cy), multiply_affine(rotation, (1, 0, 0, 1, -cx, -cy)))
            else:
                operation = rotation
        elif name == "skewx" and values:
            operation = (1, 0, math.tan(math.radians(values[0])), 1, 0, 0)
        elif name == "skewy" and values:
            operation = (1, math.tan(math.radians(values[0])), 0, 1, 0, 0)
        matrix = multiply_affine(matrix, operation)
    return matrix


def sample_quadratic(segment: dict[str, Any], steps: int = 24) -> list[Point]:
    start, control, end = segment["from"], segment["control"], segment["to"]
    return [
        Point(
            (1 - t) ** 2 * start.x + 2 * (1 - t) * t * control.x + t * t * end.x,
            (1 - t) ** 2 * start.y + 2 * (1 - t) * t * control.y + t * t * end.y,
        )
        for t in (index / steps for index in range(steps + 1))
    ]


def sample_cubic(segment: dict[str, Any], steps: int = 32) -> list[Point]:
    start, control1, control2, end = segment["from"], segment["control1"], segment["control2"], segment["to"]
    return [
        Point(
            (1 - t) ** 3 * start.x + 3 * (1 - t) ** 2 * t * control1.x + 3 * (1 - t) * t * t * control2.x + t ** 3 * end.x,
            (1 - t) ** 3 * start.y + 3 * (1 - t) ** 2 * t * control1.y + 3 * (1 - t) * t * t * control2.y + t ** 3 * end.y,
        )
        for t in (index / steps for index in range(steps + 1))
    ]


def path_polylines(segments: list[dict[str, Any]]) -> list[list[Point]]:
    polylines: list[list[Point]] = []
    current: list[Point] = []
    for segment in segments:
        kind = segment["type"]
        if kind == "M":
            if current:
                polylines.append(current)
            current = [segment["to"]]
            continue
        sampled = (
            sample_arc(segment) if kind == "A" else
            sample_quadratic(segment) if kind == "Q" else
            sample_cubic(segment) if kind == "C" else
            [segment["from"], segment["to"]]
        )
        if not current:
            current.append(sampled[0])
        current.extend(sampled[1:])
        if kind == "Z":
            polylines.append(current)
            current = []
    if current:
        polylines.append(current)
    return polylines


def rounded_rect_points(x: float, y: float, width: float, height: float, rx: float, ry: float, steps: int = 10) -> list[Point]:
    rx, ry = min(abs(rx), width / 2), min(abs(ry), height / 2)
    if rx <= EPSILON or ry <= EPSILON:
        return [Point(x, y), Point(x + width, y), Point(x + width, y + height), Point(x, y + height), Point(x, y)]
    points: list[Point] = []
    for cx, cy, start in [
        (x + width - rx, y + ry, -90), (x + width - rx, y + height - ry, 0),
        (x + rx, y + height - ry, 90), (x + rx, y + ry, 180),
    ]:
        points.extend(Point(cx + rx * math.cos(math.radians(start + 90 * index / steps)), cy + ry * math.sin(math.radians(start + 90 * index / steps))) for index in range(steps + 1))
    points.append(points[0])
    return points


def element_polylines(tag: str, attrs: dict[str, str]) -> list[list[Point]]:
    if tag == "path":
        return path_polylines(parse_path(attrs.get("d", "")))
    if tag == "line":
        return [[Point(numeric(attrs.get("x1"), 0) or 0, numeric(attrs.get("y1"), 0) or 0), Point(numeric(attrs.get("x2"), 0) or 0, numeric(attrs.get("y2"), 0) or 0)]]
    if tag in {"polyline", "polygon"}:
        points = parse_points(attrs.get("points", ""))
        if tag == "polygon" and points:
            points.append(points[0])
        return [points]
    if tag == "circle":
        cx, cy, radius = numeric(attrs.get("cx"), 0) or 0, numeric(attrs.get("cy"), 0) or 0, abs(numeric(attrs.get("r"), 0) or 0)
        return [[Point(cx + radius * math.cos(math.tau * index / 96), cy + radius * math.sin(math.tau * index / 96)) for index in range(97)]]
    if tag == "ellipse":
        cx, cy = numeric(attrs.get("cx"), 0) or 0, numeric(attrs.get("cy"), 0) or 0
        rx, ry = abs(numeric(attrs.get("rx"), 0) or 0), abs(numeric(attrs.get("ry"), 0) or 0)
        return [[Point(cx + rx * math.cos(math.tau * index / 96), cy + ry * math.sin(math.tau * index / 96)) for index in range(97)]]
    x, y = numeric(attrs.get("x"), 0) or 0, numeric(attrs.get("y"), 0) or 0
    width, height = abs(numeric(attrs.get("width"), 0) or 0), abs(numeric(attrs.get("height"), 0) or 0)
    rx = abs(numeric(attrs.get("rx"), numeric(attrs.get("ry"), 0)) or 0)
    ry = abs(numeric(attrs.get("ry"), rx) or rx)
    return [rounded_rect_points(x, y, width, height, rx, ry)]


def plot_items(svg_text: str, view_box: Bounds) -> list[list[list[Point]]]:
    root = ET.fromstring(svg_text)
    items: list[list[list[Point]]] = []

    def visit(node: ET.Element, parent_matrix: Affine = IDENTITY) -> None:
        tag, attrs = local_name(node.tag), dict(node.attrib)
        matrix = multiply_affine(parent_matrix, parse_transform(attrs.get("transform")))
        if tag in SHAPE_TAGS:
            try:
                source_lines = element_polylines(tag, attrs)
            except ValueError:
                source_lines = []
            normalized_lines = [
                [
                    Point(
                        (transformed.x - view_box.x) * 48 / view_box.width,
                        (transformed.y - view_box.y) * 48 / view_box.height,
                    )
                    for point in polyline
                    for transformed in [apply_affine(matrix, point)]
                ]
                for polyline in source_lines
            ]
            items.append(normalized_lines)
        for child in node:
            visit(child, matrix)

    visit(root)
    return items


def render_detection_plot(svg_text: str, report: dict[str, Any], output_path: Path | None = None, show: bool = False) -> None:
    """Render detected geometry, bounds, labels, and QA state with Matplotlib."""
    cache = Path(tempfile.gettempdir()) / "unlimited-shapes-matplotlib"
    cache.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("MPLCONFIGDIR", str(cache))
    os.environ.setdefault("XDG_CACHE_HOME", str(cache))
    try:
        import matplotlib
        if not show:
            matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from matplotlib.lines import Line2D
        from matplotlib.patches import Circle, Rectangle
    except ImportError as error:
        raise ValueError("Matplotlib is required for --show/--plot. Install it with: python3 -m pip install matplotlib") from error

    source_view = report["source"]["viewBox"]
    view_box = Bounds(source_view["x"], source_view["y"], source_view["width"], source_view["height"])
    geometry = plot_items(svg_text, view_box)
    manual_review = set(report["makerPreflight"]["manualReview"])
    palette = {
        "line": "#2563eb", "curve": "#7c3aed", "circle": "#059669", "ellipse": "#0d9488",
        "rect": "#0891b2", "polygon": "#db2777", "review": "#d97706", "error": "#dc2626",
    }

    figure, axis = plt.subplots(figsize=(10, 10), constrained_layout=True)
    figure.patch.set_facecolor("#f8fafc")
    axis.set_facecolor("white")
    for value in range(0, 49):
        major = value % 4 == 0
        axis.axvline(value, color="#cbd5e1" if major else "#e2e8f0", linewidth=0.55 if major else 0.25, zorder=0)
        axis.axhline(value, color="#cbd5e1" if major else "#e2e8f0", linewidth=0.55 if major else 0.25, zorder=0)
    axis.add_patch(Rectangle((0, 0), 48, 48, fill=False, edgecolor="#16a34a", linewidth=1.4, linestyle=(0, (5, 3)), zorder=1))
    # Canonical painted padding boundaries. They are evidence guides only;
    # the icon maker selects one semantic keyshape for the finished icon.
    axis.add_patch(Circle((24, 24), 22, fill=False, edgecolor="#16a34a", linewidth=0.7, linestyle=(0, (4, 3)), alpha=0.55, zorder=1))
    axis.add_patch(Rectangle((4, 4), 40, 40, fill=False, edgecolor="#0d9488", linewidth=0.7, linestyle=(0, (3, 3)), alpha=0.45, zorder=1))
    axis.add_patch(Rectangle((6, 2), 36, 44, fill=False, edgecolor="#7c3aed", linewidth=0.7, linestyle=(0, (2, 3)), alpha=0.4, zorder=1))
    axis.add_patch(Rectangle((2, 6), 44, 36, fill=False, edgecolor="#db2777", linewidth=0.7, linestyle=(0, (2, 3)), alpha=0.4, zorder=1))

    for element, polylines in zip(report["elements"], geometry):
        index = element["index"]
        kind = element["classification"]["kind"]
        has_error = any(issue["severity"] == "error" for issue in element["specIssues"])
        if has_error:
            color = palette["error"]
        elif index in manual_review or element["specIssues"]:
            color = palette["review"]
        elif kind in {"straight-line", "point-dot", "polyline"}:
            color = palette["line"]
        elif "curve" in kind or "arc" in kind:
            color = palette["curve"]
        elif kind in {"circle", "ellipse"}:
            color = palette[kind]
        elif kind in {"square", "rectangle", "rounded-square", "rounded-rectangle", "gapped-rounded-rectangle", "pill"}:
            color = palette["rect"]
        else:
            color = palette["polygon"]
        for polyline in polylines:
            if not polyline:
                continue
            xs, ys = [point.x for point in polyline], [point.y for point in polyline]
            if len(polyline) == 1 or (max(xs) - min(xs) < 0.02 and max(ys) - min(ys) < 0.02):
                axis.scatter(xs[0], ys[0], s=30, color=color, zorder=4)
            else:
                axis.plot(xs, ys, color=color, linewidth=2.4, solid_capstyle="round", solid_joinstyle="round", zorder=3)
        all_points = [point for polyline in polylines for point in polyline]
        display_bounds = bounds_from_points(all_points)
        if display_bounds:
            axis.add_patch(Rectangle((display_bounds.x, display_bounds.y), display_bounds.width, display_bounds.height, fill=False, edgecolor=color, linewidth=0.9, linestyle=(0, (3, 2)), alpha=0.75, zorder=2))
            atom = element["classification"].get("atomicShape")
            marker = " !" if has_error else (" ?" if index in manual_review else "")
            primary = "line" if kind == "straight-line" else kind
            label = f"{index}: {primary}" + (f" → {atom}" if atom and atom != primary else "") + marker
            vertical = display_bounds.height > max(display_bounds.width * 2.5, 4)
            anchor = (display_bounds.x + display_bounds.width / 2, display_bounds.y + display_bounds.height / 2) if vertical else (display_bounds.x, display_bounds.y)
            axis.annotate(label, anchor, xytext=(4, 0) if vertical else (3, -4), textcoords="offset points", fontsize=7.5, color=color, weight="bold", va="bottom" if vertical else "top", ha="center" if vertical else "left", rotation=90 if vertical else 0, zorder=5, bbox={"boxstyle": "round,pad=0.2", "facecolor": "white", "edgecolor": color, "alpha": 0.88, "linewidth": 0.5})

    summary = report["summary"]
    status = "READY" if summary["readyForIconMaker"] else "REVIEW REQUIRED"
    status_color = "#15803d" if summary["readyForIconMaker"] else "#b45309"
    axis.text(0.01, 0.01, f"{status}\n{summary['elementCount']} elements · {summary['atomicCandidateCount']} atom candidates · {summary['warningCount']} warnings · {summary['errorCount']} errors", transform=axis.transAxes, fontsize=9, color=status_color, va="bottom", ha="left", bbox={"boxstyle": "round,pad=0.45", "facecolor": "white", "edgecolor": status_color, "alpha": 0.94})
    axis.legend(handles=[
        Line2D([0], [0], color=palette["line"], lw=2.4, label="line / dot"),
        Line2D([0], [0], color=palette["curve"], lw=2.4, label="curve / arc"),
        Line2D([0], [0], color=palette["circle"], lw=2.4, label="circle / ellipse"),
        Line2D([0], [0], color=palette["rect"], lw=2.4, label="rect / pill"),
        Line2D([0], [0], color=palette["review"], lw=2.4, label="warning / review"),
        Line2D([0], [0], color=palette["error"], lw=2.4, label="spec error"),
    ], loc="upper left", bbox_to_anchor=(1.01, 1), frameon=False, fontsize=8)
    axis.set_title(f"Unlimited Shapes preflight — {report['source']['name'] or 'SVG input'}", fontsize=13, weight="bold", loc="left")
    axis.set_xlim(0, 48)
    axis.set_ylim(48, 0)
    axis.set_aspect("equal", adjustable="box")
    axis.set_xticks(range(0, 49, 4))
    axis.set_yticks(range(0, 49, 4))
    axis.tick_params(labelsize=7, colors="#64748b")
    axis.set_xlabel("48-unit design grid", fontsize=9, color="#475569")
    axis.set_ylabel("Centered keyshapes: circle Ø44, square 40, portrait 36×44, landscape 44×36", fontsize=9, color="#475569")
    for spine in axis.spines.values():
        spine.set_color("#94a3b8")
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        figure.savefig(output_path, dpi=180, bbox_inches="tight", facecolor=figure.get_facecolor())
    if show:
        plt.show()
    plt.close(figure)


def path_bounds(segments: list[dict[str, Any]]) -> Bounds | None:
    points: list[Point] = []
    for segment in segments:
        if segment["type"] == "M":
            points.append(segment["to"])
        elif segment["type"] == "A":
            points.extend(sample_arc(segment))
        else:
            points.extend(value for key, value in segment.items() if key in {"from", "to", "control", "control1", "control2"})
    return bounds_from_points(points)


def unique_vertices(segments: list[dict[str, Any]], tolerance: float) -> list[Point]:
    vertices: list[Point] = []
    for segment in segments:
        target = segment.get("to")
        if segment["type"] != "M" and target and all(distance(target, value) > tolerance for value in vertices):
            vertices.append(target)
    return vertices


def is_collinear(segments: list[dict[str, Any]], tolerance: float) -> bool:
    lines = [segment for segment in segments if segment["type"] == "L"]
    if not lines:
        return False
    origin, direction = lines[0]["from"], vector(lines[0]["from"], lines[0]["to"])
    scale = max(magnitude(direction), 1)
    return all(abs(cross(direction, vector(origin, segment["to"]))) / scale <= tolerance for segment in lines)


def arc_sweep_degrees(segment: dict[str, Any]) -> float | None:
    """Absolute swept angle of one ``A`` segment, in degrees.

    The sweep separates the open-arc families: the ``arc`` atom is a 180°
    half-ellipse, while ``quarter-arc`` is a 90° corner contour. Returns
    ``None`` for a degenerate arc that carries no usable sweep.
    """
    start, end = segment["from"], segment["to"]
    rx, ry = abs(segment["rx"]), abs(segment["ry"])
    if rx <= EPSILON or ry <= EPSILON or distance(start, end) <= EPSILON:
        return None
    phi = math.radians(segment["rotation"])
    cos_phi, sin_phi = math.cos(phi), math.sin(phi)
    dx, dy = (start.x - end.x) / 2, (start.y - end.y) / 2
    x1p, y1p = cos_phi * dx + sin_phi * dy, -sin_phi * dx + cos_phi * dy
    scale = x1p * x1p / (rx * rx) + y1p * y1p / (ry * ry)
    if scale > 1:
        factor = math.sqrt(scale)
        rx, ry = rx * factor, ry * factor
    numerator = max(0.0, rx * rx * ry * ry - rx * rx * y1p * y1p - ry * ry * x1p * x1p)
    denominator = rx * rx * y1p * y1p + ry * ry * x1p * x1p
    sign = -1 if segment["largeArc"] == segment["sweep"] else 1
    coefficient = 0 if denominator <= EPSILON else sign * math.sqrt(numerator / denominator)
    cxp, cyp = coefficient * rx * y1p / ry, coefficient * -ry * x1p / rx
    u = Point((x1p - cxp) / rx, (y1p - cyp) / ry)
    v = Point((-x1p - cxp) / rx, (-y1p - cyp) / ry)
    delta = math.atan2(cross(u, v), dot(u, v))
    if not segment["sweep"] and delta > 0:
        delta -= math.tau
    if segment["sweep"] and delta < 0:
        delta += math.tau
    return abs(math.degrees(delta))


def open_arc_atom(arcs: list[dict[str, Any]]) -> str:
    """Pick the open-arc atom that matches the swept angle of a single arc.

    A sweep at or below 135° is closer to the 90° ``quarter-arc`` corner than
    to the 180° ``arc`` half-ellipse; anything wider stays ``arc``.
    """
    if len(arcs) != 1:
        return "arc"
    sweep = arc_sweep_degrees(arcs[0])
    return "quarter-arc" if sweep is not None and sweep <= QUARTER_ARC_MAX_SWEEP else "arc"


def is_s_bend(arcs: list[dict[str, Any]], tolerance: float) -> bool:
    """Recognize two equal, opposite-sweep quarter ellipses joined at midpoint."""
    if len(arcs) != 2:
        return False
    first, second = arcs
    if first["sweep"] == second["sweep"] or first["largeArc"] or second["largeArc"]:
        return False
    if not all((
        near(first["rx"], second["rx"], tolerance),
        near(first["ry"], second["ry"], tolerance),
        near(first["rotation"], second["rotation"], tolerance),
        distance(first["to"], second["from"]) <= tolerance,
    )):
        return False
    first_step = vector(first["from"], first["to"])
    second_step = vector(second["from"], second["to"])
    if not (near(first_step.x, second_step.x, tolerance) and near(first_step.y, second_step.y, tolerance)):
        return False
    sweeps = (arc_sweep_degrees(first), arc_sweep_degrees(second))
    return all(sweep is not None and abs(sweep - 90) <= 0.2 for sweep in sweeps)


def is_gapped_rounded_rectangle(visible: list[dict[str, Any]], tolerance: float) -> bool:
    """True for a ``gapped-rounded-rectangle``: a rounded box broken in its head.

    Nine alternating segments — head run, corner, side, corner, side, corner,
    side, corner, head run — where the four corner arcs are equal and circular
    and the two head runs are collinear, codirectional, and equal in length. The
    equal runs are what separate a deliberately gapped frame from an arbitrary
    line/arc compound, and they put the opening at the centre of the head.
    """
    if [segment["type"] for segment in visible] != ["L", "A", "L", "A", "L", "A", "L", "A", "L"]:
        return False
    arcs, lines = visible[1::2], visible[0::2]
    radius = min(arcs[0]["rx"], arcs[0]["ry"])
    if radius <= tolerance:
        return False
    for arc in arcs:
        if not near(arc["rx"], arc["ry"], tolerance) or not near(min(arc["rx"], arc["ry"]), radius, tolerance):
            return False
    head, tail = vector(lines[0]["from"], lines[0]["to"]), vector(lines[-1]["from"], lines[-1]["to"])
    scale = max(magnitude(head), magnitude(tail), 1)
    if abs(cross(head, tail)) > tolerance * scale or dot(head, tail) <= 0:
        return False
    if not near(magnitude(head), magnitude(tail), tolerance):
        return False
    sides = [vector(segment["from"], segment["to"]) for segment in lines[1:4]]
    if min(magnitude(side) for side in sides) <= tolerance:
        return False
    for before, after in zip(sides, sides[1:]):
        if abs(dot(before, after)) / magnitude(before) > tolerance:
            return False
    return dot(sides[0], sides[2]) < 0


def is_arch(visible: list[dict[str, Any]], tolerance: float) -> bool:
    """True for an open ``arch``: one arc head carried on two straight jambs (L, A, L).

    The jambs must be perpendicular to the head's chord and run in opposite
    directions, which is what separates an arch from an arbitrary
    line/arc/line compound path.
    """
    if [segment["type"] for segment in visible] != ["L", "A", "L"]:
        return False
    rise, head, fall = visible
    chord = vector(head["from"], head["to"])
    up, down = vector(rise["from"], rise["to"]), vector(fall["from"], fall["to"])
    span = magnitude(chord)
    if min(span, magnitude(up), magnitude(down)) <= tolerance:
        return False
    if any(abs(dot(chord, jamb)) / span > tolerance for jamb in (up, down)):
        return False
    return dot(up, down) < 0


def is_hook(visible: list[dict[str, Any]], tolerance: float) -> bool:
    """True for a J-hook: unequal opposing stems joined by a half-circle bowl."""
    if [segment["type"] for segment in visible] != ["L", "A", "L"]:
        return False
    stem, bowl, tip = visible
    chord = vector(bowl["from"], bowl["to"])
    long_side, short_side = vector(stem["from"], stem["to"]), vector(tip["from"], tip["to"])
    span = magnitude(chord)
    lengths = sorted((magnitude(long_side), magnitude(short_side)))
    sweep = arc_sweep_degrees(bowl)
    if min(span, *lengths) <= tolerance or sweep is None or abs(sweep - 180) > 0.2:
        return False
    if any(abs(dot(chord, side)) / span > tolerance for side in (long_side, short_side)):
        return False
    if dot(long_side, short_side) >= 0 or lengths[1] < lengths[0] * 1.5:
        return False
    return near(bowl["rx"], bowl["ry"], tolerance) and near(span, 2 * bowl["rx"], tolerance)


def is_water_drop(visible: list[dict[str, Any]], tolerance: float) -> bool:
    """True for a four-quadratic symmetric teardrop with one top cusp."""
    if [segment["type"] for segment in visible] != ["Q", "Q", "Q", "Q"]:
        return False
    first, second, third, fourth = visible
    apex, bottom = first["from"], second["to"]
    if distance(apex, fourth["to"]) > tolerance or not near(apex.x, bottom.x, tolerance):
        return False
    if not near(first["to"].y, third["to"].y, tolerance):
        return False
    if not near(first["to"].x + third["to"].x, 2 * apex.x, tolerance):
        return False
    return apex.y + tolerance < min(first["to"].y, third["to"].y) < bottom.y - tolerance


def is_tapered_spire(visible: list[dict[str, Any]], tolerance: float) -> bool:
    """True for two mirrored quadratic sides joined by one flat base."""
    if [segment["type"] for segment in visible] != ["Q", "L", "Q"]:
        return False
    left, base, right = visible
    apex = left["from"]
    if distance(right["to"], apex) > tolerance:
        return False
    if not near(base["from"].y, base["to"].y, tolerance):
        return False
    if not near(apex.x * 2, base["from"].x + base["to"].x, tolerance):
        return False
    if not near(left["control"].x + right["control"].x, apex.x * 2, tolerance):
        return False
    return apex.y + tolerance < base["from"].y


def is_faucet(visible: list[dict[str, Any]], tolerance: float) -> bool:
    """True for inlet/elbow/outlet geometry accompanied by a perpendicular T handle."""
    if [segment["type"] for segment in visible] != ["L", "A", "L", "L", "L"]:
        return False
    inlet, elbow, outlet, stem, handle = visible
    if distance(inlet["to"], elbow["from"]) > tolerance or distance(elbow["to"], outlet["from"]) > tolerance:
        return False
    inlet_v, outlet_v = vector(inlet["from"], inlet["to"]), vector(outlet["from"], outlet["to"])
    stem_v, handle_v = vector(stem["from"], stem["to"]), vector(handle["from"], handle["to"])
    if abs(dot(inlet_v, outlet_v)) > tolerance * max(magnitude(inlet_v), magnitude(outlet_v), 1):
        return False
    if abs(dot(stem_v, handle_v)) > tolerance * max(magnitude(stem_v), magnitude(handle_v), 1):
        return False
    return arc_sweep_degrees(elbow) is not None and abs((arc_sweep_degrees(elbow) or 0) - 90) <= 0.2


def is_open_end_wrench(visible: list[dict[str, Any]], tolerance: float) -> bool:
    """True for a two-arc ring, straight shaft, and paired open 45-degree jaw arms."""
    if [segment["type"] for segment in visible] != ["A", "A", "L", "L", "L"]:
        return False
    first, second, shaft, upper, lower = visible
    if distance(first["to"], second["from"]) > tolerance or distance(second["to"], first["from"]) > tolerance:
        return False
    if not all(near(value, first["rx"], tolerance) for value in (first["ry"], second["rx"], second["ry"])):
        return False
    neck = shaft["to"]
    if distance(upper["from"], neck) > tolerance or distance(lower["from"], neck) > tolerance:
        return False
    jaws = (vector(neck, upper["to"]), vector(neck, lower["to"]))
    if dot(jaws[0], jaws[1]) > tolerance or not near(magnitude(jaws[0]), magnitude(jaws[1]), tolerance):
        return False
    shaft_v = vector(shaft["from"], shaft["to"])
    return all(abs(abs(dot(shaft_v, jaw)) / (magnitude(shaft_v) * magnitude(jaw)) - 2**-.5) <= 0.02 for jaw in jaws)


def is_dashed_rectangle(visible: list[dict[str, Any]], tolerance: float) -> bool:
    """True for disconnected axis-aligned segments distributed over four box edges."""
    if len(visible) < 8 or any(segment["type"] != "L" for segment in visible):
        return False
    points = [point for segment in visible for point in (segment["from"], segment["to"])]
    min_x, max_x = min(point.x for point in points), max(point.x for point in points)
    min_y, max_y = min(point.y for point in points), max(point.y for point in points)
    if max_x - min_x <= tolerance or max_y - min_y <= tolerance:
        return False
    sides: set[str] = set()
    for segment in visible:
        start, end = segment["from"], segment["to"]
        if near(start.y, min_y, tolerance) and near(end.y, min_y, tolerance): sides.add("top")
        elif near(start.x, max_x, tolerance) and near(end.x, max_x, tolerance): sides.add("right")
        elif near(start.y, max_y, tolerance) and near(end.y, max_y, tolerance): sides.add("bottom")
        elif near(start.x, min_x, tolerance) and near(end.x, min_x, tolerance): sides.add("left")
        else: return False
    breaks = sum(distance(first["to"], second["from"]) > tolerance for first, second in zip(visible, visible[1:]))
    return sides == {"top", "right", "bottom", "left"} and breaks >= 3


def is_open_rectangle(visible: list[dict[str, Any]], tolerance: float) -> bool:
    """True for an ``open-rectangle``: three sides of a rectangle, one missing.

    Three straight segments — jamb, head, jamb — where the two jambs are equal
    in length, perpendicular to the head, and run in opposite directions. That
    is what separates the atom from an L-bend, a Z-bend, or a staircase, and it
    is the flat-headed analogue of :func:`is_arch`.
    """
    if any(segment["type"] != "L" for segment in visible):
        return False
    # Sources routinely break one side at a midpoint vertex, so collapse runs of
    # collinear same-direction segments before counting the sides.
    sides: list[Point] = []
    for segment in visible:
        side = vector(segment["from"], segment["to"])
        if sides:
            previous = sides[-1]
            scale = max(magnitude(previous), magnitude(side), 1)
            if abs(cross(previous, side)) <= tolerance * scale and dot(previous, side) > 0:
                sides[-1] = Point(previous.x + side.x, previous.y + side.y)
                continue
        sides.append(side)
    if len(sides) != 3:
        return False
    left, head, right = sides
    span = magnitude(head)
    if min(span, magnitude(left), magnitude(right)) <= tolerance:
        return False
    if any(abs(dot(head, jamb)) / span > tolerance for jamb in (left, right)):
        return False
    if not near(magnitude(left), magnitude(right), tolerance):
        return False
    return dot(left, right) < 0


def is_open_gable(visible: list[dict[str, Any]], tolerance: float) -> bool:
    """True for an ``open-gable``: a peaked head on two walls, the base absent.

    Four straight sides — wall, roof, roof, wall — where the two walls are
    equal in length, parallel to each other and perpendicular to the head's
    chord, the two roof edges are equal in length, and the apex lies on the
    perpendicular bisector of the line joining the wall heads. That symmetry is
    what separates the atom from an arbitrary four-bend polyline, and it is the
    pointed-head analogue of :func:`is_open_rectangle` and the open analogue of
    :func:`is_gable`.
    """
    if any(segment["type"] != "L" for segment in visible):
        return False
    # Sources routinely break one side at a midpoint vertex, so collapse runs of
    # collinear same-direction segments before counting the sides.
    sides: list[Point] = []
    for segment in visible:
        side = vector(segment["from"], segment["to"])
        if sides:
            previous = sides[-1]
            scale = max(magnitude(previous), magnitude(side), 1)
            if abs(cross(previous, side)) <= tolerance * scale and dot(previous, side) > 0:
                sides[-1] = Point(previous.x + side.x, previous.y + side.y)
                continue
        sides.append(side)
    if len(sides) != 4:
        return False
    left, up, down, right = sides
    if min(magnitude(side) for side in sides) <= tolerance:
        return False
    if not near(magnitude(left), magnitude(right), tolerance):
        return False
    if not near(magnitude(up), magnitude(down), tolerance):
        return False
    if dot(left, right) >= 0:
        return False
    # The chord between the two wall heads, which the walls must be square to
    # and which the apex must sit over the middle of.
    chord = Point(up.x + down.x, up.y + down.y)
    span = magnitude(chord)
    if span <= tolerance:
        return False
    if any(abs(dot(chord, wall)) / span > tolerance for wall in (left, right)):
        return False
    return abs(dot(chord, Point(up.x - down.x, up.y - down.y))) / span <= tolerance


def is_gable(vertices: list[Point], tolerance: float) -> bool:
    """True for a ``gable`` pentagon: a rectangular body under a peaked head.

    Walks the five sides looking for the base / wall / roof / roof / wall
    arrangement: the two walls equal in length, parallel to each other and
    perpendicular to the base, the two roof sides equal in length, and the
    apex on the base's perpendicular bisector. That symmetry is what separates
    a gable from any other pentagon.
    """
    count = len(vertices)
    sides = [vector(point, vertices[(index + 1) % count]) for index, point in enumerate(vertices)]
    for start in range(count):
        base, left_wall, left_roof, right_roof, right_wall = (sides[(start + step) % count] for step in range(count))
        apex = vertices[(start + 3) % count]
        base_start, base_end = vertices[start], vertices[(start + 1) % count]
        span = magnitude(base)
        limit = tolerance * max(span, 1)
        if min(span, magnitude(left_wall), magnitude(right_wall), magnitude(left_roof), magnitude(right_roof)) <= tolerance:
            continue
        # Both walls stand square to the base and run in opposite directions.
        if any(abs(dot(base, wall)) > limit for wall in (left_wall, right_wall)):
            continue
        if dot(left_wall, right_wall) >= 0:
            continue
        if not near(magnitude(left_wall), magnitude(right_wall), tolerance):
            continue
        if not near(magnitude(left_roof), magnitude(right_roof), tolerance):
            continue
        # The apex sits over the middle of the base, so the head is symmetric.
        midpoint = Point((base_start.x + base_end.x) / 2, (base_start.y + base_end.y) / 2)
        if abs(dot(base, vector(midpoint, apex))) > limit:
            continue
        return True
    return False


def is_cloud(visible: list[dict[str, Any]], tolerance: float) -> bool:
    """Recognize the registry's closed, symmetric six-quadratic cloud family."""
    if [segment["type"] for segment in visible] != ["Q", "Q", "Q", "Q", "Q", "L", "Q"]:
        return False
    points = [visible[0]["from"], *(segment["to"] for segment in visible)]
    bounds = bounds_from_points(points)
    if not bounds or min(bounds.width, bounds.height) <= tolerance:
        return False
    midpoint = bounds.x + bounds.width / 2
    pairs = [(points[0], points[4]), (points[1], points[3]), (points[5], points[6])]
    if not near(points[2].x, midpoint, tolerance) or not near(points[2].y, bounds.y, tolerance):
        return False
    if not near(points[5].y, bounds.y + bounds.height, tolerance) or not near(points[6].y, bounds.y + bounds.height, tolerance):
        return False
    return all(
        near(left.x + right.x, 2 * midpoint, tolerance) and near(left.y, right.y, tolerance)
        for left, right in pairs
    )


def is_cut_corner_box(vertices: list[Point], tolerance: float) -> bool:
    """True for a ``cut-corner-box`` pentagon: a rectangle with one corner cut.

    Walks the five sides looking for the chamfer / roof / wall / floor / wall
    arrangement: the four surviving box sides mutually square, the opposite
    pairs running in opposite directions, and the fifth side meeting both of
    its neighbours at 45 degrees. The 45 degree cut is what separates the atom
    from a general pentagon and from :func:`is_gable`, whose head is a
    symmetric peak rather than a single corner run.
    """
    count = len(vertices)
    sides = [vector(point, vertices[(index + 1) % count]) for index, point in enumerate(vertices)]
    if min(magnitude(side) for side in sides) <= tolerance:
        return False
    for start in range(count):
        chamfer, roof, right_wall, floor, left_wall = (sides[(start + step) % count] for step in range(count))
        box = (roof, right_wall, floor, left_wall)
        limit = tolerance * max(magnitude(side) for side in box)
        # The four surviving sides are the sides of a box: each square to the
        # next, and each opposite pair running back the other way.
        if any(abs(dot(side, box[(index + 1) % 4])) > limit for index, side in enumerate(box)):
            continue
        if dot(roof, floor) >= 0 or dot(right_wall, left_wall) >= 0:
            continue
        # The cut meets both of its neighbours at 45 degrees, which is exactly
        # the statement that it spends the same length on each box axis. Both
        # sides of that comparison are lengths, so the tolerance means the same
        # thing here as everywhere else in this module.
        along_roof = abs(dot(chamfer, roof)) / magnitude(roof)
        along_wall = abs(dot(chamfer, left_wall)) / magnitude(left_wall)
        if not near(along_roof, along_wall, tolerance):
            continue
        return True
    return False


def is_sloped_box(vertices: list[Point], tolerance: float) -> bool:
    """Recognize a quadrilateral with parallel walls, a square base, and a 15-degree roof."""
    if len(vertices) != 4:
        return False
    sides = [vector(point, vertices[(index + 1) % 4]) for index, point in enumerate(vertices)]
    for start in range(4):
        roof, wall_a, base, wall_b = (sides[(start + step) % 4] for step in range(4))
        if min(*(magnitude(side) for side in (roof, wall_a, base, wall_b))) <= tolerance:
            continue
        if abs(cross(wall_a, wall_b)) > tolerance * max(magnitude(wall_a), magnitude(wall_b), 1):
            continue
        if dot(wall_a, wall_b) >= 0 or abs(dot(base, wall_a)) > tolerance * max(magnitude(base), 1):
            continue
        cosine = abs(dot(roof, base)) / (magnitude(roof) * magnitude(base))
        angle = math.degrees(math.acos(min(1, max(-1, cosine))))
        if abs(angle - 15) <= 0.1 and dot(roof, base) < 0:
            return True
    return False


def is_twin_gable(vertices: list[Point], tolerance: float) -> bool:
    """Recognize the registry's symmetric seven-vertex twin-gable shell."""
    if len(vertices) != 7:
        return False
    bounds = bounds_from_points(vertices)
    if not bounds or bounds.width <= tolerance or bounds.height <= tolerance:
        return False
    rise = min(bounds.width / 4, bounds.height)
    expected = [
        Point(bounds.x, bounds.y + bounds.height),
        Point(bounds.x, bounds.y + rise),
        Point(bounds.x + bounds.width / 4, bounds.y),
        Point(bounds.x + bounds.width / 2, bounds.y + rise),
        Point(bounds.x + 3 * bounds.width / 4, bounds.y),
        Point(bounds.x + bounds.width, bounds.y + rise),
        Point(bounds.x + bounds.width, bounds.y + bounds.height),
    ]
    for candidate in (expected, list(reversed(expected))):
        for offset in range(7):
            if all(
                near(vertices[index].x, candidate[(index + offset) % 7].x, tolerance)
                and near(vertices[index].y, candidate[(index + offset) % 7].y, tolerance)
                for index in range(7)
            ):
                return True
    return False


def polygon_kind(vertices: list[Point], tolerance: float) -> dict[str, Any]:
    count = len(vertices)
    if count == 3:
        sides = [vector(point, vertices[(index + 1) % count]) for index, point in enumerate(vertices)]
        right = any(abs(dot(side, sides[(index + 1) % count])) <= tolerance * max(magnitude(side), 1) for index, side in enumerate(sides))
        kind = "right-triangle" if right else "triangle"
        return {"kind": kind, "atomicShape": kind, "confidence": 0.95}
    if count == 5 and is_gable(vertices, tolerance):
        return {"kind": "gable", "atomicShape": "gable", "confidence": 0.9}
    if count == 5 and is_cut_corner_box(vertices, tolerance):
        return {"kind": "cut-corner-box", "atomicShape": "cut-corner-box", "confidence": 0.9}
    if count == 7 and is_twin_gable(vertices, tolerance):
        return {"kind": "twin-gable", "atomicShape": "twin-gable", "confidence": 0.94}
    if count == 4 and is_sloped_box(vertices, tolerance):
        return {"kind": "sloped-box", "atomicShape": "sloped-box", "confidence": 0.92}
    if count != 4:
        return {"kind": "polygon", "atomicShape": None, "confidence": 0.7}
    sides = [vector(point, vertices[(index + 1) % count]) for index, point in enumerate(vertices)]
    lengths = [magnitude(side) for side in sides]
    parallel = abs(cross(sides[0], sides[2])) <= tolerance * max(lengths[0], lengths[2], 1) and abs(cross(sides[1], sides[3])) <= tolerance * max(lengths[1], lengths[3], 1)
    right_angles = all(abs(dot(side, sides[(index + 1) % count])) <= tolerance * max(magnitude(side), 1) for index, side in enumerate(sides))
    equal_sides = max(lengths) - min(lengths) <= tolerance
    if parallel and right_angles:
        bounds = bounds_from_points(vertices)
        diagonal = all(abs(side.x) > tolerance and abs(side.y) > tolerance for side in sides)
        if equal_sides and diagonal and bounds and near(bounds.width, bounds.height, tolerance):
            return {"kind": "diamond", "atomicShape": "diamond", "confidence": 0.95}
        kind = "square" if equal_sides else "rectangle"
        return {"kind": kind, "atomicShape": kind, "confidence": 0.94}
    if parallel and equal_sides:
        return {"kind": "diamond", "atomicShape": "diamond", "confidence": 0.9}
    return {"kind": "quadrilateral", "atomicShape": None, "confidence": 0.7}


def is_bulb_outline(visible: list[dict[str, Any]], tolerance: float) -> bool:
    """Recognize the registry's open six-quadratic symmetric bulb contour."""
    if len(visible) != 6 or any(segment["type"] != "Q" for segment in visible):
        return False
    points = [point for segment in visible for point in (segment["from"], segment["control"], segment["to"])]
    bounds = bounds_from_points(points)
    if not bounds or bounds.width <= tolerance or bounds.height <= tolerance:
        return False
    left, top = bounds.x, bounds.y
    right, bottom = left + bounds.width, top + bounds.height
    start, end = visible[0]["from"], visible[-1]["to"]
    apex = visible[2]["to"]
    checks = (
        near(start.x, left + bounds.width / 3, tolerance),
        near(end.x, left + 2 * bounds.width / 3, tolerance),
        near(start.y, bottom, tolerance),
        near(end.y, bottom, tolerance),
        near(visible[1]["to"].x, left, tolerance),
        near(visible[3]["to"].x, right, tolerance),
        near(apex.x, left + bounds.width / 2, tolerance),
        near(apex.y, top, tolerance),
    )
    return all(checks)


def classify_path(segments: list[dict[str, Any]], view_box: Bounds) -> dict[str, Any]:
    drawing = [segment for segment in segments if segment["type"] != "M"]
    types = {segment["type"] for segment in drawing}
    closed = "Z" in types
    visible = [segment for segment in drawing if segment["type"] != "Z"]
    tolerance = max(view_box.width, view_box.height) * 0.0025
    if not visible:
        return {"kind": "empty-path", "atomicShape": None, "confidence": 1}
    if "C" in types:
        return {"kind": "cubic-curve", "atomicShape": None, "confidence": 1, "unsupported": True}
    if types <= {"L", "Z"}:
        total = sum(distance(segment["from"], segment["to"]) for segment in visible)
        if not closed and total <= tolerance:
            return {"kind": "point-dot", "atomicShape": "line", "confidence": 1}
        if not closed and is_dashed_rectangle(visible, tolerance):
            return {"kind": "dashed-rectangle", "atomicShape": "dashed-rectangle", "confidence": 0.94}
        if not closed and is_collinear(visible, tolerance):
            return {"kind": "straight-line", "atomicShape": "line", "confidence": 0.99}
        if not closed and is_open_rectangle(visible, tolerance):
            return {"kind": "open-rectangle", "atomicShape": "open-rectangle", "confidence": 0.9}
        if not closed and is_open_gable(visible, tolerance):
            return {"kind": "open-gable", "atomicShape": "open-gable", "confidence": 0.9}
        if closed:
            return polygon_kind(unique_vertices(drawing, tolerance), tolerance)
        return {"kind": "polyline", "atomicShape": None, "confidence": 0.9}
    if types <= {"A", "Z"}:
        arcs = [segment for segment in visible if segment["type"] == "A"]
        if closed and len(arcs) == 2 and near(arcs[0]["rx"], arcs[1]["rx"], tolerance) and near(arcs[0]["ry"], arcs[1]["ry"], tolerance):
            circular = near(arcs[0]["rx"], arcs[0]["ry"], tolerance)
            # Two equal circular arcs close on themselves either as a circle or
            # as a lens. The chord between the two junctions separates them: on
            # a circle the junctions are diametrically opposite, so the chord is
            # exactly 2r; on a lens the arcs meet at cusps and the chord is
            # shorter than the diameter.
            chord = distance(arcs[0]["from"], arcs[0]["to"])
            if circular and chord + tolerance < 2 * arcs[0]["rx"]:
                return {"kind": "lens", "atomicShape": "lens", "confidence": 0.9}
            kind = "circle" if circular else "ellipse"
            return {"kind": kind, "atomicShape": kind, "confidence": 0.92}
        if closed:
            return {"kind": "closed-arc-shape", "atomicShape": None, "confidence": 0.9}
        if is_s_bend(arcs, tolerance):
            return {"kind": "s-bend", "atomicShape": "s-bend", "confidence": 0.95}
        atom = open_arc_atom(arcs)
        return {"kind": atom, "atomicShape": atom, "confidence": 0.9}
    if types <= {"Q", "Z"}:
        if not closed and is_bulb_outline(visible, tolerance):
            return {"kind": "bulb-outline", "atomicShape": "bulb-outline", "confidence": 0.94}
        if closed and is_water_drop(visible, tolerance):
            return {"kind": "water-drop", "atomicShape": "water-drop", "confidence": 0.94}
        return {"kind": "closed-quadratic-shape" if closed else "quadratic-curve", "atomicShape": None if closed else "curve", "confidence": 0.95}
    if closed and types <= {"Q", "L", "Z"}:
        if is_tapered_spire(visible, tolerance):
            return {"kind": "tapered-spire", "atomicShape": "tapered-spire", "confidence": 0.94}
        if is_cloud(visible, tolerance):
            return {"kind": "cloud", "atomicShape": "cloud", "confidence": 0.94}
    if "A" in types and types <= {"L", "A", "Z"}:
        arcs = [segment for segment in visible if segment["type"] == "A"]
        lines = [segment for segment in visible if segment["type"] == "L"]
        if not closed and is_faucet(visible, tolerance):
            return {"kind": "faucet", "atomicShape": "faucet", "confidence": 0.93}
        if not closed and is_open_end_wrench(visible, tolerance):
            return {"kind": "open-end-wrench", "atomicShape": "open-end-wrench", "confidence": 0.93}
        if not closed and is_hook(visible, tolerance):
            return {"kind": "hook", "atomicShape": "hook", "confidence": 0.94}
        if not closed and is_arch(visible, tolerance):
            return {"kind": "arch", "atomicShape": "arch", "confidence": 0.9}
        if not closed and is_gapped_rounded_rectangle(visible, tolerance):
            radius = min(min(segment["rx"], segment["ry"]) for segment in arcs)
            return {"kind": "gapped-rounded-rectangle", "atomicShape": "gapped-rounded-rectangle", "confidence": 0.9, "inferredRadius": radius}
        if closed and len(arcs) >= 2 and len(lines) >= 2:
            bounds = path_bounds(segments)
            radius = min(min(segment["rx"], segment["ry"]) for segment in arcs)
            pill = bool(bounds and radius >= min(bounds.width, bounds.height) * 0.42)
            if pill:
                return {"kind": "pill", "atomicShape": "pill", "confidence": 0.84, "inferredRadius": radius}
            bounds = path_bounds(segments)
            atom = "rounded-square" if bounds and near(bounds.width, bounds.height, tolerance) else "rounded-rectangle"
            return {"kind": "rounded-rectangle", "atomicShape": atom, "confidence": 0.84, "inferredRadius": radius}
        return {"kind": "compound-line-arc", "atomicShape": None, "confidence": 0.75}
    return {"kind": "compound-path", "atomicShape": None, "confidence": 0.65}


def angle_info(start: Point, end: Point) -> dict[str, float | int]:
    angle = math.degrees(math.atan2(end.y - start.y, end.x - start.x)) % 180
    snapped = round(angle / 15) * 15
    canonical = 0 if snapped == 180 else snapped
    deviation = min(abs(angle - snapped), abs(angle - canonical))
    return {"degrees": clean(angle), "nearest15": canonical, "deviation": clean(deviation)}


def primitive_geometry(tag: str, attrs: dict[str, str]) -> dict[str, Any]:
    if tag == "circle":
        cx, cy, radius = numeric(attrs.get("cx"), 0) or 0, numeric(attrs.get("cy"), 0) or 0, abs(numeric(attrs.get("r"), 0) or 0)
        return {"classification": {"kind": "circle", "atomicShape": "circle", "confidence": 1}, "bounds": Bounds(cx - radius, cy - radius, 2 * radius, 2 * radius), "radius": radius}
    if tag == "ellipse":
        cx, cy = numeric(attrs.get("cx"), 0) or 0, numeric(attrs.get("cy"), 0) or 0
        rx, ry = abs(numeric(attrs.get("rx"), 0) or 0), abs(numeric(attrs.get("ry"), 0) or 0)
        circular = near(rx, ry, max(rx, ry, 1) * 0.01)
        kind = "circle" if circular else "ellipse"
        return {"classification": {"kind": kind, "atomicShape": kind, "confidence": 1}, "bounds": Bounds(cx - rx, cy - ry, 2 * rx, 2 * ry), "radius": rx if circular else None}
    if tag == "rect":
        x, y = numeric(attrs.get("x"), 0) or 0, numeric(attrs.get("y"), 0) or 0
        width, height = abs(numeric(attrs.get("width"), 0) or 0), abs(numeric(attrs.get("height"), 0) or 0)
        radius = abs(numeric(attrs.get("rx"), numeric(attrs.get("ry"), 0)) or 0)
        kind = "square" if near(width, height, max(width, height, 1) * 0.01) else "rectangle"
        if radius > 0:
            kind = "pill" if radius >= min(width, height) * 0.49 else ("rounded-square" if kind == "square" else "rounded-rectangle")
        return {"classification": {"kind": kind, "atomicShape": kind, "confidence": 1}, "bounds": Bounds(x, y, width, height), "radius": radius or None}
    if tag == "line":
        start = Point(numeric(attrs.get("x1"), 0) or 0, numeric(attrs.get("y1"), 0) or 0)
        end = Point(numeric(attrs.get("x2"), 0) or 0, numeric(attrs.get("y2"), 0) or 0)
        point_dot = distance(start, end) <= EPSILON
        return {"classification": {"kind": "point-dot" if point_dot else "straight-line", "atomicShape": "line", "confidence": 1}, "bounds": bounds_from_points([start, end]), "angle": None if point_dot else angle_info(start, end)}
    points = parse_points(attrs.get("points", ""))
    if tag == "polygon":
        return {"classification": polygon_kind(points, 0.01), "bounds": bounds_from_points(points)}
    segments = [{"type": "L", "from": points[index], "to": point} for index, point in enumerate(points[1:])]
    straight = bool(segments and is_collinear(segments, 0.01))
    return {"classification": {"kind": "straight-line" if straight else "polyline", "atomicShape": "line" if straight else None, "confidence": 0.98 if straight else 0.9}, "bounds": bounds_from_points(points), "angle": angle_info(points[0], points[-1]) if straight else None}


def normalized_bounds(bounds: Bounds | None, view_box: Bounds) -> dict[str, float | int] | None:
    if bounds is None:
        return None
    return {
        "x": clean((bounds.x - view_box.x) * 48 / view_box.width),
        "y": clean((bounds.y - view_box.y) * 48 / view_box.height),
        "width": clean(bounds.width * 48 / view_box.width),
        "height": clean(bounds.height * 48 / view_box.height),
    }


def spec_issues(element: dict[str, Any], view_box: Bounds) -> list[dict[str, str]]:
    issues: list[dict[str, str]] = []
    classification, normalized = element["classification"], element["normalizedBounds"]
    if classification.get("unsupported"):
        issues.append({"rule": "R3", "severity": "error", "message": "Cubic curve detected; replace it with an arc or quadratic curve."})
    angle = element.get("angle")
    if angle and angle["deviation"] > 1:
        issues.append({"rule": "R3", "severity": "warning", "message": f"Line angle {angle['degrees']}° is {angle['deviation']}° away from the 15° grid."})
    if normalized and classification["kind"] in {"circle", "ellipse", "square", "rounded-square"} and (normalized["width"] < 4 or normalized["height"] < 4):
        issues.append({"rule": "R3", "severity": "warning", "message": f"Outlined {classification['kind']} normalizes below 4×4u; convert it to a point-line dot or simplify it."})
    if element.get("radius") and classification["kind"] in {"rounded-square", "rounded-rectangle", "gapped-rounded-rectangle"}:
        radius = element["radius"] * 48 / max(view_box.width, view_box.height)
        if not near(radius, 4, 0.35) and not near(radius, 8, 0.35):
            issues.append({"rule": "R3", "severity": "warning", "message": f"Corner radius normalizes to {clean(radius)}u; new-grid corners must resolve to 4u or 8u."})
    if element.get("transform"):
        issues.append({"rule": "R1", "severity": "info", "message": "Transform is preserved as metadata; flatten it before converting coordinates to maker instances."})
    return issues


def analyze_svg(svg_text: str, source_name: str | None = None) -> dict[str, Any]:
    try:
        root = ET.fromstring(svg_text)
    except ET.ParseError as error:
        raise ValueError(f"Invalid SVG XML: {error}") from error
    if local_name(root.tag) != "svg":
        raise ValueError("Input root must be <svg>")
    view_box = parse_view_box(root)
    elements: list[dict[str, Any]] = []

    def visit(node: ET.Element, inherited_transforms: tuple[str, ...] = ()) -> None:
        tag, attrs = local_name(node.tag), dict(node.attrib)
        own_transform = attrs.get("transform")
        transforms = inherited_transforms + ((own_transform,) if own_transform else ())
        if tag in SHAPE_TAGS:
            parse_error = None
            if tag == "path":
                try:
                    segments = parse_path(attrs.get("d", ""))
                    classification = classify_path(segments, view_box)
                    geometry: dict[str, Any] = {"classification": classification, "bounds": path_bounds(segments), "segments": segments}
                    lines = [segment for segment in segments if segment["type"] == "L"]
                    if classification["kind"] == "straight-line" and lines:
                        geometry["angle"] = angle_info(lines[0]["from"], lines[-1]["to"])
                    if classification.get("inferredRadius"):
                        geometry["radius"] = classification["inferredRadius"]
                except ValueError as error:
                    parse_error = str(error)
                    geometry = {"classification": {"kind": "unparsed-path", "atomicShape": None, "confidence": 0, "unsupported": True}, "bounds": None, "segments": []}
            else:
                geometry = primitive_geometry(tag, attrs)
            bounds = geometry.get("bounds")
            element = {
                "index": len(elements), "tag": tag, "id": attrs.get("id"),
                "sourceHint": attrs.get("data-shape"), "sourceHintScore": numeric(attrs.get("data-shape-score")),
                "transform": " ".join(transforms) or None,
                "classification": geometry["classification"],
                "bounds": bounds.rounded() if bounds else None,
                "normalizedBounds": normalized_bounds(bounds, view_box),
                "angle": geometry.get("angle"), "radius": clean(geometry["radius"]) if geometry.get("radius") else None,
                "pathCommands": list(dict.fromkeys(segment["type"] for segment in geometry.get("segments", []))) if "segments" in geometry else None,
                "parseError": parse_error,
            }
            element["specIssues"] = spec_issues(element, view_box)
            if parse_error:
                element["specIssues"].append({"rule": "R3", "severity": "error", "message": parse_error})
            elements.append(element)
        for child in node:
            visit(child, transforms)

    visit(root)
    category_counts: dict[str, int] = {}
    for element in elements:
        kind = element["classification"]["kind"]
        category_counts[kind] = category_counts.get(kind, 0) + 1
    errors = [issue for element in elements for issue in element["specIssues"] if issue["severity"] == "error"]
    warnings = [issue for element in elements for issue in element["specIssues"] if issue["severity"] == "warning"]
    manual_review = [
        element["index"] for element in elements
        if element["transform"] or not element["classification"].get("atomicShape") or element["classification"]["confidence"] < 0.8 or element["classification"].get("unsupported")
    ]
    return {
        "schemaVersion": 1,
        "source": {"name": source_name, "viewBox": view_box.rounded(), "width": root.attrib.get("width"), "height": root.attrib.get("height")},
        "targetSpec": {
            "designCanvas": 48,
            "shipCanvas": 24,
            "grid": {"minor": 1, "major": 4},
            "keyshapes": [
                {"name": "circle-44", "shape": "circle", "diameter": 44, "cardinalPadding": 2},
                {"name": "square-40", "shape": "rect", "width": 40, "height": 40, "padding": [4, 4]},
                {"name": "portrait-36x44", "shape": "rect", "width": 36, "height": 44, "padding": [6, 2]},
                {"name": "landscape-44x36", "shape": "rect", "width": 44, "height": 36, "padding": [2, 6]},
            ],
            "regularStroke": {"design": 4, "ship": 2}, "angleStep": 15,
            "cornerRadii": [4, 8], "curves": ["arc", "quadratic"],
        },
        "summary": {
            "elementCount": len(elements), "categoryCounts": category_counts,
            "atomicCandidateCount": sum(bool(element["classification"].get("atomicShape")) for element in elements),
            "manualReviewCount": len(manual_review), "errorCount": len(errors), "warningCount": len(warnings),
            "readyForIconMaker": not errors and not manual_review,
        },
        "elements": elements,
        "makerPreflight": {
            "suggestedAtoms": [
                {"sourceElement": element["index"], "shapeId": element["classification"]["atomicShape"], "confidence": element["classification"]["confidence"], "normalizedBounds": element["normalizedBounds"], "rotation": element["angle"]["nearest15"] if element.get("angle") else 0}
                for element in elements if element["classification"].get("atomicShape")
            ],
            "manualReview": manual_review,
            "note": "Suggestions are semantic preprocessing, not final geometry. Simplify, snap, center, and enforce R4/R5 during icon making.",
        },
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="SVG reference to analyze")
    parser.add_argument("-o", "--output", type=Path, help="write JSON report to this path; defaults to stdout")
    parser.add_argument("--strict", action="store_true", help="exit 3 when the report needs manual review")
    parser.add_argument("--compact", action="store_true", help="write compact JSON")
    parser.add_argument("--plot", type=Path, metavar="IMAGE", help="save a labeled Matplotlib visualization (PNG, SVG, PDF, etc.)")
    parser.add_argument("--show", action="store_true", help="open the Matplotlib visualization interactively")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        svg_text = args.input.read_text(encoding="utf-8")
        report = analyze_svg(svg_text, args.input.name)
        output = json.dumps(report, ensure_ascii=False, indent=None if args.compact else 2) + "\n"
        if args.output:
            args.output.write_text(output, encoding="utf-8")
            print(f"Detected {report['summary']['elementCount']} SVG elements; report written to {args.output}", file=sys.stderr)
        else:
            sys.stdout.write(output)
        if args.plot or args.show:
            render_detection_plot(svg_text, report, args.plot, args.show)
            if args.plot:
                print(f"Matplotlib visualization written to {args.plot}", file=sys.stderr)
        return 3 if args.strict and not report["summary"]["readyForIconMaker"] else 0
    except (OSError, ValueError) as error:
        print(f"Shape detection failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
