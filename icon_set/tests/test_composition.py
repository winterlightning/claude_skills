"""The frozen CONTAINER_COMBINE template.

Its protected slot was withdrawn on 2026-09-07 -- see
``contracts/composition-templates.v1.json``. What a container clears is now
measured per pair by the ``mic`` check on the flattened composition rather
than reserved in advance, so these tests assert the measurement, and assert
that the reservation is really gone.
"""

from __future__ import annotations

import unittest

from icon_set.model import contracts
from icon_set.model.icons.base import Icon
from icon_set.model.icons.combined import CombinedIcon
from icon_set.model.icons import registry
from icon_set.model.icons.registry import create
from icon_set.model.keyshapes import Keyshape
from icon_set.model.position import Position
from icon_set.model.profiles import Profile
from icon_set.scripts_compose import compose  # noqa: F401  (see conftest note)
from icon_set.validation import slots

CLASSES = contracts.composition_templates()["classes"]
TEMPLATE = CLASSES["CONTAINER_COMBINE"]
CONTENT = TEMPLATE["children"][1]
#: Where a hosted child lands. Advisory: nothing forbids container ink here.
CONTENT_REGION = (
    float(CONTENT["position"][0]),
    float(CONTENT["position"][1]),
    float(CONTENT["position"][0] + Profile[CONTENT["profile"]].spec.canvas_size),
    float(CONTENT["position"][1] + Profile[CONTENT["profile"]].spec.canvas_size),
)


def sub(icon_id: str = "mark", keyshape: Keyshape = Keyshape.SQUARE) -> Icon:
    icon = Icon(icon_id, Profile.SUB32, semantic_role="SUB", keyshape=keyshape)
    icon.semantic_kind = "state"
    return icon


def errors_for(icon: Icon, check: str) -> list[str]:
    return [line for line in icon.validate_icon().errors if line.startswith(check)]


class ContentRegionTests(unittest.TestCase):
    """``slots`` survives as a measuring tool; it no longer enforces anything."""

    def test_the_content_region_is_the_sub32_canvas_centred_on_container64(self) -> None:
        canvas = Profile.CONTAINER64.spec.canvas_size
        inset = (canvas - Profile.SUB32.spec.canvas_size) / 2
        self.assertEqual(
            CONTENT_REGION, (inset, inset, canvas - inset, canvas - inset)
        )

    def test_distance_is_zero_inside_the_region(self) -> None:
        self.assertEqual(slots.point_to_rect(32, 32, CONTENT_REGION), 0.0)

    def test_distance_is_exact_for_a_straight_segment(self) -> None:
        from icon_set.model.primitives import Line, Point

        line = Line("a", Point(2, 32), Point(8, 32))
        self.assertAlmostEqual(slots.distance_to_rect(line, CONTENT_REGION), 8.0)


class WithdrawnSlotTests(unittest.TestCase):
    def test_the_template_no_longer_carries_a_slot(self) -> None:
        self.assertNotIn("slot", TEMPLATE)
        self.assertIn("withdrawn_slot", TEMPLATE)
        self.assertEqual(TEMPLATE["withdrawn_slot"]["was"], [16, 16, 48, 48])

    def test_a_container_may_paint_inside_the_content_region(self) -> None:
        """The case the reservation used to forbid, and the reason it went.

        browser-window's divider crosses the old slot's top edge. Under the
        slot rule it was an error and the icon could not be drawn; now it is
        just ink, and the icon validates.
        """
        window = create("browser-window")
        found = slots.intrusions(window.primitives, CONTENT_REGION)
        self.assertTrue(found, "expected the title-bar divider to cross the region")
        self.assertEqual(window.validate_icon().status, "valid")

    def test_an_open_container_still_hosts_everything(self) -> None:
        """Withdrawing the reservation took nothing away from containers that had room."""
        for host in ("container-circle", "container-square", "container-rounded-square"):
            for content in ("plus", "heart", "check"):
                with self.subTest(host=host, content=content):
                    report = compose(host, content).validate_icon()
                    self.assertEqual(report.status, "valid", report.describe())

    def test_hosting_is_now_a_measured_fact_not_a_guarantee(self) -> None:
        """A container with real interior furniture may simply not fit a child.

        That is reported by `mic`, against the ink that is actually there,
        and it is a fact about the pair rather than a defect in the container.
        """
        report = compose("browser-window", "circle").validate_icon()
        self.assertEqual(report.status, "invalid")
        self.assertTrue(any(line.startswith("mic") for line in report.errors))
        self.assertEqual(create("browser-window").validate_icon().status, "valid")


class ContainerCombineTests(unittest.TestCase):

    def test_a_valid_composition_passes_every_check(self) -> None:
        combined = compose("container-circle", "plus")
        report = combined.validate_icon()
        self.assertEqual(report.status, "valid", report.describe())
        self.assertIs(combined.profile, Profile.CONTAINER64)

    def test_wrong_child_position_fails(self) -> None:
        combined = CombinedIcon(
            "bad", "CONTAINER_COMBINE", Keyshape.CIRCLE,
            icons=[create("container-circle"), create("plus")],
            positions=[Position(0, 0), Position(12, 16)],
        )
        failures = errors_for(combined, "composition")
        self.assertTrue(any("must sit at [16, 16]" in line for line in failures))

    def test_a_noun_may_be_hosted_as_content(self) -> None:
        """A slot constrains geometry, never the participant's semantic kind.

        heart and circle are nouns that stand alone as MAIN. Both are also
        perfectly good content inside a container, and an earlier version
        rejected them for it.
        """
        for content in ("heart", "circle", "star", "square"):
            with self.subTest(content=content):
                icon = create(content)
                self.assertEqual(icon.semantic_role, "MAIN")
                self.assertEqual(icon.semantic_kind, "noun")
                report = compose("container-circle", content).validate_icon()
                self.assertEqual(report.status, "valid", report.describe())

    def test_the_composed_record_carries_the_contextual_role(self) -> None:
        """`semantic_role` stays the icon's own; `slot_role` says what it does here."""
        children = compose("container-circle", "heart").to_record()["children"]
        self.assertEqual([c["slot_role"] for c in children], ["container", "content"])
        self.assertEqual(children[1]["icon_id"], "heart")
        self.assertEqual(children[1]["semantic_role"], "MAIN")

    def test_content_that_cannot_fit_the_slot_is_rejected_on_size(self) -> None:
        """The rejection that remains is geometric, and says so."""
        combined = CombinedIcon(
            "bad", "CONTAINER_COMBINE", Keyshape.CIRCLE,
            icons=[create("container-circle"), create("container-square")],
            positions=[Position(0, 0), Position(16, 16)],
        )
        failures = errors_for(combined, "composition")
        self.assertTrue(any("must be SUB32" in line for line in failures))
        self.assertTrue(any("32x32 units" in line for line in failures))

    def test_wrong_participant_count_fails(self) -> None:
        combined = CombinedIcon(
            "bad", "CONTAINER_COMBINE", Keyshape.CIRCLE,
            icons=[create("container-circle")], positions=[Position(0, 0)],
        )
        self.assertTrue(errors_for(combined, "composition"))

    def test_compose_refuses_an_unfrozen_class_by_name(self) -> None:
        from icon_set.scripts_compose import frozen_classes, template

        unfrozen = [n for n, row in CLASSES.items() if not row.get("frozen")]
        for name in unfrozen:
            with self.subTest(composition_class=name):
                with self.assertRaises(ValueError) as caught:
                    template(name)
                self.assertIn("no frozen arrangement", str(caught.exception))
        self.assertEqual(frozen_classes(), ["CONTAINER_COMBINE"])

    def test_unfrozen_classes_are_still_rejected(self) -> None:
        """Read from the contract, so freezing one does not leave this stale."""
        unfrozen = [n for n, row in CLASSES.items() if not row.get("frozen")]
        self.assertTrue(unfrozen)
        for name in unfrozen:
            with self.subTest(composition_class=name):
                combined = CombinedIcon(
                    "x", name, Keyshape.CIRCLE,
                    icons=[create("container-circle"), create("plus")],
                    positions=[Position(0, 0), Position(16, 16)],
                )
                failures = errors_for(combined, "composition")
                self.assertTrue(any("no frozen template" in line for line in failures))


class ParticipantScopeTests(unittest.TestCase):
    """A child's internal spacing is judged at its own profile, not the parent's."""

    def test_a_childs_own_spacing_is_not_rejudged_at_the_parent_scale(self) -> None:
        # skip-forward's wedge and rail sit 8 units apart: legal at SUB32, whose
        # minimum is 7. CONTAINER64's minimum is 10, so re-judging the child at
        # the parent's scale would reject it for being small rather than crowded.
        standalone = create("skip-forward")
        self.assertEqual(standalone.validate_icon().status, "valid")
        self.assertEqual(compose("container-square", "skip-forward").validate_icon().status, "valid")

    def test_clearance_between_participants_is_still_checked(self) -> None:
        """A window's title-bar divider genuinely crowds a full-height child.

        This is the check that replaced the protected slot. Nothing forbids
        the divider from crossing where a child would sit; the composition is
        simply measured, and this pair does not clear.
        """
        report = compose("browser-window", "circle").validate_icon()
        self.assertEqual(report.status, "invalid")
        self.assertTrue(any(line.startswith("mic") for line in report.errors))

    def test_element_ownership_is_explicit_and_excludes_parent_geometry(self) -> None:
        combined = compose("container-square", "plus")
        combined.add_line("1:fake:parent", (1, 1), (2, 2))
        drawing = combined.draw()
        owners = dict(drawing.owners)
        self.assertEqual(owners["0:container-square:outline"], 0)
        self.assertEqual(owners["1:plus:bar-horizontal"], 1)
        self.assertNotIn("1:fake:parent", owners)

    def test_a_child_must_be_a_valid_icon_in_its_own_right(self) -> None:
        broken = sub("broken", Keyshape.SQUARE)
        broken.add_polyline("outline", (8, 8), (24, 8), (24, 24), (8, 24), closed=True)
        combined = CombinedIcon(
            "bad", "CONTAINER_COMBINE", Keyshape.CIRCLE,
            icons=[create("container-circle"), broken],
            positions=[Position(0, 0), Position(16, 16)],
        )
        failures = errors_for(combined, "composition")
        self.assertTrue(any("valid icon in its own right" in line for line in failures))


class ResolvedGeometryTests(unittest.TestCase):
    """A composite's geometry lives in its children, not in `.primitives`."""

    def test_a_composite_is_measured_from_its_resolved_drawing(self) -> None:
        combined = compose("container-square", "check")
        self.assertEqual(combined.primitives, [])
        self.assertTrue(combined.draw().primitives)
        self.assertEqual(combined.validate_icon().status, "valid")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
