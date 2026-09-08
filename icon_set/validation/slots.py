"""Distance from authored geometry to a protected rectangular slot.

A protected slot is a filled region, not a boundary: a container's ink must stay
out of it entirely, so the measurement wanted is the distance from a centerline
to the *filled* rectangle, which is zero anywhere inside. Painted ink enters the
slot exactly when that distance drops below the envelope radius.

Distance to a filled axis-aligned rectangle is convex, and a straight segment is
convex, so the minimum along a segment is found exactly by ternary search.
An arc is not convex in its parameter, so it is scanned and then refined — the
same treatment :mod:`icon_set.validation.envelope` already gives a general
ellipse, and the reason the MIC engine, which is exact for straight geometry and
rigorously bounded for curves, remains the authority on part-to-part clearance.
"""

from __future__ import annotations

import math

from ..model.primitives import Arc, Line, Point, Primitive
from ..model.profiles import ENVELOPE_RADIUS
from .envelope import arc_geometry

Rect = tuple[float, float, float, float]

#: Parameter samples per arc before local refinement.
ARC_SAMPLES = 720


def point_to_rect(x: float, y: float, rect: Rect) -> float:
    """Distance from a point to a filled rectangle; zero when inside."""
    left, top, right, bottom = rect
    dx = max(left - x, 0.0, x - right)
    dy = max(top - y, 0.0, y - bottom)
    return math.hypot(dx, dy)


def point_in_rect(x: float, y: float, rect: Rect, margin: float = 0.0) -> bool:
    left, top, right, bottom = rect
    return (
        left - margin <= x <= right + margin
        and top - margin <= y <= bottom + margin
    )


def _refine(evaluate, low: float, high: float, iterations: int = 80) -> float:
    """Ternary search for the minimum of a unimodal function on [low, high]."""
    for _ in range(iterations):
        third = (high - low) / 3.0
        a, b = low + third, high - third
        if evaluate(a) < evaluate(b):
            high = b
        else:
            low = a
    return evaluate((low + high) / 2.0)


def _segment_to_rect(start: Point, end: Point, rect: Rect) -> float:
    x1, y1 = float(start.x), float(start.y)
    x2, y2 = float(end.x), float(end.y)
    if (x1, y1) == (x2, y2):
        return point_to_rect(x1, y1, rect)

    def at(t: float) -> float:
        return point_to_rect(x1 + (x2 - x1) * t, y1 + (y2 - y1) * t, rect)

    return min(at(0.0), at(1.0), _refine(at, 0.0, 1.0))


def _arc_to_rect(arc: Arc, rect: Rect) -> float:
    geometry = arc_geometry(arc)

    def at(t: float) -> float:
        angle = geometry.start_angle + geometry.delta_angle * t
        x, y = geometry.point(angle)
        return point_to_rect(x, y, rect)

    samples = [(at(i / ARC_SAMPLES), i / ARC_SAMPLES) for i in range(ARC_SAMPLES + 1)]
    best, index = min((value, i) for i, (value, _) in enumerate(samples))
    step = 1.0 / ARC_SAMPLES
    low = max(0.0, samples[index][1] - step)
    high = min(1.0, samples[index][1] + step)
    return min(best, _refine(at, low, high))


def distance_to_rect(primitive: Primitive, rect: Rect) -> float:
    """Minimum distance from one primitive's centerline to a filled rectangle."""
    if isinstance(primitive, Line):
        return _segment_to_rect(primitive.start, primitive.end, rect)
    if isinstance(primitive, Arc):
        return _arc_to_rect(primitive, rect)
    raise TypeError(f"unsupported primitive: {type(primitive).__name__}")


def intrusions(
    primitives: list[Primitive],
    rect: Rect,
    *,
    radius: float = ENVELOPE_RADIUS,
) -> list[tuple[str, float]]:
    """Primitives whose painted ink reaches into ``rect``, with the distance."""
    found = []
    for primitive in primitives:
        distance = distance_to_rect(primitive, rect)
        if distance < radius:
            found.append((primitive.element_id, distance))
    return found


def grow(rect: Rect, amount: float) -> Rect:
    left, top, right, bottom = rect
    return (left - amount, top - amount, right + amount, bottom + amount)
