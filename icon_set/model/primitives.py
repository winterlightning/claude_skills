"""Typed drawing primitives and the serializable geometry AST.

The primitive list is both the OOP model's internal geometry and the agent
interchange format, so there is one source of truth. Authored coordinates are
integers on grid 1; a resolved drawing carries primitives, contour topology,
named anchors, and declared relationships together.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

RelationshipKind = Literal["connect", "occlude", "knockout"]


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def as_tuple(self) -> tuple[int, int]:
        return (self.x, self.y)


@dataclass(frozen=True)
class Line:
    element_id: str
    start: Point
    end: Point

    @property
    def is_dot(self) -> bool:
        """A zero-length line is a deliberate round-cap point."""
        return self.start == self.end


@dataclass(frozen=True)
class Arc:
    element_id: str
    start: Point
    end: Point
    radius_x: int
    radius_y: int
    large_arc: bool = False
    sweep: bool = True


ControlPoint = tuple[float, float]
CubicSegment = tuple[ControlPoint, ControlPoint, ControlPoint]


@dataclass(frozen=True)
class Bezier:
    """A chain of cubic segments between two integer nodes.

    ``start`` and ``end`` are authored nodes on grid 1. ``segments`` holds each
    cubic as ``(control1, control2, knot)``; controls and interior knots may be
    fractional, and the last knot must equal ``end``.
    """

    element_id: str
    start: Point
    end: Point
    segments: tuple[CubicSegment, ...]

    def cubics(self) -> list[tuple[ControlPoint, ControlPoint, ControlPoint, ControlPoint]]:
        """Each segment as four explicit points ``(p0, c1, c2, p3)``."""
        result = []
        p0 = (float(self.start.x), float(self.start.y))
        for c1, c2, p3 in self.segments:
            result.append((p0, tuple(c1), tuple(c2), tuple(p3)))
            p0 = tuple(p3)
        return result

    def sample(self, per_segment: int = 48) -> list[ControlPoint]:
        """Points along the centerline, both ends included."""
        points = [(float(self.start.x), float(self.start.y))]
        for p0, c1, c2, p3 in self.cubics():
            for index in range(1, per_segment + 1):
                points.append(cubic_point(p0, c1, c2, p3, index / per_segment))
        return points

    def extrema(self) -> list[ControlPoint]:
        """Interior knots plus every axis extremum, solved exactly per segment."""
        found = [tuple(p3) for _, _, p3 in self.segments[:-1]]
        for p0, c1, c2, p3 in self.cubics():
            for axis in (0, 1):
                a = -p0[axis] + 3 * c1[axis] - 3 * c2[axis] + p3[axis]
                b = 2 * (p0[axis] - 2 * c1[axis] + c2[axis])
                c = c1[axis] - p0[axis]
                roots = []
                if abs(a) < 1e-12:
                    if abs(b) > 1e-12:
                        roots.append(-c / b)
                else:
                    disc = b * b - 4 * a * c
                    if disc >= 0:
                        root = disc ** 0.5
                        roots.extend(((-b + root) / (2 * a), (-b - root) / (2 * a)))
                for t in roots:
                    if 0.0 < t < 1.0:
                        found.append(cubic_point(p0, c1, c2, p3, t))
        return found


def cubic_point(p0, c1, c2, p3, t: float) -> ControlPoint:
    u = 1.0 - t
    return (
        u * u * u * p0[0] + 3 * u * u * t * c1[0] + 3 * u * t * t * c2[0] + t * t * t * p3[0],
        u * u * u * p0[1] + 3 * u * u * t * c1[1] + 3 * u * t * t * c2[1] + t * t * t * p3[1],
    )


Primitive = Line | Arc | Bezier


@dataclass(frozen=True)
class Relationship:
    kind: RelationshipKind
    members: tuple[str, ...]


@dataclass(frozen=True)
class Contour:
    contour_id: str
    members: tuple[str, ...]
    closed: bool = False


@dataclass(frozen=True)
class HumanFigure:
    """Detached stick-figure parts; gap values are targets, not measurements."""

    figure_id: str
    head: str
    torso: str
    torso_junction: Literal["start", "end"]

    @property
    def centerline_gap(self) -> int:
        return 8

    @property
    def ink_gap(self) -> int:
        return 4


@dataclass(frozen=True)
class ResolvedDrawing:
    primitives: tuple[Primitive, ...]
    contours: tuple[Contour, ...]
    anchors: tuple[tuple[str, Point], ...]
    relationships: tuple[Relationship, ...]
    # Explicit ownership of flattened primitives and contours, assigned by composition.
    owners: tuple[tuple[str, int], ...] = ()
    human_figures: tuple[HumanFigure, ...] = ()

    def by_id(self) -> dict[str, Primitive]:
        return {primitive.element_id: primitive for primitive in self.primitives}


@dataclass(frozen=True)
class Position:
    x: int
    y: int


def translate(
    primitive: Primitive,
    position: Position,
    *,
    element_id: str | None = None,
) -> Primitive:
    """Integer translation only. Composition never scales or rotates."""

    def move(point: Point) -> Point:
        return Point(point.x + position.x, point.y + position.y)

    resolved_id = primitive.element_id if element_id is None else element_id
    if isinstance(primitive, Line):
        return Line(resolved_id, move(primitive.start), move(primitive.end))
    if isinstance(primitive, Bezier):
        shift = lambda p: (p[0] + position.x, p[1] + position.y)  # noqa: E731
        return Bezier(
            resolved_id, move(primitive.start), move(primitive.end),
            tuple((shift(c1), shift(c2), shift(p3)) for c1, c2, p3 in primitive.segments),
        )
    return Arc(
        resolved_id,
        move(primitive.start), move(primitive.end),
        primitive.radius_x, primitive.radius_y,
        primitive.large_arc, primitive.sweep,
    )


def primitive_to_dict(primitive: Primitive) -> dict:
    """Serialize one primitive for the interchange AST."""
    if isinstance(primitive, Line):
        return {
            "kind": "line",
            "element_id": primitive.element_id,
            "start": list(primitive.start.as_tuple()),
            "end": list(primitive.end.as_tuple()),
        }
    if isinstance(primitive, Bezier):
        return {
            "kind": "bezier",
            "element_id": primitive.element_id,
            "start": list(primitive.start.as_tuple()),
            "end": list(primitive.end.as_tuple()),
            "segments": [[list(c1), list(c2), list(p3)] for c1, c2, p3 in primitive.segments],
        }
    return {
        "kind": "arc",
        "element_id": primitive.element_id,
        "start": list(primitive.start.as_tuple()),
        "end": list(primitive.end.as_tuple()),
        "radius_x": primitive.radius_x,
        "radius_y": primitive.radius_y,
        "large_arc": primitive.large_arc,
        "sweep": primitive.sweep,
    }


def primitive_from_dict(data: dict) -> Primitive:
    """Rebuild one primitive from the interchange AST."""
    kind = data.get("kind")
    start = Point(*data["start"])
    end = Point(*data["end"])
    if kind == "line":
        return Line(data["element_id"], start, end)
    if kind == "arc":
        return Arc(
            data["element_id"], start, end,
            data["radius_x"], data["radius_y"],
            bool(data.get("large_arc", False)), bool(data.get("sweep", True)),
        )
    if kind == "bezier":
        return Bezier(
            data["element_id"], start, end,
            tuple((tuple(c1), tuple(c2), tuple(p3)) for c1, c2, p3 in data["segments"]),
        )
    raise ValueError(f"unknown primitive kind: {kind!r}")
