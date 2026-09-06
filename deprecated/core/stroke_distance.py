#!/usr/bin/env python3
"""Conservative distances between disconnected SVG centerline components.

This numerical module consumes :func:`icon_geometry.resolve_icon` output; it
does not read SVG, interpret paint/style, or write reports. Its caller must
enforce a uniform round stroke before interpreting ``distance - stroke_width``
as visible ink clearance.

Each drawable M-separated subpath is a contour. A lone M and a coincident-end
SVG arc draw nothing; an explicit zero-length L is a round-cap dot. Contours
belong to one component only when they share original, drawn command endpoints
or their original straight segments demonstrably intersect. Ink overlap is
never a connection. We deliberately do not infer curve/curve or curve/line
interior connections from flattened chords: an unresolved contact is REVIEW.
Spacing inside a single connected component is outside this check's scope.

Distances are continuous segment-to-segment minima, not sampled point-cloud
minima. Q/C curves are adaptively subdivided using a control-hull Hausdorff
bound; an elliptic arc uses ||p''|| * angular_span**2 / 8. Reported bounds
include both curves' flattening errors and floating-point construction guards.
Exact rational line predicates prevent tiny positive gaps being merged, and
exact squared chord distances preserve the inclusive straight-line threshold.
The nearest points shown in a report lie on the bounded polyline approximation,
not necessarily on the original curves. Ambiguous thresholds, ill-conditioned
arc construction, and finite work limits never return PASS.
"""

from __future__ import annotations

import heapq
import itertools
import math
from dataclasses import dataclass, field
from fractions import Fraction

from icon_geometry import Command


Point = tuple[float, float]
Bounds = tuple[float, float, float, float]

# Limits are intentionally independent of the SVG reader: the public numerical
# API must remain bounded even when called directly with normalized Commands.
MAX_COMMANDS = 8192
MAX_CONTOURS = 256
MAX_SEGMENTS = 32768
MAX_ADAPTIVE_NODES = 131072
MAX_SUBDIVISION_DEPTH = 24
MAX_DISTANCE_TESTS = 250000
MAX_CONNECTION_TESTS = 100000
MAX_COORDINATE = 1_000_000.0


class _NeedsReview(ValueError):
    """The engine cannot certify a result within its numerical/work limits."""


@dataclass
class _Budget:
    commands: int = 0
    segments: int = 0
    adaptive_nodes: int = 0
    distance_tests: int = 0
    connection_tests: int = 0

    def use(self, name: str, limit: int) -> None:
        count = getattr(self, name) + 1
        setattr(self, name, count)
        if count > limit:
            raise _NeedsReview(f"Work limit exceeded: {name} > {limit}; no spacing pass can be certified.")


@dataclass
class _Segment:
    a: Point
    b: Point
    error: float = 0.0
    original_straight: bool = False

    @property
    def bounds(self) -> Bounds:
        return (min(self.a[0], self.b[0]), min(self.a[1], self.b[1]),
                max(self.a[0], self.b[0]), max(self.a[1], self.b[1]))


@dataclass
class _Node:
    bounds: Bounds
    count: int
    segments: list[_Segment] | None = None
    left: _Node | None = None
    right: _Node | None = None


@dataclass
class _Contour:
    identifier: str
    element_id: str
    subpath_index: int
    commands: list[Command]
    segments: list[_Segment] = field(default_factory=list)
    endpoints: set[Point] = field(default_factory=set)
    has_curves: bool = False
    component_id: str | None = None
    tree: _Node | None = None

    @property
    def error(self) -> float:
        return max((segment.error for segment in self.segments), default=0.0)

    @property
    def bounds(self) -> Bounds:
        return _union_bounds([segment.bounds for segment in self.segments])


def _number(value: object, label: str, *, positive: bool = False) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label} must be a finite number")
    try:
        result = float(value)
    except (OverflowError, ValueError) as error:
        raise ValueError(f"{label} must be a finite number") from error
    if not math.isfinite(result) or (positive and result <= 0):
        raise ValueError(f"{label} must be a finite {'positive ' if positive else ''}number")
    if abs(result) > MAX_COORDINATE:
        raise _NeedsReview(f"{label} exceeds the supported numeric range (+/-{MAX_COORDINATE:g})")
    return result


def _point(value: object) -> Point:
    if not isinstance(value, (tuple, list)) or len(value) != 2:
        raise ValueError("Each normalized command point must contain two coordinates")
    return (_number(value[0], "x coordinate"), _number(value[1], "y coordinate"))


def _cross(a: Point, b: Point) -> float:
    return a[0] * b[1] - a[1] * b[0]


def _subtract(a: Point, b: Point) -> Point:
    return (a[0] - b[0], a[1] - b[1])


def _midpoint(a: Point, b: Point) -> Point:
    return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)


def _guard(points: list[Point] | tuple[Point, ...], multiplier: int = 64) -> float:
    """Arithmetic guard, separate from the intentional flattening tolerance."""
    scale = max(1.0, *(abs(value) for point in points for value in point))
    return multiplier * math.ulp(scale)


def _orientation(a: Point, b: Point, c: Point) -> int:
    """Exact sign for binary floating-point inputs, with a fast safe filter."""
    ab = _subtract(b, a)
    ac = _subtract(c, a)
    left, right = ab[0] * ac[1], ab[1] * ac[0]
    determinant = left - right
    error = 8 * math.ulp(1.0) * (abs(left) + abs(right))
    if abs(determinant) > error:
        return 1 if determinant > 0 else -1
    ax, ay, bx, by, cx, cy = map(Fraction, (*a, *b, *c))
    exact = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
    return (exact > 0) - (exact < 0)


def _on_segment(point: Point, a: Point, b: Point) -> bool:
    return (min(a[0], b[0]) <= point[0] <= max(a[0], b[0])
            and min(a[1], b[1]) <= point[1] <= max(a[1], b[1])
            and _orientation(a, b, point) == 0)


def _intersection(a: Point, b: Point, c: Point, d: Point) -> Point | None:
    """A proof of straight-segment contact, never an epsilon-based merge."""
    if (max(a[0], b[0]) < min(c[0], d[0]) or max(c[0], d[0]) < min(a[0], b[0])
            or max(a[1], b[1]) < min(c[1], d[1]) or max(c[1], d[1]) < min(a[1], b[1])):
        return None
    first, second = _orientation(a, b, c), _orientation(a, b, d)
    third, fourth = _orientation(c, d, a), _orientation(c, d, b)
    for sign, point, begin, end in ((first, c, a, b), (second, d, a, b),
                                     (third, a, c, d), (fourth, b, c, d)):
        if sign == 0 and _on_segment(point, begin, end):
            return point
    if first * second >= 0 or third * fourth >= 0:
        return None
    # Exact parameter arithmetic avoids unstable near-parallel intersection
    # coordinates. Classification was already proved by orientation signs.
    ax, ay, bx, by, cx, cy, dx, dy = map(Fraction, (*a, *b, *c, *d))
    denominator = (bx - ax) * (dy - cy) - (by - ay) * (dx - cx)
    parameter = ((cx - ax) * (dy - cy) - (cy - ay) * (dx - cx)) / denominator
    return (float(ax + parameter * (bx - ax)), float(ay + parameter * (by - ay)))


def _point_segment(point: Point, a: Point, b: Point) -> tuple[float, Point]:
    dx, dy = b[0] - a[0], b[1] - a[1]
    squared = dx * dx + dy * dy
    if not squared:
        return math.dist(point, a), a
    fraction = max(0.0, min(1.0, ((point[0] - a[0]) * dx + (point[1] - a[1]) * dy) / squared))
    nearest = (a[0] + fraction * dx, a[1] + fraction * dy)
    return math.dist(point, nearest), nearest


def _segment_distance(first: _Segment, second: _Segment) -> tuple[float, Point, Point]:
    crossing = _intersection(first.a, first.b, second.a, second.b)
    if crossing is not None:
        return 0.0, crossing, crossing
    candidates = []
    for point in (first.a, first.b):
        distance, nearest = _point_segment(point, second.a, second.b)
        candidates.append((distance, point, nearest))
    for point in (second.a, second.b):
        distance, nearest = _point_segment(point, first.a, first.b)
        candidates.append((distance, nearest, point))
    return min(candidates, key=lambda item: item[0])


def _exact_point_segment(point: Point, a: Point, b: Point) -> tuple[Fraction, Point]:
    px, py, ax, ay, bx, by = map(Fraction, (*point, *a, *b))
    dx, dy = bx - ax, by - ay
    squared = dx * dx + dy * dy
    fraction = Fraction(0) if not squared else max(Fraction(0), min(Fraction(1), ((px - ax) * dx + (py - ay) * dy) / squared))
    x, y = ax + fraction * dx, ay + fraction * dy
    return (px - x) ** 2 + (py - y) ** 2, (float(x), float(y))


def _exact_segment_distance(first: _Segment, second: _Segment) -> tuple[Fraction, Point, Point]:
    crossing = _intersection(first.a, first.b, second.a, second.b)
    if crossing is not None:
        return Fraction(0), crossing, crossing
    candidates = []
    for point in (first.a, first.b):
        squared, nearest = _exact_point_segment(point, second.a, second.b)
        candidates.append((squared, point, nearest))
    for point in (second.a, second.b):
        squared, nearest = _exact_point_segment(point, first.a, first.b)
        candidates.append((squared, nearest, point))
    return min(candidates, key=lambda item: item[0])


def _sqrt_interval(squared: Fraction) -> tuple[float, float, float]:
    """Tight enclosing floats for the square root of an exact squared distance."""
    if not squared:
        return 0.0, 0.0, 0.0
    # Converting the squared value directly to float can underflow even when
    # its square root is representable (e.g. a 1e-200 line separation). Scale
    # the rational into [approximately 1, 4] before taking the square root.
    exponent = squared.numerator.bit_length() - squared.denominator.bit_length()
    exponent -= exponent % 2
    scaled = squared / (1 << exponent) if exponent >= 0 else squared * (1 << -exponent)
    estimate = math.ldexp(math.sqrt(float(scaled)), exponent // 2)
    exact = Fraction(estimate) ** 2
    if exact == squared:
        return estimate, estimate, estimate
    lower = upper = estimate
    for _ in range(8):
        if Fraction(lower) ** 2 <= squared and Fraction(upper) ** 2 >= squared:
            break
        if Fraction(lower) ** 2 > squared:
            lower = math.nextafter(lower, -math.inf)
        if Fraction(upper) ** 2 < squared:
            upper = math.nextafter(upper, math.inf)
    else:
        raise _NeedsReview("The exact squared distance could not be enclosed within the floating-point work limit")
    return estimate, lower, upper


def _union_bounds(bounds: list[Bounds]) -> Bounds:
    return (min(item[0] for item in bounds), min(item[1] for item in bounds),
            max(item[2] for item in bounds), max(item[3] for item in bounds))


def _bounds_lower(first: Bounds, second: Bounds) -> float:
    dx = max(0.0, first[0] - second[2], second[0] - first[2])
    dy = max(0.0, first[1] - second[3], second[1] - first[3])
    return max(0.0, math.hypot(dx, dy) - _guard(((first[0], first[1]), (first[2], first[3]),
                                               (second[0], second[1]), (second[2], second[3]))))


def _build_tree(segments: list[_Segment]) -> _Node:
    bounds = _union_bounds([segment.bounds for segment in segments])
    if len(segments) <= 8:
        return _Node(bounds, len(segments), segments=segments)
    axis = 0 if bounds[2] - bounds[0] >= bounds[3] - bounds[1] else 1
    ordered = sorted(segments, key=lambda segment: (segment.a[axis] + segment.b[axis]) / 2)
    middle = len(ordered) // 2
    return _Node(bounds, len(segments), left=_build_tree(ordered[:middle]), right=_build_tree(ordered[middle:]))


def _nearest(first: _Contour, second: _Contour, budget: _Budget) -> tuple[Fraction, Point, Point]:
    """Branch-and-bound over continuous chords; refine contenders exactly."""
    if first.tree is None:
        first.tree = _build_tree(first.segments)
    if second.tree is None:
        second.tree = _build_tree(second.segments)
    serial = itertools.count()
    queue = [(_bounds_lower(first.tree.bounds, second.tree.bounds), next(serial), first.tree, second.tree)]
    best_squared = None
    best_upper = math.inf
    nearest_points = None
    while queue:
        lower, _, left, right = heapq.heappop(queue)
        if lower > best_upper:
            continue
        if left.segments is not None and right.segments is not None:
            for one in left.segments:
                for two in right.segments:
                    if _bounds_lower(one.bounds, two.bounds) > best_upper:
                        continue
                    budget.use("distance_tests", MAX_DISTANCE_TESTS)
                    estimate, _, _ = _segment_distance(one, two)
                    if estimate - _guard((one.a, one.b, two.a, two.b), 128) > best_upper:
                        continue
                    squared, point_a, point_b = _exact_segment_distance(one, two)
                    if best_squared is None or squared < best_squared:
                        best_squared = squared
                        _, _, best_upper = _sqrt_interval(squared)
                        nearest_points = (point_a, point_b)
                        if not squared:
                            return squared, point_a, point_b
        else:
            if right.segments is not None or (left.segments is None and left.count >= right.count):
                children = ((left.left, right), (left.right, right))
            else:
                children = ((left, right.left), (left, right.right))
            for one, two in children:
                bound = _bounds_lower(one.bounds, two.bounds)
                if bound <= best_upper:
                    heapq.heappush(queue, (bound, next(serial), one, two))
    if best_squared is None or nearest_points is None:
        raise _NeedsReview("No continuous distance could be certified for a drawable contour pair")
    return best_squared, *nearest_points


def _add_segment(contour: _Contour, a: Point, b: Point, budget: _Budget,
                 *, error: float = 0.0, straight: bool = False) -> None:
    if not all(math.isfinite(value) and abs(value) <= MAX_COORDINATE for point in (a, b) for value in point):
        raise _NeedsReview("Flattened geometry exceeds the supported finite numeric range")
    if not math.isfinite(error) or error < 0:
        raise _NeedsReview("Could not establish a finite curve approximation bound")
    budget.use("segments", MAX_SEGMENTS)
    contour.segments.append(_Segment(a, b, error, straight))


def _bezier(contour: _Contour, points: list[Point], tolerance: float, budget: _Budget) -> None:
    # A Bézier is in its control hull. The convex capsule around the finite
    # endpoint chord contains that hull when it contains every control point.
    # Conversely the curve's continuous projection covers the entire chord.
    # Thus max control-point-to-segment distance is a two-sided Hausdorff bound.
    stack = [(points, 0, 0.0)]
    while stack:
        control, depth, roundoff = stack.pop()
        budget.use("adaptive_nodes", MAX_ADAPTIVE_NODES)
        guard = _guard(control)
        flatness = max((_point_segment(point, control[0], control[-1])[0] for point in control[1:-1]), default=0.0)
        bound = flatness + roundoff + guard
        if bound <= tolerance:
            _add_segment(contour, control[0], control[-1], budget, error=bound)
            continue
        if depth >= MAX_SUBDIVISION_DEPTH:
            raise _NeedsReview("Bézier subdivision depth exhausted before the requested error bound was reached")
        levels = [control]
        while len(levels[-1]) > 1:
            levels.append([_midpoint(a, b) for a, b in zip(levels[-1], levels[-1][1:])])
        left = [level[0] for level in levels]
        right = [level[-1] for level in reversed(levels)]
        # Every de Casteljau step is a convex combination. Past endpoint/control
        # error is not amplified; only this subdivision's rounding is added.
        next_roundoff = roundoff + guard
        stack.append((right, depth + 1, next_roundoff))
        stack.append((left, depth + 1, next_roundoff))


def _arc(contour: _Contour, begin: Point, end: Point, parameters: tuple,
         tolerance: float, budget: _Budget) -> None:
    rx, ry, rotation, large, sweep = parameters
    if begin == end:
        return
    if not rx or not ry:
        _add_segment(contour, begin, end, budget, straight=True)
        return
    # SVG endpoint-to-center conversion, expressed dimensionlessly to avoid
    # rx**2 * ry**2 overflow. Extremely ill-conditioned arcs need human review.
    phi = math.radians(rotation % 360)
    cosine, sine = math.cos(phi), math.sin(phi)
    dx, dy = (begin[0] - end[0]) / 2, (begin[1] - end[1]) / 2
    x = cosine * dx + sine * dy
    y = -sine * dx + cosine * dy
    radius_scale = math.hypot(x / rx, y / ry)
    if not math.isfinite(radius_scale) or radius_scale == 0:
        raise _NeedsReview("Arc radii/endpoints are too ill-conditioned to certify")
    if radius_scale > 1:
        rx, ry = rx * radius_scale, ry * radius_scale
    normalized_x, normalized_y = x / rx, y / ry
    squared = normalized_x * normalized_x + normalized_y * normalized_y
    if not math.isfinite(squared) or squared <= 0 or max(rx, ry) > MAX_COORDINATE:
        raise _NeedsReview("Corrected arc radii are outside the supported numeric range")
    sign = -1 if large == sweep else 1
    factor = sign * math.sqrt(max(0.0, (1.0 - squared) / squared))
    center_x = factor * rx * normalized_y
    center_y = -factor * ry * normalized_x
    cx = cosine * center_x - sine * center_y + (begin[0] + end[0]) / 2
    cy = sine * center_x + cosine * center_y + (begin[1] + end[1]) / 2
    u = ((x - center_x) / rx, (y - center_y) / ry)
    v = ((-x - center_x) / rx, (-y - center_y) / ry)
    start = math.atan2(u[1], u[0])
    delta = math.atan2(_cross(u, v), u[0] * v[0] + u[1] * v[1])
    if not sweep and delta > 0:
        delta -= 2 * math.pi
    if sweep and delta < 0:
        delta += 2 * math.pi
    if not math.isfinite(delta) or delta == 0:
        raise _NeedsReview("Arc angular span could not be certified")
    radius = max(rx, ry)
    # sqrt near a diametric arc is poorly conditioned. Give the reconstructed
    # ellipse an explicit guard that grows with that conditioning; never pretend
    # that an unbounded center conversion has the requested 0.001 accuracy.
    roundoff = 128 * math.ulp(max(1.0, abs(cx), abs(cy), radius))
    center_condition = radius / max(min(rx, ry), math.ulp(radius))
    roundoff *= max(1.0, center_condition)
    if squared < 1:
        roundoff += 16 * math.ulp(1.0) * radius / max(math.sqrt(1 - squared), math.ulp(1.0))
    else:
        # Radius correction chooses the diametric case. The actual correction
        # error is bounded by O(sqrt(machine epsilon)) in reconstructed center.
        roundoff += 8 * radius * math.sqrt(math.ulp(1.0))
    if roundoff >= tolerance:
        raise _NeedsReview("Arc center conversion uncertainty exceeds the requested approximation tolerance")

    def at(angle: float) -> Point:
        return (cx + rx * cosine * math.cos(angle) - ry * sine * math.sin(angle),
                cy + rx * sine * math.cos(angle) + ry * cosine * math.sin(angle))

    # Check endpoint reconstruction; replacing the computed endpoints by the
    # original endpoints adds at most their residual to the interpolation bound.
    roundoff += max(math.dist(at(start), begin), math.dist(at(start + delta), end))
    if roundoff >= tolerance:
        raise _NeedsReview("Arc endpoint reconstruction uncertainty exceeds the requested approximation tolerance")
    stack = [(start, start + delta, begin, end, 0)]
    while stack:
        low, high, a, b, depth = stack.pop()
        budget.use("adaptive_nodes", MAX_ADAPTIVE_NODES)
        # For p(theta) = center + R * (rx*cos(theta), ry*sin(theta)),
        # ||p''|| <= max(rx, ry); linear interpolation error <= M*h*h/8.
        bound = radius * (high - low) ** 2 / 8 + roundoff
        if bound <= tolerance:
            _add_segment(contour, a, b, budget, error=bound)
            continue
        if depth >= MAX_SUBDIVISION_DEPTH:
            raise _NeedsReview("Arc subdivision depth exhausted before the requested error bound was reached")
        middle = (low + high) / 2
        point = at(middle)
        stack.append((middle, high, point, b, depth + 1))
        stack.append((low, middle, a, point, depth + 1))


def _validated_commands(raw: object, budget: _Budget) -> list[Command]:
    if not isinstance(raw, list) or not raw:
        raise ValueError("Each resolved path needs a non-empty normalized commands list")
    commands = []
    counts = {"M": 1, "L": 1, "Q": 2, "C": 3, "A": 1, "Z": 0}
    for command in raw:
        budget.use("commands", MAX_COMMANDS)
        if not isinstance(command, Command) or command.type not in counts:
            raise ValueError("Expected normalized icon_geometry.Command objects (M/L/Q/C/A/Z)")
        if not isinstance(command.points, list) or len(command.points) != counts[command.type]:
            raise ValueError(f"Invalid normalized {command.type} command point count")
        points = [_point(point) for point in command.points]
        arc = None
        if command.type == "A":
            if not isinstance(command.arc, (tuple, list)) or len(command.arc) != 5:
                raise ValueError("Arc commands need rx, ry, rotation, large-arc and sweep parameters")
            rx, ry, rotation = (_number(value, "arc parameter") for value in command.arc[:3])
            large, sweep = command.arc[3:]
            if rx < 0 or ry < 0 or type(large) is not int or type(sweep) is not int or large not in (0, 1) or sweep not in (0, 1):
                raise ValueError("Arc radii must be non-negative and arc flags must be integer 0/1")
            arc = (rx, ry, rotation, large, sweep)
        elif command.arc is not None:
            raise ValueError("Only normalized A commands may carry arc parameters")
        commands.append(Command(command.type, points, arc))
    if commands[0].type != "M":
        raise ValueError("Each normalized path must begin with M")
    return commands


def _contours(paths: object, tolerance: float, budget: _Budget) -> list[_Contour]:
    if not isinstance(paths, list) or not paths:
        raise ValueError("Expected a non-empty list from icon_geometry.resolve_icon")
    contours = []
    identifiers = set()
    for path in paths:
        if not isinstance(path, dict):
            raise ValueError("Each resolved path must be an object")
        element_id = path.get("elementId", path.get("id"))
        if not isinstance(element_id, str) or not element_id or element_id in identifiers:
            raise ValueError("Each resolved path needs a unique non-empty elementId")
        identifiers.add(element_id)
        commands = _validated_commands(path.get("commands"), budget)
        chunks = []
        for command in commands:
            if command.type == "M":
                chunks.append([])
            chunks[-1].append(command)
        for index, chunk in enumerate(chunks, 1):
            contour = _Contour(f"{element_id}:subpath-{index}", element_id, index, chunk)
            cursor = start = chunk[0].points[0]
            for command in chunk[1:]:
                if command.type == "Z":
                    if contour.segments:
                        _add_segment(contour, cursor, start, budget, straight=True)
                        contour.endpoints.update((cursor, start))
                    cursor = start
                    continue
                end = command.points[-1]
                if command.type == "L":
                    _add_segment(contour, cursor, end, budget, straight=True)
                elif command.type in ("Q", "C"):
                    contour.has_curves = True
                    _bezier(contour, [cursor, *command.points], tolerance, budget)
                elif command.type == "A":
                    if cursor != end:
                        contour.has_curves = contour.has_curves or bool(command.arc[0] and command.arc[1])
                        _arc(contour, cursor, end, command.arc, tolerance, budget)
                    else:
                        cursor = end
                        continue
                else:
                    raise ValueError(f"Unexpected command {command.type} inside a subpath")
                contour.endpoints.update((cursor, end))
                cursor = end
            if contour.segments:
                contours.append(contour)
                if len(contours) > MAX_CONTOURS:
                    raise _NeedsReview(f"Contour limit exceeded ({MAX_CONTOURS}); no spacing pass can be certified")
    if not contours:
        raise ValueError("No drawable contours: lone movetos and coincident-endpoint arcs do not count")
    return contours


def _path_data(commands: list[Command]) -> str:
    """Keep geometry precision in overlays; the shared writer rounds to 4 dp."""
    def number(value: float) -> str:
        return "0" if value == 0 else format(value, ".17g")
    result = []
    for command in commands:
        if command.type == "Z":
            result.append("Z")
            continue
        points = " ".join(number(value) for point in command.points for value in point)
        if command.type == "A":
            params = " ".join(number(value) for value in command.arc)
            result.append(f"A {params} {points}")
        else:
            result.append(f"{command.type} {points}")
    return " ".join(result)


def _connection(first: _Contour, second: _Contour, budget: _Budget) -> dict | None:
    shared = first.endpoints & second.endpoints
    if shared:
        return {"reason": "shared original drawn-command endpoint", "point": list(min(shared))}
    if _bounds_lower(first.bounds, second.bounds) > first.error + second.error:
        return None
    straight_a = [segment for segment in first.segments if segment.original_straight]
    straight_b = [segment for segment in second.segments if segment.original_straight]
    for one in straight_a:
        for two in straight_b:
            if _bounds_lower(one.bounds, two.bounds) > 0:
                continue
            budget.use("connection_tests", MAX_CONNECTION_TESTS)
            intersection = _intersection(one.a, one.b, two.a, two.b)
            if intersection is not None:
                return {"reason": "exact original straight-segment intersection", "point": list(intersection)}
    return None


def _pair(first: _Contour, second: _Contour, minimum: float, stroke: float, budget: _Budget) -> dict:
    squared, point_a, point_b = _nearest(first, second, budget)
    distance, lower, upper = _sqrt_interval(squared)
    error = first.error + second.error
    lower = max(0.0, math.nextafter(lower - error, -math.inf)) if error else lower
    upper = math.nextafter(upper + error, math.inf) if error else upper
    ambiguous_contact = bool(first.has_curves or second.has_curves) and lower == 0
    if ambiguous_contact:
        status = "review"
        reason = "Possible curve-interior contact is not a proved centerline connection; inspect/redesign before accepting."
    elif not error:
        status = "pass" if squared >= Fraction(minimum) ** 2 else "fail"
        reason = "Exact straight-segment spacing meets the minimum." if status == "pass" else "Exact straight-segment spacing is below the minimum."
    elif lower >= minimum:
        status, reason = "pass", "The conservative distance lower bound meets the minimum."
    elif upper < minimum:
        status, reason = "fail", "Even the conservative distance upper bound is below the minimum."
    else:
        status, reason = "review", "The curve distance interval crosses the minimum; refine the drawing or request a tighter certified check."
    return {
        "closestContours": [first.identifier, second.identifier],
        "centerlineDistance": distance,
        "inkClearance": max(0.0, distance - stroke),
        "signedInkClearance": distance - stroke,
        "lowerBound": lower,
        "upperBound": upper,
        "inkClearanceLowerBound": max(0.0, lower - stroke),
        "inkClearanceUpperBound": max(0.0, upper - stroke),
        "approximationError": error,
        "nearestPoints": [list(point_a), list(point_b)],
        "requiredCenterline": minimum,
        "requiredInkClearance": max(0.0, minimum - stroke),
        "status": status,
        "reason": reason,
        "ambiguousContact": ambiguous_contact,
    }


def analyze_paths(paths: list[dict], *, minimum_distance: float = 8.0,
                  stroke_width: float = 4.0, tolerance: float = 0.001) -> dict:
    """Return a JSON-safe PASS/FAIL/REVIEW verdict for disconnected components.

    ``tolerance`` bounds each contour's polyline error, not permission to violate
    the minimum. Every component pair is checked; pairs within a demonstrably
    connected component are explicitly excluded. Invalid inputs FAIL; exhausted
    numerical/work bounds REVIEW. Both are non-passing (``ok`` is false).
    """
    budget = _Budget()
    report = {"ok": False, "status": "fail", "contours": [], "components": [], "pairs": [],
              "connectedPairs": [], "excludedPairs": [], "errors": []}
    try:
        minimum = _number(minimum_distance, "minimum_distance", positive=True)
        stroke = _number(stroke_width, "stroke_width", positive=True)
        requested_tolerance = _number(tolerance, "tolerance", positive=True)
        report.update({
            "requiredCenterline": minimum,
            "requiredInkClearance": max(0.0, minimum - stroke),
            "strokeWidth": stroke,
            "tolerance": requested_tolerance,
            "measurement": {
                "method": "continuous segment distance with adaptive curve Hausdorff bounds",
                "nearestPoints": "points on the bounded polyline approximation; exact for original straight segments",
                "connections": "shared original drawn endpoints or exact original straight intersections only; never ink contact",
                "scope": "disconnected centerline components, not spacing inside a connected component",
            },
        })
        contours = _contours(paths, requested_tolerance, budget)
        parents = list(range(len(contours)))

        def root(index: int) -> int:
            while parents[index] != index:
                parents[index] = parents[parents[index]]
                index = parents[index]
            return index

        direct = {}
        for i, first in enumerate(contours):
            for j in range(i + 1, len(contours)):
                second = contours[j]
                connection = _connection(first, second, budget)
                if connection is not None:
                    first_root, second_root = root(i), root(j)
                    parents[max(first_root, second_root)] = min(first_root, second_root)
                    evidence = {"contourIds": [first.identifier, second.identifier], **connection}
                    direct[(i, j)] = evidence
                    report["connectedPairs"].append(evidence)

        groups = {}
        for index in range(len(contours)):
            groups.setdefault(root(index), []).append(index)
        members = list(groups.values())
        for index, group in enumerate(members, 1):
            component_id = f"component-{index}"
            contour_ids = [contours[member].identifier for member in group]
            for member in group:
                contours[member].component_id = component_id
            report["components"].append({
                "id": component_id,
                "memberIds": contour_ids,
                "contourIds": list(contour_ids),
                "elementIds": list(dict.fromkeys(contours[member].element_id for member in group)),
                "bounds": list(_union_bounds([contours[member].bounds for member in group])),
            })
        report["contours"] = [{
            "id": contour.identifier,
            "elementId": contour.element_id,
            "subpathIndex": contour.subpath_index,
            "componentId": contour.component_id,
            "pathData": _path_data(contour.commands),
            "bounds": list(contour.bounds),
            "segmentCount": len(contour.segments),
            "approximationError": contour.error,
            "hasCurves": contour.has_curves,
        } for contour in contours]
        for group in members:
            for position, first in enumerate(group):
                for second in group[position + 1:]:
                    report["excludedPairs"].append({
                        "contourIds": [contours[first].identifier, contours[second].identifier],
                        "componentId": contours[first].component_id,
                        "reason": "same proved connected centerline component",
                        "directConnection": direct.get((first, second)),
                    })

        for first_index, first_group in enumerate(members):
            for second_index in range(first_index + 1, len(members)):
                second_group = members[second_index]
                distances = [_pair(contours[first], contours[second], minimum, stroke, budget)
                             for first in first_group for second in second_group]
                nearest = min(distances, key=lambda row: row["centerlineDistance"])
                lower = min(row["lowerBound"] for row in distances)
                upper = min(row["upperBound"] for row in distances)
                ambiguous = any(row["ambiguousContact"] for row in distances)
                if ambiguous:
                    status, reason = "review", "A possible curved connection between these components is not proved; do not silently merge or approve them."
                elif any(row["status"] == "fail" for row in distances):
                    status, reason = "fail", "At least one disconnected contour pair is provably closer than the required minimum."
                elif any(row["status"] == "review" for row in distances):
                    status, reason = "review", "The conservative curve distance interval crosses the required minimum."
                else:
                    status, reason = "pass", "Every contour pair between these components meets the required minimum."
                pair = {**nearest,
                        "componentIds": [f"component-{first_index + 1}", f"component-{second_index + 1}"],
                        "memberIds": [[contours[member].identifier for member in group] for group in (first_group, second_group)],
                        "lowerBound": lower, "upperBound": upper,
                        "approximationError": max(nearest["approximationError"], nearest["centerlineDistance"] - lower,
                                                  upper - nearest["centerlineDistance"]),
                        "inkClearanceLowerBound": max(0.0, lower - stroke),
                        "inkClearanceUpperBound": max(0.0, upper - stroke),
                        "status": status, "reason": reason, "ambiguousContact": ambiguous,
                        "contourPairs": distances}
                report["pairs"].append(pair)
        statuses = {pair["status"] for pair in report["pairs"]}
        report["status"] = "fail" if "fail" in statuses else "review" if "review" in statuses else "pass"
        report["ok"] = report["status"] == "pass"
        report["minimumCenterlineDistance"] = min((row["centerlineDistance"] for row in report["pairs"]), default=None)
        report["minimumInkClearance"] = min((row["inkClearance"] for row in report["pairs"]), default=None)
        report["errors"] = [f"{' / '.join(row['componentIds'])}: {row['reason']}" for row in report["pairs"] if row["status"] != "pass"]
        report["reason"] = ("No disconnected centerline components to compare." if not report["pairs"] else
                            "All disconnected components meet the required spacing." if report["ok"] else
                            "Disconnected spacing needs repair or review; this result is not a pass.")
    except _NeedsReview as error:
        report.update(ok=False, status="review", errors=[str(error)], reason=str(error))
    except (ValueError, TypeError, OverflowError, ZeroDivisionError, ArithmeticError) as error:
        report.update(ok=False, status="fail", errors=[str(error)], reason=str(error))
    report["stats"] = {"commands": budget.commands, "flattenedSegments": budget.segments,
                       "adaptiveNodes": budget.adaptive_nodes, "distanceTests": budget.distance_tests,
                       "connectionTests": budget.connection_tests}
    return report
