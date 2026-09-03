#!/usr/bin/env python3
"""Canonical centered painted-keyshape helpers for every icon profile.

The normal defaults and exported constants are retained for older callers.
Pass ``icon_type="sub"`` for the 32u/16px sub-icon profile or
``icon_type="container"`` for the dedicated 64u/32px container profile.
"""

from __future__ import annotations

import math

from icon_profiles import (
    DEFAULT_ICON_TYPE,
    canonical_tokens as profile_tokens,
    get_profile,
)


_NORMAL = get_profile(DEFAULT_ICON_TYPE)
DESIGN_CANVAS = float(_NORMAL["designCanvas"])
SHIP_CANVAS = float(_NORMAL["shipCanvas"])
REGULAR_STROKE = float(_NORMAL["designStroke"])
CENTER = float(_NORMAL["center"]["x"])
CENTERLINE_INSET = REGULAR_STROKE / 2.0

# Retained for compatibility with normal-profile callers.
_NORMAL_BY_ORIENTATION = {
    item["orientation"]: item for item in profile_tokens(DEFAULT_ICON_TYPE)
}
KEYFIT_MAJOR = float(_NORMAL_BY_ORIENTATION["circle"]["width"])
CIRCLE_DIAMETER = KEYFIT_MAJOR
SQUARE_SIZE = float(_NORMAL_BY_ORIENTATION["square"]["width"])
PORTRAIT_SIZE = (
    float(_NORMAL_BY_ORIENTATION["portrait"]["width"]),
    float(_NORMAL_BY_ORIENTATION["portrait"]["height"]),
)
LANDSCAPE_SIZE = (
    float(_NORMAL_BY_ORIENTATION["landscape"]["width"]),
    float(_NORMAL_BY_ORIENTATION["landscape"]["height"]),
)


def token_box(
    width: float, height: float, icon_type: str = DEFAULT_ICON_TYPE
) -> tuple[float, float, float, float]:
    """Centered design-space bounds ``(left, top, right, bottom)``."""
    center = get_profile(icon_type)["center"]
    left = float(center["x"]) - width / 2.0
    top = float(center["y"]) - height / 2.0
    return left, top, left + width, top + height


def canonical_tokens(icon_type: str = DEFAULT_ICON_TYPE) -> list[dict]:
    """Canonical painted targets in specification order."""
    return profile_tokens(icon_type)


def token_named(name: str, icon_type: str = DEFAULT_ICON_TYPE) -> dict | None:
    return next(
        (item for item in canonical_tokens(icon_type) if item["name"] == name),
        None,
    )


def allowed_sizes(icon_type: str = DEFAULT_ICON_TYPE) -> tuple[tuple[float, float], ...]:
    return tuple(
        (item["width"], item["height"])
        for item in canonical_tokens(icon_type)
    )


def candidate_tokens(
    bounds: tuple[float, float, float, float],
    allow_circle: bool = True,
    icon_type: str = DEFAULT_ICON_TYPE,
) -> list[dict]:
    """Semantically plausible targets for the painted box."""
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    tokens = {
        item["orientation"]: item for item in canonical_tokens(icon_type)
    }
    isotropic = [tokens["square"]]
    if allow_circle:
        isotropic.append(tokens["circle"])
    if abs(width - height) <= 0.25:
        return isotropic
    if width > height:
        return [tokens["landscape"], *isotropic]
    return [tokens["portrait"], *isotropic]


def contains(
    outer: tuple[float, float, float, float],
    inner: tuple[float, float, float, float],
    tolerance: float = 0.0,
) -> bool:
    return (
        inner[0] >= outer[0] - tolerance
        and inner[1] >= outer[1] - tolerance
        and inner[2] <= outer[2] + tolerance
        and inner[3] <= outer[3] + tolerance
    )


def matches(
    target: tuple[float, float, float, float],
    actual: tuple[float, float, float, float],
    tolerance: float = 0.0,
) -> bool:
    return all(
        abs(expected - measured) <= tolerance
        for expected, measured in zip(target, actual)
    )


def validate_optical_bounds(check: dict, target_bounds, actual_bounds, tolerance: float = 1e-3) -> list[str]:
    """Validate an explicit optical fit without weakening painted containment.

    Sparse marks and narrow glyphs need not be stretched to four keyshape edges.
    Their authored painted bounds and reason must be recorded, not inferred from
    a passing render. Circle radial containment is checked by the caller.
    """
    failures = []
    if not isinstance(check.get("rationale"), str) or not check["rationale"].strip():
        failures.append("optical keyshape fit requires a nonempty rationale")
    declared = check.get("paintedBounds")
    if (not isinstance(declared, (list, tuple)) or len(declared) != 4
            or any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in declared)):
        return failures + ["optical keyshape fit requires four finite paintedBounds in design units"]
    if declared[0] >= declared[2] or declared[1] >= declared[3]:
        failures.append("optical paintedBounds must have positive width and height")
    if not contains(tuple(target_bounds), tuple(declared), tolerance):
        failures.append("declared optical paintedBounds exceed the selected keyshape")
    if not contains(tuple(target_bounds), tuple(actual_bounds), tolerance):
        failures.append("painted geometry exceeds the selected optical keyshape")
    if not matches(tuple(declared), tuple(actual_bounds), tolerance):
        failures.append("optical paintedBounds are stale: measured paint does not match the declaration")
    return failures


def circle_overflow(
    points: list[tuple[float, float]],
    stroke_width: float = 0.0,
    icon_type: str = DEFAULT_ICON_TYPE,
) -> float:
    """Positive radial overflow beyond the selected circle keyshape."""
    if not points:
        return 0.0
    profile = get_profile(icon_type)
    circle = next(
        item for item in canonical_tokens(icon_type) if item["shape"] == "circle"
    )
    allowed_radius = float(circle["diameter"]) / 2.0 - stroke_width / 2.0
    center = profile["center"]
    return max(
        math.hypot(x - center["x"], y - center["y"]) - allowed_radius
        for x, y in points
    )


def nearest(
    bounds: tuple[float, float, float, float],
    allow_circle: bool = True,
    icon_type: str = DEFAULT_ICON_TYPE,
) -> dict:
    """Diagnostic target selected by edge distance, then area difference."""

    def scored(item: dict) -> tuple[float, float]:
        box = token_box(item["width"], item["height"], icon_type)
        distance = sum(
            abs(expected - measured)
            for expected, measured in zip(box, bounds)
        )
        area_delta = abs(
            item["width"] * item["height"]
            - (bounds[2] - bounds[0]) * (bounds[3] - bounds[1])
        )
        return distance, area_delta

    candidates = candidate_tokens(bounds, allow_circle, icon_type)
    containing = [
        item
        for item in candidates
        if contains(
            token_box(item["width"], item["height"], icon_type), bounds
        )
    ]
    item = min(containing or candidates, key=scored)
    box = token_box(item["width"], item["height"], icon_type)
    return {
        **item,
        "bounds": list(box),
        "edgeDeltaToTarget": {
            "left": bounds[0] - box[0],
            "top": bounds[1] - box[1],
            "right": box[2] - bounds[2],
            "bottom": box[3] - bounds[3],
        },
    }


def assign(
    bounds: tuple[float, float, float, float],
    tolerance: float = 0.0,
    allow_circle: bool = True,
    icon_type: str = DEFAULT_ICON_TYPE,
) -> dict | None:
    """The canonical centered target whose rectangular bounds are matched."""
    for item in candidate_tokens(bounds, allow_circle, icon_type):
        box = token_box(item["width"], item["height"], icon_type)
        if matches(box, bounds, tolerance):
            return {**item, "bounds": list(box)}
    return None


def max_box(icon_type: str = DEFAULT_ICON_TYPE) -> tuple[float, float, float, float]:
    circle = next(
        item for item in canonical_tokens(icon_type) if item["shape"] == "circle"
    )
    return token_box(circle["width"], circle["height"], icon_type)


def describe(icon_type: str = DEFAULT_ICON_TYPE) -> str:
    return ", ".join(item["name"] for item in canonical_tokens(icon_type))
