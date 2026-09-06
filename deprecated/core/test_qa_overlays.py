#!/usr/bin/env python3
"""Fail-closed CLI and source-preservation regression tests for hole/pinch QA."""
from __future__ import annotations

from contextlib import redirect_stderr, redirect_stdout
import io
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest import mock

import qa_overlays as qa


def svg(radius=18):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" '
            'fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">'
            f'<circle cx="24" cy="24" r="{radius}"/></svg>')


class HoleCliTests(unittest.TestCase):
    def setUp(self):
        self.temporary = TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.inputs = self.root / "inputs"
        self.inputs.mkdir()
        self.output = self.root / "qa"

    def source(self, name="icon.svg", content=None, directory=None):
        path = (directory or self.inputs) / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(svg() if content is None else content, encoding="utf-8")
        return path

    def run_cli(self, inputs, *extra, output=None):
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            return qa.main([*map(str, inputs), "--samples-per-unit", "8", "--output-dir", str(output or self.output), *map(str, extra)])

    def rows(self):
        return json.loads((self.output / "hole-diameters.json").read_text())

    def test_all_pass_returns_zero_with_complete_deduplicated_coverage(self):
        first = self.source()
        second = self.source("upper.SVG")
        self.assertEqual(self.run_cli([self.inputs, first]), 0)
        rows = self.rows()
        self.assertEqual({item["source"] for item in rows}, {str(first), str(second)})
        self.assertEqual(len(rows), 2)
        self.assertTrue(all(item["status"] == "pass" for item in rows))
        self.assertIn("No inputs failed", (self.output / "hole_error/README.md").read_text())

    def test_real_undersized_hole_returns_one_and_keeps_editable_repair_instructions(self):
        source = self.source(content=svg(2.5))
        before = source.read_bytes()
        self.assertEqual(self.run_cli([source]), 1)
        row = self.rows()[0]
        self.assertEqual(row["status"], "fail")
        self.assertGreater(row["failed_hole_count"], 0)
        current = list((self.output / "hole_error").glob("run-*/README.md"))
        self.assertEqual(len(current), 1)
        guide = current[0].read_text()
        self.assertIn("authoritative editable JSON", guide)
        self.assertIn("distance → holes/pinches → keyshape", guide)
        self.assertNotIn("Repair in place", guide)
        self.assertEqual((current[0].parent / "1/icon.svg").read_bytes(), before)
        self.assertEqual(source.read_bytes(), before)

    def test_pinch_result_returns_one_even_when_there_are_no_failed_holes(self):
        source = self.source()
        pinch = {"pinch": 1, "center_viewbox": [24, 24], "bbox_viewbox": [23, 23, 2, 2],
                 "trapped_area_design_u2": 1, "trapped_radius_design_u": .5,
                 "closure_margin_design_u": .25, "minimum_fill_depth_design_u": 1, "status": "fail"}
        with mock.patch.object(qa, "find_pinches", return_value=[pinch]):
            self.assertEqual(self.run_cli([source]), 1)
        self.assertEqual(self.rows()[0]["failed_hole_count"], 0)
        self.assertEqual(self.rows()[0]["pinch_count"], 1)

    def test_processing_error_is_an_explicit_failed_row_and_does_not_skip_other_inputs(self):
        good = self.source("good.svg")
        bad = self.source("broken.svg", "<svg")
        self.assertEqual(self.run_cli([good, bad]), 1)
        rows = {item["file"]: item for item in self.rows()}
        self.assertEqual(set(rows), {"good.svg", "broken.svg"})
        self.assertEqual(rows["good.svg"]["status"], "pass")
        self.assertEqual(rows["broken.svg"]["status"], "fail")
        self.assertTrue(rows["broken.svg"]["processingErrors"])
        self.assertEqual(json.loads((self.output / "broken.metrics.json").read_text())["status"], "fail")
        self.assertIn("broken.svg", (self.output / "hole-radius-report.html").read_text())
        self.assertIn("processing-error", (self.output / "hole-diameters.csv").read_text())

    def test_missing_non_svg_and_empty_folder_are_not_skipped_in_mixed_selection(self):
        good = self.source()
        missing = self.inputs / "missing.svg"
        non_svg = self.source("readme.txt", "not an icon")
        empty = self.root / "empty"
        empty.mkdir()
        self.assertEqual(self.run_cli([good, missing, non_svg, empty]), 1)
        rows = self.rows()
        self.assertEqual({item["source"] for item in rows}, {str(item) for item in (good, missing, non_svg, empty)})
        self.assertEqual(sum(item["status"] == "fail" for item in rows), 3)

    def test_only_missing_input_still_writes_a_failed_aggregate(self):
        missing = self.inputs / "missing.svg"
        self.assertEqual(self.run_cli([missing]), 1)
        self.assertEqual(self.rows()[0]["source"], str(missing))
        self.assertTrue(self.rows()[0]["processingErrors"])

    def test_no_inputs_empty_selection_and_invalid_arguments_exit_two(self):
        empty = self.root / "empty-only"
        empty.mkdir()
        for arguments in ([], [str(empty)], [str(self.source()), "--samples-per-unit", "2"]):
            with self.subTest(arguments=arguments), redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as raised:
                    qa.main([*arguments, "--output-dir", str(self.output)])
                self.assertEqual(raised.exception.code, 2)

    def test_duplicate_stems_fail_both_rows_without_colliding_artifacts(self):
        first = self.source(directory=self.root / "first")
        second = self.source(directory=self.root / "second")
        self.assertEqual(self.run_cli([first, second]), 1)
        self.assertEqual(len(self.rows()), 2)
        self.assertTrue(all("duplicate stems" in item["processingErrors"][0] for item in self.rows()))
        self.assertFalse((self.output / "icon.metrics.json").exists())

    def test_report_and_evidence_errors_return_one(self):
        source = self.source()
        for function in ("write_aggregate", "collect_failures"):
            with self.subTest(function=function), mock.patch.object(qa, function, side_effect=OSError("report blocked")):
                self.assertEqual(self.run_cli([source]), 1)

    def test_processing_error_replaces_old_pass_metrics_and_omits_stale_overlay_evidence(self):
        source = self.source()
        self.assertEqual(self.run_cli([source]), 0)
        with mock.patch.object(qa, "render_ink_mask", side_effect=OSError("render unavailable")):
            self.assertEqual(self.run_cli([source]), 1)
        self.assertEqual(self.rows()[0]["status"], "fail")
        metrics = json.loads((self.output / "icon.metrics.json").read_text())
        self.assertEqual(metrics["status"], "fail")
        self.assertIn("render unavailable", metrics["processingErrors"][0])
        evidence = list((self.output / "hole_error").glob("run-*/1"))
        self.assertEqual(len(evidence), 1)
        self.assertFalse((evidence[0] / "icon_holes.png").exists())

    def test_malformed_and_inconsistent_measurements_fail_closed(self):
        source = self.source()
        malformed = (None, {"status": "pass"},
                     {"file": source.name, "source": str(source), "status": "pass", "hole_count": 0,
                      "failed_hole_count": 0, "pinch_count": 0, "holes": [{"status": "fail"}], "pinches": []})
        for value in malformed:
            with self.subTest(value=value), mock.patch.object(qa, "process", return_value=value):
                self.assertEqual(self.run_cli([source]), 1)
                self.assertTrue(self.rows()[0]["processingErrors"])

    def test_qa_or_error_directory_containing_input_is_rejected_before_writes(self):
        source = self.source()
        before = source.read_bytes()
        for output, extra in ((self.inputs, ()), (self.output, ("--error-dir", self.inputs)),
                              (self.output, ("--error-dir", self.output))):
            with self.subTest(output=output, extra=extra):
                self.assertEqual(self.run_cli([source], *extra, output=output), 1)
                self.assertEqual(source.read_bytes(), before)
        self.assertEqual(list(self.inputs.iterdir()), [source])

    def test_symlink_and_hardlink_report_collisions_preserve_source(self):
        source = self.source()
        before = source.read_bytes()
        self.output.mkdir()
        target = self.output / "icon.metrics.json"
        target.symlink_to(source)
        self.assertEqual(self.run_cli([source]), 1)
        self.assertEqual(source.read_bytes(), before)
        target.unlink()
        target.hardlink_to(source)
        self.assertEqual(self.run_cli([source]), 1)
        self.assertEqual(source.read_bytes(), before)

    def test_failure_collection_keeps_unrelated_svgs_and_prior_runs(self):
        source = self.source(content=svg(2.5))
        errors = self.output / "hole_error"
        errors.mkdir(parents=True)
        unrelated = errors / "keep-me.svg"
        unrelated.write_text("unrelated user artifact")
        self.assertEqual(self.run_cli([source]), 1)
        self.assertEqual(self.run_cli([source]), 1)
        self.assertEqual(unrelated.read_text(), "unrelated user artifact")
        self.assertEqual(len(list(errors.glob("run-*"))), 2)
        source.write_text(svg())
        self.assertEqual(self.run_cli([source]), 0)
        self.assertEqual(len(list(errors.glob("run-*"))), 2)
        self.assertIn("No inputs failed", (errors / "README.md").read_text())

    def test_process_and_collect_failures_direct_apis_reject_input_collisions(self):
        source = self.source()
        self.output.mkdir()
        (self.output / "icon_holes.png").hardlink_to(source)
        with self.assertRaisesRegex(ValueError, "overwrite a selected input"):
            qa.process(source, self.output, 8)
        row = qa._error_result(source, "failed", "normal", 1, 1)
        with self.assertRaisesRegex(ValueError, "contains a selected input"):
            qa.collect_failures([row], self.output, self.inputs, 1, 1)
        self.assertEqual(source.read_text(), svg())

    def test_process_binds_exact_report_to_source_bytes_and_effective_profile(self):
        source = self.source()
        self.output.mkdir()
        report = qa.process(source, self.output, 8)
        self.assertEqual(report["status"], "pass")
        self.assertEqual(report["svgSha256"], hashlib.sha256(source.read_bytes()).hexdigest())
        encoded = json.dumps(qa.get_profile("normal"), sort_keys=True, separators=(",", ":"),
                             ensure_ascii=False, allow_nan=False).encode("utf-8")
        self.assertEqual(report["profileSha256"], hashlib.sha256(encoded).hexdigest())
        self.assertEqual(json.loads((self.output / "icon.metrics.json").read_text()), report)

    def test_source_change_during_measurement_returns_persisted_nonpass(self):
        source = self.source()
        original_bytes = source.read_bytes()
        self.output.mkdir()
        render = qa.render_ink_mask

        def render_then_change(*args, **kwargs):
            mask = render(*args, **kwargs)
            source.write_text(svg(17))
            return mask

        with mock.patch.object(qa, "render_ink_mask", side_effect=render_then_change):
            report = qa.process(source, self.output, 8)
        self.assertEqual(report["status"], "fail")
        self.assertIn("SVG changed during", report["processingErrors"][0])
        self.assertEqual(report["svgSha256"], hashlib.sha256(original_bytes).hexdigest())
        self.assertNotEqual(report["svgSha256"], hashlib.sha256(source.read_bytes()).hexdigest())
        self.assertEqual(json.loads((self.output / "icon.metrics.json").read_text()), report)

    def test_executable_exit_code_propagates_real_failure(self):
        source = self.source(content=svg(2.5))
        result = subprocess.run([sys.executable, "-B", str(Path(qa.__file__)), str(source),
                                 "--samples-per-unit", "8", "--output-dir", str(self.output)],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
