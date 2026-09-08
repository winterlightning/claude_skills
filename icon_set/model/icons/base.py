"""The primary authoring API: ``Icon`` owns typed drawing primitives.

Concrete subjects extend ``Icon``. Geometry is authored directly in final
canvas coordinates for one profile; a second profile is a separately authored
sibling, never a scaled copy.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Literal, TYPE_CHECKING

from ..keyshapes import FreeKeyshapeSpec, Keyshape
from ..primitives import (
    Arc,
    Contour,
    Line,
    Point,
    Primitive,
    Relationship,
    RelationshipKind,
    ResolvedDrawing,
    primitive_to_dict,
)
from ..profiles import GRID, LINE_CAP, LINE_JOIN, STROKE_WIDTH, Profile

if TYPE_CHECKING:  # pragma: no cover - typing only
    from ...validation.report import ValidationReport

ExportFormat = Literal["svg", "png"]
SemanticRole = Literal["MAIN", "SUB"]


class Icon:
    STROKE_WIDTH = STROKE_WIDTH
    LINE_CAP = LINE_CAP
    LINE_JOIN = LINE_JOIN
    GRID = GRID

    #: The family this icon belongs to: ``sub``, ``solo`` or ``container``.
    #: A family owns exactly one profile (see the profile contract), and the
    #: validator rejects an icon whose profile is not its family's. ``None``
    #: marks an unfamilied draft built directly from ``Icon``; nothing in the
    #: registry or the build is ever unfamilied.
    family: str | None = None

    #: Metadata defaults a subject may override.
    #: ``semantic_kind`` is what the subject *is*; ``semantic_role`` is the slot
    #: it fills. A MAIN must be a noun and a SUB must be a verb, state, or
    #: modifier, and the validator enforces exactly that pairing.
    semantic_kind: str = "modifier"
    category: str = "primitives"
    aliases: tuple[str, ...] = ()
    composition_class: str = "SOLO"
    keywords: tuple[str, ...] = ()
    variant_of: str | None = None
    variant_label: str = ""

    def __init__(
        self,
        icon_id: str,
        profile: Profile,
        *,
        semantic_role: SemanticRole | None,
        keyshape: Keyshape,
        free_keyshape: FreeKeyshapeSpec | None = None,
        primitives: Iterable[Primitive] = (),
        contours: Iterable[Contour] = (),
        relationships: Iterable[Relationship] = (),
    ) -> None:
        if keyshape is Keyshape.FREE and free_keyshape is None:
            raise ValueError("FREE requires a FreeKeyshapeSpec")
        if keyshape is not Keyshape.FREE and free_keyshape is not None:
            raise ValueError("free_keyshape is only valid with Keyshape.FREE")
        self.icon_id = icon_id
        self.profile = profile
        self.semantic_role = semantic_role
        self.keyshape = keyshape
        self.free_keyshape = free_keyshape
        self.primitives: list[Primitive] = list(primitives)
        self.contours: list[Contour] = list(contours)
        self.anchors: dict[str, Point] = {}
        self.relationships: list[Relationship] = list(relationships)

    # -- authoring ---------------------------------------------------------

    def add_line(
        self,
        element_id: str,
        start: tuple[int, int],
        end: tuple[int, int],
    ) -> "Icon":
        self.primitives.append(Line(element_id, Point(*start), Point(*end)))
        return self

    def add_arc(
        self,
        element_id: str,
        start: tuple[int, int],
        end: tuple[int, int],
        *,
        radius_x: int,
        radius_y: int | None = None,
        large_arc: bool = False,
        sweep: bool = True,
    ) -> "Icon":
        self.primitives.append(Arc(
            element_id, Point(*start), Point(*end), radius_x,
            radius_x if radius_y is None else radius_y,
            large_arc, sweep,
        ))
        return self

    def add_dot(self, element_id: str, at: tuple[int, int]) -> "Icon":
        """A zero-length line: one round cap, painted as a stroke-wide point."""
        return self.add_line(element_id, at, at)

    def add_polyline(
        self,
        element_id: str,
        *points: tuple[int, int],
        closed: bool = False,
    ) -> "Icon":
        """Author a run of joined segments as one contour.

        Segments are emitted as ``<element_id>-1..n`` and grouped in a contour
        named ``element_id`` so the renderer produces round joins rather than
        independent caps at every interior vertex.
        """
        if len(points) < 2:
            raise ValueError(f"{element_id}: a polyline needs at least two points")
        sequence = list(points)
        if closed:
            sequence.append(points[0])
        members = []
        for index in range(len(sequence) - 1):
            segment_id = f"{element_id}-{index + 1}"
            self.add_line(segment_id, sequence[index], sequence[index + 1])
            members.append(segment_id)
        return self.add_contour(element_id, *members, closed=closed)

    def add_anchor(self, name: str, point: tuple[int, int]) -> "Icon":
        self.anchors[name] = Point(*point)
        return self

    def add_contour(
        self,
        contour_id: str,
        *members: str,
        closed: bool = False,
    ) -> "Icon":
        self.contours.append(Contour(contour_id, tuple(members), closed))
        return self

    def relate(
        self,
        kind: RelationshipKind,
        *members: str,
    ) -> "Icon":
        self.relationships.append(Relationship(kind, tuple(members)))
        return self

    # -- resolution --------------------------------------------------------

    def keyshape_bounds(self) -> tuple[int, int, int, int]:
        if self.keyshape is Keyshape.FREE:
            assert self.free_keyshape is not None
            return self.free_keyshape.bounds_for(self.profile)
        return self.keyshape.bounds_for(self.profile)

    def draw(self) -> ResolvedDrawing:
        return ResolvedDrawing(
            tuple(self.primitives),
            tuple(self.contours),
            tuple(self.anchors.items()),
            tuple(self.relationships),
        )

    # -- artifacts ---------------------------------------------------------

    def to_svg(self) -> str:
        from ...renderers.svg import render_svg

        return render_svg(self)

    def export_icon_to(
        self,
        destination: str | Path,
        format: ExportFormat | None = None,
    ) -> Path:
        """Export SVG or PNG; infer the format from the suffix when omitted."""
        path = Path(destination)
        resolved = (format or path.suffix.lstrip(".")).lower()
        if resolved not in ("svg", "png"):
            raise ValueError(
                f"unsupported export format: {resolved!r}; expected 'svg' or 'png'"
            )
        path.parent.mkdir(parents=True, exist_ok=True)
        if resolved == "svg":
            path.write_text(self.to_svg(), encoding="utf-8")
        else:
            from ...renderers.png import render_png

            path.write_bytes(render_png(self))
        return path

    def validate_icon(self) -> "ValidationReport":
        """Delegate to the M5 validator chain without changing this API."""
        from ...validation.validator import IconValidator

        return IconValidator().validate(self)

    # -- interchange -------------------------------------------------------

    def to_record(self) -> dict:
        """The serializable icon record: geometry AST plus locked metadata."""
        drawing = self.draw()
        record = {
            "icon_id": self.icon_id,
            "name": self.icon_id,
            "aliases": list(self.aliases),
            "category": self.category,
            "keywords": list(self.keywords),
            "family": self.family,
            "profile": self.profile.name,
            "canvas_size": self.profile.spec.canvas_size,
            "semantic_role": self.semantic_role,
            "semantic_kind": self.semantic_kind,
            "composition_class": self.composition_class,
            "keyshape": self.keyshape.name,
            "keyshape_bounds": list(self.keyshape_bounds()),
            "style": {
                "stroke_width": self.STROKE_WIDTH,
                "line_cap": self.LINE_CAP,
                "line_join": self.LINE_JOIN,
                "grid": self.GRID,
            },
            "primitives": [primitive_to_dict(p) for p in drawing.primitives],
            "contours": [
                {
                    "contour_id": contour.contour_id,
                    "members": list(contour.members),
                    "closed": contour.closed,
                }
                for contour in drawing.contours
            ],
            "anchors": {name: list(point.as_tuple()) for name, point in drawing.anchors},
            "relationships": [
                {"kind": relation.kind, "members": list(relation.members)}
                for relation in drawing.relationships
            ],
        }
        if self.variant_of:
            record["variant_of"] = self.variant_of
            record["variant_label"] = self.variant_label
        if self.free_keyshape is not None:
            record["free_keyshape"] = {
                "bounds": [
                    self.free_keyshape.left, self.free_keyshape.top,
                    self.free_keyshape.right, self.free_keyshape.bottom,
                ],
                "rationale": self.free_keyshape.rationale,
                "approval_id": self.free_keyshape.approval_id,
            }
        return record

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        return (
            f"{type(self).__name__}(icon_id={self.icon_id!r}, "
            f"profile={self.profile.name}, keyshape={self.keyshape.name}, "
            f"primitives={len(self.primitives)})"
        )
