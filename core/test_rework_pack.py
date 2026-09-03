#!/usr/bin/env python3
"""Fail-closed local publication tests; geometry/raster gates are isolated mocks.

The gate implementations have their own suites. These tests ensure failed,
stale, skipped, or unsafe work can never replace a prior manifest delivery.
"""
from __future__ import annotations

from contextlib import ExitStack
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import types
import unittest
from unittest.mock import Mock, patch
from urllib.parse import unquote

import rework_pack


SHIP = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M3 12H21"/></svg>\n'
DESIGN = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path d="M6 24H42"/></svg>\n'
PROTOTYPE = '<svg xmlns="http://www.w3.org/2000/svg"><circle cx="4" cy="4" r="2"/></svg>\n'
PRIOR = '<svg xmlns="http://www.w3.org/2000/svg"><path d="M1 1L2 2"/></svg>\n'


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.targets.extend(value for name, value in attrs if name == "href")


class ReworkPackTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.pack = self.root / "test-pack"
        self.pack.mkdir()
        self.folder = self.pack / "sym_1"
        self.folder.mkdir()
        self.prototype = self.folder / "sym_1_prototype.svg"
        self.prototype.write_text(PROTOTYPE)
        self.destination = self.folder / "sym_1_rework.svg"
        self.destination.write_text(PRIOR)
        self.symbol = {"sid": "sym_1", "name": "Test icon", "minimal_description": "A line.",
                       "files": {"prototype": "sym_1/sym_1_prototype.svg"}, "upload": "sym_1/sym_1_rework.svg"}
        self.write_manifest([self.symbol])
        self.source = self.pack / "editable" / "test-icon.json"
        self.doc = {
            "schemaVersion": 2, "name": "test-icon", "iconType": "normal", "canvas": 48, "strokeWidth": 4,
            "keyfitCheck": {"targetToken": "square-40"},
            "sourceAnalysis": {
                "symbolId": "sym_1", "incomplete": False,
                "lucideReferences": [{"name": "minus", "reason": "A thin symbol.", "principles": ["Round caps."]}],
                "spacingChecks": [],
                "visualReview": {"status": "pass", "shipSize": 24, "notes": "Reviewed at 24px.",
                                 "geometrySha256": hashlib.sha256(SHIP.encode()).hexdigest()},
            },
            "elements": [{"id": "stroke", "tag": "line", "attrs": {"x1": 6, "y1": 24, "x2": 42, "y2": 24}}],
        }
        self.write_source()
        self.rows = rework_pack.load_pack(self.pack)
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        self.profile = {"designCanvas": 48, "shipCanvas": 24, "designStroke": 4, "shipStroke": 2}
        self.resolve = Mock(return_value=["resolved geometry"])
        self.structural = Mock(return_value=subprocess.CompletedProcess([], 0, "PASS\n", ""))
        self.grid = Mock(return_value={"status": "pass"})
        self.keyshape = Mock(return_value={"status": "pass"})
        self.holes = Mock(return_value={"status": "pass"})

        def report(filename):
            def write(results, output, *args):
                output.mkdir(parents=True, exist_ok=True)
                (output / filename).write_text("<html>Mock gate report</html>")
            return write

        modules = {
            "icon_geometry": types.SimpleNamespace(resolve_icon=self.resolve, svg=lambda paths, size, stroke, scale=1: SHIP if size == 24 else DESIGN),
            "icon_profiles": types.SimpleNamespace(validate_document_profile=lambda document: (document["iconType"], self.profile)),
            "check_svg_grid": types.SimpleNamespace(inspect=self.grid, apply_exceptions=lambda report, *args: report,
                                                    write_report=Mock(side_effect=report("grid-report.html"))),
            "check_keyfit": types.SimpleNamespace(process=self.keyshape, write_aggregate=Mock(side_effect=report("keyfit-report.html"))),
            "qa_overlays": types.SimpleNamespace(process=self.holes, write_aggregate=Mock(side_effect=report("hole-radius-report.html"))),
            "lucide_reference": types.SimpleNamespace(reference_paths=lambda name: (Path(name), Path(name))),
        }
        self.modules = modules
        self.stack.enter_context(patch.dict(sys.modules, modules))
        self.stack.enter_context(patch.object(rework_pack.subprocess, "run", self.structural))
        self.stack.enter_context(patch.object(rework_pack, "render_sheet", side_effect=lambda rows, output, sources=False: output.write_bytes(b"test contact sheet")))

    def write_manifest(self, symbols):
        (self.pack / "manifest.json").write_text(json.dumps({"symbols": symbols}))

    def write_source(self):
        self.source.parent.mkdir(parents=True, exist_ok=True)
        self.source.write_text(json.dumps(self.doc))

    def build(self, skip_qa=False):
        return rework_pack.build(self.pack, self.rows, skip_qa)

    def results(self):
        return json.loads((self.pack / "rework-results.json").read_text())

    def assert_preserved(self):
        self.assertEqual(self.prototype.read_text(), PROTOTYPE)
        self.assertEqual(self.destination.read_text(), PRIOR)

    def assert_not_delivered(self, reason):
        self.assert_preserved()
        row = self.results()["symbols"][0]
        self.assertFalse(row["delivered"])
        self.assertEqual(row["status"], "fail")
        self.assertTrue(any(reason in failure for failure in row["failures"]), row["failures"])

    def test_skip_qa_emits_draft_only_and_never_replaces_delivery(self):
        self.assertEqual(self.build(skip_qa=True), 1)
        self.assert_preserved()
        self.assertEqual((self.pack / "output" / "test-icon.svg").read_text(), SHIP)
        result = self.results()
        self.assertTrue(result["diagnosticOnly"])
        self.assertFalse(result["uploaded"])
        self.assertFalse(result["symbols"][0]["delivered"])
        self.assertEqual(result["symbols"][0]["status"], "draft")
        self.structural.assert_not_called()
        self.grid.assert_not_called()
        self.keyshape.assert_not_called()
        self.holes.assert_not_called()
        gallery = (self.pack / "review.html").read_text()
        self.assertIn("automated QA and visual-review verification were skipped", gallery)
        self.assertNotIn("All required automated checks and recorded visual review passed", gallery)
        self.assertNotIn("grid-report.html", gallery)

    def test_missing_visual_review_preserves_prior_destination(self):
        self.doc["sourceAnalysis"].pop("visualReview")
        self.write_source()
        self.assertEqual(self.build(), 1)
        self.assert_not_delivered("visual review")

    def test_stale_visual_geometry_hash_preserves_prior_destination(self):
        self.doc["sourceAnalysis"]["visualReview"]["geometrySha256"] = "0" * 64
        self.write_source()
        self.assertEqual(self.build(), 1)
        self.assert_not_delivered("missing or stale")

    def test_wrong_size_or_missing_visual_notes_preserves_prior_destination(self):
        self.doc["sourceAnalysis"]["visualReview"].update(shipSize=48, notes="")
        self.write_source()
        self.assertEqual(self.build(), 1)
        self.assert_not_delivered("true-size visual review")

    def test_structural_failure_does_not_reuse_old_passing_evidence(self):
        stale = self.pack / "qa" / "old-run" / "structural"
        stale.mkdir(parents=True)
        (stale / "test-icon.log").write_text("PASS")
        self.structural.return_value = subprocess.CompletedProcess([], 1, "Invalid geometry", "Validation failed")
        self.assertEqual(self.build(), 1)
        self.assert_not_delivered("structural")
        fresh = Path(self.results()["qaDirectory"]) / "structural" / "test-icon.log"
        self.assertNotEqual(fresh.parent, stale)
        self.assertIn("Invalid geometry", fresh.read_text())

    def test_any_grid_keyshape_or_hole_gate_failure_blocks_delivery(self):
        for gate, mock in (("grid", self.grid), ("keyshape", self.keyshape), ("holes", self.holes)):
            with self.subTest(gate=gate):
                mock.return_value = {"status": "fail", "reason": "test failure"}
                self.assertEqual(self.build(), 1)
                self.assert_not_delivered(gate)
                mock.return_value = {"status": "pass"}

    def test_geometry_resolution_failure_preserves_prior_destination(self):
        self.resolve.side_effect = ValueError("bad geometry")
        self.assertEqual(self.build(), 1)
        self.assert_not_delivered("bad geometry")

    def test_report_generation_failure_prevents_publication(self):
        self.modules["check_svg_grid"].write_report.side_effect = OSError("cannot write report")
        with self.assertRaisesRegex(OSError, "cannot write report"):
            self.build()
        self.assert_preserved()

    def test_passing_delivery_is_local_and_prior_output_has_recoverable_backup(self):
        self.assertEqual(self.build(), 0)
        self.assertEqual(self.destination.read_text(), SHIP)
        self.assertEqual(self.prototype.read_text(), PROTOTYPE)
        result = self.results()
        self.assertTrue(result["symbols"][0]["delivered"])
        self.assertFalse(result["uploaded"])
        self.assertEqual((Path(result["qaDirectory"]) / "previous-delivery" / self.destination.name).read_text(), PRIOR)
        self.assertFalse(list(self.folder.glob(".rework-delivery-*")))

    def test_copy_failure_preserves_prior_destination_and_cleans_staging_file(self):
        def fail_copy(source, target):
            target.write(b"partial")
            raise OSError("simulated partial copy")
        with patch.object(rework_pack.shutil, "copyfileobj", side_effect=fail_copy):
            self.assertEqual(self.build(), 1)
        self.assert_not_delivered("simulated partial copy")
        self.assertFalse(list(self.folder.glob(".rework-delivery-*")))

    def test_source_changed_after_gate_checks_is_not_delivered(self):
        def mutate_source(*args):
            self.source.write_text(self.source.read_text() + "\n")
            return {"status": "pass"}
        self.holes.side_effect = mutate_source
        self.assertEqual(self.build(), 1)
        self.assert_not_delivered("source changed")

    def test_emitted_geometry_changed_after_gate_checks_is_not_delivered(self):
        def mutate_svg(*args):
            (self.pack / "output" / "test-icon.svg").write_text("not reviewed")
            return {"status": "pass"}
        self.holes.side_effect = mutate_svg
        self.assertEqual(self.build(), 1)
        self.assert_not_delivered("geometry changed")

    def test_report_links_resolve_to_generated_gate_report_files(self):
        self.assertEqual(self.build(), 0)
        parser = Links()
        parser.feed((self.pack / "review.html").read_text())
        for filename in ("grid-report.html", "keyfit-report.html", "hole-radius-report.html"):
            targets = [target for target in parser.targets if target.endswith(filename)]
            self.assertEqual(len(targets), 1, filename)
            self.assertTrue((self.pack / unquote(targets[0])).is_file(), targets[0])
        self.assertNotIn("holes/index.html", parser.targets)

    def test_absolute_escape_and_symlink_manifest_paths_are_rejected(self):
        outside = self.root / "outside.svg"
        outside.write_text(PROTOTYPE)
        for value in (str(outside), "../outside.svg", ".", ""):
            with self.subTest(value=value), self.assertRaises(ValueError):
                rework_pack.scoped_path(self.pack, value)
        linked = self.pack / "linked.svg"
        linked.symlink_to(outside)
        with self.assertRaises(ValueError):
            rework_pack.scoped_path(self.pack, "linked.svg")
        linked_dir = self.pack / "linked-dir"
        linked_dir.symlink_to(self.root, target_is_directory=True)
        with self.assertRaises(ValueError):
            rework_pack.scoped_path(self.pack, "linked-dir/new.svg")
        self.assertEqual(outside.read_text(), PROTOTYPE)

    def test_prototype_and_destination_identity_is_rejected(self):
        self.symbol["files"]["prototype"] = self.symbol["upload"]
        self.write_manifest([self.symbol])
        with self.assertRaisesRegex(ValueError, "prototype"):
            rework_pack.load_pack(self.pack)
        self.assert_preserved()

    def test_destination_cannot_overwrite_another_symbols_prototype(self):
        second_dir = self.pack / "sym_2"
        second_dir.mkdir()
        second = {"sid": "sym_2", "name": "Second icon", "files": {"prototype": "sym_1/sym_1_rework.svg"}, "upload": "sym_2/sym_2_rework.svg"}
        self.write_manifest([self.symbol, second])
        with self.assertRaisesRegex(ValueError, "prototype"):
            rework_pack.load_pack(self.pack)
        self.assert_preserved()

    def test_editable_directory_symlink_is_rejected(self):
        external = self.root / "external-editable"
        self.source.parent.rename(external)
        self.source.parent.symlink_to(external, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlink|escapes"):
            self.build()
        self.assert_preserved()

    def test_generated_svg_symlink_cannot_modify_prototype_even_in_draft_mode(self):
        output = self.pack / "output"
        output.mkdir()
        (output / "test-icon.svg").symlink_to(self.prototype)
        with self.assertRaisesRegex(ValueError, "symlink|escapes"):
            self.build(skip_qa=True)
        self.assert_preserved()

    def test_generated_svg_hardlink_cannot_modify_prototype(self):
        output = self.pack / "output"
        output.mkdir()
        (output / "test-icon.svg").hardlink_to(self.prototype)
        with self.assertRaisesRegex(ValueError, "prototype"):
            self.build(skip_qa=True)
        self.assert_preserved()

    def test_existing_report_symlink_is_rejected_before_emission(self):
        outside = self.root / "outside.html"
        outside.write_text("preserve outside")
        (self.pack / "review.html").symlink_to(outside)
        with self.assertRaisesRegex(ValueError, "symlink|escapes"):
            self.build()
        self.assert_preserved()
        self.assertEqual(outside.read_text(), "preserve outside")
        self.assertFalse((self.pack / "output").exists())

    def test_manifest_prototype_cannot_also_be_generated_output(self):
        output = self.pack / "output"
        output.mkdir()
        generated = output / "test-icon.svg"
        generated.write_text(PROTOTYPE)
        self.symbol["files"]["prototype"] = "output/test-icon.svg"
        self.write_manifest([self.symbol])
        self.rows = rework_pack.load_pack(self.pack)
        with self.assertRaisesRegex(ValueError, "prototype"):
            self.build(skip_qa=True)
        self.assertEqual(generated.read_text(), PROTOTYPE)
        self.assertEqual(self.destination.read_text(), PRIOR)

    def test_malformed_reference_evidence_blocks_delivery_without_breaking_gallery(self):
        self.doc["sourceAnalysis"]["lucideReferences"] = [42, {"reason": "missing name"}]
        self.write_source()
        self.assertEqual(self.build(), 1)
        self.assert_not_delivered("get")
        self.assertTrue((self.pack / "review.html").is_file())


if __name__ == "__main__":
    unittest.main()
