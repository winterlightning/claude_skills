"""The primary authoring API: ``Icon`` owns typed drawing primitives.

Concrete subjects extend ``Icon``. Geometry is authored directly in final
canvas coordinates for one profile; a second profile is a separately authored
sibling, never a scaled copy.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, Literal, TYPE_CHECKING

from ..keyshapes import FreeKeyshapeSpec, Keyshape
from ..metadata import record_metadata
from ..primitives import (
    Arc,
    Bezier,
    Contour,
    HumanFigure,
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
    from ..fitting import FitResult
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
    #: Every category the icon belongs to; ``category`` is the primary one.
    categories: tuple[str, ...] = ()
    aliases: tuple[str, ...] = ()
    composition_class: str = "SOLO"
    keywords: tuple[str, ...] = ()
    variant_of: str | None = None
    variant_label: str = ""
    # Explicit visual acceptance of one SVG; automatic checks still run.
    exception: dict | None = None

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
        self.human_figures: list[HumanFigure] = []

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

    def add_bezier(
        self,
        element_id: str,
        start: tuple[int, int],
        *segments: tuple[tuple[float, float], tuple[float, float], tuple[float, float]],
    ) -> "Icon":
        """Author a smooth run of cubics from ``start``.

        Each segment is ``(control1, control2, knot)``. Nodes where the curve
        meets other geometry stay integer; smooth controls may be fractional.
        """
        if not segments:
            raise ValueError(f"{element_id}: a bezier needs at least one segment")
        last = segments[-1][2]
        source_native = getattr(self, "sizing_mode", None) == "text-source-native-v2"
        self.primitives.append(Bezier(
            element_id, Point(*start),
            Point(*last) if source_native else Point(int(last[0]), int(last[1])),
            tuple((tuple(c1), tuple(c2), tuple(p3)) for c1, c2, p3 in segments),
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

    def mark_human_figure(
        self,
        figure_id: str,
        *,
        head: str,
        torso: str,
        torso_junction: Literal["start", "end"],
    ) -> "Icon":
        """Flag a detached head and its own upper torso for future validation.

        Call after creating geometry. Head may name a primitive or contour;
        torso names the upper line/arc/Bezier primitive, with the neck endpoint
        identified explicitly. This metadata neither connects nor moves ink
        and does not certify the required 8-centerline / 4-ink gap.
        """
        if not figure_id or any(f.figure_id == figure_id for f in self.human_figures):
            raise ValueError("human figure ID must be nonempty and unique")
        if torso_junction not in ("start", "end"):
            raise ValueError("torso_junction must be 'start' or 'end'")
        primitives = {p.element_id for p in self.primitives}
        contours = {c.contour_id: c for c in self.contours}
        if head not in primitives and head not in contours:
            raise ValueError(f"unknown human head: {head!r}")
        if torso not in primitives:
            raise ValueError(f"human torso must name an upper torso primitive: {torso!r}")
        if head == torso or (head in contours and torso in contours[head].members):
            raise ValueError("detached head and torso must be distinct geometry")
        self.human_figures.append(HumanFigure(figure_id, head, torso, torso_junction))
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
            human_figures=tuple(self.human_figures),
        )

    # -- artifacts ---------------------------------------------------------

    def fit_to_keyshape(self, keyshape: Keyshape, *, force_stretch: bool = False) -> "FitResult":
        """Return a new SOLO48 fitting candidate and its full QA report.

        Scales centerlines, keeps stroke width fixed, and snaps to
        the integer grid. Exact fitting and visual quality are not guaranteed;
        remaining problems are reported for manual adjustment. Never mutates
        this icon or registers/publishes the candidate. With force_stretch,
        rectangular targets use independent x/y scales, including arc radii.
        Circle targets retain radial proportional fitting.
        """
        from ..fitting import fit_to_keyshape

        return fit_to_keyshape(self, keyshape, force_stretch=force_stretch)

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

    def export_json_graph(self, destination: str | Path) -> Path:
        """Write the construction graph as UTF-8 JSON and return its path.

        Uses the existing icon record format: ordered primitives, contours,
        anchors, relationships, and metadata (profile, keyshape, and style).
        Compositions include resolved geometry and child placement metadata.
        Parent directories are created as needed; no rendering or validation
        is performed, so an in-progress drawing can also be exported.
        """
        document = json.dumps(self.to_record(), indent=2, ensure_ascii=False, allow_nan=False)
        path = Path(destination)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(document + "\n", encoding="utf-8")
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
            **record_metadata(self),
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
        if drawing.human_figures:
            record["human_figures"] = [
                {"figure_id": f.figure_id, "head": f.head, "torso": f.torso,
                 "torso_junction": f.torso_junction,
                 "centerline_gap": f.centerline_gap, "ink_gap": f.ink_gap}
                for f in drawing.human_figures
            ]
        if self.variant_of:
            record["variant_of"] = self.variant_of
            record["variant_label"] = self.variant_label
        if self.exception is not None:
            record["exception"] = dict(self.exception)
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
