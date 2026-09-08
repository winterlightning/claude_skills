"""Composition: an icon that owns ordered child icons and matching positions.

``CombinedIcon`` stores private ``PlacedIcon`` pairs and exposes derived
``icons``/``positions`` arrays, so ``icons[n]`` always maps to ``positions[n]``
and a caller cannot break parity by mutating one returned list. List order is
paint/z-order. Children are translated by integers and flattened; they are
never nested as a child canvas, scaled, or mutated.
"""

from __future__ import annotations

from typing import Iterable

from .. import contracts
from ..keyshapes import FreeKeyshapeSpec, Keyshape
from ..position import PlacedIcon, Position
from ..primitives import Contour, Point, Relationship, ResolvedDrawing, translate
from ..profiles import Profile
from .base import Icon

COMPOSITION_CLASSES = (
    "SOLO",
    "SIDE_COMBINE",
    "CONTAINER_COMBINE",
    "DIAGRAM_COMBINE",
)


class CombinedIcon(Icon):
    """A composition. It is emitted on CONTAINER64 and belongs to the
    ``container`` family: a composition is a container with its slot filled."""

    family = "container"

    def __init__(
        self,
        icon_id: str,
        composition_class: str,
        keyshape: Keyshape,
        *,
        free_keyshape: FreeKeyshapeSpec | None = None,
        icons: Iterable[Icon] = (),
        positions: Iterable[Position] = (),
    ) -> None:
        super().__init__(
            icon_id, Profile.for_family(CombinedIcon.family),
            semantic_role=None, keyshape=keyshape,
            free_keyshape=free_keyshape,
        )
        if composition_class not in COMPOSITION_CLASSES:
            raise ValueError(f"unknown composition class: {composition_class!r}")
        self.composition_class = composition_class
        icon_list = list(icons)
        position_list = list(positions)
        if len(icon_list) != len(position_list):
            raise ValueError("icons and positions must have equal length")
        self._children = [
            PlacedIcon(icon, position)
            for icon, position in zip(icon_list, position_list)
        ]

    @property
    def icons(self) -> list[Icon]:
        return [child.icon for child in self._children]

    @property
    def positions(self) -> list[Position]:
        return [child.position for child in self._children]

    @property
    def children(self) -> tuple[PlacedIcon, ...]:
        return tuple(self._children)

    def add_icon(self, icon: Icon, position: Position) -> "CombinedIcon":
        """Append one icon/position pair atomically."""
        self._children.append(PlacedIcon(icon, position))
        return self

    def draw(self) -> ResolvedDrawing:
        parent = super().draw()
        primitives = list(parent.primitives)
        contours = list(parent.contours)
        anchors = list(parent.anchors)
        relationships = list(parent.relationships)
        owners = []

        for index, child in enumerate(self._children):
            prefix = f"{index}:{child.icon.icon_id}:"
            drawing = child.icon.draw()
            owners.extend((prefix + p.element_id, index) for p in drawing.primitives)
            owners.extend((prefix + c.contour_id, index) for c in drawing.contours)
            primitives.extend(
                translate(
                    primitive,
                    child.position,
                    element_id=prefix + primitive.element_id,
                )
                for primitive in drawing.primitives
            )
            contours.extend(
                Contour(
                    prefix + contour.contour_id,
                    tuple(prefix + member for member in contour.members),
                    contour.closed,
                )
                for contour in drawing.contours
            )
            anchors.extend(
                (
                    prefix + name,
                    Point(
                        point.x + child.position.x,
                        point.y + child.position.y,
                    ),
                )
                for name, point in drawing.anchors
            )
            relationships.extend(
                Relationship(
                    relation.kind,
                    tuple(prefix + member for member in relation.members),
                )
                for relation in drawing.relationships
            )

        return ResolvedDrawing(
            tuple(primitives),
            tuple(contours),
            tuple(anchors),
            tuple(relationships),
            tuple(owners),
        )

    def to_record(self) -> dict:
        record = super().to_record()
        # `slot_role` is the contextual role -- what this child does *here*.
        # `semantic_role` stays the icon's own standalone description, so a
        # heart placed as content still reads as the noun it is.
        template = contracts.composition_templates()["classes"].get(
            self.composition_class, {}
        )
        specs = template.get("children", [])
        record["children"] = [
            {
                "icon_id": child.icon.icon_id,
                "profile": child.icon.profile.name,
                "semantic_role": child.icon.semantic_role,
                "semantic_kind": child.icon.semantic_kind,
                "slot_role": specs[index]["slot_role"] if index < len(specs) else None,
                "position": [child.position.x, child.position.y],
            }
            for index, child in enumerate(self._children)
        ]
        return record
