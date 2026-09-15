"""The skill documentation must stay true to the contracts it describes.

Docs drift silently. These tests fail loudly instead: every internal link has to
resolve, every path the skill points an agent at has to exist, and the numbers
quoted in prose have to match the frozen contracts.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

from icon_set.model import contracts
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
SKILL = PACKAGE_ROOT / "skills" / "icon-design"
DOCS = sorted(SKILL.glob("*.md"))
LINK = re.compile(r"\]\(([^)#]+)(?:#[^)]*)?\)")
BACKTICK_PATH = re.compile(r"`(icon_set/[A-Za-z0-9_./*-]+)`")


class SkillStructureTests(unittest.TestCase):
    def test_the_skill_exists_with_an_entrypoint(self) -> None:
        self.assertTrue((SKILL / "SKILL.md").is_file())
        self.assertGreaterEqual(len(DOCS), 7)

    def test_frontmatter_makes_it_loadable(self) -> None:
        text = (SKILL / "SKILL.md").read_text()
        self.assertTrue(text.startswith("---\n"))
        block = text.split("---", 2)[1]
        self.assertRegex(block, r"(?m)^name: icon-design$")
        self.assertIn("description:", block)

    def test_every_internal_link_resolves(self) -> None:
        for doc in DOCS:
            for target in LINK.findall(doc.read_text()):
                if target.startswith(("http", "mailto")):
                    continue
                with self.subTest(doc=doc.name, target=target):
                    self.assertTrue((doc.parent / target).resolve().exists())

    def test_every_referenced_repository_path_exists(self) -> None:
        repo = PACKAGE_ROOT.parent
        for doc in DOCS:
            for quoted in BACKTICK_PATH.findall(doc.read_text()):
                if "*" in quoted:
                    continue
                with self.subTest(doc=doc.name, path=quoted):
                    self.assertTrue((repo / quoted).exists(), quoted)


class QuotedNumberTests(unittest.TestCase):
    """Numbers repeated in prose must match the machine-readable source."""

    def setUp(self) -> None:
        self.fitting = (SKILL / "keyshape-fitting.md").read_text()

    def test_every_profiles_keyshape_table_matches_the_contract(self) -> None:
        """All three families get a ready-to-use table, not just SUB32."""
        squashed = self.fitting.replace(" ", "")
        for profile in Profile:
            for shape in Keyshape:
                if shape is Keyshape.FREE or shape.is_radial:
                    continue
                left, top, right, bottom = shape.bounds_for(profile)
                visible = f"({left},{top})-({right},{bottom})"
                centerline = f"({left + 2},{top + 2})-({right - 2},{bottom - 2})"
                with self.subTest(profile=profile.name, keyshape=shape.name):
                    self.assertIn(visible, squashed)
                    self.assertIn(centerline, squashed)

    def test_circle_radii_match(self) -> None:
        for profile in Profile:
            visible = int(Keyshape.CIRCLE.visible_radius_for(profile))
            centre = profile.spec.center
            with self.subTest(profile=profile.name):
                self.assertIn(f"radius {visible} about {centre}".replace(" ", ""), self.fitting.replace(" ", ""))
                self.assertIn(f"radius {visible - 2}", self.fitting)

    def test_the_family_table_names_every_binding(self) -> None:
        text = (SKILL / "SKILL.md").read_text()
        for family, row in contracts.families().items():
            with self.subTest(family=family):
                self.assertIn(f"`{family}`", text)
                self.assertIn(f"`{row['profile']}`", text)
                self.assertIn(f"`{row['package'].rsplit('/', 1)[-1]}/`", text)

    def test_no_document_uses_a_retired_profile_name(self) -> None:
        for doc in DOCS + [PACKAGE_ROOT / "README.md"]:
            text = doc.read_text()
            with self.subTest(doc=doc.name):
                for retired in ("MAIN48", "COMPOSITE64", "Primitive32", "Solo64", "build_primitives"):
                    self.assertNotIn(retired, text)

    def test_mic_values_match_the_contract(self) -> None:
        text = (SKILL / "authoring.md").read_text()
        mic = [Profile[name].spec.mic for name in ("SUB32", "SOLO48", "CONTAINER64")]
        centerline = [
            Profile[name].spec.equal_stroke_centerline_min
            for name in ("SUB32", "SOLO48", "CONTAINER64")
        ]
        self.assertIn(" / ".join(str(v) for v in mic), text)
        self.assertIn(" / ".join(str(v) for v in centerline), text)

    def test_check_names_match_the_validator(self) -> None:
        from icon_set.validation.report import CHECK_ORDER

        text = (SKILL / "validation.md").read_text()
        for check in CHECK_ORDER:
            with self.subTest(check=check):
                self.assertIn(f"`{check}`", text)

    def test_free_icons_named_in_the_docs_really_use_free(self) -> None:
        from icon_set.model.icons.registry import create

        match = re.search(r"Six do in this set — ([^—]+?) — because", self.fitting)
        assert match, "the FREE list paragraph changed shape"
        names = [n.strip().strip("`") for n in match.group(1).split(",")]
        self.assertEqual(len(names), 6)
        for name in names:
            with self.subTest(icon=name):
                self.assertIs(create(name).keyshape, Keyshape.FREE)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
