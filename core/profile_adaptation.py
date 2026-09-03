#!/usr/bin/env python3
"""Conservative, review-required adaptation of outline SVG design geometry.

This module does not write files, approve icons, infer semantic relationships,
or reuse editable JSON geometry. It reads an explicit safe SVG subset, applies
one stroke-compensated uniform fit, and reports the consequences of grid snap.
"""
from __future__ import annotations

from copy import deepcopy
import io
import math
from pathlib import Path
import re
import xml.etree.ElementTree as ET

from icon_geometry import Command, ELEMENT_ATTRS, ELEMENT_ID, NUMBER, finite_number, primitive_commands, resolve_icon, sample

SVG_NS = "http://www.w3.org/2000/svg"
EPSILON = 1e-9
MAX_SOURCE_BYTES = 4 * 1024 * 1024
MAX_COMMANDS = 10000
PAINT_ATTRS = {"fill", "stroke", "stroke-width", "stroke-linecap", "stroke-linejoin"}
ROOT_ATTRS = PAINT_ATTRS | {"viewBox", "width", "height"}


def _format(value: float) -> str:
    value = finite_number(value)
    return str(int(value)) if value.is_integer() else repr(value)


def _path_text(commands: list[Command]) -> str:
    """Keep normalized command geometry and arc rotation precision intact."""
    parts = []
    for command in commands:
        if command.type == "Z":
            parts.append("Z")
            continue
        points = " ".join(_format(value) for point in command.points for value in point)
        if command.type == "A":
            rx, ry, rotation, large, sweep = command.arc
            parts.append(f"A {_format(rx)} {_format(ry)} {_format(rotation)} {large} {sweep} {points}")
        else:
            parts.append(f"{command.type} {points}")
    return " ".join(parts)


def _local_tag(tag: object) -> str:
    if not isinstance(tag, str):
        raise ValueError("SVG comments or processing instructions are not supported")
    if tag.startswith("{"):
        namespace, _, name = tag[1:].partition("}")
        if namespace != SVG_NS:
            raise ValueError(f"unsupported SVG namespace {namespace!r}")
        return name
    return tag


def _length(value: str, label: str) -> float:
    match = re.fullmatch(rf"\s*({NUMBER})\s*(?:px)?\s*", value)
    if not match:
        raise ValueError(f"{label} must be a finite unitless or px length")
    return finite_number(match.group(1), label)


def _paint(attributes: dict, inherited: dict | None, context: str) -> dict:
    paint = {**(inherited or {}), **{key: value for key, value in attributes.items() if key in PAINT_ATTRS}}
    for key, expected in (("fill", "none"), ("stroke", "currentColor"),
                          ("stroke-linecap", "round"), ("stroke-linejoin", "round")):
        if paint.get(key) != expected:
            raise ValueError(f"{context}: {key} must resolve to {expected!r}")
    stroke = finite_number(paint.get("stroke-width"), f"{context} stroke-width")
    if stroke <= 0:
        raise ValueError(f"{context}: stroke-width must be positive")
    if inherited and stroke != finite_number(inherited["stroke-width"]):
        raise ValueError(f"{context}: different element strokes are not supported")
    paint["stroke-width"] = stroke
    return paint


def _bounded_commands(paths: list[dict], canvas: float) -> None:
    """Bound diagnostic sampling work, rejecting extreme non-icon input."""
    count = sum(len(path["commands"]) for path in paths)
    if count > MAX_COMMANDS:
        raise ValueError(f"SVG exceeds the {MAX_COMMANDS}-command adaptation limit")
    extent = 16 * canvas
    if not math.isfinite(extent):
        raise ValueError("canvas exceeds the bounded icon-analysis range")
    workload = 0.0
    for path in paths:
        cursor = start = None
        for command in path["commands"]:
            previous = cursor
            if command.type == "M":
                start = command.points[0]
            if command.type == "Z":
                if cursor is not None and start is not None:
                    workload += math.dist(cursor, start)
                cursor = start
            for point in command.points:
                if any(abs(value) > extent for value in point):
                    raise ValueError("geometry exceeds the bounded icon-analysis range")
                if cursor is not None:
                    workload += math.dist(cursor, point)
                cursor = point
            if command.arc:
                rx, ry = command.arc[:2]
                if max(rx, ry) > extent:
                    raise ValueError("arc radius exceeds the bounded icon-analysis range")
                if rx and ry and previous != command.points[0]:
                    if min(rx * rx, ry * ry) == 0:
                        raise ValueError("arc radii are too small for stable diagnostic sampling")
                    expansion = _arc_expansion(previous, command)
                    effective_radius = max(rx, ry) * expansion
                    if not math.isfinite(effective_radius) or effective_radius > extent:
                        raise ValueError("expanded arc radius exceeds the bounded icon-analysis range")
                    workload += math.tau * effective_radius
    if not math.isfinite(workload) or workload > 1000000:
        raise ValueError("geometry exceeds the bounded adaptation sampling budget")


def read_design_svg(path: Path) -> dict:
    """Read flat, round-stroked, currentColor/no-fill SVG into v2 elements.

    Every node and attribute must belong to the supported subset. Presentation
    attributes are checked against the common outline style before normalization;
    element IDs are retained, or assigned deterministically when absent.
    """
    path = Path(path)
    if path.stat().st_size > MAX_SOURCE_BYTES:
        raise ValueError("SVG is too large for bounded icon adaptation")
    data = path.read_bytes()
    if len(data) > MAX_SOURCE_BYTES:
        raise ValueError("SVG is too large for bounded icon adaptation")
    try:
        text = data.decode("utf-8-sig")
    except UnicodeDecodeError as error:
        raise ValueError("design SVG must use UTF-8") from error
    if re.search(r"<!\s*(?:DOCTYPE|ENTITY)\b", text, re.I):
        raise ValueError("DTD/entity declarations are not supported")
    if "<!--" in text:
        raise ValueError("SVG comments are not supported")
    instructions = re.findall(r"<\?\s*([\w:-]+)", text)
    if any(target != "xml" for target in instructions):
        raise ValueError("SVG processing instructions are not supported")
    try:
        for _, (_, namespace) in ET.iterparse(io.StringIO(text), events=("start-ns",)):
            if namespace != SVG_NS:
                raise ValueError(f"unsupported SVG namespace {namespace!r}")
        parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True, insert_pis=True))
        root = ET.fromstring(text, parser=parser)
    except ET.ParseError as error:
        raise ValueError(f"invalid SVG XML: {error}") from error
    if _local_tag(root.tag) != "svg":
        raise ValueError("design input root must be svg")
    extra = set(root.attrib) - ROOT_ATTRS
    if extra:
        raise ValueError(f"unsupported root SVG attributes: {sorted(extra)}")
    if root.text and root.text.strip():
        raise ValueError("non-geometry SVG text is not supported")
    raw_view = root.get("viewBox", "")
    if re.search(r",\s*,|^\s*,|,\s*$", raw_view):
        raise ValueError("malformed design viewBox")
    view = [finite_number(value, "viewBox") for value in raw_view.replace(",", " ").split()]
    if len(view) != 4 or view[:2] != [0, 0] or view[2] <= 0 or view[2] != view[3]:
        raise ValueError("design viewBox must be an origin-zero positive square")
    canvas = view[2]
    for field in ("width", "height"):
        if field in root.attrib and _length(root.attrib[field], field) != canvas:
            raise ValueError(f"SVG {field} must equal its design viewBox canvas")
    paint = _paint(root.attrib, None, "SVG root")
    explicit_ids = [node.get("id") for node in root if isinstance(node.tag, str) and node.get("id") is not None]
    if len(explicit_ids) != len(set(explicit_ids)):
        raise ValueError("duplicate SVG element IDs are not supported")
    used = set(explicit_ids)
    elements = []
    for index, node in enumerate(root, start=1):
        tag = _local_tag(node.tag)
        if tag not in ELEMENT_ATTRS:
            raise ValueError(f"unsupported SVG node {tag!r}; only flat outline geometry is accepted")
        if list(node) or node.text and node.text.strip() or node.tail and node.tail.strip():
            raise ValueError(f"{tag}: nested nodes or text are not supported")
        extra = set(node.attrib) - ELEMENT_ATTRS[tag] - PAINT_ATTRS - {"id"}
        if extra:
            raise ValueError(f"{tag}: unsupported attributes {sorted(extra)}")
        _paint(node.attrib, paint, f"element {index}")
        identifier = node.get("id")
        if identifier is None:
            identifier = f"element-{index:03d}"
            while identifier in used:
                identifier += "-auto"
            used.add(identifier)
        if not ELEMENT_ID.fullmatch(identifier):
            raise ValueError(f"invalid SVG element ID {identifier!r}")
        commands = primitive_commands(tag, {key: value for key, value in node.attrib.items() if key in ELEMENT_ATTRS[tag]})
        elements.append({"id": identifier, "tag": "path", "attrs": {"d": _path_text(commands)}})
    if not elements:
        raise ValueError("design SVG contains no supported geometry")
    paths = resolve_icon({"schemaVersion": 2, "elements": elements})
    _bounded_commands(paths, canvas)
    return {"canvas": canvas, "strokeWidth": paint["stroke-width"], "elements": elements}


def _profile(profile: dict) -> tuple[float, float, float]:
    canvas = finite_number(profile.get("canvas", profile.get("designCanvas")), "profile canvas")
    stroke = finite_number(profile.get("strokeWidth", profile.get("designStroke")), "profile stroke")
    grid = finite_number(profile.get("validation", {}).get("gridStep", 1), "profile gridStep")
    if min(canvas, stroke, grid) <= 0 or stroke >= canvas:
        raise ValueError("profile canvas, stroke, and grid must be positive with stroke smaller than canvas")
    return canvas, stroke, grid


def _token(token: dict, canvas: float, stroke: float) -> tuple[float, float]:
    width, height = (finite_number(token.get(field), f"token {field}") for field in ("width", "height"))
    if min(width, height) <= stroke or max(width, height) > canvas:
        raise ValueError("selected token must fit the canvas and have positive centerline dimensions")
    return width, height


def _snap_distance(value: float, grid: float) -> float:
    return round(math.floor(abs(value) / grid + .5 + 1e-12) * grid, 12)


class _CoordinateMap:
    def __init__(self, source_center: float, target_center: float, scale: float, grid: float):
        self.source_center, self.target_center, self.scale, self.grid = source_center, target_center, scale, grid
        self.locked = {round(source_center, 12): target_center}

    def ideal(self, value: float) -> float:
        return self.target_center + (value - self.source_center) * self.scale

    def __call__(self, value: float) -> float:
        key = round(value, 12)
        if key in self.locked:
            return self.locked[key]
        offset = (value - self.source_center) * self.scale
        return round(self.target_center + math.copysign(_snap_distance(offset, self.grid), offset), 12)

    def proposal(self, pairs: list[tuple[float, float]]) -> dict | None:
        proposed = dict(self.locked)
        for source, target in pairs:
            for key, value in ((source, target), (2 * self.source_center - source, 2 * self.target_center - target)):
                key, value = round(key, 12), round(value, 12)
                if key in proposed and abs(proposed[key] - value) > EPSILON:
                    return None
                proposed[key] = value
        return proposed


def _full_ellipse(commands: list[Command]) -> dict | None:
    visible = commands[:-1] if commands[-1].type == "Z" else commands
    if [command.type for command in visible] != ["M", "A", "A"]:
        return None
    start, opposite, end = [command.points[0] for command in visible]
    first, second = visible[1].arc, visible[2].arc
    if start != end or first[:3] != second[:3] or first[4] != second[4]:
        return None
    rx, ry, rotation = first[:3]
    if min(rx, ry) <= 0 or abs(rotation % 180) > EPSILON and abs(rx - ry) > EPSILON:
        return None
    cx, cy = (start[0] + opposite[0]) / 2, (start[1] + opposite[1]) / 2
    vertical = abs(start[0] - opposite[0]) <= EPSILON and abs(abs(start[1] - opposite[1]) - 2 * ry) <= EPSILON
    horizontal = abs(start[1] - opposite[1]) <= EPSILON and abs(abs(start[0] - opposite[0]) - 2 * rx) <= EPSILON
    return {"cx": cx, "cy": cy, "rx": rx, "ry": ry} if vertical or horizontal else None


def _painted_bounds(paths: list[dict], stroke: float) -> list[float] | None:
    points = [point for path in paths for point in sample(path["commands"], density=1)[0]]
    if not points:
        return None
    radius = stroke / 2
    return [min(x for x, _ in points) - radius, min(y for _, y in points) - radius,
            max(x for x, _ in points) + radius, max(y for _, y in points) + radius]


def _arc_expansion(start: tuple, command: Command) -> float:
    rx, ry, rotation, _, _ = command.arc
    if not rx or not ry or start == command.points[0]:
        return 1.0
    end = command.points[0]
    dx, dy = (start[0] - end[0]) / 2, (start[1] - end[1]) / 2
    phi = math.radians(rotation)
    x, y = math.cos(phi) * dx + math.sin(phi) * dy, -math.sin(phi) * dx + math.cos(phi) * dy
    return max(1.0, math.hypot(x / rx, y / ry))


def adapt_geometry(source: dict, source_profile: dict, target_profile: dict,
                   source_token: dict, target_token: dict) -> dict:
    """Uniformly fit and symmetrically grid-snap SVG-derived geometry.

    This is an adaptation candidate, never QA approval. Source/target metadata
    describes the transformation; all contour commands come from source elements.
    """
    source_canvas, source_stroke, _ = _profile(source_profile)
    target_canvas, target_stroke, grid = _profile(target_profile)
    if finite_number(source.get("canvas")) != source_canvas or finite_number(source.get("strokeWidth")) != source_stroke:
        raise ValueError("SVG canvas/stroke does not match the selected source profile")
    center_grid_units = target_canvas / (2 * grid)
    if not math.isfinite(center_grid_units) or abs(center_grid_units - round(center_grid_units)) > EPSILON:
        raise ValueError("center-symmetric adaptation requires the target center on its grid")
    sw, sh = _token(source_token, source_canvas, source_stroke)
    tw, th = _token(target_token, target_canvas, target_stroke)
    scale = min((tw - target_stroke) / (sw - source_stroke), (th - target_stroke) / (sh - source_stroke))
    if not math.isfinite(scale) or scale <= 0:
        raise ValueError("stroke-compensated fit must have a finite positive scale")
    paths = resolve_icon({"schemaVersion": 2, "elements": deepcopy(source.get("elements"))})
    _bounded_commands(paths, source_canvas)
    xmap, ymap = (_CoordinateMap(source_canvas / 2, target_canvas / 2, scale, grid) for _ in range(2))
    target_bounds = [(target_canvas - tw) / 2, (target_canvas - th) / 2,
                     (target_canvas + tw) / 2, (target_canvas + th) / 2]
    inner = [target_bounds[0] + target_stroke / 2, target_bounds[1] + target_stroke / 2,
             target_bounds[2] - target_stroke / 2, target_bounds[3] - target_stroke / 2]
    warnings, ellipse_plans = [], {}
    for path in paths:
        ellipse = _full_ellipse(path["commands"])
        if ellipse is None:
            continue
        radii = [max(grid, _snap_distance(ellipse[key] * scale, grid)) for key in ("rx", "ry")]
        proposals = []
        for axis, (mapper, key, radius) in enumerate(zip((xmap, ymap), ("cx", "cy"), radii)):
            low, high = inner[axis] + radius, inner[axis + 2] - radius
            low, high = math.ceil((low - EPSILON) / grid) * grid, math.floor((high + EPSILON) / grid) * grid
            if low > high:
                proposals = []
                break
            center = min(high, max(low, mapper(ellipse[key])))
            source_radius = ellipse["rx" if axis == 0 else "ry"]
            proposals.append(mapper.proposal([(ellipse[key], center),
                (ellipse[key] - source_radius, center - radius), (ellipse[key] + source_radius, center + radius)]))
        if len(proposals) != 2 or any(proposal is None for proposal in proposals):
            warnings.append(f"{path['id']}: full ellipse cannot be reconstructed without conflicting shared/grid coordinates; arc deformation remains for review")
            continue
        xmap.locked, ymap.locked = proposals
        ellipse_plans[path["id"]] = tuple(radii)

    adapted, ideal_paths, movements = [], [], []
    collapsed, curve_changes, radius_changes, expansions = [], [], [], []
    dots, fractional_source, source_coordinates = 0, set(), (set(), set())
    for path in paths:
        commands, ideal_commands = [], []
        source_cursor = target_cursor = ideal_cursor = None
        source_start = target_start = ideal_start = None
        for index, command in enumerate(path["commands"]):
            ideal_points = [(xmap.ideal(x), ymap.ideal(y)) for x, y in command.points]
            points = [(xmap(x), ymap(y)) for x, y in command.points]
            point_moves = [math.dist(ideal, actual) for ideal, actual in zip(ideal_points, points)]
            movements.extend(point_moves)
            for x, y in command.points:
                source_coordinates[0].add(x)
                source_coordinates[1].add(y)
                for axis, value in enumerate((x, y)):
                    if abs(value - round(value)) > EPSILON:
                        fractional_source.add((axis, value))
            arc, ideal_arc = command.arc, command.arc
            radius_delta = 0.0
            if arc:
                rx, ry, rotation, large, sweep = arc
                ideal_arc = (rx * scale, ry * scale, rotation, large, sweep)
                radii = ellipse_plans.get(path["id"], tuple(max(grid, _snap_distance(radius * scale, grid)) if radius > 0 else 0 for radius in (rx, ry)))
                arc = (*radii, rotation, large, sweep)
                radius_delta = max(abs(radii[axis] - ideal_arc[axis]) for axis in (0, 1))
                if radius_delta > EPSILON:
                    radius_changes.append({"elementId": path["id"], "commandIndex": index, "idealRadii": list(ideal_arc[:2]), "radii": list(radii)})
            transformed = Command(command.type, points, arc)
            ideal = Command(command.type, ideal_points, ideal_arc)
            commands.append(transformed)
            ideal_commands.append(ideal)
            context = {"elementId": path["id"], "commandIndex": index, "type": command.type}
            if command.type == "M":
                source_cursor = source_start = command.points[0]
                target_cursor = target_start = points[0]
                ideal_cursor = ideal_start = ideal_points[0]
                continue
            if command.type == "Z":
                if source_cursor != source_start and target_cursor == target_start:
                    collapsed.append(context)
                source_cursor, target_cursor, ideal_cursor = source_start, target_start, ideal_start
                continue
            if command.type == "L" and source_cursor == command.points[-1]:
                dots += 1
            elif (command.type in {"L", "A"} and source_cursor != command.points[-1] and target_cursor == points[-1]
                  or command.type in {"Q", "C"} and any(point != source_cursor for point in command.points) and all(point == target_cursor for point in points)):
                collapsed.append(context)
            if command.type in {"A", "Q", "C"}:
                start_move = math.dist(ideal_cursor, target_cursor)
                deformation = max([start_move, radius_delta, *point_moves])
                if deformation > EPSILON:
                    curve_changes.append({**context, "maximumControlOrRadiusMovement": deformation})
                if command.type == "A":
                    expansion = _arc_expansion(target_cursor, transformed)
                    if expansion > 1 + EPSILON:
                        expansions.append({**context, "svgRadiusExpansionFactor": expansion})
            source_cursor, target_cursor, ideal_cursor = command.points[-1], points[-1], ideal_points[-1]
        adapted.append({**path, "commands": commands})
        ideal_paths.append({**path, "commands": ideal_commands})
    merges = []
    for axis, (coordinates, mapper) in enumerate(zip(source_coordinates, (xmap, ymap))):
        grouped = {}
        for coordinate in sorted(coordinates):
            grouped.setdefault(mapper(coordinate), []).append(coordinate)
        merges.extend({"axis": "xy"[axis], "target": target, "sourceValues": values} for target, values in grouped.items() if len(values) > 1)
    if fractional_source:
        warnings.append(f"{len(fractional_source)} fractional source coordinate levels were transformed/snapped; original tangency or grid exceptions are not preserved approvals")
    if curve_changes:
        warnings.append(f"{len(curve_changes)} curve segment(s) changed beyond uniform scaling; review curvature and tangency")
    if expansions:
        warnings.append(f"{len(expansions)} arc(s) require SVG's implicit radius expansion after snapping")
    if collapsed:
        warnings.append(f"{len(collapsed)} previously nonzero segment(s) collapsed on the target grid; no semantic repair was attempted")
    if merges:
        warnings.append(f"{len(merges)} groups of distinct coordinate levels merged on the grid; spacing must be rechecked")
    _bounded_commands(adapted, target_canvas)
    _bounded_commands(ideal_paths, target_canvas)
    actual_bounds = _painted_bounds(adapted, target_stroke)
    overflow = ([max(0, target_bounds[0] - actual_bounds[0]), max(0, target_bounds[1] - actual_bounds[1]),
                 max(0, actual_bounds[2] - target_bounds[2]), max(0, actual_bounds[3] - target_bounds[3])] if actual_bounds else None)
    if overflow and max(overflow) > EPSILON:
        warnings.append("snapped painted bounds exceed the selected target token; keyshape QA must reject or review the candidate")
    metrics = {
        "strategy": "uniform-stroke-compensated-fit-and-center-symmetric-grid",
        "requiresReview": True, "sourceCanvas": source_canvas, "targetCanvas": target_canvas,
        "sourceStrokeWidth": source_stroke, "targetStrokeWidth": target_stroke,
        "sourceToken": source_token.get("name"), "targetToken": target_token.get("name"),
        "uniformScale": scale, "gridStep": grid, "elementCount": len(paths),
        "pointCount": len(movements), "movedPointCount": sum(value > EPSILON for value in movements),
        "maxSnapDistance": max(movements, default=0),
        "rmsSnapDistance": math.sqrt(sum(value * value for value in movements) / len(movements)) if movements else 0,
        "preservedDotCount": dots, "reconstructedEllipseCount": len(ellipse_plans),
        "collapsedSegments": collapsed, "curveDeformations": curve_changes,
        "radiusAdjustments": radius_changes, "implicitArcExpansions": expansions,
        "coordinateMerges": merges, "fractionalSourceCoordinateCount": len(fractional_source),
        "sourcePaintedBounds": _painted_bounds(paths, source_stroke),
        "uniformPaintedBounds": _painted_bounds(ideal_paths, target_stroke),
        "adaptedPaintedBounds": actual_bounds, "targetTokenBounds": target_bounds,
        "paintedOverflow": overflow,
    }
    elements = []
    for path in adapted:
        element = {"id": path["id"], "tag": "path", "attrs": {"d": _path_text(path["commands"])}}
        if path.get("role") is not None:
            element["role"] = path["role"]
        elements.append(element)
    return {"elements": elements, "warnings": warnings, "metrics": metrics}
