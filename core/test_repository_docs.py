#!/usr/bin/env python3
"""Repository checks for maintained Markdown links and script inventory drift."""

from __future__ import annotations

import re
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
        inventory_path = ROOT / "docs" / "scripts.md"
        self.assertTrue(inventory_path.is_file(), "docs/scripts.md is missing")
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
            "core/check_svg_grid.py",
            "core/render_overlap_audit.py",
            "core/check_keyfit.py",
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
        self.assertIn('grid|keyshape|holes) target="$QA_ROOT/$gate"', verify_stage)
        self.assertIn('[[ ! -L "$QA_ROOT" ]]', verify_stage)
        self.assertIn('rm -rf -- "$target"', verify_stage)
        for gate, command in (
            ("grid", "core/check_svg_grid.py"),
            ("keyshape", "core/check_keyfit.py"),
            ("holes", "core/qa_overlays.py"),
        ):
            with self.subTest(fresh_report_gate=gate):
                reset_at = verify_stage.index(f'reset_qa_dir "{gate}"')
                command_at = verify_stage.index(f"if ! python3 {command}", reset_at)
                command_end = verify_stage.index("\n  fi", command_at)
                self.assertLess(reset_at, command_at)
                self.assertIn("QA_FAILED=1", verify_stage[command_at:command_end])

        self.assertIn("python3 - \"$BATCH\" <<'PY' || QA_FAILED=1", verify_stage)


if __name__ == "__main__":
    unittest.main()
