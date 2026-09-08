"""Deterministic SVG emitter.

One resolved scene in, one canonical document out: the exact profile viewBox,
the locked global style, integer coordinates, and no transform of any kind.
Contour members are merged into a single ``<path>`` so interior vertices paint
as round joins rather than two independent round caps.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from xml.sax.saxutils import escape, quoteattr

from ..model.primitives import Arc, Line, Primitive, ResolvedDrawing
from ..model.profiles import FILL, LINE_CAP, LINE_JOIN, STROKE, STROKE_WIDTH

if TYPE_CHECKING:  # pragma: no cover - typing only
    from ..model.icons.base import Icon

SVG_NS = "http://www.w3.org/2000/svg"


def _number(value: float) -> str:
    """Integers stay integers; the model authors nothing else."""
    if float(value).is_integer():
        return str(int(value))
    return f"{value:g}"


def _move_to(primitive: Primitive) -> str:
    return f"M{_number(primitive.start.x)} {_number(primitive.start.y)}"


def _segment(primitive: Primitive) -> str:
    if isinstance(primitive, Line):
        if primitive.is_dot:
            # An explicit zero-length line is a round-cap point. Emit it so the
            # command survives round-trip rather than collapsing to a lone M.
            return f"L{_number(primitive.end.x)} {_number(primitive.end.y)}"
        return f"L{_number(primitive.end.x)} {_number(primitive.end.y)}"
    if isinstance(primitive, Arc):
        return (
            f"A{_number(primitive.radius_x)} {_number(primitive.radius_y)} 0 "
            f"{int(primitive.large_arc)} {int(primitive.sweep)} "
            f"{_number(primitive.end.x)} {_number(primitive.end.y)}"
        )
    raise TypeError(f"unsupported primitive: {type(primitive).__name__}")


def build_paths(drawing: ResolvedDrawing) -> list[dict]:
    """Group primitives into emitted paths, preserving authored order.

    Every primitive belongs to exactly one path: a contour's members become one
    path in contour order, and any primitive outside a contour becomes its own
    single-segment path. Contour members must be contiguous head-to-tail.
    """
    by_id = drawing.by_id()
    if len(by_id) != len(drawing.primitives):
        seen: set[str] = set()
        duplicates = sorted(
            {p.element_id for p in drawing.primitives if p.element_id in seen or seen.add(p.element_id)}
        )
        raise ValueError(f"duplicate element ids: {duplicates}")

    claimed: dict[str, str] = {}
    contour_ids: set[str] = set()
    for contour in drawing.contours:
        if contour.contour_id in contour_ids:
            raise ValueError(f"duplicate contour id: {contour.contour_id!r}")
        contour_ids.add(contour.contour_id)
        if not contour.members:
            raise ValueError(f"contour {contour.contour_id!r} has no members")
        for member in contour.members:
            if member not in by_id:
                raise ValueError(
                    f"contour {contour.contour_id!r} references unknown element {member!r}"
                )
            if member in claimed:
                raise ValueError(
                    f"element {member!r} belongs to contours "
                    f"{claimed[member]!r} and {contour.contour_id!r}"
                )
            claimed[member] = contour.contour_id

    collisions = contour_ids & (set(by_id) - set(claimed))
    if collisions:
        raise ValueError(f"conflicting emitted path ids: {sorted(collisions)}")

    contours_by_id = {contour.contour_id: contour for contour in drawing.contours}
    paths: list[dict] = []
    emitted: set[str] = set()

    for primitive in drawing.primitives:
        contour_id = claimed.get(primitive.element_id)
        if contour_id is None:
            paths.append({
                "id": primitive.element_id,
                "contour_id": None,
                "closed": False,
                "members": [primitive.element_id],
                "d": f"{_move_to(primitive)}{_segment(primitive)}",
                "primitives": [primitive],
            })
            emitted.add(primitive.element_id)
            continue
        if contour_id in emitted:
            continue
        contour = contours_by_id[contour_id]
        members = [by_id[member] for member in contour.members]
        cursor = members[0].start
        commands = [_move_to(members[0])]
        for index, member in enumerate(members):
            if member.start != cursor:
                raise ValueError(
                    f"contour {contour_id!r} is not contiguous at member "
                    f"{contour.members[index]!r}: expected start "
                    f"{cursor.as_tuple()}, got {member.start.as_tuple()}"
                )
            commands.append(_segment(member))
            cursor = member.end
        if contour.closed:
            if cursor != members[0].start:
                raise ValueError(
                    f"closed contour {contour_id!r} does not return to its start: "
                    f"ends at {cursor.as_tuple()}, started at {members[0].start.as_tuple()}"
                )
            commands.append("Z")
        paths.append({
            "id": contour_id,
            "contour_id": contour_id,
            "closed": contour.closed,
            "members": list(contour.members),
            "d": "".join(commands),
            "primitives": members,
        })
        emitted.add(contour_id)
    members = [member for path in paths for member in path["members"]]
    if len(members) != len(by_id) or set(members) != set(by_id):
        raise ValueError("every primitive must be emitted exactly once")
    return paths


def render_svg(icon: "Icon") -> str:
    canvas = icon.profile.spec.canvas_size
    paths = build_paths(icon.draw())
    if not paths:
        raise ValueError(f"{icon.icon_id}: an icon must contain drawable geometry")
    lines = [
        f'<svg xmlns="{SVG_NS}" width="{canvas}" height="{canvas}" '
        f'viewBox="0 0 {canvas} {canvas}" fill="{FILL}" stroke="{STROKE}" '
        f'stroke-width="{STROKE_WIDTH}" stroke-linecap="{LINE_CAP}" '
        f'stroke-linejoin="{LINE_JOIN}">',
        f'  <title>{escape(icon.icon_id)}</title>',
    ]
    for path in paths:
        lines.append(f'  <path id={quoteattr(path["id"])} d="{path["d"]}"/>')
    lines.append("</svg>")
    return "\n".join(lines) + "\n"
