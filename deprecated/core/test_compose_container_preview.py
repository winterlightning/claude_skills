#!/usr/bin/env python3
"""Regression tests for the non-shipping container preview compositor."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

from compose_container_preview import compose


CORE = Path(__file__).resolve().parent


def container_document(accepted_keyshape: str = "circle-32") -> dict:
    return {
        "name": "badge-container",
        "iconType": "container",
        "canvas": 64,
        "strokeWidth": 4,
        "keyfitCheck": {"targetToken": "circle-60"},
        "containerSlot": {
            "x": 16,
            "y": 16,
            "w": 32,
            "h": 32,
            "acceptedKeyshape": accepted_keyshape,
        },
        "instances": [
            {
                "shapeId": "circle",
                "x": 4,
                "y": 4,
                "w": 56,
                "h": 56,
                "rotation": 0,
                "z": 0,
            }
        ],
    }


def sub_document(keyshape: str = "circle-32") -> dict:
    if keyshape == "circle-32":
        shape_id, x, y, width, height = "circle", 2, 2, 28, 28
    elif keyshape == "square-32":
        shape_id, x, y, width, height = "square", 2, 2, 28, 28
    else:
        raise ValueError(f"unsupported test keyshape {keyshape}")
    return {
        "name": f"preview-{keyshape}-sub",
        "iconType": "sub",
        "canvas": 32,
        "strokeWidth": 4,
        "keyfitCheck": {"targetToken": keyshape},
        "instances": [
            {
                "shapeId": shape_id,
                "x": x,
                "y": y,
                "w": width,
                "h": height,
                "rotation": 0,
                "z": 0,
            }
        ],
    }


def write_fixture(
    root: Path,
    *,
    accepted_keyshape: str = "circle-32",
    sub_keyshape: str = "circle-32",
) -> Path:
    sources = root / "sources"
    sources.mkdir()
    (sources / "container.json").write_text(
        json.dumps(container_document(accepted_keyshape)),
        encoding="utf-8",
    )
    (sources / "sub.json").write_text(
        json.dumps(sub_document(sub_keyshape)),
        encoding="utf-8",
    )
    manifest = root / "filled-preview.json"
    manifest.write_text(
        json.dumps(
            {
                "schemaVersion": 1,
                "kind": "container-filled-preview",
                "name": "badge-container-filled-preview",
                "container": "sources/container.json",
                "sub": "sources/sub.json",
            }
        ),
        encoding="utf-8",
    )
    return manifest


class ContainerPreviewTests(unittest.TestCase):
    def test_manifest_is_lightweight_and_regeneration_is_deterministic(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            manifest_path = write_fixture(root)
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertEqual(manifest["kind"], "container-filled-preview")
            self.assertNotIn("iconType", manifest)
            self.assertNotIn("instances", manifest)

            first_design, first_ship = compose(manifest_path, root / "out-a")
            second_design, second_ship = compose(manifest_path, root / "out-b")
            self.assertEqual(first_design.read_bytes(), second_design.read_bytes())
            self.assertEqual(first_ship.read_bytes(), second_ship.read_bytes())

    def test_preview_uses_native_64_container_canvas_and_centered_slot(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            manifest_path = write_fixture(root)
            design, ship = compose(manifest_path, root / "out")
            design_text = design.read_text(encoding="utf-8")
            ship_text = ship.read_text(encoding="utf-8")
            self.assertIn('viewBox="0 0 64 64"', design_text)
            self.assertIn('viewBox="0 0 64 64"', ship_text)
            self.assertIn('<path d="M 32 18 A 14 14', design_text)
            self.assertIn('<path d="M 32 18 A 14 14', ship_text)
            self.assertEqual(design_text, ship_text)

    def test_reusable_sub_source_is_a_real_sub_profile_document(self):
        circle = sub_document("circle-32")
        square = sub_document("square-32")
        self.assertEqual(
            (circle["iconType"], circle["canvas"], circle["keyfitCheck"]["targetToken"]),
            ("sub", 32, "circle-32"),
        )
        self.assertEqual(
            (square["iconType"], square["canvas"], square["keyfitCheck"]["targetToken"]),
            ("sub", 32, "square-32"),
        )

    def test_manifest_references_are_resolved_relative_to_the_manifest(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            manifest = write_fixture(root)
            design, ship = compose(manifest, root / "out")
            self.assertIn('<path d="M 32 18 A 14 14', design.read_text(encoding="utf-8"))
            self.assertIn('<path d="M 32 18 A 14 14', ship.read_text(encoding="utf-8"))

    def test_accepted_keyshape_must_match_sub_declaration(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            manifest = write_fixture(
                root,
                accepted_keyshape="circle-32",
                sub_keyshape="square-32",
            )
            with self.assertRaisesRegex(
                ValueError,
                "container accepts circle-32, but sub declares square-32",
            ):
                compose(manifest, root / "out")

    def test_compositor_rejects_absolute_references(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            absolute_container = root / "container.json"
            absolute_container.write_text(
                json.dumps(container_document()),
                encoding="utf-8",
            )
            manifest = root / "absolute.json"
            manifest.write_text(
                json.dumps(
                    {
                        "schemaVersion": 1,
                        "kind": "container-filled-preview",
                        "name": "absolute-preview",
                        "container": str(absolute_container),
                        "sub": "sub.json",
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "path must be relative"):
                compose(manifest, root / "out")

    def test_cli_labels_outputs_non_shipping(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            manifest = write_fixture(root)
            result = subprocess.run(
                [
                    sys.executable,
                    str(CORE / "compose_container_preview.py"),
                    str(manifest),
                    "--out-dir",
                    str(root / "out"),
                ],
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("NON-SHIPPING preview emitted", result.stdout)


if __name__ == "__main__":
    unittest.main()
