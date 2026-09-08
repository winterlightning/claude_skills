"""Exact painted-ink envelope for authored geometry.

Every cap and every join in this profile is round, so the painted region is
exactly the Minkowski sum of the centerline with a disc of radius
``stroke / 2``. Two consequences the validator relies on:

* the visible bounding box is the centerline bounding box grown by that radius
  on all four sides, exactly; and
* the visible radial extent about a point is the centerline radial extent plus
  that radius, exactly.

So the work here is finding true centerline extrema. Straight segments are
their endpoints. An elliptical arc additionally reaches an axis extremum
wherever its parameter sweep crosses one, and reaches its farthest-from-centre
point wherever the sweep crosses the outward radial direction; both are solved
in closed form rather than sampled.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from ..model.primitives import Arc, Line, Primitive
from ..model.profiles import ENVELOPE_RADIUS

Bounds = tuple[float, float, float, float]


@dataclass(frozen=True)
class ArcGeometry:
    """Centre parameterization of an SVG endpoint arc."""

    center_x: float
    center_y: float
    radius_x: float
    radius_y: float
    start_angle: float
    delta_angle: float

    def point(self, angle: float) -> tuple[float, float]:
        return (
            self.center_x + self.radius_x * math.cos(angle),
            self.center_y + self.radius_y * math.sin(angle),
        )

    def contains_angle(self, angle: float) -> bool:
        """True when ``angle`` lies on the drawn sweep."""
        if self.delta_angle >= 0:
            offset = (angle - self.start_angle) % (2 * math.pi)
            return offset <= self.delta_angle + 1e-12
        offset = (self.start_angle - angle) % (2 * math.pi)
        return offset <= -self.delta_angle + 1e-12


class DegenerateArcError(ValueError):
    """The arc's radii cannot span its endpoints even after correction."""


def arc_geometry(arc: Arc) -> ArcGeometry:
    """Endpoint-to-centre conversion following the SVG implementation notes."""
    x1, y1 = float(arc.start.x), float(arc.start.y)
    x2, y2 = float(arc.end.x), float(arc.end.y)
    rx, ry = abs(float(arc.radius_x)), abs(float(arc.radius_y))
    if rx == 0 or ry == 0:
        raise DegenerateArcError(
            f"{arc.element_id}: an arc needs non-zero radii; a straight run must be a line"
        )
    if x1 == x2 and y1 == y2:
        raise DegenerateArcError(
            f"{arc.element_id}: coincident endpoints draw nothing"
        )
    dx2, dy2 = (x1 - x2) / 2.0, (y1 - y2) / 2.0
    lam = (dx2 * dx2) / (rx * rx) + (dy2 * dy2) / (ry * ry)
    if lam > 1.0:
        scale = math.sqrt(lam)
        rx *= scale
        ry *= scale
    numerator = rx * rx * ry * ry - rx * rx * dy2 * dy2 - ry * ry * dx2 * dx2
    denominator = rx * rx * dy2 * dy2 + ry * ry * dx2 * dx2
    factor = math.sqrt(max(0.0, numerator / denominator)) if denominator else 0.0
    if bool(arc.large_arc) == bool(arc.sweep):
        factor = -factor
    cxp = factor * rx * dy2 / ry
    cyp = -factor * ry * dx2 / rx
    cx = cxp + (x1 + x2) / 2.0
    cy = cyp + (y1 + y2) / 2.0
    start = math.atan2((y1 - cy) / ry, (x1 - cx) / rx)
    end = math.atan2((y2 - cy) / ry, (x2 - cx) / rx)
    delta = end - start
    if arc.sweep and delta < 0:
        delta += 2 * math.pi
    elif not arc.sweep and delta > 0:
        delta -= 2 * math.pi
    return ArcGeometry(cx, cy, rx, ry, start, delta)


def centerline_points(primitive: Primitive) -> list[tuple[float, float]]:
    """Endpoints plus every interior axis extremum of one primitive."""
    points = [
        (float(primitive.start.x), float(primitive.start.y)),
        (float(primitive.end.x), float(primitive.end.y)),
    ]
    if isinstance(primitive, Line):
        return points
    geometry = arc_geometry(primitive)
    # An axis-aligned ellipse reaches its x extrema at 0 and pi, its y extrema
    # at pi/2 and 3pi/2. Include only those the sweep actually crosses.
    for angle in (0.0, math.pi / 2, math.pi, 3 * math.pi / 2):
        if geometry.contains_angle(angle):
            points.append(geometry.point(angle))
    return points


def centerline_bounds(primitives: list[Primitive]) -> Bounds:
    points: list[tuple[float, float]] = []
    for primitive in primitives:
        points.extend(centerline_points(primitive))
    if not points:
        raise ValueError("no geometry to measure")
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    return (min(xs), min(ys), max(xs), max(ys))


def visible_bounds(primitives: list[Primitive], radius: float = ENVELOPE_RADIUS) -> Bounds:
    """Painted bounds: the centerline box grown by the envelope radius."""
    left, top, right, bottom = centerline_bounds(primitives)
    return (left - radius, top - radius, right + radius, bottom + radius)


def _radial_extent(primitive: Primitive, center: tuple[float, float]) -> float:
    cx, cy = center
    best = max(
        math.hypot(point[0] - cx, point[1] - cy)
        for point in (
            (float(primitive.start.x), float(primitive.start.y)),
            (float(primitive.end.x), float(primitive.end.y)),
        )
    )
    if isinstance(primitive, Line):
        return best
    geometry = arc_geometry(primitive)
    if abs(geometry.radius_x - geometry.radius_y) < 1e-12:
        # Circular arc: the farthest point from `center` lies on the ray from
        # the arc centre through `center`, if the sweep reaches that direction.
        dx, dy = geometry.center_x - cx, geometry.center_y - cy
        distance = math.hypot(dx, dy)
        if distance < 1e-12:
            return max(best, geometry.radius_x)
        angle = math.atan2(dy, dx)
        if geometry.contains_angle(angle):
            best = max(best, distance + geometry.radius_x)
        return best
    # General ellipse: solve d/dt of the squared distance numerically over the
    # sweep. The extrema of a quartic in cos/sin are few; a dense parameter
    # scan refined by ternary search is exact to well under the grid.
    steps = 720
    for index in range(steps + 1):
        angle = geometry.start_angle + geometry.delta_angle * index / steps
        px, py = geometry.point(angle)
        best = max(best, math.hypot(px - cx, py - cy))
    return best


def centerline_radial_extent(
    primitives: list[Primitive],
    center: tuple[float, float],
) -> float:
    if not primitives:
        raise ValueError("no geometry to measure")
    return max(_radial_extent(primitive, center) for primitive in primitives)


def visible_radial_extent(
    primitives: list[Primitive],
    center: tuple[float, float],
    radius: float = ENVELOPE_RADIUS,
) -> float:
    """Painted radial extent: centerline extent plus the envelope radius."""
    return centerline_radial_extent(primitives, center) + radius
