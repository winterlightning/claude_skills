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


SHIP = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48"><path d="M6 24H42"/></svg>\n'
DESIGN = SHIP  # Compatibility filename only; there is one native output size.
PROTOTYPE = '<svg xmlns="http://www.w3.org/2000/svg"><circle cx="4" cy="4" r="2"/></svg>\n'
PRIOR = '<svg xmlns="http://www.w3.org/2000/svg"><path d="M1 1L2 2"/></svg>\n'


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.targets.extend(value for name, value in attrs if name == "href")


class NativeReviewTests(unittest.TestCase):
    """Exercise real renderers separately from mocked publication gates."""

    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.pack = Path(self.temp.name).resolve()
        self.rows = []
        for index, (icon_type, size) in enumerate((("sub", 32), ("normal", 48), ("container", 64)), 1):
            prototype = self.pack / f"{icon_type}-prototype.svg"
            output = self.pack / f"{icon_type}.svg"
            svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" '
                   f'width="{size}" height="{size}" fill="none" stroke="black" stroke-width="4">'
                   f'<circle cx="{size / 2}" cy="{size / 2}" r="{size / 2 - 4}"/></svg>')
            prototype.write_text(svg)
            output.write_text(svg)
            self.rows.append({"sid": f"sym_{index}", "name": icon_type, "brief": "Native-size test",
                              "iconType": icon_type, "shipSize": size // 2, "prototype": prototype,
                              "ship": output, "editable": self.pack / f"{icon_type}.json"})

    def test_missing_type_defaults_to_native_normal_not_historical_hint(self):
        self.assertEqual(rework_pack.native_review_size({"shipSize": 24}), 48)

    def test_contact_sheets_render_each_icon_once_at_its_native_profile_size(self):
        import cairosvg
        from PIL import Image

        for sources in (False, True):
            with self.subTest(sources=sources), patch.object(cairosvg, "svg2png", wraps=cairosvg.svg2png) as render:
                destination = self.pack / ("sources.png" if sources else "output.png")
                rework_pack.render_sheet(self.rows, destination, sources=sources)
                self.assertEqual(render.call_count, 3)
                self.assertEqual([(call.kwargs["output_width"], call.kwargs["output_height"])
                                  for call in render.call_args_list], [(32, 32), (48, 48), (64, 64)])
                with Image.open(destination) as sheet:
                    self.assertEqual(sheet.size, (1100, 188))

    def test_gallery_uses_only_native_size_prototype_and_output_images(self):
        class Images(HTMLParser):
            def __init__(self):
                super().__init__()
                self.images = []

            def handle_starttag(self, tag, attrs):
                if tag == "img":
                    self.images.append(dict(attrs))

        rework_pack.write_gallery(self.pack, self.rows, self.pack / "qa", draft=True)
        document = (self.pack / "review.html").read_text()
        parser = Images()
        parser.feed(document)
        self.assertEqual(len(parser.images), 6)
        self.assertEqual([(item["width"], item["height"]) for item in parser.images],
                         [("32", "32"), ("32", "32"), ("48", "48"), ("48", "48"), ("64", "64"), ("64", "64")])
        for row, size in zip(self.rows, (32, 48, 64)):
            self.assertEqual(sum(item["src"] == row["ship"].name for item in parser.images), 1)
            self.assertIn(f"{size}×{size}px native size · 1:1", document)


class RealCanvasGatePublicationTests(unittest.TestCase):
    """Keep the real canvas/raster gate while older gates report success."""

    def run_pack(self, *, wrong_width=False, small_circle=False):
        import check_svg_grid
        import icon_geometry
        import icon_profiles
        import qa_overlays

        temporary = TemporaryDirectory(prefix="real-pack-canvas-gate-")
        self.addCleanup(temporary.cleanup)
        pack = Path(temporary.name).resolve()
        (pack / "sym_1").mkdir()
        prototype = pack / "sym_1/sym_1_prototype.svg"
        destination = pack / "sym_1/sym_1_rework.svg"
        prototype.write_text(PROTOTYPE)
        destination.write_text(PRIOR)
        symbol = {"sid": "sym_1", "name": "Circle", "files": {"prototype": "sym_1/sym_1_prototype.svg"},
                  "upload": "sym_1/sym_1_rework.svg"}
        (pack / "manifest.json").write_text(json.dumps({"symbols": [symbol]}))
        profile = icon_profiles.get_profile("normal")
        circle = next(token for token in profile["keyshapes"] if token["shape"] == "circle")
        center = profile["designCanvas"] / 2
        radius = (circle["width"] - profile["designStroke"]) / 2
        doc = {"schemaVersion": 2, "name": "test-circle", "iconType": "normal",
               "canvas": profile["designCanvas"], "strokeWidth": profile["designStroke"],
               "keyfitCheck": {"targetToken": circle["name"], "mode": "exact"},
               "elements": [{"id": "rim", "tag": "circle", "attrs": {
                   "cx": center, "cy": center, "r": radius / 2 if small_circle else radius}}],
               "sourceAnalysis": {"symbolId": "sym_1", "incomplete": False,
                   "lucideReferences": [{"name": "circle", "reason": "Continuous round outline.",
                                         "principles": ["Keep uniform stroke and circular contour."]}]}}
        emitted = icon_geometry.svg(icon_geometry.resolve_icon(doc), profile["designCanvas"], profile["designStroke"])
        if wrong_width:
            emitted = emitted.replace(f'width="{profile["designCanvas"]:g}"', f'width="{profile["designCanvas"] / 2:g}"', 1)
        doc["sourceAnalysis"]["visualReview"] = {"status": "pass", "shipSize": profile["designCanvas"],
            "notes": "Test fixture review matched to emitted bytes.",
            "geometrySha256": hashlib.sha256(emitted.encode()).hexdigest()}
        (pack / "editable").mkdir()
        (pack / "editable/test-circle.json").write_text(json.dumps(doc))

        def report(rows, output, *args):
            output.mkdir(parents=True, exist_ok=True)

        with (patch.object(icon_geometry, "svg", return_value=emitted),
              patch.object(rework_pack.subprocess, "run", return_value=subprocess.CompletedProcess([], 0, "PASS", "")),
              patch.object(check_svg_grid, "inspect", return_value={"status": "pass"}),
              patch.object(check_svg_grid, "write_report", side_effect=report),
              patch.object(qa_overlays, "process", return_value={"status": "pass"}),
              patch.object(qa_overlays, "write_aggregate", side_effect=report),
              patch.object(rework_pack, "render_sheet", side_effect=lambda rows, output, sources=False: output.write_bytes(b"sheet"))):
            status = rework_pack.build(pack, rework_pack.load_pack(pack))
        self.assertEqual(prototype.read_text(), PROTOTYPE)
        result = json.loads((pack / "rework-results.json").read_text())
        return status, result, destination, emitted

    def test_real_gate_emits_persisted_compatible_evidence_and_allows_native_circle(self):
        status, result, destination, emitted = self.run_pack()
        self.assertEqual(status, 0, result["symbols"][0]["failures"])
        self.assertEqual(destination.read_text(), emitted)
        self.assertTrue(result["symbols"][0]["delivered"])
        qa = Path(result["qaDirectory"])
        aggregate = json.loads((qa / "canvas-keyshape/canvas-keyshape-results.json").read_text())
        self.assertTrue(aggregate["ok"])
        self.assertEqual(aggregate["checked"], 2)
        self.assertTrue((qa / "keyshape/test-circle_keyfit.png").is_file())
        self.assertTrue((qa / "keyshape/keyfit-report.html").is_file())

    def test_real_canvas_gate_blocks_wrong_width_even_when_other_checks_pass(self):
        status, result, destination, _ = self.run_pack(wrong_width=True)
        self.assertEqual(status, 1)
        self.assertEqual(destination.read_text(), PRIOR)
        self.assertFalse(result["symbols"][0]["delivered"])
        self.assertTrue(any("width" in failure for failure in result["symbols"][0]["failures"]))

    def test_real_painted_gate_blocks_tiny_centered_icon_even_when_other_checks_pass(self):
        status, result, destination, _ = self.run_pack(small_circle=True)
        self.assertEqual(status, 1)
        self.assertEqual(destination.read_text(), PRIOR)
        self.assertFalse(result["symbols"][0]["delivered"])
        self.assertTrue(any("canvas/keyshape" in failure for failure in result["symbols"][0]["failures"]))


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
                "visualReview": {"status": "pass", "shipSize": 48, "notes": "Reviewed at native 48px.",
                                 "geometrySha256": hashlib.sha256(SHIP.encode()).hexdigest()},
            },
            "elements": [{"id": "stroke", "tag": "line", "attrs": {"x1": 6, "y1": 24, "x2": 42, "y2": 24}}],
        }
        self.write_source()
        self.rows = rework_pack.load_pack(self.pack)
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        self.profile = {"designCanvas": 48, "shipCanvas": 48, "designStroke": 4, "shipStroke": 4}
        self.resolve = Mock(return_value=["resolved geometry"])
        self.structural = Mock(return_value=subprocess.CompletedProcess([], 0, "PASS\n", ""))
        self.grid = Mock(return_value={"status": "pass"})
        self.keyshape = Mock(return_value={"status": "pass"})
        self.holes = Mock(return_value={"status": "pass"})

        def canvas_gate(emitted, *, editable, icon_type, output_dir):
            artifacts = output_dir / "files" / emitted.stem
            artifacts.mkdir(parents=True, exist_ok=True)
            keyfit = {"file": emitted.name, **self.keyshape()}
            keyfit_report = artifacts / f"{emitted.stem}.keyfit.json"
            keyfit_overlay = artifacts / f"{emitted.stem}_keyfit.png"
            keyfit_report.write_text(json.dumps(keyfit))
            keyfit_overlay.write_bytes(b"mock raster overlay")
            snapshot = json.dumps(self.profile, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
            passed = keyfit["status"] == "pass"
            result = {"file": emitted.name, "ok": passed, "status": "pass" if passed else "fail",
                    "errors": [] if passed else ["declared keyshape mismatch"], "issues": [], "keyfit": keyfit,
                    "svgSha256": hashlib.sha256(emitted.read_bytes()).hexdigest(),
                    "editableSha256": hashlib.sha256(editable.read_bytes()).hexdigest(),
                    "profileSha256": hashlib.sha256(snapshot).hexdigest(),
                    "evidenceDirectory": str(artifacts),
                    "keyfitReport": str(keyfit_report), "keyfitOverlay": str(keyfit_overlay)}
            (artifacts / "canvas-keyshape.json").write_text(json.dumps(result))
            return result

        self.canvas_gate_result = canvas_gate
        self.canvas_gate = Mock(side_effect=canvas_gate)

        def report(filename):
            def write(results, output, *args):
                output.mkdir(parents=True, exist_ok=True)
                (output / filename).write_text("<html>Mock gate report</html>")
            return write

        modules = {
            "icon_geometry": types.SimpleNamespace(resolve_icon=self.resolve, svg=Mock(return_value=SHIP)),
            "icon_profiles": types.SimpleNamespace(validate_document_profile=lambda document: (document["iconType"], self.profile),
                                                   get_profile=lambda icon_type=None: self.profile),
            "check_svg_grid": types.SimpleNamespace(inspect=self.grid, apply_exceptions=lambda report, *args: report,
                                                    write_report=Mock(side_effect=report("grid-report.html"))),
            "check_keyfit": types.SimpleNamespace(process=self.keyshape, write_aggregate=Mock(side_effect=report("keyfit-report.html"))),
            "qa_overlays": types.SimpleNamespace(process=self.holes, write_aggregate=Mock(side_effect=report("hole-radius-report.html"))),
            "validate_icon_keyshapes": types.SimpleNamespace(check_file=self.canvas_gate),
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
        self.canvas_gate.assert_not_called()
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
        self.doc["sourceAnalysis"]["visualReview"].update(shipSize=24, notes="")
        self.write_source()
        self.assertEqual(self.build(), 1)
        self.assert_not_delivered("native-size visual review")

    def test_historical_24px_review_cannot_approve_native_48px_output(self):
        self.doc["sourceAnalysis"]["visualReview"].update(shipSize=24, notes="Historical half-size review.")
        self.write_source()
        self.assertEqual(self.build(), 1)
        self.assert_not_delivered("native-size visual review at 48×48px")

    def test_canonical_output_and_compatibility_alias_are_identical_native_geometry(self):
        self.assertEqual(self.build(), 0)
        self.modules["icon_geometry"].svg.assert_called_once_with(["resolved geometry"], 48, 4)
        output = self.pack / "output"
        self.assertEqual((output / "test-icon.svg").read_bytes(), (output / "test-icon-design.svg").read_bytes())
        self.assertEqual(self.results()["symbols"][0]["shipSize"], 48)

    def test_build_leaves_numeric_qa_thresholds_to_the_selected_profile(self):
        self.assertEqual(self.build(), 0)
        self.assertEqual(self.canvas_gate.call_count, 2)
        for call in self.canvas_gate.call_args_list:
            self.assertEqual(call.kwargs["icon_type"], "normal")
            self.assertEqual(call.kwargs["editable"], self.source)
            self.assertNotIn("tolerance", call.kwargs)
        self.assertEqual(self.holes.call_args.args[3:5], (None, None))
        self.assertEqual(self.modules["qa_overlays"].write_aggregate.call_args.args[2:], (None, None))

    def test_canvas_keyshape_checks_both_native_filenames_and_copies_raster_evidence(self):
        self.assertEqual(self.build(), 0)
        checked = [call.args[0].name for call in self.canvas_gate.call_args_list]
        self.assertEqual(checked, ["test-icon.svg", "test-icon-design.svg"])
        qa = Path(self.results()["qaDirectory"])
        aggregate = json.loads((qa / "canvas-keyshape" / "canvas-keyshape-results.json").read_text())
        self.assertEqual(aggregate["checked"], 2)
        self.assertEqual(aggregate["failed"], 0)
        self.assertIs(aggregate["ok"], True)
        self.assertTrue((qa / "keyshape" / "test-icon.keyfit.json").is_file())
        self.assertTrue((qa / "keyshape" / "test-icon_keyfit.png").is_file())

    def test_missing_malformed_failed_and_errored_canvas_reports_block_delivery(self):
        for report in (None, {}, {"ok": True, "status": "pass"},
                       {"ok": False, "status": "fail", "errors": ["wrong width"], "keyfit": {"status": "pass"}},
                       {"ok": True, "status": "pass", "errors": ["renderer error"], "keyfit": {"status": "pass"}},
                       {"ok": True, "status": "pass", "errors": [], "keyfit": {"status": "error"}}):
            with self.subTest(report=report):
                self.canvas_gate.side_effect = None
                self.canvas_gate.return_value = report
                self.assertEqual(self.build(), 1)
                self.assert_not_delivered("canvas/keyshape")

    def test_canvas_gate_exception_cannot_reuse_an_old_pass(self):
        stale = self.pack / "qa" / "old-run" / "canvas-keyshape"
        stale.mkdir(parents=True)
        (stale / "canvas-keyshape-results.json").write_text('{"ok":true,"failed":0}')
        self.canvas_gate.side_effect = RuntimeError("renderer unavailable")
        self.assertEqual(self.build(), 1)
        self.assert_not_delivered("renderer unavailable")
        aggregate = json.loads((Path(self.results()["qaDirectory"]) / "canvas-keyshape" / "canvas-keyshape-results.json").read_text())
        self.assertIs(aggregate["ok"], False)
        self.assertEqual(aggregate["failed"], 2)

    def test_failed_design_alias_blocks_delivery_even_when_canonical_passes(self):
        def gate(emitted, **kwargs):
            report = self.canvas_gate_result(emitted, **kwargs)
            if emitted.name.endswith("-design.svg"):
                report.update(ok=False, status="fail", errors=["incorrect alias size"])
            return report
        self.canvas_gate.side_effect = gate
        self.assertEqual(self.build(), 1)
        self.assert_not_delivered("incorrect alias size")

    def test_unbound_canvas_evidence_or_missing_raster_artifacts_block_delivery(self):
        for field in ("file", "svgSha256", "editableSha256", "profileSha256", "evidenceDirectory", "keyfitReport", "keyfitOverlay"):
            with self.subTest(field=field):
                def gate(emitted, **kwargs):
                    report = self.canvas_gate_result(emitted, **kwargs)
                    report.pop(field)
                    return report
                self.canvas_gate.side_effect = gate
                self.assertEqual(self.build(), 1)
                self.assert_not_delivered("canvas/keyshape")

    def test_custom_container_profile_still_requires_filled_preview_evidence(self):
        self.doc["iconType"] = "custom-frame"
        self.profile["containerSlot"] = {"x": 8, "y": 8, "w": 32, "h": 32, "acceptedProfile": "sub"}
        self.write_source()
        self.assertEqual(self.build(), 1)
        self.assert_not_delivered("container delivery requires separate filled-preview evidence")

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

    def test_design_alias_changed_after_gate_checks_is_not_delivered(self):
        def mutate_alias(*args):
            (self.pack / "output" / "test-icon-design.svg").write_text("not reviewed")
            return {"status": "pass"}
        self.holes.side_effect = mutate_alias
        self.assertEqual(self.build(), 1)
        self.assert_not_delivered("svgSha256")

    def test_canvas_evidence_removed_after_other_gates_is_not_delivered(self):
        def remove_evidence(*args):
            for report in (self.pack / "qa").rglob("canvas-keyshape.json"):
                report.unlink()
            return {"status": "pass"}
        self.holes.side_effect = remove_evidence
        self.assertEqual(self.build(), 1)
        self.assert_not_delivered("delivery:")

    def test_canvas_evidence_changed_to_error_after_other_gates_is_not_delivered(self):
        def mutate_evidence(*args):
            for report in (self.pack / "qa").rglob("canvas-keyshape.json"):
                content = json.loads(report.read_text())
                content.update(status="error", ok=False, errors=["gate crashed"])
                report.write_text(json.dumps(content))
            return {"status": "pass"}
        self.holes.side_effect = mutate_evidence
        self.assertEqual(self.build(), 1)
        self.assert_not_delivered("canvas/keyshape evidence is no longer passing")

    def test_report_links_resolve_to_generated_gate_report_files(self):
        self.assertEqual(self.build(), 0)
        parser = Links()
        parser.feed((self.pack / "review.html").read_text())
        for filename in ("canvas-keyshape-results.json", "grid-report.html", "keyfit-report.html", "hole-radius-report.html"):
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

    def test_generation_pack_delivery_named_after_upload_label_is_accepted(self):
        self.symbol["upload"] = "sym_1/sym_1_generated.svg"
        (self.pack / "manifest.json").write_text(json.dumps({"kind": "generate", "api": {"label": "generated"},
                                                              "symbols": [self.symbol]}))
        rows = rework_pack.load_pack(self.pack)
        self.assertEqual(rows[0]["destination"], self.folder / "sym_1_generated.svg")
        # Without the label the pack still only accepts the rework name.
        self.write_manifest([self.symbol])
        with self.assertRaisesRegex(ValueError, "unexpected rework destination"):
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
