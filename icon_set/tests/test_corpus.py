"""Every registered icon must pass every locked rule, with no review verdicts."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from icon_set.model import contracts
from icon_set.model.icons import registry
from icon_set.model.icons.registry import all_icons, create, icon_ids, icons_in
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.renderers.svg import render_svg

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
DIST = PACKAGE_ROOT / "dist"


def dist_dir(family: str) -> Path:
    return PACKAGE_ROOT / contracts.families()[family]["dist"]


class CorpusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.icons = list(all_icons())

    def test_the_corpus_is_not_empty(self) -> None:
        self.assertGreaterEqual(len(self.icons), 50)

    def test_every_icon_validates(self) -> None:
        for icon in self.icons:
            with self.subTest(icon=icon.icon_id):
                report = icon.validate_icon()
                self.assertEqual(report.status, "valid", report.describe())

    def test_no_icon_returns_an_uncertified_review(self) -> None:
        """A REVIEW verdict means a rule could not be proved, not that it passed."""
        for icon in self.icons:
            with self.subTest(icon=icon.icon_id):
                self.assertEqual(icon.validate_icon().warnings, ())

    def test_each_family_ships_its_own_profile_and_no_other(self) -> None:
        """sub is SUB32, solo is SOLO48, container is CONTAINER64 -- one-to-one."""
        bases = registry.families()
        self.assertEqual(set(bases), {"sub", "solo", "container"})
        expected = {
            "sub": Profile.SUB32, "solo": Profile.SOLO48, "container": Profile.CONTAINER64,
        }
        for icon in self.icons:
            with self.subTest(icon=icon.icon_id):
                owners = [name for name, base in bases.items() if isinstance(icon, base)]
                self.assertEqual(len(owners), 1, f"{icon.icon_id} belongs to {owners}")
                family = owners[0]
                self.assertEqual(icon.family, family)
                self.assertIs(icon.profile, expected[family])
                self.assertIs(icon.profile, Profile.for_family(family))
                if family != "sub":
                    self.assertEqual(icon.semantic_role, "MAIN")

    def test_every_profile_has_shipped_icons(self) -> None:
        """No profile in the contract is dead: each family has at least one icon."""
        for family in contracts.families():
            with self.subTest(family=family):
                self.assertTrue(list(icons_in(family)), f"{family} ships nothing")

    def test_each_icon_lives_in_its_familys_folder(self) -> None:
        for icon in self.icons:
            package = contracts.families()[icon.family]["package"].rsplit("/", 1)[-1]
            with self.subTest(icon=icon.icon_id):
                self.assertIn(f".icons.{package}.", type(icon).__module__)

    def test_no_geometry_is_shared_between_profiles(self) -> None:
        """A profile sibling is separately authored, never a scaled copy."""
        by_profile: dict[str, set[tuple]] = {}
        for icon in self.icons:
            shape = tuple(
                (p.element_id, p.start.as_tuple(), p.end.as_tuple())
                for p in icon.draw().primitives
            )
            by_profile.setdefault(icon.profile.name, set()).add(shape)
        profiles = list(by_profile)
        for index, first in enumerate(profiles):
            for second in profiles[index + 1:]:
                with self.subTest(pair=(first, second)):
                    self.assertEqual(by_profile[first] & by_profile[second], set())

    def test_ids_are_unique_and_sorted(self) -> None:
        ids = icon_ids()
        self.assertEqual(list(ids), sorted(set(ids)))

    def test_every_free_use_is_approved(self) -> None:
        approved = contracts.approved_free_keyshapes()
        for icon in self.icons:
            if icon.keyshape is not Keyshape.FREE:
                continue
            with self.subTest(icon=icon.icon_id):
                self.assertIn((icon.icon_id, icon.profile.name), approved)

    def test_free_is_the_exception_not_the_rule(self) -> None:
        free = [icon for icon in self.icons if icon.keyshape is Keyshape.FREE]
        self.assertLess(len(free), len(self.icons) // 4)

    def test_every_standard_keyshape_is_exercised(self) -> None:
        used = {icon.keyshape for icon in self.icons}
        for shape in Keyshape:
            with self.subTest(keyshape=shape.name):
                self.assertIn(shape, used)

    def test_records_carry_the_required_metadata(self) -> None:
        for icon in self.icons:
            with self.subTest(icon=icon.icon_id):
                record = icon.to_record()
                for field in (
                    "icon_id", "category", "profile", "semantic_role",
                    "semantic_kind", "composition_class", "keyshape",
                    "keyshape_bounds", "primitives", "style",
                ):
                    self.assertIn(field, record)
                self.assertTrue(record["primitives"])

    def test_registry_creates_fresh_instances(self) -> None:
        first, second = create("plus"), create("plus")
        self.assertIsNot(first, second)
        self.assertEqual(render_svg(first), render_svg(second))

    def test_unknown_id_fails(self) -> None:
        with self.assertRaises(KeyError):
            create("no-such-icon")


class DistTests(unittest.TestCase):
    """The committed build must match what the model renders right now.

    Each family ships to its own folder with its own manifest, and the folders
    never mix profiles.
    """

    def setUp(self) -> None:
        missing = [f for f in contracts.families() if not (dist_dir(f) / "manifest.json").is_file()]
        if missing:
            self.skipTest(f"dist/ not built for {missing}; run scripts/build.py")

    def test_each_family_manifest_matches_the_registry(self) -> None:
        for family in contracts.families():
            manifest = json.loads((dist_dir(family) / "manifest.json").read_text())
            with self.subTest(family=family):
                self.assertEqual(manifest["family"], family)
                self.assertEqual(manifest["profile"], Profile.for_family(family).name)
                self.assertEqual(
                    [record["icon_id"] for record in manifest["icons"]],
                    [icon.icon_id for icon in icons_in(family)],
                )
                self.assertEqual({r["profile"] for r in manifest["icons"]}, {manifest["profile"]})
                self.assertEqual({r["family"] for r in manifest["icons"]}, {family})

    def test_family_folders_do_not_share_icons(self) -> None:
        seen: dict[str, str] = {}
        for family in contracts.families():
            for path in dist_dir(family).glob("*.svg"):
                self.assertNotIn(path.stem, seen, f"{path.stem} in {family} and {seen.get(path.stem)}")
                seen[path.stem] = family
        self.assertEqual(sorted(seen), sorted(icon_ids()))

    def test_no_legacy_mixed_folder_remains(self) -> None:
        self.assertFalse((DIST / "primitives").exists(), "dist/primitives mixed two profiles")

    def test_exported_svg_matches_the_model(self) -> None:
        for icon in all_icons():
            path = dist_dir(icon.family) / f"{icon.icon_id}.svg"
            with self.subTest(icon=icon.icon_id):
                self.assertTrue(path.is_file(), f"missing {path}")
                self.assertEqual(path.read_text(), render_svg(icon))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
