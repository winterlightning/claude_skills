"""The per-family slash skills are generated from the contracts and must be current.

``/icon-sub``, ``/icon-solo`` and ``/icon-container`` live in
``<repo>/.claude/skills/`` so Claude Code can invoke them. Each is pinned to one
family; these tests hold the generated files to the contract and refuse drift.
"""

from __future__ import annotations

import importlib.util
import re
import unittest
from pathlib import Path

from icon_set.model import contracts
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile

REPO_ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = REPO_ROOT / ".claude" / "skills"
GENERATOR = REPO_ROOT / "icon_set" / "scripts" / "generate_skills.py"


def _generator():
    spec = importlib.util.spec_from_file_location("icon_set._generate_skills", GENERATOR)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class GeneratedSkillTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.gen = _generator()

    def _path(self, family: str) -> Path:
        return SKILLS_DIR / f"icon-{family}" / "SKILL.md"

    def test_one_skill_per_family_exists(self) -> None:
        for family in contracts.families():
            with self.subTest(family=family):
                self.assertTrue(self._path(family).is_file(), f"run scripts/generate_skills.py")
        # Hand-authored skills may sit alongside these (`/icon-brief` writes the
        # briefs the family skills are then run against). What must hold is that
        # every *generated* skill belongs to a family: a leftover icon-<family>
        # for a family the contract has dropped would still be invocable.
        generated = sorted(
            path.name for path in SKILLS_DIR.glob("icon-*")
            if (path / "SKILL.md").is_file()
            and "Generated from the contracts" in (path / "SKILL.md").read_text(encoding="utf-8")
        )
        self.assertEqual(generated, sorted(f"icon-{f}" for f in contracts.families()))

    def test_generated_files_are_current(self) -> None:
        for family in contracts.families():
            with self.subTest(family=family):
                self.assertEqual(
                    self._path(family).read_text(encoding="utf-8"),
                    self.gen.render(family),
                    "stale; run python3 icon_set/scripts/generate_skills.py",
                )

    def test_frontmatter_is_loadable(self) -> None:
        for family in contracts.families():
            text = self._path(family).read_text(encoding="utf-8")
            with self.subTest(family=family):
                self.assertTrue(text.startswith("---\n"))
                block = text.split("---", 2)[1]
                self.assertRegex(block, rf"(?m)^name: icon-{family}$")
                self.assertRegex(block, r"(?m)^description: .+")
                self.assertIn("$ARGUMENTS", text)

    def test_each_skill_is_pinned_to_its_own_family_only(self) -> None:
        for family, row in contracts.families().items():
            text = self._path(family).read_text(encoding="utf-8")
            profile = Profile.for_family(family)
            with self.subTest(family=family):
                self.assertIn(f"| Family | `{family}` |", text)
                self.assertIn(f"| Profile | `{row['profile']}` |", text)
                self.assertIn(f"Subclass | `{row['base_class']}`", text)
                self.assertIn(f"icon_set/{row['package']}/", text)
                self.assertIn(f"icon_set/{row['dist']}/", text)
                self.assertIn(f"build.py --family {family}", text)
                # Other families appear only as hand-off pointers.
                for other, other_row in contracts.families().items():
                    if other == family:
                        continue
                    self.assertIn(f"`/icon-{other}`", text)
                    self.assertNotIn(f"class <ClassName>({other_row['base_class']})", text)
                self.assertNotIn("MAIN48", text)
                self.assertNotIn("COMPOSITE64", text)
                self.assertEqual(profile.spec.canvas_size, int(row["profile"][-2:]))

    def test_numbers_match_the_contract(self) -> None:
        for family in contracts.families():
            text = self._path(family).read_text(encoding="utf-8").replace(" ", "")
            profile = Profile.for_family(family)
            spec = profile.spec
            with self.subTest(family=family):
                self.assertIn(f"|{spec.mic}betweendistinctparts=**{spec.equal_stroke_centerline_min}betweencenterlines**", text)
                for shape in Keyshape:
                    if shape is Keyshape.FREE or shape.is_radial:
                        continue
                    left, top, right, bottom = shape.bounds_for(profile)
                    self.assertIn(f"({left},{top})-({right},{bottom})", text)
                    self.assertIn(f"({left + 2},{top + 2})-({right - 2},{bottom - 2})", text)
                radius = int(Keyshape.CIRCLE.visible_radius_for(profile))
                self.assertIn(f"radius{radius}about{spec.center}".replace(" ", ""), text)

    def test_every_shared_doc_the_skills_point_at_exists(self) -> None:
        pattern = re.compile(r"`(icon_set/[A-Za-z0-9_./-]+\.md)`")
        for family in contracts.families():
            text = self._path(family).read_text(encoding="utf-8")
            for quoted in set(pattern.findall(text)):
                with self.subTest(family=family, path=quoted):
                    self.assertTrue((REPO_ROOT / quoted).is_file(), quoted)

    def test_check_mode_passes_when_current(self) -> None:
        self.assertEqual(self.gen.write_all(check_only=True), 0)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
