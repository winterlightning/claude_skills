"""The ordered validator chain (ICON_SYSTEM_PLAN.md section 5).

Checks run in a fixed order and every failure names the element and the actual
coordinates. Later checks still run after an earlier failure so one pass gives
a complete picture, except where a failure makes a later measurement
meaningless (unparsable geometry, for instance).

Nothing here may repair, scale, thin, or relax. A conflict is reported.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..model import contracts
from ..model.keyshapes import Keyshape
from ..model.primitives import Arc, Line
from ..model.profiles import (
    CANVAS_OVERFLOW_TOLERANCE,
    CIRCLE_TOUCH_TOLERANCE,
    FILL,
    GRID,
    LINE_CAP,
    LINE_JOIN,
    NUMERIC_EPSILON,
    RECT_FIT_TOLERANCE,
    SEMANTIC_ROLES,
    STROKE,
    STROKE_WIDTH,
    Profile,
)
from . import envelope
from .path_commands import commands_for_path
from .report import CHECK_ORDER, Finding, ValidationReport
from .stroke_distance import analyze_paths
from .svg_reader import SvgRoundTripError, parse_svg
from .structure import check_structure

if TYPE_CHECKING:  # pragma: no cover - typing only
    from ..model.icons.base import Icon

NOUN_KINDS = frozenset({"noun"})
SUB_KINDS = frozenset({"verb", "state", "modifier"})


class IconValidator:
    """Runs every locked rule against one resolved icon.

    ``require_free_approval`` is the release gate. With it on -- the default, and
    what the build script uses -- a FREE icon needs an exceptions record marked
    ``approved``. With it off, a ``proposed`` record is accepted, so an agent can
    author a FREE icon and submit the record for review instead of being blocked;
    a proposed record still never reaches a release build.
    """

    def __init__(self, *, require_free_approval: bool = True) -> None:
        self.require_free_approval = require_free_approval

    def validate(self, icon: "Icon") -> ValidationReport:
        errors: list[Finding] = []
        warnings: list[Finding] = []
        run: list[str] = []
        review = False

        # Measure the *resolved* drawing, never `icon.primitives`. For a SOLO
        # icon the two are identical, but a CombinedIcon holds its geometry in
        # its placed children and only draw() flattens them; measuring the raw
        # attribute reports a composite as empty.
        try:
            drawing = icon.draw()
            resolved = list(drawing.primitives)
        except (ValueError, TypeError, AttributeError) as error:
            errors.append(Finding(CHECK_ORDER[0], f"cannot resolve geometry: {error}"))
            return ValidationReport.build(errors, warnings, run)

        run.append(CHECK_ORDER[0])
        structural_errors = check_structure(icon, drawing)
        if structural_errors:
            errors.extend(Finding(CHECK_ORDER[0], message) for message in structural_errors)
            return ValidationReport.build(errors, warnings, run)
        self._check_schema_profile(icon, resolved, errors)
        if not isinstance(icon.profile, Profile) or not isinstance(icon.keyshape, Keyshape):
            return ValidationReport.build(errors, warnings, run)

        run.append(CHECK_ORDER[1])
        self._check_style_grid(icon, resolved, errors)

        # Emitted paths are the shared input for bounds, MIC and round-trip.
        try:
            from ..renderers.svg import build_paths

            paths = build_paths(drawing)
            document = icon.to_svg()
        except (ValueError, TypeError) as error:
            errors.append(Finding("style/grid", str(error), None))
            return ValidationReport.build(errors, warnings, run)

        run.append(CHECK_ORDER[2])
        self._check_bounds(icon, resolved, errors)

        run.append(CHECK_ORDER[3])
        review |= self._check_mic(icon, paths, errors, warnings, drawing)

        run.append(CHECK_ORDER[4])
        self._check_keyshape(icon, errors)

        run.append(CHECK_ORDER[5])
        self._check_composition(icon, errors)

        run.append(CHECK_ORDER[6])
        self._check_round_trip(icon, document, paths, errors)

        run.append(CHECK_ORDER[7])
        self._check_reproducibility(icon, document, errors)

        return ValidationReport.build(errors, warnings, run, review=review)

    # -- 1. schema / profile ----------------------------------------------

    def _check_schema_profile(
        self, icon: "Icon", resolved: list, errors: list[Finding]
    ) -> None:
        check = CHECK_ORDER[0]
        if not icon.icon_id or not isinstance(icon.icon_id, str):
            errors.append(Finding(check, "icon_id must be a non-empty string"))
        if not isinstance(icon.profile, Profile):
            errors.append(Finding(check, f"unknown profile: {icon.profile!r}"))
            return
        self._check_family(icon, errors)
        if not isinstance(icon.keyshape, Keyshape):
            errors.append(Finding(check, f"unknown keyshape: {icon.keyshape!r}"))
        if icon.semantic_role is not None and icon.semantic_role not in SEMANTIC_ROLES:
            errors.append(Finding(
                check,
                f"semantic_role {icon.semantic_role!r} is not one of {list(SEMANTIC_ROLES)}",
            ))
        if not resolved:
            errors.append(Finding(check, "an icon must contain at least one primitive"))
        if icon.keyshape is Keyshape.FREE:
            self._check_free_approval(icon, errors)

    def _check_family(self, icon: "Icon", errors: list[Finding]) -> None:
        """A family authors on its own profile and no other.

        ``sub`` is SUB32, ``solo`` is SOLO48, ``container`` is CONTAINER64; the
        binding is read from the profile contract. An unfamilied draft (``family``
        None) is allowed here so a raw ``Icon`` can be validated while it is being
        worked on, but the registry never produces one and the record schema
        requires a family, so nothing unfamilied ships.
        """
        check = CHECK_ORDER[0]
        family = icon.family
        if family is None:
            return
        known = contracts.families()
        if family not in known:
            errors.append(Finding(
                check, f"unknown family {family!r}; known: {sorted(known)}",
            ))
            return
        owned = known[family]["profile"]
        if icon.profile.name != owned:
            errors.append(Finding(
                check,
                f"family {family!r} authors on {owned} only, but this icon is on "
                f"{icon.profile.name}; a {icon.profile.name} drawing belongs to the "
                f"{icon.profile.family!r} family and its folder",
                detail={"family": family, "profile": icon.profile.name, "owned": owned},
            ))

    def _check_free_approval(self, icon: "Icon", errors: list[Finding]) -> None:
        check = CHECK_ORDER[0]
        spec = icon.free_keyshape
        if spec is None:
            errors.append(Finding(check, "FREE requires a FreeKeyshapeSpec"))
            return
        if not spec.rationale:
            errors.append(Finding(check, "FREE requires a written rationale"))
        record = contracts.approved_free_keyshapes().get((icon.icon_id, icon.profile.name))
        if record is None:
            errors.append(Finding(
                check,
                f"FREE use of {icon.icon_id!r} has no approved record in "
                "contracts/exceptions.v1.json",
            ))
            return
        approved = tuple(record["bounds"])
        declared = (spec.left, spec.top, spec.right, spec.bottom)
        if approved != declared:
            errors.append(Finding(
                check,
                f"FREE bounds {declared} do not match approved bounds {approved}",
                detail={"declared": declared, "approved": approved},
            ))
        if spec.approval_id != record["approval_id"]:
            errors.append(Finding(
                check,
                f"FREE approval_id {spec.approval_id!r} does not match the "
                f"recorded {record['approval_id']!r}",
            ))
        status = record.get("status", "proposed")
        if self.require_free_approval and status != "approved":
            errors.append(Finding(
                check,
                f"FREE record for {icon.icon_id!r} is {status!r}; release requires "
                "'approved'. A human reviews the rationale and bounds, then sets it.",
            ))

    # -- 2. style / grid ---------------------------------------------------

    def _check_style_grid(
        self, icon: "Icon", resolved: list, errors: list[Finding]
    ) -> None:
        check = CHECK_ORDER[1]
        if icon.STROKE_WIDTH != STROKE_WIDTH:
            errors.append(Finding(check, f"stroke width must be {STROKE_WIDTH}, got {icon.STROKE_WIDTH}"))
        if icon.LINE_CAP != LINE_CAP:
            errors.append(Finding(check, f"line cap must be {LINE_CAP!r}, got {icon.LINE_CAP!r}"))
        if icon.LINE_JOIN != LINE_JOIN:
            errors.append(Finding(check, f"line join must be {LINE_JOIN!r}, got {icon.LINE_JOIN!r}"))
        if icon.GRID != GRID:
            errors.append(Finding(check, f"grid must be {GRID}, got {icon.GRID}"))
        for primitive in resolved:
            for label, point in (("start", primitive.start), ("end", primitive.end)):
                for axis, value in (("x", point.x), ("y", point.y)):
                    if not isinstance(value, int) or isinstance(value, bool):
                        errors.append(Finding(
                            check,
                            f"{label}.{axis} must be an integer on grid {GRID}, got {value!r}",
                            primitive.element_id,
                        ))
            if isinstance(primitive, Arc):
                for label, value in (("radius_x", primitive.radius_x), ("radius_y", primitive.radius_y)):
                    if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
                        errors.append(Finding(
                            check,
                            f"{label} must be a positive integer, got {value!r}",
                            primitive.element_id,
                        ))
            elif not isinstance(primitive, Line):
                errors.append(Finding(
                    check,
                    f"unsupported primitive type {type(primitive).__name__}",
                    primitive.element_id,
                ))

    # -- 3. canvas / keyshape bounds --------------------------------------

    def _check_bounds(
        self, icon: "Icon", resolved: list, errors: list[Finding]
    ) -> None:
        check = CHECK_ORDER[2]
        canvas = icon.profile.spec.canvas_size
        try:
            painted = envelope.visible_bounds(resolved)
        except (ValueError, ZeroDivisionError) as error:
            errors.append(Finding(check, f"cannot measure the painted envelope: {error}"))
            return

        limit = CANVAS_OVERFLOW_TOLERANCE + NUMERIC_EPSILON
        if (
            painted[0] < -limit or painted[1] < -limit
            or painted[2] > canvas + limit or painted[3] > canvas + limit
        ):
            errors.append(Finding(
                check,
                f"visible ink {_fmt(painted)} leaves the {canvas}x{canvas} canvas",
                detail={"painted": painted, "canvas": canvas},
            ))

        try:
            target = icon.keyshape_bounds()
        except ValueError as error:
            errors.append(Finding(check, f"cannot resolve keyshape bounds: {error}"))
            return

        if icon.keyshape.is_radial:
            self._check_radial_fit(icon, resolved, errors)
            return

        deltas = [abs(painted[index] - target[index]) for index in range(4)]
        if max(deltas) > RECT_FIT_TOLERANCE + NUMERIC_EPSILON:
            errors.append(Finding(
                check,
                f"visible ink {_fmt(painted)} does not match the "
                f"{icon.keyshape.name} envelope {_fmt(target)} "
                f"(deltas {[round(d, 4) for d in deltas]}, tolerance {RECT_FIT_TOLERANCE})",
                detail={"painted": painted, "target": target},
            ))

    def _check_radial_fit(
        self, icon: "Icon", resolved: list, errors: list[Finding]
    ) -> None:
        check = CHECK_ORDER[2]
        center = icon.profile.spec.center
        required = icon.keyshape.visible_radius_for(icon.profile)
        extent = envelope.visible_radial_extent(resolved, center)
        if extent > required + CANVAS_OVERFLOW_TOLERANCE + NUMERIC_EPSILON:
            errors.append(Finding(
                check,
                f"visible ink reaches radius {extent:.4f} about {center}, "
                f"outside the {icon.keyshape.name} radius {required}",
                detail={"extent": extent, "required": required},
            ))
        elif extent < required - CIRCLE_TOUCH_TOLERANCE - NUMERIC_EPSILON:
            errors.append(Finding(
                check,
                f"visible ink reaches only radius {extent:.4f} about {center}; "
                f"{icon.keyshape.name} requires at least "
                f"{required - CIRCLE_TOUCH_TOLERANCE} so the artwork touches its envelope",
                detail={"extent": extent, "required": required},
            ))

    # -- 4. minimum ink clearance -----------------------------------------

    def _check_mic(
        self,
        icon: "Icon",
        paths: list[dict],
        errors: list[Finding],
        warnings: list[Finding],
        drawing,
    ) -> bool:
        check = CHECK_ORDER[3]
        spec = icon.profile.spec
        payload = [
            {
                "elementId": path["id"],
                "commands": commands_for_path(path["primitives"], path["closed"]),
            }
            for path in paths
        ]
        if len(payload) < 2:
            return False
        review = False
        result = analyze_paths(
            payload,
            minimum_distance=float(spec.equal_stroke_centerline_min),
            stroke_width=float(STROKE_WIDTH),
        )
        if result["status"] == "pass":
            return False

        declared = _declared_connections(drawing)
        owners = dict(drawing.owners)
        unexplained = False
        for pair in result.get("pairs", []):
            if pair.get("status") == "pass":
                continue
            first, second = _pair_elements(pair)
            if first in owners and owners[first] == owners.get(second):
                # Both parts belong to one placed child, whose internal spacing
                # was already proved against its own profile when that icon was
                # validated. A SUB32 icon's parts are authored 32 units apart at
                # most; re-judging them at CONTAINER64's larger absolute minimum
                # would reject a legal child for being small, not for crowding.
                # Clearance between different participants is still checked here
                # at the parent's minimum.
                continue
            if frozenset((first, second)) in declared:
                # A declared contact is recorded, never a global bypass: it
                # excuses this pair only, and only for `connect`.
                continue
            unexplained = True
            distance = pair.get("centerlineDistance")
            near = pair.get("nearestPoints") or [None, None]
            location = f" nearest {_fmt(near[0])}<->{_fmt(near[1])}" if near[0] else ""
            measured = f"{distance:g}" if isinstance(distance, (int, float)) else "unresolved"
            finding = Finding(
                check,
                f"{first} and {second} are {measured} apart on centerlines"
                f"{location}; {icon.profile.name} requires at least "
                f"{spec.equal_stroke_centerline_min} (ink clearance {spec.mic}) "
                "unless the contact is declared with a scoped `connect` relationship",
                first,
                detail=pair,
            )
            if pair.get("status") == "review" or pair.get("ambiguousContact"):
                warnings.append(finding)
                review = True
            else:
                errors.append(finding)

        if result["status"] == "review" and not unexplained and not result.get("pairs"):
            # Only warn when no pair explains the verdict. If every non-passing
            # pair was excused by a scoped declaration, the engine's overall
            # `review` has already been accounted for, and repeating it as a
            # warning would make a correctly declared contact unshippable.
            warnings.append(Finding(
                check,
                "clearance could not be certified within the engine's numerical limits: "
                + "; ".join(result.get("errors", []) or ["work limits reached"]),
            ))
            return True
        if result["status"] == "fail" and not result.get("pairs"):
            # A structural failure (invalid input) carries no pair to point at,
            # so surface the engine's own message rather than nothing.
            for message in result.get("errors", []):
                errors.append(Finding(check, message))
        return review

    # -- 5. keyshape -------------------------------------------------------

    def _check_keyshape(self, icon: "Icon", errors: list[Finding]) -> None:
        check = CHECK_ORDER[4]
        if icon.keyshape is Keyshape.FREE:
            return
        table = contracts.keyshapes()["resolved"][icon.profile.name]
        row = table.get(icon.keyshape.name)
        if row is None:
            errors.append(Finding(check, f"{icon.keyshape.name} has no locked definition for {icon.profile.name}"))
            return
        resolved = list(icon.keyshape.bounds_for(icon.profile))
        if resolved != row["visible_bounds"]:
            errors.append(Finding(
                check,
                f"{icon.keyshape.name} resolved to {resolved}, contract says {row['visible_bounds']}",
            ))
        size = icon.keyshape.size_for(icon.profile)
        if [size.width, size.height] != [row["width"], row["height"]]:
            errors.append(Finding(
                check,
                f"{icon.keyshape.name} sized {size.width}x{size.height}, "
                f"contract says {row['width']}x{row['height']}",
            ))

    # -- 6. composition ----------------------------------------------------

    def _check_composition(self, icon: "Icon", errors: list[Finding]) -> None:
        check = CHECK_ORDER[5]
        templates = contracts.composition_templates()["classes"]
        template = templates.get(icon.composition_class)
        if template is None:
            errors.append(Finding(check, f"unknown composition class {icon.composition_class!r}"))
            return
        if not template.get("frozen", False):
            frozen = sorted(
                name for name, row in templates.items() if row.get("frozen", False)
            )
            errors.append(Finding(
                check,
                f"composition class {icon.composition_class!r} has no frozen template in "
                f"this release; available: {frozen}",
            ))
            return
        if icon.profile.name not in template["output_profiles"]:
            errors.append(Finding(
                check,
                f"{icon.composition_class} cannot emit {icon.profile.name}; "
                f"allowed: {template['output_profiles']}",
            ))
        role, kind = icon.semantic_role, icon.semantic_kind
        if role == "MAIN" and kind not in NOUN_KINDS:
            errors.append(Finding(
                check,
                f"role MAIN requires a noun, got semantic_kind {kind!r}",
            ))
        if role == "SUB" and kind not in SUB_KINDS:
            errors.append(Finding(
                check,
                f"role SUB requires a verb, state, or modifier, got semantic_kind {kind!r}",
            ))
        if role is None and icon.composition_class == "SOLO":
            errors.append(Finding(check, "a SOLO icon must declare a semantic role"))
        if "children" in template:
            self._check_children(icon, template, errors)

    def _check_children(self, icon: "Icon", template: dict, errors: list[Finding]) -> None:
        """Each participant is the profile the template names, at the position it names.

        This is the whole of the composition's geometric contract. Until
        2026-09-07 it also enforced a protected slot -- a reserved 32x32 the
        container's ink had to stay out of -- and that reservation is
        withdrawn; see ``composition-templates.v1.json``. What a container
        clears is now measured by the MIC check on the flattened drawing,
        which reads the ink that is actually there, rather than promised in
        advance by keeping a rectangle empty.
        """
        check = CHECK_ORDER[5]
        children = getattr(icon, "children", None)
        if children is None:
            errors.append(Finding(
                check,
                f"{icon.composition_class} needs placed children; "
                f"{type(icon).__name__} carries none",
            ))
            return
        expected = template["children"]
        limits = template.get("participants", {})
        if not limits.get("min", 0) <= len(children) <= limits.get("max", len(children)):
            errors.append(Finding(
                check,
                f"{icon.composition_class} takes {limits.get('min')}-{limits.get('max')} "
                f"participants, got {len(children)}",
            ))
            return

        # A composition constrains geometry, never the participant's semantic
        # kind. MAIN/SUB says what an icon is when it stands alone; what it
        # can play here is decided by whether it fits and clears. A noun is
        # welcome as content.
        content_size = Profile[expected[1]["profile"]].spec.canvas_size
        for spec, child in zip(expected, children):
            label = f"child {spec['index']} ({spec['slot_role']})"
            if child.icon.profile.name != spec["profile"]:
                errors.append(Finding(
                    check,
                    f"{label} must be {spec['profile']}, got "
                    f"{child.icon.profile.name}; the content region is "
                    f"{content_size}x{content_size} units",
                    child.icon.icon_id,
                ))
            position = [child.position.x, child.position.y]
            if position != spec["position"]:
                errors.append(Finding(
                    check,
                    f"{label} must sit at {spec['position']}, got {position}",
                    child.icon.icon_id,
                ))

        for spec, child in zip(expected, children):
            report = IconValidator(
                require_free_approval=self.require_free_approval
            ).validate(child.icon)
            if not report.ok:
                errors.append(Finding(
                    check,
                    f"child {spec['index']} ({spec['slot_role']}) is not a valid icon in "
                    f"its own right: {report.errors[0] if report.errors else report.status}",
                    child.icon.icon_id,
                ))

    # -- 7. SVG round-trip -------------------------------------------------

    def _check_round_trip(
        self,
        icon: "Icon",
        document: str,
        paths: list[dict],
        errors: list[Finding],
    ) -> None:
        check = CHECK_ORDER[6]
        canvas = icon.profile.spec.canvas_size
        try:
            parsed = parse_svg(document)
        except SvgRoundTripError as error:
            errors.append(Finding(check, str(error)))
            return
        if parsed.view_box != (0.0, 0.0, float(canvas), float(canvas)):
            errors.append(Finding(check, f"viewBox is {parsed.view_box}, expected (0, 0, {canvas}, {canvas})"))
        if (parsed.width, parsed.height) != (canvas, canvas):
            errors.append(Finding(check, f"size is {parsed.width}x{parsed.height}, expected {canvas}x{canvas}"))
        expected_style = {
            "fill": FILL, "stroke": STROKE, "stroke-width": str(STROKE_WIDTH),
            "stroke-linecap": LINE_CAP, "stroke-linejoin": LINE_JOIN,
        }
        if parsed.style != expected_style:
            errors.append(Finding(check, f"canonical style drift: {parsed.style} != {expected_style}"))
        expected_paths = tuple((path["id"], path["d"]) for path in paths)
        if parsed.paths != expected_paths:
            errors.append(Finding(
                check,
                "reparsed path data differs from the emitted scene",
                detail={"parsed": parsed.paths, "expected": expected_paths},
            ))

    # -- 8. reproducibility ------------------------------------------------

    def _check_reproducibility(self, icon: "Icon", document: str, errors: list[Finding]) -> None:
        check = CHECK_ORDER[7]
        if icon.to_svg() != document:
            errors.append(Finding(check, "two renders of the same model produced different SVG"))


def _fmt(values) -> str:
    if values is None:
        return "?"
    return "(" + ", ".join(f"{value:g}" for value in values) + ")"


def _pair_elements(pair: dict) -> tuple[str, str]:
    """Map a spacing pair back to the emitted path ids the author controls."""
    ids = (
        pair.get("closestContours")
        or pair.get("elementIds")
        or pair.get("contourIds")
        or ["?", "?"]
    )
    first = str(ids[0]).split(":subpath-")[0]
    second = str(ids[-1]).split(":subpath-")[0]
    return first, second


def _declared_connections(drawing) -> set[frozenset[str]]:
    """Contacts the author declared as intentional, narrowly scoped."""
    declared: set[frozenset[str]] = set()
    for relation in drawing.relationships:
        if relation.kind != "connect":
            continue
        members = list(relation.members)
        for index, first in enumerate(members):
            for second in members[index + 1:]:
                declared.add(frozenset((first, second)))
    return declared
