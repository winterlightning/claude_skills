"""Family, folder and profile are one binding, enforced three ways.

``sub`` is SUB32, ``solo`` is SOLO48, ``container`` is CONTAINER64. A family
base cannot be talked onto another canvas, the registry refuses a module in the
wrong folder, and the validator rejects an icon whose profile is not its
family's. Each guard is tested on its own so a regression in one cannot hide
behind another.
"""

from __future__ import annotations

import types
import unittest

from icon_set.model import contracts
from icon_set.model.icons import registry
from icon_set.model.icons.base import Icon
from icon_set.model.icons.container._base import Container64
from icon_set.model.icons.family import FamilyIcon
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile


class ContractBindingTests(unittest.TestCase):
    def test_the_contract_binds_each_family_to_one_profile_folder_and_dist(self) -> None:
        families = contracts.families()
        self.assertEqual(list(families), ["sub", "solo", "container"])
        self.assertEqual(
            {name: row["profile"] for name, row in families.items()},
            {"sub": "SUB32", "solo": "SOLO48", "container": "CONTAINER64"},
        )
        self.assertEqual(
            {name: row["package"].rsplit("/", 1)[-1] for name, row in families.items()},
            {"sub": "sub", "solo": "solo", "container": "container"},
        )
        self.assertEqual(
            {name: row["dist"].rsplit("/", 1)[-1] for name, row in families.items()},
            {"sub": "sub32", "solo": "solo48", "container": "container64"},
        )

    def test_profiles_point_back_at_their_family(self) -> None:
        for name, row in contracts.families().items():
            with self.subTest(family=name):
                self.assertEqual(contracts.family_for_profile(row["profile"]), name)


class FamilyBaseTests(unittest.TestCase):
    def test_each_base_authors_on_its_own_profile(self) -> None:
        for base, profile in (
            (Sub32, Profile.SUB32), (Solo48, Profile.SOLO48), (Container64, Profile.CONTAINER64),
        ):
            class Probe(base):  # type: ignore[misc, valid-type]
                icon_id = "probe"
                keyshape = Keyshape.SQUARE

                def build(self) -> None:
                    left, top, right, bottom = self.keyshape_bounds()
                    self.add_polyline(
                        "outline", (left + 2, top + 2), (right - 2, top + 2),
                        (right - 2, bottom - 2), (left + 2, bottom - 2), closed=True,
                    )

            with self.subTest(base=base.__name__):
                icon = Probe()
                self.assertIs(icon.profile, profile)
                self.assertEqual(icon.family, profile.family)
                self.assertEqual(icon.profile.spec.canvas_size, int(profile.name[-2:]))
                self.assertEqual(icon.validate_icon().status, "valid")

    def test_a_subclass_cannot_choose_another_familys_canvas(self) -> None:
        """The profile is not a class attribute; there is nothing to override."""
        class Rogue(Solo48):
            icon_id = "rogue"
            profile = Profile.CONTAINER64  # ignored: the family decides

            def build(self) -> None:
                self.add_line("a", (5, 24), (43, 24))

        self.assertIs(Rogue().profile, Profile.SOLO48)

    def test_a_base_without_a_family_is_abstract(self) -> None:
        class Nameless(FamilyIcon):
            icon_id = "x"

            def build(self) -> None:  # pragma: no cover
                pass

        with self.assertRaises(TypeError):
            Nameless()

    def test_container_base_places_the_content_anchors(self) -> None:
        """Advisory anchors: where a hosted child lands, not a region to avoid."""
        icon = registry.create("container-circle")
        self.assertEqual(icon.anchors["content-top-left"].as_tuple(), (16, 16))
        self.assertEqual(icon.anchors["content-bottom-right"].as_tuple(), (48, 48))

    def test_a_container_may_paint_through_the_content_region(self) -> None:
        """The protected slot was withdrawn, so interior ink is no longer an error."""
        icon = registry.create("browser-window")
        report = icon.validate_icon()
        self.assertEqual(report.status, "valid", report.describe())
        divider = next(p for p in icon.primitives if p.element_id == "divider")
        self.assertEqual(divider.start.y, 22)
        self.assertGreater(divider.start.y + 2, 16)


class RegistryFolderTests(unittest.TestCase):
    def test_families_resolve_to_their_bases(self) -> None:
        self.assertEqual(
            registry.families(), {"sub": Sub32, "solo": Solo48, "container": Container64}
        )

    def test_every_module_in_a_family_folder_is_discovered(self) -> None:
        for family in contracts.families():
            with self.subTest(family=family):
                modules = registry._modules(family)
                self.assertTrue(modules)
                self.assertTrue(all(m.startswith(family + ".") for m in modules))
                self.assertFalse(any(m.endswith("._base") for m in modules))

    def test_a_module_in_the_wrong_folder_is_refused(self) -> None:
        """A Solo48 dropped into sub/ must fail loudly, never build on SUB32."""
        module = types.ModuleType("icon_set.model.icons.sub.stray")

        class Stray(Solo48):
            icon_id = "stray"

            def build(self) -> None:  # pragma: no cover
                pass

        Stray.__module__ = module.__name__
        module.Stray = Stray  # type: ignore[attr-defined]
        with self.assertRaises(TypeError) as caught:
            registry._collect(module, "sub", Sub32, registry.families(), {})
        message = str(caught.exception)
        self.assertIn("'solo'", message)
        self.assertIn("'sub'", message)

    def test_icons_in_returns_only_that_family(self) -> None:
        for family in contracts.families():
            with self.subTest(family=family):
                icons = list(registry.icons_in(family))
                self.assertTrue(icons)
                self.assertEqual({icon.family for icon in icons}, {family})
                self.assertEqual({icon.profile for icon in icons}, {Profile.for_family(family)})


class ValidatorFamilyTests(unittest.TestCase):
    def _draft(self, family: str | None, profile: Profile) -> Icon:
        icon = Icon("draft", profile, semantic_role="SUB", keyshape=Keyshape.SQUARE)
        icon.family = family
        icon.semantic_kind = "state"
        left, top, right, bottom = icon.keyshape_bounds()
        icon.add_polyline(
            "outline", (left + 2, top + 2), (right - 2, top + 2),
            (right - 2, bottom - 2), (left + 2, bottom - 2), closed=True,
        )
        return icon

    def test_a_family_on_the_wrong_profile_fails_schema_profile(self) -> None:
        for family, wrong in (("sub", Profile.SOLO48), ("solo", Profile.CONTAINER64), ("container", Profile.SUB32)):
            with self.subTest(family=family, profile=wrong.name):
                errors = [
                    line for line in self._draft(family, wrong).validate_icon().errors
                    if line.startswith("schema/profile")
                ]
                self.assertTrue(errors, "mismatch went unreported")
                self.assertIn(f"family '{family}'", errors[0])
                self.assertIn(wrong.name, errors[0])

    def test_a_family_on_its_own_profile_passes(self) -> None:
        for family in contracts.families():
            with self.subTest(family=family):
                report = self._draft(family, Profile.for_family(family)).validate_icon()
                self.assertFalse([e for e in report.errors if "family" in e], report.describe())

    def test_an_unknown_family_is_rejected(self) -> None:
        errors = self._draft("primitive", Profile.SUB32).validate_icon().errors
        self.assertTrue(any("unknown family 'primitive'" in line for line in errors))

    def test_an_unfamilied_draft_is_tolerated_but_never_shipped(self) -> None:
        draft = self._draft(None, Profile.SUB32)
        self.assertFalse([e for e in draft.validate_icon().errors if "family" in e])
        self.assertIsNone(draft.to_record()["family"])
        for icon in registry.all_icons():
            self.assertIsNotNone(icon.family)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
