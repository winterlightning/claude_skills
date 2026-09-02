#!/usr/bin/env python3
"""Regression coverage for normal, sub, and container profile plumbing."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

from icon_profiles import (
    canonical_tokens,
    document_icon_type,
    get_profile,
    validate_container_slot,
    validate_document_profile,
)
from keyfit import assign, circle_overflow, token_box
from validate_icon import container_paint_overlap


CORE = Path(__file__).resolve().parent


class IconProfileTests(unittest.TestCase):
    def test_normal_defaults_are_unchanged(self):
        profile = get_profile("normal")
        self.assertEqual(
            (profile["designCanvas"], profile["shipCanvas"], profile["designStroke"], profile["shipStroke"]),
            (48, 24, 4, 2),
        )
        self.assertEqual(profile["minimumDistinctCenterlineDistance"], 4)
        self.assertEqual(
            [item["name"] for item in canonical_tokens("normal")],
            ["circle-44", "square-40", "portrait-36x44", "landscape-44x36"],
        )

    def test_sub_profile_has_32_16_canvas_and_its_own_tokens(self):
        profile = get_profile("sub")
        self.assertEqual((profile["designCanvas"], profile["shipCanvas"]), (32, 16))
        self.assertEqual(profile["minimumDistinctCenterlineDistance"], 3)
        self.assertEqual(
            [item["name"] for item in canonical_tokens("sub")],
            ["circle-28", "square-24", "portrait-24x28", "landscape-28x24"],
        )
        self.assertEqual(token_box(28, 24, "sub"), (2, 4, 30, 28))
        self.assertEqual(assign((2, 4, 30, 28), icon_type="sub")["name"], "landscape-28x24")
        self.assertLessEqual(circle_overflow([(16, 4)], 4, "sub"), 0)

    def test_profile_declarations_reject_cross_profile_canvas(self):
        with self.assertRaisesRegex(ValueError, "sub design canvas is fixed at 32"):
            validate_document_profile({"iconType": "sub", "canvas": 48, "strokeWidth": 4})
        with self.assertRaisesRegex(ValueError, "container design canvas is fixed at 64"):
            validate_document_profile(
                {
                    "iconType": "container",
                    "canvas": 48,
                    "strokeWidth": 4,
                    "containerSlot": {
                        "x": 16,
                        "y": 16,
                        "w": 32,
                        "h": 32,
                        "acceptedKeyshape": "square-24",
                    },
                }
            )

    def test_explicit_empty_icon_type_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "unknown iconType"):
            document_icon_type({"iconType": ""})

    def test_container_has_a_dedicated_64_32_outer_profile(self):
        normal = get_profile("normal")
        container = get_profile("container")
        self.assertEqual(
            (container["designCanvas"], container["shipCanvas"]),
            (64, 32),
        )
        self.assertEqual(container["center"], {"x": 32, "y": 32})
        self.assertEqual(
            (container["designStroke"], container["shipStroke"]),
            (normal["designStroke"], normal["shipStroke"]),
        )
        self.assertEqual(container["minimumDistinctCenterlineDistance"], 4)
        self.assertEqual(
            [item["name"] for item in canonical_tokens("container")],
            ["circle-60", "square-56", "portrait-52x60", "landscape-60x52"],
        )
        self.assertEqual(token_box(60, 52, "container"), (2, 6, 62, 58))

    def test_container_slot_translates_each_sub_keyshape(self):
        expected = {
            "circle-28": [18, 18, 46, 46],
            "square-24": [20, 20, 44, 44],
            "portrait-24x28": [20, 18, 44, 46],
            "landscape-28x24": [18, 20, 46, 44],
        }
        for token, bounds in expected.items():
            with self.subTest(token=token):
                slot = validate_container_slot({
                    "containerSlot": {"x": 16, "y": 16, "w": 32, "h": 32, "acceptedKeyshape": token}
                })
                self.assertEqual(slot["acceptedBounds"], bounds)
                self.assertEqual(slot["protectedBounds"], [16, 16, 48, 48])
                self.assertEqual(slot["minimumClearSquare"], 32)

    def test_container_slot_metadata_and_painted_overlap_are_enforced(self):
        document = {
            "iconType": "container",
            "canvas": 64,
            "strokeWidth": 4,
            "containerSlot": {"x": 16, "y": 16, "w": 32, "h": 32, "acceptedKeyshape": "circle-28"},
        }
        _, profile = validate_document_profile(document)
        slot = validate_container_slot(document, profile)
        self.assertTrue(container_paint_overlap([(32, 32)], slot, 4))
        self.assertFalse(container_paint_overlap([(32, 4)], slot, 4))
        self.assertTrue(container_paint_overlap([(16, 16)], slot, 4))
        self.assertFalse(container_paint_overlap([(14, 16)], slot, 4))
        self.assertTrue(container_paint_overlap([(14.1, 16)], slot, 4))
        document["containerSlot"]["acceptedKeyshape"] = "circle-44"
        with self.assertRaisesRegex(ValueError, "unknown containerSlot.acceptedKeyshape"):
            validate_document_profile(document)

    def test_emit_and_validate_sub_and_container_documents(self):
        fixtures = [
            {
                "name": "profile-sub",
                "iconType": "sub",
                "canvas": 32,
                "strokeWidth": 4,
                "keyfitCheck": {"targetToken": "circle-28"},
                "instances": [{"shapeId": "circle", "x": 4, "y": 4, "w": 24, "h": 24, "rotation": 0, "z": 0}],
            },
            {
                "name": "profile-container",
                "iconType": "container",
                "canvas": 64,
                "strokeWidth": 4,
                "keyfitCheck": {"targetToken": "circle-60"},
                "containerSlot": {"x": 16, "y": 16, "w": 32, "h": 32, "acceptedKeyshape": "circle-28"},
                "instances": [{"shapeId": "circle", "x": 4, "y": 4, "w": 56, "h": 56, "rotation": 0, "z": 0}],
            },
        ]
        with TemporaryDirectory() as folder:
            root = Path(folder)
            for document in fixtures:
                with self.subTest(iconType=document["iconType"]):
                    editable = root / f"{document['name']}.json"
                    editable.write_text(json.dumps(document), encoding="utf-8")
                    emitted = subprocess.run(
                        [sys.executable, str(CORE / "emit_icon.py"), str(editable), "--out-dir", str(root)],
                        capture_output=True,
                        text=True,
                    )
                    self.assertEqual(emitted.returncode, 0, emitted.stdout + emitted.stderr)
                    checked = subprocess.run(
                        [sys.executable, str(CORE / "validate_icon.py"), str(editable), "--dir", str(root)],
                        capture_output=True,
                        text=True,
                    )
                    self.assertEqual(checked.returncode, 0, checked.stdout + checked.stderr)
                    ship_canvas = get_profile(document["iconType"])["shipCanvas"]
                    self.assertIn(f'viewBox="0 0 {ship_canvas} {ship_canvas}"', (root / f"{document['name']}.svg").read_text())

    def test_incomplete_source_analysis_is_an_explicit_gate(self):
        document = {
            "name": "incomplete-profile",
            "canvas": 48,
            "strokeWidth": 4,
            "keyfitCheck": {"targetToken": "circle-44"},
            "sourceAnalysis": {"incomplete": True},
            "instances": [{"shapeId": "circle", "x": 4, "y": 4, "w": 40, "h": 40, "rotation": 0, "z": 0}],
        }
        with TemporaryDirectory() as folder:
            root = Path(folder)
            editable = root / "incomplete-profile.json"
            editable.write_text(json.dumps(document), encoding="utf-8")
            subprocess.run(
                [sys.executable, str(CORE / "emit_icon.py"), str(editable), "--out-dir", str(root)],
                check=True,
                capture_output=True,
                text=True,
            )
            checked = subprocess.run(
                [sys.executable, str(CORE / "validate_icon.py"), str(editable), "--dir", str(root)],
                capture_output=True,
                text=True,
            )
            self.assertEqual(checked.returncode, 1)
            self.assertIn("sourceAnalysis is marked incomplete", checked.stdout)

    def test_structural_validation_rejects_noncanonical_emitted_geometry(self):
        document = {
            "name": "parity-profile",
            "iconType": "normal",
            "canvas": 48,
            "strokeWidth": 4,
            "keyfitCheck": {"targetToken": "square-40"},
            "instances": [{"shapeId": "square", "x": 6, "y": 6, "w": 36, "h": 36, "rotation": 0, "z": 0}],
        }
        with TemporaryDirectory() as folder:
            root = Path(folder)
            editable = root / "parity-profile.json"
            editable.write_text(json.dumps(document), encoding="utf-8")
            subprocess.run(
                [sys.executable, str(CORE / "emit_icon.py"), str(editable), "--out-dir", str(root)],
                check=True,
                capture_output=True,
                text=True,
            )
            (root / "parity-profile.svg").write_text(
                (root / "parity-profile-design.svg").read_text(encoding="utf-8"),
                encoding="utf-8",
            )
            checked = subprocess.run(
                [sys.executable, str(CORE / "validate_icon.py"), str(editable), "--dir", str(root)],
                capture_output=True,
                text=True,
            )
            self.assertEqual(checked.returncode, 1)
            self.assertIn("does not match canonical core/emit_icon.py output", checked.stdout)

    def test_structural_validation_leaves_angle_authority_to_grid_gate(self):
        document = {
            "name": "star-profile",
            "iconType": "sub",
            "canvas": 32,
            "strokeWidth": 4,
            "keyfitCheck": {"targetToken": "square-24"},
            "gridExceptions": {
                "offAngleInstances": [0],
                "reason": "A canonical five-point star has exact off-grid edges.",
            },
            "instances": [{"shapeId": "star", "x": 6, "y": 6, "w": 20, "h": 20, "rotation": 0, "z": 0}],
        }
        with TemporaryDirectory() as folder:
            root = Path(folder)
            editable = root / "star-profile.json"
            editable.write_text(json.dumps(document), encoding="utf-8")
            subprocess.run(
                [sys.executable, str(CORE / "emit_icon.py"), str(editable), "--out-dir", str(root)],
                check=True,
                capture_output=True,
                text=True,
            )
            checked = subprocess.run(
                [sys.executable, str(CORE / "validate_icon.py"), str(editable), "--dir", str(root)],
                capture_output=True,
                text=True,
            )
            self.assertEqual(checked.returncode, 0, checked.stdout + checked.stderr)

    def test_overlap_audit_uses_the_declared_profile_canvas(self):
        document = {
            "name": "overlap-sub",
            "iconType": "sub",
            "canvas": 32,
            "strokeWidth": 4,
            "sourceAnalysis": {
                "spacingChecks": [
                    {"instances": [0, 1], "relation": "ordinary-distinct", "pair": ["left", "right"]}
                ]
            },
            "instances": [
                {"shapeId": "line", "x": 4, "y": 8, "w": 8, "h": 1, "rotation": 0, "z": 0},
                {"shapeId": "line", "x": 20, "y": 8, "w": 8, "h": 1, "rotation": 0, "z": 1},
            ],
        }
        with TemporaryDirectory() as folder:
            root = Path(folder)
            editable = root / "overlap-sub.json"
            output = root / "overlap-sub.svg"
            editable.write_text(json.dumps(document), encoding="utf-8")
            checked = subprocess.run(
                [sys.executable, str(CORE / "render_overlap_audit.py"), str(editable), str(output)],
                capture_output=True,
                text=True,
            )
            self.assertEqual(checked.returncode, 0, checked.stdout + checked.stderr)
            report = output.read_text(encoding="utf-8")
            self.assertIn('viewBox="0 0 32 37"', report)
            self.assertIn("ordinary-distinct · 3u", report)

    def test_structural_spacing_floor_is_profile_specific(self):
        fixtures = [
            ("sub-distance-three", "sub", 32, "square-24", 20, 8.5, 0, None),
            ("sub-distance-under-three", "sub", 32, "square-24", 20, 8.25, 1, "under the 3u sub collision floor"),
            ("normal-distance-three", "normal", 48, "square-40", 36, 8.5, 1, "under the 4u normal collision floor"),
        ]
        with TemporaryDirectory() as folder:
            root = Path(folder)
            for name, icon_type, canvas, token, shell_size, detail_y, expected_code, expected_message in fixtures:
                with self.subTest(icon_type=icon_type, detail_y=detail_y):
                    document = {
                        "name": name,
                        "iconType": icon_type,
                        "canvas": canvas,
                        "strokeWidth": 4,
                        "keyfitCheck": {"targetToken": token},
                        "instances": [
                            {"shapeId": "square", "x": 6, "y": 6, "w": shell_size, "h": shell_size, "rotation": 0, "z": 0},
                            {"shapeId": "line", "x": 10, "y": detail_y, "w": 12, "h": 1, "rotation": 0, "z": 1},
                        ],
                    }
                    editable = root / f"{name}.json"
                    editable.write_text(json.dumps(document), encoding="utf-8")
                    subprocess.run(
                        [sys.executable, str(CORE / "emit_icon.py"), str(editable), "--out-dir", str(root)],
                        check=True,
                        capture_output=True,
                        text=True,
                    )
                    checked = subprocess.run(
                        [sys.executable, str(CORE / "validate_icon.py"), str(editable), "--dir", str(root)],
                        capture_output=True,
                        text=True,
                    )
                    self.assertEqual(checked.returncode, expected_code, checked.stdout + checked.stderr)
                    if expected_message:
                        self.assertIn(expected_message, checked.stdout)

    def test_container_validator_rejects_paint_in_protected_region(self):
        document = {
            "name": "colliding-container",
            "iconType": "container",
            "canvas": 64,
            "strokeWidth": 4,
            "keyfitCheck": {"targetToken": "circle-60"},
            "containerSlot": {"x": 16, "y": 16, "w": 32, "h": 32, "acceptedKeyshape": "circle-28"},
            "instances": [
                {"shapeId": "circle", "x": 4, "y": 4, "w": 56, "h": 56, "rotation": 0, "z": 0},
                {"shapeId": "dot", "x": 14, "y": 14, "w": 4, "h": 4, "rotation": 0, "z": 1},
            ],
        }
        with TemporaryDirectory() as folder:
            root = Path(folder)
            editable = root / "colliding-container.json"
            editable.write_text(json.dumps(document), encoding="utf-8")
            subprocess.run(
                [sys.executable, str(CORE / "emit_icon.py"), str(editable), "--out-dir", str(root)],
                check=True,
                capture_output=True,
                text=True,
            )
            checked = subprocess.run(
                [sys.executable, str(CORE / "validate_icon.py"), str(editable), "--dir", str(root)],
                capture_output=True,
                text=True,
            )
            self.assertEqual(checked.returncode, 1)
            self.assertIn("container paint enters the protected 32x32 clearance", checked.stdout)


if __name__ == "__main__":
    unittest.main()
