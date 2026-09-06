#!/usr/bin/env python3
"""Regression coverage for isolated, explicitly unapproved adaptation trials."""
from __future__ import annotations

import argparse
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import adapt_icon as adapter
from icon_geometry import resolve_icon, svg
from icon_profiles import get_profile


class AdaptTrialTests(unittest.TestCase):
    def setUp(self):
        self.temporary = TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.sources = self.root / "sources"
        self.metadata = self.root / "metadata"
        self.sources.mkdir()
        self.metadata.mkdir()
        self.document = {
            "schemaVersion": 2, "name": "circle-outline", "iconType": "normal",
            "canvas": 48, "strokeWidth": 4, "cornerStyle": "round",
            "keyfitCheck": {"targetToken": "circle-44", "mode": "exact"},
            "elements": [{"id": "outline", "tag": "circle", "attrs": {"cx": 24, "cy": 24, "r": 20}}],
            "sourceAnalysis": {"incomplete": False, "spacingChecks": [],
                               "visualReview": {"status": "pass", "shipSize": 24, "geometrySha256": "old"}},
        }
        self.source = self.sources / "circle-outline-design.svg"
        self.source.write_text(svg(resolve_icon(self.document), 48, 4).replace(' width="48" height="48"', ""))
        self.metadata_path = self.metadata / "circle-outline.json"
        self.metadata_path.write_text(json.dumps(self.document))

    def args(self, **kwargs):
        fields = dict(input=self.sources, from_profile="normal", to_profile="sub", metadata_dir=self.metadata,
                      source_keyshape=None, target_keyshape=None, out_dir=self.root / "trial")
        return argparse.Namespace(**{**fields, **kwargs})

    def test_folder_selects_only_immediate_design_files(self):
        (self.sources / "circle-outline.svg").write_text(self.source.read_text())
        (self.sources / "nested").mkdir()
        (self.sources / "nested/hidden-design.svg").write_text(self.source.read_text())
        self.assertEqual(adapter.select_sources(self.sources), [self.source])
        self.assertEqual(adapter.select_sources(self.sources / "circle-outline.svg"), [self.sources / "circle-outline.svg"])

    def test_selection_rejects_symlinks_unsafe_names_and_empty_folders(self):
        linked = self.root / "linked.svg"
        linked.symlink_to(self.source)
        with self.assertRaisesRegex(ValueError, "symlink"):
            adapter.select_sources(linked)
        unsafe = self.sources / "Not Safe-design.svg"
        unsafe.write_text(self.source.read_text())
        with self.assertRaisesRegex(ValueError, "kebab"):
            adapter.select_sources(self.sources)
        with self.assertRaisesRegex(ValueError, "No .*design"):
            adapter.select_sources(self.metadata)

    def test_output_must_be_new_and_separate(self):
        with self.assertRaisesRegex(ValueError, "new output"):
            adapter.prepare_output(self.metadata, [self.source], self.metadata)
        for path in (self.sources / "trial", self.metadata / "trial"):
            with self.subTest(path=path), self.assertRaisesRegex(ValueError, "separate"):
                adapter.prepare_output(path, [self.source], self.metadata)
            self.assertFalse(path.exists())
        linked = self.root / "linked"
        linked.symlink_to(self.metadata, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlinks"):
            adapter.prepare_output(linked / "trial", [self.source], self.metadata)

    def test_metadata_parity_accepts_legacy_intrinsic_size_omission(self):
        source = adapter.read_design_svg(self.source)
        metadata = adapter.verified_metadata(self.metadata_path, source, "normal")
        self.assertEqual(metadata["elements"][0]["tag"], "circle")
        self.assertEqual(source["canvas"], 48)
        self.assertEqual(source["strokeWidth"], 4)

    def test_mismatched_metadata_never_supplies_geometry(self):
        source = adapter.read_design_svg(self.source)
        changed = deepcopy(self.document)
        changed["elements"][0]["attrs"]["r"] = 18
        self.metadata_path.write_text(json.dumps(changed))
        with self.assertRaisesRegex(ValueError, "geometry/order"):
            adapter.verified_metadata(self.metadata_path, source, "normal")
        with self.assertRaisesRegex(ValueError, "source profile"):
            adapter.verified_metadata(self.metadata_path, source, "sub")

    def test_token_mapping_uses_shape_and_orientation_not_dimensions_alone(self):
        sub = get_profile("sub")
        circle = adapter.token_named(get_profile("normal"), "circle-44")
        self.assertEqual(adapter.matching_token(circle, sub)["name"], "circle-32")
        square = adapter.token_named(get_profile("normal"), "square-40")
        self.assertEqual(adapter.matching_token(square, sub)["name"], "square-32")
        sub["keyshapes"].append({**sub["keyshapes"][0], "name": "other-circle"})
        with self.assertRaisesRegex(ValueError, "ambiguous"):
            adapter.matching_token(circle, sub)
        self.assertEqual(adapter.matching_token(circle, sub, "circle-32")["name"], "circle-32")

    def test_fresh_draft_keeps_exact_mode_and_invalidates_old_approval(self):
        source = adapter.read_design_svg(self.source)
        metadata = adapter.verified_metadata(self.metadata_path, source, "normal")
        normal, sub = get_profile("normal"), get_profile("sub")
        document, result = adapter.make_draft("circle-outline-sub", source, normal, sub, "normal", "sub",
            adapter.token_named(normal, "circle-44"), adapter.token_named(sub, "circle-32"), metadata, {})
        self.assertEqual(document["canvas"], 32)
        self.assertEqual(document["strokeWidth"], 4)
        self.assertEqual(document["keyfitCheck"], {"targetToken": "circle-32", "mode": "exact"})
        self.assertTrue(document["sourceAnalysis"]["incomplete"])
        self.assertEqual(document["sourceAnalysis"]["visualReview"], {"status": "pending", "shipSize": 32})
        self.assertNotIn("geometrySha256", document["sourceAnalysis"]["visualReview"])
        self.assertEqual(document["elements"][0]["id"], "outline")
        self.assertEqual(adapter.measured_painted_bounds(document), [0, 0, 32, 32])
        self.assertIn("metrics", result)

    def test_spacing_reuses_only_intent_and_remeasures_distances(self):
        document = {"schemaVersion": 2, "strokeWidth": 4, "elements": [
            {"id": "left", "tag": "path", "attrs": {"d": "M 8 4 L 8 28"}},
            {"id": "right", "tag": "path", "attrs": {"d": "M 16 4 L 16 28"}},
        ]}
        metadata = {"iconType": "normal", "strokeWidth": 4, "sourceAnalysis": {"spacingChecks": [{"elements": ["left", "right"], "relation": "visual-opening",
            "minimum": 3, "minimumCenterline": 8, "centerlineDistance": 99, "paintedClearance": 95, "status": "pass"}]}}
        check, = adapter.refreshed_relationships(metadata, document)
        self.assertEqual(check["centerlineDistance"], 8)
        self.assertEqual(check["paintedClearance"], 4)
        self.assertEqual(check["minimum"], 4)
        self.assertEqual(check["minimumCenterline"], 8)
        self.assertEqual(check["reviewStatus"], "pending")
        self.assertNotIn("status", check)

    def test_container_adaptation_is_rejected_without_output(self):
        with self.assertRaisesRegex(ValueError, "container slots"):
            adapter.run_trial(self.args(to_profile="container"))
        self.assertFalse((self.root / "trial").exists())

    def test_unknown_explicit_tokens_are_rejected_before_output_creation(self):
        for args in (self.args(target_keyshape="missing"), self.args(metadata_dir=None, source_keyshape="missing")):
            with self.subTest(args=args), self.assertRaisesRegex(ValueError, "Unknown profile keyshape"):
                adapter.run_trial(args)
            self.assertFalse((self.root / "trial").exists())

    @unittest.skipUnless(all(importlib.util.find_spec(name) for name in ("cairosvg", "PIL", "numpy", "cv2")), "raster dependencies unavailable")
    def test_real_trial_writes_native_drafts_and_qa_without_changing_inputs(self):
        old = {path: path.read_bytes() for path in (self.source, self.metadata_path)}
        report = adapter.run_trial(self.args())
        self.assertEqual(report["status"], "trial-complete")
        self.assertEqual((report["sourceCount"], report["draftCount"], report["numericPassCount"], report["approvedCount"]), (1, 1, 1, 0))
        self.assertTrue(report["originalsUnchanged"])
        for path, content in old.items():
            self.assertEqual(path.read_bytes(), content)
        output = self.root / "trial"
        row, = report["files"]
        self.assertEqual(row["qa"]["structure"]["status"], "blocked-draft")
        self.assertEqual(row["qa"]["structure"]["geometryIssues"], [])
        self.assertEqual(row["qa"]["gateOrder"], ["distance", "holes", "keyshape"])
        self.assertEqual(row["qa"]["spacing"]["status"], "pass")
        self.assertEqual(len(row["qa"]["canvasKeyshape"]), 2)
        for result in row["qa"]["canvasKeyshape"]:
            self.assertTrue(result["ok"])
            self.assertTrue(Path(result["keyfitOverlay"]).is_file())
        self.assertEqual((output / row["svg"]).read_bytes(), (output / "output/circle-outline-sub-design.svg").read_bytes())
        self.assertTrue(json.loads((output / row["editable"]).read_text())["sourceAnalysis"]["incomplete"])
        self.assertIn('width="32" height="32"', (output / row["svg"]).read_text())
        self.assertIn("All results are unapproved drafts", (output / "review.html").read_text())
        self.assertTrue((output / "comparison.png").is_file())
        with self.assertRaisesRegex(ValueError, "new output"):
            adapter.run_trial(self.args())

    def test_a_completed_experiment_can_have_no_passing_drafts(self):
        fake_qa = {"mechanicalChecksPassed": False, "grid": {"status": "review"}, "spacing": {"status": "fail"},
                   "keyshape": {"status": "fail"}, "holes": {"status": "fail"}}
        with patch.object(adapter, "run_qa", return_value=fake_qa), patch.object(adapter, "write_reviews"):
            report = adapter.run_trial(self.args())
        self.assertEqual(report["status"], "trial-complete")
        self.assertEqual(report["numericPassCount"], 0)
        self.assertEqual(report["approvedCount"], 0)
        self.assertEqual(report["files"][0]["status"], "draft-needs-geometry-review")

    @unittest.skipUnless(all(importlib.util.find_spec(name) for name in ("cairosvg", "PIL", "numpy", "cv2")), "raster dependencies unavailable")
    def test_collapsed_segment_signal_cannot_receive_numeric_pass(self):
        real_draft = adapter.make_draft

        def flagged_draft(*args, **kwargs):
            document, result = real_draft(*args, **kwargs)
            document["adaptation"]["metrics"]["collapsedSegments"] = [{"elementId": "outline", "commandIndex": 1, "type": "L"}]
            return document, result

        with patch.object(adapter, "make_draft", side_effect=flagged_draft), patch.object(adapter, "write_reviews"):
            report = adapter.run_trial(self.args())
        self.assertEqual(report["status"], "trial-complete")
        self.assertEqual(report["numericPassCount"], 0)
        self.assertEqual(report["files"][0]["qa"]["adaptationStructure"]["status"], "review")

    def test_processing_errors_are_explicit_rows_not_silent_omissions(self):
        self.metadata_path.write_text("{}")
        with patch.object(adapter, "write_reviews"):
            report = adapter.run_trial(self.args())
        self.assertEqual(report["status"], "trial-error")
        self.assertEqual(report["draftCount"], 0)
        self.assertEqual(len(report["files"]), 1)
        self.assertEqual(report["files"][0]["status"], "error")

    def test_external_input_changes_cannot_leave_a_false_unchanged_claim(self):
        def external_edit(*args, **kwargs):
            self.metadata_path.write_text("{\"externallyChanged\":true}")
            return {"mechanicalChecksPassed": False, "grid": {"status": "review"}, "spacing": {"status": "fail"},
                    "keyshape": {"status": "fail"}, "holes": {"status": "fail"}}
        with patch.object(adapter, "run_qa", side_effect=external_edit), patch.object(adapter, "write_reviews") as review:
            report = adapter.run_trial(self.args())
        self.assertEqual(report["status"], "trial-error")
        self.assertFalse(report["originalsUnchanged"])
        self.assertIn(str(self.metadata_path), report["changedInputs"])
        self.assertFalse(review.call_args.kwargs["originals_unchanged"])

    def run_mocked_gates(self, target_type="sub", spacing_override=None, mutate=False, hole_override=None, missing_hole_evidence=False):
        """Exercise real orchestration with isolated checker results, not text assertions."""
        profile = get_profile(target_type)
        document = deepcopy(self.document)
        document.update(iconType=target_type, canvas=profile["canvas"], strokeWidth=profile["strokeWidth"])
        output = self.root / "mock-trial"
        emitted = output / "output" / "circle-outline.svg"
        editable = output / "editable" / "circle-outline.json"
        adapter.write_json(editable, document)
        emitted.parent.mkdir(parents=True, exist_ok=True)
        emitted.write_text("isolated native SVG test snapshot")
        emitted.with_name("circle-outline-design.svg").write_bytes(emitted.read_bytes())
        digest = adapter.sha256(json.dumps(profile, sort_keys=True, separators=(",", ":"),
                                           ensure_ascii=False, allow_nan=False).encode())
        order = []

        def structure(*args, **kwargs):
            order.append("structure")
            return subprocess.CompletedProcess(args, 1, "  FAIL sourceAnalysis is marked incomplete; finish review\n", "")

        def grid(*args, **kwargs):
            order.append("grid")
            return {"status": "pass"}

        def distance(path, **kwargs):
            order.append("distance")
            self.assertEqual(kwargs["icon_type"], target_type)
            result = {"status": "pass", "ok": True, "errors": [], "pairs": [],
                      "svgSha256": adapter.sha256(path.read_bytes()), "profileSha256": digest}
            result.update(spacing_override or {})
            return result

        def holes(*args, **kwargs):
            order.append("holes")
            if mutate:
                emitted.write_text("changed after distance gate")
            result = {"status": "pass", "processingErrors": [], "nativeSizeIssues": [],
                      "hole_count": 0, "failed_hole_count": 0, "pinch_count": 0, "holes": [], "pinches": [],
                      "configuredMinimumRadiusDesignUnits": profile["validation"]["minimumEnclosedRadius"],
                      "configuredMinimumFillDepthDesignUnits": profile["validation"]["minimumSolidFillDepth"],
                      "svgSha256": adapter.sha256(emitted.read_bytes()), "profileSha256": digest}
            result.update(hole_override or {})
            metrics = output / "qa/holes/circle-outline.metrics.json"
            overlay = output / "qa/holes/circle-outline_holes.png"
            adapter.write_json(metrics, result)
            overlay.write_bytes(b"isolated overlay")
            if missing_hole_evidence:
                metrics.unlink()
            return result

        def keyshape(path, **kwargs):
            order.append("keyshape")
            self.assertEqual(kwargs["icon_type"], target_type)
            self.assertEqual(kwargs["editable"], editable)
            return {"status": "pass", "ok": True, "errors": [], "keyfit": {"status": "pass"},
                    "svgSha256": adapter.sha256(path.read_bytes()),
                    "editableSha256": adapter.sha256(editable.read_bytes()), "profileSha256": digest}

        ink = {"status": "pass", "holeCount": 0, "pinches": []}
        with patch.object(adapter.subprocess, "run", side_effect=structure), \
                patch("check_svg_grid.inspect", side_effect=grid), \
                patch("check_svg_spacing.check_file", side_effect=distance), \
                patch("qa_overlays.process", side_effect=holes), \
                patch("validate_icon_keyshapes.check_file", side_effect=keyshape), \
                patch.object(adapter, "authored_ink_diagnostics", return_value=ink):
            report = adapter.run_qa(document, editable, emitted, self.source, "normal", get_profile("normal"),
                                    target_type, profile, output)
        return order, report

    def test_all_supported_trial_profiles_use_ordered_three_gates_and_both_aliases(self):
        for profile in ("normal", "sub"):
            with self.subTest(profile=profile):
                order, report = self.run_mocked_gates(profile)
                self.assertEqual(order, ["structure", "grid", "distance", "holes", "keyshape", "keyshape"])
                self.assertTrue(report["mechanicalChecksPassed"])
                self.assertEqual(report["visualApproval"], "pending")

    def test_unresolved_failed_malformed_or_stale_distance_cannot_pass_trial(self):
        for override in ({"status": "review", "ok": False}, {"status": "fail", "ok": False},
                         {"status": "error", "ok": False, "errors": ["unreadable"]},
                         {"ok": None}, {"pairs": None}, {"pairs": [{"status": "review"}]},
                         {"svgSha256": "old"}, {"profileSha256": "old"}):
            with self.subTest(override=override):
                _, report = self.run_mocked_gates(spacing_override=override)
                self.assertFalse(report["mechanicalChecksPassed"])

    def test_edit_after_distance_invalidates_the_whole_trial_gate_set(self):
        _, report = self.run_mocked_gates(mutate=True)
        self.assertFalse(report["mechanicalChecksPassed"])
        self.assertEqual(len(report["changedInputs"]), 1)

    def test_missing_stale_or_contradictory_hole_evidence_blocks_trial(self):
        for override in ({"svgSha256": "old"}, {"profileSha256": "old"},
                         {"status": "fail"}, {"processingErrors": ["renderer error"]},
                         {"failed_hole_count": 1}, {"pinch_count": 1},
                         {"holes": [{"status": "fail"}]}, {"hole_count": 1},
                         {"configuredMinimumRadiusDesignUnits": 0.1},
                         {"configuredMinimumFillDepthDesignUnits": 0}):
            with self.subTest(override=override):
                _, report = self.run_mocked_gates(hole_override=override)
                self.assertFalse(report["mechanicalChecksPassed"])
        _, report = self.run_mocked_gates(missing_hole_evidence=True)
        self.assertFalse(report["mechanicalChecksPassed"])


if __name__ == "__main__":
    unittest.main()
