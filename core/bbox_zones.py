#!/usr/bin/env python3
"""Report each SVG's drawn bounding box against its canvas, as 0-33 / 33-66 / 66-100 bands."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

SVG_NS = "http://www.w3.org/2000/svg"
NUMBER = r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?"
SAMPLES = 48
BANDS = ((0.0, 33.0, "0-33"), (33.0, 66.0, "33-66"), (66.0, 100.0, "66-100"))


def band(percent: float) -> str:
    for low, high, label in BANDS:
        if percent < high or high == 100.0:
            return label if percent >= low else BANDS[0][2]
    return BANDS[-1][2]


# ---------------------------------------------------------------- transforms

def parse_transform(value: str | None) -> tuple[float, float, float, float, float, float]:
    matrix = (1.0, 0.0, 0.0, 1.0, 0.0, 0.0)
    if not value:
        return matrix
    for name, raw in re.findall(r"(\w+)\s*\(([^)]*)\)", value):
        args = [float(v) for v in re.findall(NUMBER, raw)]
        if name == "translate":
            step = (1, 0, 0, 1, args[0], args[1] if len(args) > 1 else 0.0)
        elif name == "scale":
            sx = args[0]; sy = args[1] if len(args) > 1 else sx
            step = (sx, 0, 0, sy, 0, 0)
        elif name == "rotate":
            angle = math.radians(args[0]); cos, sin = math.cos(angle), math.sin(angle)
            step = (cos, sin, -sin, cos, 0, 0)
            if len(args) == 3:
                cx, cy = args[1], args[2]
                step = compose(compose((1, 0, 0, 1, cx, cy), step), (1, 0, 0, 1, -cx, -cy))
        elif name == "matrix" and len(args) == 6:
            step = tuple(args)
        elif name == "skewX":
            step = (1, 0, math.tan(math.radians(args[0])), 1, 0, 0)
        elif name == "skewY":
            step = (1, math.tan(math.radians(args[0])), 0, 1, 0, 0)
        else:
            continue
        matrix = compose(matrix, step)
    return matrix


def compose(m: tuple, n: tuple) -> tuple:
    a1, b1, c1, d1, e1, f1 = m
    a2, b2, c2, d2, e2, f2 = n
    return (a1*a2 + c1*b2, b1*a2 + d1*b2, a1*c2 + c1*d2, b1*c2 + d1*d2, a1*e2 + c1*f2 + e1, b1*e2 + d1*f2 + f1)


def apply(matrix: tuple, point: tuple[float, float]) -> tuple[float, float]:
    a, b, c, d, e, f = matrix
    x, y = point
    return (a*x + c*y + e, b*x + d*y + f)


def scale_of(matrix: tuple) -> float:
    a, b, c, d, _, _ = matrix
    return math.sqrt(abs(a*d - b*c)) or 1.0


# ---------------------------------------------------------------- path points

def bezier(points: list[tuple[float, float]], order: int) -> list[tuple[float, float]]:
    out = []
    for step in range(1, SAMPLES + 1):
        t = step / SAMPLES
        u = 1 - t
        if order == 3:
            (x0, y0), (x1, y1), (x2, y2), (x3, y3) = points
            out.append((u*u*u*x0 + 3*u*u*t*x1 + 3*u*t*t*x2 + t*t*t*x3,
                        u*u*u*y0 + 3*u*u*t*y1 + 3*u*t*t*y2 + t*t*t*y3))
        else:
            (x0, y0), (x1, y1), (x2, y2) = points
            out.append((u*u*x0 + 2*u*t*x1 + t*t*x2, u*u*y0 + 2*u*t*y1 + t*t*y2))
    return out


def arc(start: tuple[float, float], rx: float, ry: float, rotation: float,
        large: int, sweep: int, end: tuple[float, float]) -> list[tuple[float, float]]:
    x0, y0 = start
    x1, y1 = end
    if rx == 0 or ry == 0 or (abs(x1 - x0) < 1e-12 and abs(y1 - y0) < 1e-12):
        return [end]
    rx, ry = abs(rx), abs(ry)
    phi = math.radians(rotation)
    cos, sin = math.cos(phi), math.sin(phi)
    dx, dy = (x0 - x1) / 2, (y0 - y1) / 2
    x1p, y1p = cos*dx + sin*dy, -sin*dx + cos*dy
    lam = (x1p*x1p) / (rx*rx) + (y1p*y1p) / (ry*ry)
    if lam > 1:
        rx, ry = rx*math.sqrt(lam), ry*math.sqrt(lam)
    num = rx*rx*ry*ry - rx*rx*y1p*y1p - ry*ry*x1p*x1p
    den = rx*rx*y1p*y1p + ry*ry*x1p*x1p
    factor = math.sqrt(max(num, 0) / den) * (-1 if large == sweep else 1)
    cxp, cyp = factor * rx * y1p / ry, factor * -ry * x1p / rx
    cx = cos*cxp - sin*cyp + (x0 + x1) / 2
    cy = sin*cxp + cos*cyp + (y0 + y1) / 2
    start_angle = math.atan2((y1p - cyp) / ry, (x1p - cxp) / rx)
    end_angle = math.atan2((-y1p - cyp) / ry, (-x1p - cxp) / rx)
    delta = end_angle - start_angle
    if sweep and delta < 0:
        delta += 2 * math.pi
    elif not sweep and delta > 0:
        delta -= 2 * math.pi
    out = []
    for step in range(1, SAMPLES + 1):
        angle = start_angle + delta * step / SAMPLES
        px, py = rx * math.cos(angle), ry * math.sin(angle)
        out.append((cos*px - sin*py + cx, sin*px + cos*py + cy))
    return out


def path_points(d: str) -> list[tuple[float, float]]:
    points: list[tuple[float, float]] = []
    current = (0.0, 0.0)
    origin = (0.0, 0.0)
    prev_cubic = prev_quad = None
    for chunk in re.findall(r"[A-Za-z][^A-Za-z]*", d):
        kind = chunk[0]
        args = [float(v) for v in re.findall(NUMBER, chunk[1:])]
        upper = kind.upper()
        relative = kind.islower()
        index = 0
        first = True
        while True:
            def take(count: int) -> list[float]:
                nonlocal index
                values = args[index:index + count]
                index += count
                return values

            def absolute(pair: list[float]) -> tuple[float, float]:
                return (pair[0] + current[0], pair[1] + current[1]) if relative else (pair[0], pair[1])

            if upper == "Z":
                current = origin
                points.append(current)
                break
            if index >= len(args):
                break
            if upper in ("M", "L", "T"):
                current_prev = current
                current = absolute(take(2))
                if upper == "T":
                    control = current_prev if prev_quad is None else (2*current_prev[0] - prev_quad[0], 2*current_prev[1] - prev_quad[1])
                    points.extend(bezier([current_prev, control, current], 2))
                    prev_quad = control
                else:
                    points.append(current)
                    prev_quad = prev_cubic = None
                if upper == "M":
                    if first:
                        origin = current
                    upper = "L"  # subsequent implicit pairs are lineto
            elif upper in ("H", "V"):
                value = take(1)[0]
                if upper == "H":
                    current = (value + current[0], current[1]) if relative else (value, current[1])
                else:
                    current = (current[0], value + current[1]) if relative else (current[0], value)
                points.append(current)
                prev_quad = prev_cubic = None
            elif upper in ("C", "S"):
                start = current
                if upper == "C":
                    c1 = absolute(take(2)); c2 = absolute(take(2))
                else:
                    c1 = start if prev_cubic is None else (2*start[0] - prev_cubic[0], 2*start[1] - prev_cubic[1])
                    c2 = absolute(take(2))
                current = absolute(take(2))
                points.extend(bezier([start, c1, c2, current], 3))
                prev_cubic, prev_quad = c2, None
            elif upper == "Q":
                start = current
                control = absolute(take(2))
                current = absolute(take(2))
                points.extend(bezier([start, control, current], 2))
                prev_quad, prev_cubic = control, None
            elif upper == "A":
                values = take(7)
                start = current
                current = (values[5] + start[0], values[6] + start[1]) if relative else (values[5], values[6])
                points.extend(arc(start, values[0], values[1], values[2], int(values[3]), int(values[4]), current))
                prev_quad = prev_cubic = None
            else:
                raise ValueError(f"unsupported path command {kind!r}")
            first = False
            if index >= len(args):
                break
    return points


def element_points(tag: str, attrs: dict) -> list[tuple[float, float]]:
    def num(key: str, fallback: float = 0.0) -> float:
        return float(attrs.get(key, fallback) or fallback)

    if tag == "path":
        return path_points(attrs.get("d", ""))
    if tag == "rect":
        x, y, w, h = num("x"), num("y"), num("width"), num("height")
        return [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    if tag in ("circle", "ellipse"):
        cx, cy = num("cx"), num("cy")
        rx = num("r") if tag == "circle" else num("rx")
        ry = rx if tag == "circle" else num("ry")
        return [(cx - rx, cy - ry), (cx + rx, cy - ry), (cx + rx, cy + ry), (cx - rx, cy + ry)]
    if tag == "line":
        return [(num("x1"), num("y1")), (num("x2"), num("y2"))]
    if tag in ("polyline", "polygon"):
        values = [float(v) for v in re.findall(NUMBER, attrs.get("points", ""))]
        return list(zip(values[0::2], values[1::2]))
    return []


# ---------------------------------------------------------------- traversal

def walk(node: ET.Element, matrix: tuple, stroke: float, include_stroke: bool,
         box: list[float]) -> None:
    matrix = compose(matrix, parse_transform(node.get("transform")))
    raw_stroke = node.get("stroke-width")
    if raw_stroke:
        stroke = float(re.search(NUMBER, raw_stroke).group())
    tag = node.tag.split("}")[-1]
    points = element_points(tag, node.attrib)
    if points:
        painted = node.get("stroke", "none") not in ("none", "") or node.get("stroke-width") is not None
        pad = (stroke * scale_of(matrix) / 2) if (include_stroke and painted) else 0.0
        for point in points:
            x, y = apply(matrix, point)
            box[0] = min(box[0], x - pad); box[1] = min(box[1], y - pad)
            box[2] = max(box[2], x + pad); box[3] = max(box[3], y + pad)
    for child in node:
        walk(child, matrix, stroke, include_stroke, box)


def measure(path: Path, include_stroke: bool) -> dict:
    root = ET.parse(path).getroot()
    view = [float(v) for v in re.findall(NUMBER, root.get("viewBox", "") or "")]
    if len(view) != 4:
        width = float(re.search(NUMBER, root.get("width", "0")).group())
        height = float(re.search(NUMBER, root.get("height", "0")).group())
        view = [0.0, 0.0, width, height]
    vx, vy, vw, vh = view
    if vw <= 0 or vh <= 0:
        raise ValueError(f"{path.name}: canvas has no positive size")

    box = [math.inf, math.inf, -math.inf, -math.inf]
    stroke = float(re.search(NUMBER, root.get("stroke-width", "1")).group())
    for child in root:
        walk(child, parse_transform(root.get("transform")), stroke, include_stroke, box)
    if box[0] is math.inf or box[0] > box[2]:
        raise ValueError(f"{path.name}: no drawable geometry found")

    x0, y0, x1, y1 = box
    percent = {
        "left": (x0 - vx) / vw * 100, "right": (x1 - vx) / vw * 100,
        "top": (y0 - vy) / vh * 100, "bottom": (y1 - vy) / vh * 100,
    }
    percent["center_x"] = (percent["left"] + percent["right"]) / 2
    percent["center_y"] = (percent["top"] + percent["bottom"]) / 2
    percent["width"] = percent["right"] - percent["left"]
    percent["height"] = percent["bottom"] - percent["top"]
    return {
        "file": path.name,
        "canvas": {"x": vx, "y": vy, "width": vw, "height": vh},
        "bbox": {"x": x0, "y": y0, "width": x1 - x0, "height": y1 - y0, "x2": x1, "y2": y1},
        "percent": percent,
        "bands": {key: band(percent[key]) for key in ("left", "right", "top", "bottom", "center_x", "center_y")},
        "spans_x": sorted({band(percent["left"]), band(percent["right"])}, key=lambda b: [x[2] for x in BANDS].index(b)),
        "spans_y": sorted({band(percent["top"]), band(percent["bottom"])}, key=lambda b: [x[2] for x in BANDS].index(b)),
    }


def report(result: dict) -> str:
    canvas, box, pct, bands = result["canvas"], result["bbox"], result["percent"], result["bands"]
    lines = [
        f"{result['file']}",
        f"  canvas   {canvas['width']:g} x {canvas['height']:g}  (origin {canvas['x']:g},{canvas['y']:g})",
        f"  bbox     x {box['x']:.2f} -> {box['x2']:.2f}   y {box['y']:.2f} -> {box['y2']:.2f}"
        f"   size {box['width']:.2f} x {box['height']:.2f}",
        f"  x-axis   left {pct['left']:6.2f}% [{bands['left']}]   right {pct['right']:6.2f}% [{bands['right']}]"
        f"   center {pct['center_x']:6.2f}% [{bands['center_x']}]",
        f"  y-axis   top  {pct['top']:6.2f}% [{bands['top']}]   bottom {pct['bottom']:6.2f}% [{bands['bottom']}]"
        f"   center {pct['center_y']:6.2f}% [{bands['center_y']}]",
        f"  coverage {pct['width']:.2f}% wide x {pct['height']:.2f}% tall",
        f"  spans    x: {' + '.join(result['spans_x'])}   y: {' + '.join(result['spans_y'])}",
    ]
    return "\n".join(lines)


def collect(inputs: list[str]) -> list[Path]:
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", help="SVG files or directories")
    parser.add_argument("--no-stroke", action="store_true", help="measure path geometry only, ignoring stroke width")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = parser.parse_args()

    results, failures = [], 0
    for path in collect(args.inputs):
        try:
            results.append(measure(path, include_stroke=not args.no_stroke))
        except Exception as error:  # noqa: BLE001 - one bad file must not stop the batch
            failures += 1
            print(f"error: {error}", file=sys.stderr)
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print("\n\n".join(report(item) for item in results))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
