"""Non-destructive SOLO48 migration candidates, with unchanged validation rules."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import TYPE_CHECKING

from .keyshapes import Keyshape
from .primitives import Arc, Line, Point
from .profiles import Profile
from ..validation.envelope import centerline_bounds, centerline_radial_extent

if TYPE_CHECKING:
    from .icons.base import Icon


@dataclass(frozen=True)
class FitResult:
    icon: Icon
    report: dict


def fit_to_keyshape(icon: Icon, keyshape: Keyshape, *, force_stretch: bool = False) -> FitResult:
    """Fit measured geometry, snap shared points, and run library QA.

    The graph does not describe which body parts may be lengthened, so this
    function never invents structural edits. Force stretch independently scales
    x/y coordinates and arc radii for rectangular targets. A mismatch, snapping
    damage, or spacing failure stays visible in the report. All candidates
    require visual review, including those that pass numeric checks.
    """
    if icon.family != "solo" or icon.profile is not Profile.SOLO48:
        raise ValueError("fit_to_keyshape currently supports solo icons on SOLO48 only")
    if not isinstance(keyshape, Keyshape) or keyshape is Keyshape.FREE:
        raise ValueError("target must be a standard Keyshape, not FREE")
    from .icons.base import Icon

    if type(icon).draw is not Icon.draw:
        raise ValueError("fitting requires the standard standalone draw method")
    drawing = icon.draw()
    source = list(drawing.primitives)
    left, top, right, bottom = centerline_bounds(source)
    source_center = ((left + right) / 2, (top + bottom) / 2)
    width, height = right - left, bottom - top
    if width == 0 and height == 0:
        raise ValueError("a point-only drawing cannot be resized to a keyshape")
    target = keyshape.bounds_for(icon.profile)
    stroke_radius = icon.STROKE_WIDTH / 2
    target_center = ((target[0] + target[2]) / 2, (target[1] + target[3]) / 2)
    if keyshape.is_radial:
        scale = (keyshape.visible_radius_for(icon.profile) - stroke_radius) / centerline_radial_extent(source, source_center)
    else:
        scales = []
        if width:
            scales.append((target[2] - target[0] - 2 * stroke_radius) / width)
        if height:
            scales.append((target[3] - target[1] - 2 * stroke_radius) / height)
        scale = min(scales)
    scale_x = scale_y = scale
    if force_stretch and not keyshape.is_radial:
        if not width or not height:
            raise ValueError("force stretch requires non-zero width and height")
        scale_x = (target[2] - target[0] - 2 * stroke_radius) / width
        scale_y = (target[3] - target[1] - 2 * stroke_radius) / height

    def move(point: Point) -> Point:
        # One mapping for every occurrence preserves shared endpoints; rounding
        # relative to the integral target center preserves mirrored pairs.
        return Point(
            int(target_center[0]) + round((point.x - source_center[0]) * scale_x),
            int(target_center[1]) + round((point.y - source_center[1]) * scale_y),
        )

    candidate = deepcopy(icon)
    mode = "stretch" if force_stretch and not keyshape.is_radial else "uniform"
    suffix = "stretch" if mode == "stretch" else "fit"
    candidate.icon_id = f"{icon.icon_id}-{suffix}-{keyshape.token}"
    candidate.variant_of = icon.icon_id
    candidate.variant_label = f"{'Stretch' if mode == 'stretch' else 'Fit'} to {keyshape.name}"
    candidate.keyshape = keyshape
    candidate.free_keyshape = None
    candidate.primitives = []
    notes = []
    for primitive in source:
        start, end = move(primitive.start), move(primitive.end)
        if start == end and primitive.start != primitive.end:
            notes.append(f"{primitive.element_id}: endpoints collapsed during snapping")
        if isinstance(primitive, Line):
            transformed = Line(primitive.element_id, start, end)
        else:
            rx, ry = round(primitive.radius_x * scale_x), round(primitive.radius_y * scale_y)
            if rx < 1 or ry < 1:
                notes.append(f"{primitive.element_id}: snapped radius raised to 1")
            transformed = Arc(primitive.element_id, start, end, max(1, rx), max(1, ry),
                              primitive.large_arc, primitive.sweep)
        candidate.primitives.append(transformed)
    candidate.contours = list(drawing.contours)
    candidate.relationships = list(drawing.relationships)
    candidate.anchors = {name: move(point) for name, point in drawing.anchors}
    # This family anchor describes the canvas, not a feature of the drawing.
    if "center" in candidate.anchors:
        candidate.anchors["center"] = Point(*icon.profile.spec.center)

    from ..validation.library_qa import inspect_icon

    qa = inspect_icon(candidate)
    qa.pop('_svg', None)
    return FitResult(candidate, {
        "source_icon_id": icon.icon_id,
        "target_keyshape": keyshape.name,
        "source_centerline_bounds": list((left, top, right, bottom)),
        "target_visible_bounds": list(target),
        "mode": mode,
        "scale": scale_x if scale_x == scale_y else None,
        "scale_x": scale_x,
        "scale_y": scale_y,
        "stroke_width": candidate.STROKE_WIDTH,
        "requires_visual_review": True,
        "notes": notes,
        "validation": qa,
    })
