#!/usr/bin/env python3
"""Size classifier tests: threshold boundary, preserved container verdicts, dry run."""
from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

import classify_icon_type


def prototype(width: float, height: float = 2.0) -> str:
    # A horizontal stroke: painted width = length + stroke, painted height = stroke.
    length = width - 1.5
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="-1 -1 26 26" width="96" height="96">'
            f'<path d="M0 12 L{length:g} 12" fill="none" stroke="#111827" stroke-width="1.5"/></svg>\n')


class ClassifyIconTypeTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.batch = Path(self.temp.name) / "batch-01"

    def symbol(self, sid: str, width: float) -> Path:
        folder = self.batch / sid
        folder.mkdir(parents=True)
        (folder / f"{sid}_prototype.svg").write_text(prototype(width))
        (folder / "description.txt").write_text("Symbol ID: " + sid)
        return folder

    def run_classifier(self, **kwargs) -> list[dict]:
        options = {"sub_max": classify_icon_type.SUB_MAX, "include_stroke": True, "overwrite": False, "dry_run": False}
        options.update(kwargs)
        return [classify_icon_type.classify_prototype(path, **options)
                for path in classify_icon_type.prototypes([str(self.batch)])]

    def test_threshold_is_inclusive_at_half_the_art_box(self):
        self.symbol("sym_1", 12.0)
        self.symbol("sym_2", 12.01)
        rows = {row["sid"]: row for row in self.run_classifier()}
        self.assertEqual(rows["sym_1"]["type"], "sub")
        self.assertEqual(rows["sym_2"]["type"], "normal")
        self.assertEqual((self.batch / "sym_1" / "icon_type.txt").read_text(), "sub\n")
        self.assertEqual((self.batch / "sym_2" / "icon_type.txt").read_text(), "normal\n")

    def test_container_verdict_is_preserved_unless_overwritten(self):
        folder = self.symbol("sym_1", 24.0)
        (folder / "icon_type.txt").write_text("container\n")
        row = self.run_classifier()[0]
        self.assertEqual((row["type"], row["action"]), ("container", "preserve"))
        self.assertEqual((folder / "icon_type.txt").read_text(), "container\n")
        row = self.run_classifier(overwrite=True)[0]
        self.assertEqual((row["type"], row["action"]), ("normal", "write"))
        self.assertEqual((folder / "icon_type.txt").read_text(), "normal\n")

    def test_dry_run_writes_nothing_and_never_emits_container(self):
        folder = self.symbol("sym_1", 6.0)
        row = self.run_classifier(dry_run=True)[0]
        self.assertEqual((row["type"], row["action"]), ("sub", "would-write"))
        self.assertFalse((folder / "icon_type.txt").exists())
        self.assertNotIn("container", classify_icon_type.CLASSIFIER_TYPES)

    def test_only_matching_sid_prototypes_are_collected(self):
        self.symbol("sym_1", 6.0)
        stray = self.batch / "sym_2"
        stray.mkdir()
        (stray / "sym_9_prototype.svg").write_text(prototype(6.0))
        (self.batch / "sym_1" / "sym_1_final.svg").write_text(prototype(6.0))
        found = classify_icon_type.prototypes([str(self.batch)])
        self.assertEqual([path.name for path in found], ["sym_1_prototype.svg"])


if __name__ == "__main__":
    unittest.main()
