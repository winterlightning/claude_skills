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


Primitive = Line | Arc


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
class ResolvedDrawing:
    primitives: tuple[Primitive, ...]
    contours: tuple[Contour, ...]
    anchors: tuple[tuple[str, Point], ...]
    relationships: tuple[Relationship, ...]
    # Explicit ownership of flattened primitives and contours, assigned by composition.
    owners: tuple[tuple[str, int], ...] = ()

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
    raise ValueError(f"unknown primitive kind: {kind!r}")
