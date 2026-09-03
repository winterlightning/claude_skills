#!/usr/bin/env python3
"""Repository checks for maintained Markdown links and script inventory drift."""

from __future__ import annotations

import json
import hashlib
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"!?\[[^\]]*\]\((?P<target><[^>]+>|[^\s)]+)")
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)


def maintained_markdown() -> list[Path]:
    """Return repository documentation without sweeping generated work batches."""
    files = sorted((ROOT / "docs").rglob("*.md"))
    root_readme = ROOT / "readme.md"
    if root_readme.is_file():
        files.insert(0, root_readme)
    return files


def local_targets(source: Path) -> list[tuple[str, Path, str]]:
    targets: list[tuple[str, Path, str]] = []
    for match in LINK.finditer(source.read_text(encoding="utf-8")):
        raw = match.group("target").strip("<>")
        parsed = urlsplit(raw)
        if parsed.scheme or parsed.netloc:
            continue
        target = (
            (source.parent / unquote(parsed.path)).resolve()
            if parsed.path
            else source.resolve()
        )
        targets.append((raw, target, unquote(parsed.fragment).lower()))
    return targets


def markdown_anchors(path: Path) -> set[str]:
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for heading in HEADING.findall(path.read_text(encoding="utf-8")):
        plain = re.sub(r"!?\[([^\]]+)\]\([^)]*\)", r"\1", heading)
        plain = re.sub(r"<[^>]+>|[`*_~]", "", plain).strip().lower()
        slug = "".join(char for char in plain if char.isalnum() or char in " _-")
        slug = re.sub(r"\s+", "-", slug)
        suffix = counts.get(slug, 0)
        counts[slug] = suffix + 1
        anchors.add(slug if suffix == 0 else f"{slug}-{suffix}")
    return anchors


class RepositoryDocumentationTests(unittest.TestCase):
    def run_rework_report_preflight(self, mutate=None) -> subprocess.CompletedProcess[str]:
        """Run the wrapper's report reader with local evidence; never upload."""
        from icon_profiles import get_profile

        wrapper = (ROOT / "rework_opus.sh").read_text(encoding="utf-8")
        verify = wrapper.split("# --------------------------------------------------------------------- verify", 1)[1]
        script = verify.split('python3 - "$BATCH" <<\'PY\' || QA_FAILED=1\n', 1)[1].split("\nPY\n", 1)[0]
        with tempfile.TemporaryDirectory(prefix="rework-gate-check-") as temporary:
            batch = Path(temporary).resolve()
            (batch / "editable").mkdir()
            (batch / "output").mkdir()
            symbol = {"sid": "sym_000005", "iconName": "test-icon",
                      "design": "output/test-icon-design.svg", "ship": "output/test-icon.svg"}
            (batch / "batch.json").write_text(json.dumps({"symbols": [symbol]}))
            source = batch / "editable/test-icon.json"
            source.write_text('{"iconType":"normal"}')
            rows = []
            profile = json.dumps(get_profile("normal"), sort_keys=True, separators=(",", ":"),
                                 ensure_ascii=False, allow_nan=False).encode()
            for field in ("ship", "design"):
                emitted = batch / symbol[field]
                emitted.write_text("<svg />")
                evidence = batch / "qa/canvas-keyshape/files" / emitted.stem
                evidence.mkdir(parents=True)
                keyfit = {"file": emitted.name, "status": "pass"}
                keyfit_report = evidence / f"{emitted.stem}.keyfit.json"
                keyfit_overlay = evidence / f"{emitted.stem}_keyfit.png"
                keyfit_report.write_text(json.dumps(keyfit))
                keyfit_overlay.write_bytes(b"mock overlay")
                rows.append({"file": emitted.name, "ok": True, "status": "pass", "errors": [],
                             "issues": [], "keyfit": keyfit,
                             "svgSha256": hashlib.sha256(emitted.read_bytes()).hexdigest(),
                             "editableSha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                             "profileSha256": hashlib.sha256(profile).hexdigest(),
                             "evidenceDirectory": str(evidence), "keyfitReport": str(keyfit_report),
                             "keyfitOverlay": str(keyfit_overlay)})
            for gate, filename, field, status in (("grid", "grid-results.json", "design", "overallStatus"),
                                                 ("keyshape", "keyfit-results.json", "ship", "status"),
                                                 ("holes", "hole-diameters.json", "ship", "status")):
                folder = batch / "qa" / gate
                folder.mkdir(parents=True)
                (folder / filename).write_text(json.dumps([{"file": Path(symbol[field]).name, status: "pass"}]))
            aggregate = {"checked": 2, "failed": 0, "ok": True, "rows": rows}
            keep_report = mutate(batch, aggregate) if mutate else True
            for row in aggregate.get("rows", []) if isinstance(aggregate.get("rows"), list) else []:
                if isinstance(row, dict) and isinstance(row.get("evidenceDirectory"), str):
                    evidence = Path(row["evidenceDirectory"]) / "canvas-keyshape.json"
                    evidence.write_text(json.dumps(row))
            if keep_report is not False:
                (batch / "qa/canvas-keyshape/canvas-keyshape-results.json").write_text(json.dumps(aggregate))
            return subprocess.run([sys.executable, "-B", "-c", script, str(batch)],
                                  cwd=ROOT, capture_output=True, text=True)

    def run_rework_source_preflight(self, document: object) -> subprocess.CompletedProcess[str]:
        """Exercise only the wrapper's read-only source check, never its stages."""
        wrapper = (ROOT / "rework_opus.sh").read_text(encoding="utf-8")
        verify = wrapper.split("# --------------------------------------------------------------------- verify", 1)[1]
        script = verify.split("<<'PY' || exit 1\n", 1)[1].split("\nPY\n", 1)[0]
        with tempfile.TemporaryDirectory(prefix="rework-source-check-") as temporary:
            batch = Path(temporary)
            (batch / "editable").mkdir()
            (batch / "output").mkdir()
            symbol = {"sid": "sym_000005", "iconName": "test-icon",
                      "design": "output/test-icon-design.svg", "ship": "output/test-icon.svg"}
            (batch / "batch.json").write_text(json.dumps({"symbols": [symbol]}), encoding="utf-8")
            (batch / "editable/test-icon.json").write_text(json.dumps(document), encoding="utf-8")
            # Geometry/paint correctness belongs to the later structural gate.
            for key in ("design", "ship"):
                (batch / symbol[key]).write_text("<svg />", encoding="utf-8")
            return subprocess.run([sys.executable, "-B", "-c", script, str(batch)],
                                  cwd=ROOT, capture_output=True, text=True)

    def test_rework_source_preflight_accepts_version_two_normal_geometry(self) -> None:
        document = {"schemaVersion": 2, "name": "test-icon", "iconType": "normal",
                    "elements": [{"id": "line", "tag": "line",
                                  "attrs": {"x1": 4, "y1": 24, "x2": 44, "y2": 24}}]}
        result = self.run_rework_source_preflight(document)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_rework_source_preflight_rejects_legacy_or_mismatched_sources(self) -> None:
        valid = {"schemaVersion": 2, "name": "test-icon", "iconType": "normal",
                 "elements": [{"id": "line", "tag": "line", "attrs": {}}]}
        invalid_sources = [
            {"name": "test-icon", "instances": [{"shapeId": "line"}]},
            {**valid, "instances": []},
            {**valid, "elements": []},
            {**valid, "iconType": "sub"},
            {**valid, "name": "other-icon"},
            [],
        ]
        for document in invalid_sources:
            with self.subTest(document=document):
                result = self.run_rework_source_preflight(document)
                self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_rework_report_reader_accepts_complete_fresh_canvas_gate_evidence(self) -> None:
        result = self.run_rework_report_preflight()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_rework_report_reader_rejects_missing_failed_or_incomplete_canvas_gate(self) -> None:
        mutations = (
            lambda batch, report: False,
            lambda batch, report: report["rows"].pop(),
            lambda batch, report: report.update(rows=[]),
            lambda batch, report: report.update(rows="malformed"),
            lambda batch, report: report["rows"].append(report["rows"][0]),
            lambda batch, report: report.update(ok=False, failed=1),
            lambda batch, report: report["rows"][0].update(ok=False, status="fail", errors=["incorrect native width"]),
            lambda batch, report: report["rows"][0].update(status="error"),
            lambda batch, report: report["rows"][0].pop("keyfit"),
            lambda batch, report: report["rows"][0].update(errors=["renderer unavailable"]),
        )
        for index, mutate in enumerate(mutations):
            with self.subTest(case=index):
                result = self.run_rework_report_preflight(mutate)
                self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_rework_report_reader_rejects_stale_geometry_profile_and_missing_artifacts(self) -> None:
        mutations = (
            lambda batch, report: (batch / "output/test-icon-design.svg").write_text("changed after QA"),
            lambda batch, report: (batch / "editable/test-icon.json").write_text("changed after QA"),
            lambda batch, report: report["rows"][0].update(profileSha256="0" * 64),
            lambda batch, report: Path(report["rows"][0]["keyfitOverlay"]).unlink(),
            lambda batch, report: report["rows"][0].pop("evidenceDirectory"),
        )
        for index, mutate in enumerate(mutations):
            with self.subTest(case=index):
                result = self.run_rework_report_preflight(mutate)
                self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_local_markdown_links_resolve(self) -> None:
        missing: list[str] = []
        for source in maintained_markdown():
            for raw, target, fragment in local_targets(source):
                if not target.exists():
                    missing.append(f"{source.relative_to(ROOT)} -> {raw}")
                elif fragment and target.suffix.lower() == ".md" and fragment not in markdown_anchors(target):
                    missing.append(f"{source.relative_to(ROOT)} -> {raw} (missing heading)")
        self.assertEqual(missing, [], "broken local Markdown links:\n" + "\n".join(missing))

    def test_every_core_python_file_is_in_the_script_inventory(self) -> None:
        inventory_path = ROOT / "docs" / "shared" / "scripts.md"
        self.assertTrue(inventory_path.is_file(), "docs/shared/scripts.md is missing")
        inventory = inventory_path.read_text(encoding="utf-8")
        missing = [
            f"core/{path.name}"
            for path in sorted((ROOT / "core").glob("*.py"))
            if f"core/{path.name}" not in inventory
        ]
        self.assertEqual(missing, [], "undocumented core Python files:\n" + "\n".join(missing))

    def test_rework_verify_wires_every_automated_gate_before_upload(self) -> None:
        wrapper = (ROOT / "rework_opus.sh").read_text(encoding="utf-8")
        verify = wrapper.index("# --------------------------------------------------------------------- verify")
        upload = wrapper.index("# --------------------------------------------------------------------- upload")
        verify_stage = wrapper[verify:upload]
        for command in (
            "core/validate_icon.py",
            "core/validate_icon_keyshapes.py",
            "core/check_svg_grid.py",
            "core/render_overlap_audit.py",
            "check_keyfit.write_aggregate",
            "core/qa_overlays.py",
        ):
            with self.subTest(command=command):
                self.assertIn(command, verify_stage)
        self.assertIn("STRUCTURE_FAILED", verify_stage)
        self.assertIn("OVERLAP_FAILED", verify_stage)
        self.assertIn("QA_FAILED", verify_stage)
        self.assertNotIn("|| true", verify_stage)

        # A failed command must not be allowed to reuse a passing aggregate
        # from an earlier verification run.
        self.assertIn('grid|canvas-keyshape|keyshape|holes) target="$QA_ROOT/$gate"', verify_stage)
        self.assertIn("if active verify || active upload; then", verify_stage)
        self.assertIn('[[ ! -L "$QA_ROOT" ]]', verify_stage)
        self.assertIn('rm -rf -- "$target"', verify_stage)
        for gate, command in (
            ("grid", "core/check_svg_grid.py"),
            ("canvas-keyshape", "core/validate_icon_keyshapes.py"),
            ("holes", "core/qa_overlays.py"),
        ):
            with self.subTest(fresh_report_gate=gate):
                reset_at = verify_stage.index(f'reset_qa_dir "{gate}"')
                command_at = verify_stage.index(f"if ! python3 {command}", reset_at)
                command_end = verify_stage.index("\n  fi", command_at)
                self.assertLess(reset_at, command_at)
                self.assertIn("QA_FAILED=1", verify_stage[command_at:command_end])

        self.assertIn("python3 - \"$BATCH\" <<'PY' || QA_FAILED=1", verify_stage)

        gate_command = verify_stage.split("if ! python3 core/validate_icon_keyshapes.py", 1)[1].split("\n  fi", 1)[0]
        self.assertIn('"${SHIPS[@]}" "${DESIGNS[@]}"', gate_command)
        self.assertIn('--expected-editable-dir "$BATCH/editable"', gate_command)
        self.assertNotIn("python3 core/check_keyfit.py", verify_stage,
                         "reuse the mandatory gate's raster evidence rather than render it again")


if __name__ == "__main__":
    unittest.main()
