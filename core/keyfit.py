#!/usr/bin/env python3
"""Canonical centered keyshapes for the 48-unit design canvas.

The keyshape is the icon's painted padding boundary. Every finished icon must
exactly reach one centered target and remain inside it:

* circle: 44u diameter, 2u cardinal padding;
* square: 40x40u, 4u padding on every side;
* portrait: 36x44u, 6u side padding and 2u end padding;
* landscape: 44x36u, 2u side padding and 6u end padding.

This module is shared by declared-geometry and rasterized-paint validation so
the token names, bounds, and containment rules cannot drift.
"""

from __future__ import annotations

import math

DESIGN_CANVAS = 48.0
SHIP_CANVAS = 24.0
REGULAR_STROKE = 4.0
CENTER = DESIGN_CANVAS / 2.0
CENTERLINE_INSET = REGULAR_STROKE / 2.0

# Retained as the absolute painted maximum and for compatibility with callers.
KEYFIT_MAJOR = 44.0
CIRCLE_DIAMETER = 44.0
SQUARE_SIZE = 40.0
PORTRAIT_SIZE = (36.0, 44.0)
LANDSCAPE_SIZE = (44.0, 36.0)


def token_box(width: float, height: float) -> tuple[float, float, float, float]:
    """Centered design-space bounds ``(left, top, right, bottom)``."""
    left = (DESIGN_CANVAS - width) / 2.0
    top = (DESIGN_CANVAS - height) / 2.0
    return left, top, left + width, top + height


def canonical_tokens() -> list[dict]:
    """The four canonical painted keyshape targets, in specification order."""
    return [
        {"name": "circle-44", "orientation": "circle", "shape": "circle", "width": CIRCLE_DIAMETER, "height": CIRCLE_DIAMETER, "diameter": CIRCLE_DIAMETER},
        {"name": "square-40", "orientation": "square", "shape": "rect", "width": SQUARE_SIZE, "height": SQUARE_SIZE},
        {"name": "portrait-36x44", "orientation": "portrait", "shape": "rect", "width": PORTRAIT_SIZE[0], "height": PORTRAIT_SIZE[1]},
        {"name": "landscape-44x36", "orientation": "landscape", "shape": "rect", "width": LANDSCAPE_SIZE[0], "height": LANDSCAPE_SIZE[1]},
    ]


def token_named(name: str) -> dict | None:
    return next((item for item in canonical_tokens() if item["name"] == name), None)


def allowed_sizes() -> tuple[tuple[float, float], ...]:
    return tuple((item["width"], item["height"]) for item in canonical_tokens())


def candidate_tokens(
    bounds: tuple[float, float, float, float], allow_circle: bool = True
) -> list[dict]:
    """Semantically plausible targets for the painted box.

    Raster callers set ``allow_circle`` only after detecting a dominant large
    circular silhouette. Rectangular bounds alone cannot prove a circle.
    """
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    tokens = {item["name"]: item for item in canonical_tokens()}
    isotropic = [tokens["square-40"]]
    if allow_circle:
        isotropic.append(tokens["circle-44"])
    if abs(width - height) <= 0.25:
        return isotropic
    if width > height:
        return [tokens["landscape-44x36"], *isotropic]
    return [tokens["portrait-36x44"], *isotropic]


def contains(outer: tuple[float, float, float, float], inner: tuple[float, float, float, float], tolerance: float = 0.0) -> bool:
    return inner[0] >= outer[0] - tolerance and inner[1] >= outer[1] - tolerance and inner[2] <= outer[2] + tolerance and inner[3] <= outer[3] + tolerance


def matches(target: tuple[float, float, float, float], actual: tuple[float, float, float, float], tolerance: float = 0.0) -> bool:
    return all(abs(expected - measured) <= tolerance for expected, measured in zip(target, actual))


def circle_overflow(points: list[tuple[float, float]], stroke_width: float = 0.0) -> float:
    """Positive radial overflow beyond the 44u circle keyshape."""
    if not points:
        return 0.0
    allowed_radius = CIRCLE_DIAMETER / 2.0 - stroke_width / 2.0
    return max(math.hypot(x - CENTER, y - CENTER) - allowed_radius for x, y in points)


def nearest(
    bounds: tuple[float, float, float, float], allow_circle: bool = True
) -> dict:
    """Diagnostic target selected by edge distance, then area difference."""
    def scored(item: dict) -> tuple[float, float]:
        box = token_box(item["width"], item["height"])
        distance = sum(abs(expected - measured) for expected, measured in zip(box, bounds))
        area_delta = abs(item["width"] * item["height"] - (bounds[2] - bounds[0]) * (bounds[3] - bounds[1]))
        return distance, area_delta

    candidates = candidate_tokens(bounds, allow_circle)
    containing = [item for item in candidates if contains(token_box(item["width"], item["height"]), bounds)]
    item = min(containing or candidates, key=scored)
    box = token_box(item["width"], item["height"])
    return {
        **item,
        "bounds": list(box),
        "edgeDeltaToTarget": {
            "left": bounds[0] - box[0], "top": bounds[1] - box[1],
            "right": box[2] - bounds[2], "bottom": box[3] - bounds[3],
        },
    }


def assign(
    bounds: tuple[float, float, float, float],
    tolerance: float = 0.0,
    allow_circle: bool = True,
) -> dict | None:
    """The canonical centered target whose rectangular bounds are matched."""
    for item in candidate_tokens(bounds, allow_circle):
        box = token_box(item["width"], item["height"])
        if matches(box, bounds, tolerance):
            return {**item, "bounds": list(box)}
    return None


def max_box() -> tuple[float, float, float, float]:
    return token_box(CIRCLE_DIAMETER, CIRCLE_DIAMETER)


def describe() -> str:
    return "circle 44u diameter, square 40x40u, portrait 36x44u, and landscape 44x36u"
