"""Raster regression tests for the four painted keyshape boundaries."""

import importlib.util
import json
import subprocess
import sys
import unittest
from importlib.util import find_spec
from pathlib import Path
from tempfile import TemporaryDirectory


RASTER_AVAILABLE = all(find_spec(name) is not None for name in ("cairosvg", "numpy", "PIL"))


@unittest.skipUnless(RASTER_AVAILABLE, "raster keyshape dependencies are unavailable")
class RasterKeyshapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        script = Path(__file__).resolve().parent.parent / "core/check_keyfit.py"
        cls.script = script
        spec = importlib.util.spec_from_file_location("check_keyfit_raster", script)
        cls.module = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(cls.module)

    def check(
        self,
        body: str,
        token: str | None = None,
        *,
        icon_type: str = "normal",
        design: bool = False,
    ) -> dict:
        with TemporaryDirectory() as folder:
            root = Path(folder)
            svg = root / "icon.svg"
            profile = self.module.get_profile(icon_type)
            canvas = profile["designCanvas" if design else "shipCanvas"]
            stroke = profile["designStroke" if design else "shipStroke"]
            svg.write_text(
                f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {canvas} {canvas}" '
                f'fill="none" stroke="currentColor" stroke-width="{stroke}" '
                f'stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
            )
            return self.module.process(svg, root, 64, 2 / 64, token, icon_type)

    def test_circle_reaches_cardinals_and_stays_radial(self):
        result = self.check('<circle cx="12" cy="12" r="10"/>', "circle-44")
        self.assertEqual(result["status"], "pass")
        self.assertLessEqual(result["circleOverflowDesignU"], result["toleranceDesignUnits"])

    def test_inference_requires_a_dominant_large_circle(self):
        result = self.check('<circle cx="12" cy="12" r="10"/>')
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["assignedToken"]["name"], "circle-44")
        self.assertTrue(result["circleDetection"]["isDominantLargeCircle"])

    def test_house_silhouette_uses_rectangular_fallback(self):
        result = self.check(
            '<path d="M3.4445 7.7475V21.192H20.5555V7.7475"/>'
            '<path d="M1 9.1585L12 2.808L23 9.1585"/>'
            '<path d="M8.3335 21.192V12.6365H15.6665V21.192"/>'
        )
        self.assertFalse(result["circleDetection"]["isDominantLargeCircle"])
        self.assertEqual(result["targetToken"]["name"], "landscape-44x36")

    def test_circle_rejects_corner_paint_with_same_rectangular_bounds(self):
        result = self.check('<rect x="2" y="2" width="20" height="20"/>', "circle-44")
        self.assertEqual(result["status"], "fail")
        self.assertEqual(result["reason"], "paint-crosses-circle-keyshape")

    def test_three_rectangular_keyshapes(self):
        fixtures = (
            ('<rect x="3" y="3" width="18" height="18"/>', "square-40"),
            ('<rect x="4" y="2" width="16" height="20"/>', "portrait-36x44"),
            ('<rect x="2" y="4" width="20" height="16"/>', "landscape-44x36"),
        )
        for body, token in fixtures:
            with self.subTest(token=token):
                self.assertEqual(self.check(body, token)["status"], "pass")

    def test_sub_circle_uses_32u_design_and_16px_ship_profile(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            svg = root / "sub.svg"
            svg.write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" '
                'fill="none" stroke="currentColor" stroke-width="2">'
                '<circle cx="8" cy="8" r="7"/></svg>'
            )
            result = self.module.process(svg, root, 64, 2 / 64, "circle-32", "sub")
            self.assertEqual(result["status"], "pass")
            self.assertEqual(result["iconType"], "sub")
            self.assertEqual((result["designCanvas"], result["shipCanvas"]), (32, 16))
            self.assertEqual(result["assignedToken"]["name"], "circle-32")
            self.assertEqual(result["paintedBoundsDesign"], [0, 0, 32, 32])

    def test_sub_rectangular_keyshapes_include_stroke_at_canvas_edges(self):
        fixtures = (
            ('<rect x="1" y="1" width="14" height="14"/>', "square-32", [0, 0, 32, 32]),
            ('<rect x="2" y="1" width="12" height="14"/>', "portrait-28x32", [2, 0, 30, 32]),
            ('<rect x="1" y="2" width="14" height="12"/>', "landscape-32x28", [0, 2, 32, 30]),
        )
        for body, token, bounds in fixtures:
            with self.subTest(token=token):
                result = self.check(body, token, icon_type="sub")
                self.assertEqual(result["status"], "pass")
                self.assertEqual(result["assignedToken"]["name"], token)
                self.assertEqual(result["paintedBoundsDesign"], bounds)

    def test_sub_inference_disambiguates_equal_sized_circle_and_square(self):
        fixtures = (
            ('<circle cx="8" cy="8" r="7"/>', "circle-32", True),
            ('<rect x="1" y="1" width="14" height="14"/>', "square-32", False),
        )
        for body, token, circle_evidence in fixtures:
            with self.subTest(token=token):
                result = self.check(body, icon_type="sub")
                self.assertEqual(result["status"], "pass")
                self.assertEqual(result["assignedToken"]["name"], token)
                self.assertEqual(result["circleDetection"]["isDominantLargeCircle"], circle_evidence)

    def test_sub_declared_square_is_not_replaced_by_circle_inference(self):
        result = self.check(
            '<circle cx="8" cy="8" r="7"/>', "square-32", icon_type="sub"
        )
        self.assertTrue(result["circleDetection"]["isDominantLargeCircle"])
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["assignedToken"]["name"], "square-32")

    def test_sub_circle_rejects_corner_paint_with_shared_square_bounds(self):
        result = self.check(
            '<rect x="1" y="1" width="14" height="14"/>', "circle-32", icon_type="sub"
        )
        self.assertEqual(result["paintedBoundsDesign"], [0, 0, 32, 32])
        self.assertEqual(result["status"], "fail")
        self.assertEqual(result["reason"], "paint-crosses-circle-keyshape")

    def test_sub_keyshapes_reject_stroke_hidden_by_canvas_clipping(self):
        fixtures = (
            ('<rect x="0" y="0" width="16" height="16"/>', "square-32", [-2, -2, 34, 34]),
            ('<rect x="2" y="0" width="12" height="16"/>', "portrait-28x32", [2, -2, 30, 34]),
            ('<rect x="0" y="2" width="16" height="12"/>', "landscape-32x28", [-2, 2, 34, 30]),
            ('<circle cx="8" cy="8" r="8"/>', "circle-32", [-2, -2, 34, 34]),
        )
        for body, token, bounds in fixtures:
            with self.subTest(token=token):
                result = self.check(body, token, icon_type="sub")
                self.assertEqual(result["status"], "fail")
                self.assertEqual(result["paintedBoundsDesign"], bounds)
                self.assertTrue(any(
                    value > 0 for value in result["overflowBeyondAbsoluteKeyfitBounds"].values()
                ))

    def test_sub_design_and_ship_measure_the_same_full_canvas_boundary(self):
        design = self.check(
            '<circle cx="16" cy="16" r="14"/>', "circle-32", icon_type="sub", design=True
        )
        ship = self.check('<circle cx="8" cy="8" r="7"/>', "circle-32", icon_type="sub")
        self.assertEqual(design["status"], "pass")
        self.assertEqual(ship["status"], "pass")
        self.assertEqual(design["paintedBoundsDesign"], ship["paintedBoundsDesign"])

    def test_padded_measurement_preserves_viewport_mapping_and_source(self):
        fixtures = (
            (
                'viewBox="0 0 16 16" style="color:#008000;overflow:hidden !important"',
                '<rect x="0" y="0" width="16" height="16"/>',
                "fail",
                [-2, -2, 34, 34],
            ),
            (
                'viewBox="0 0 16 16"',
                '<rect x="6.25%" y="6.25%" width="87.5%" height="87.5%"/>',
                "pass",
                [0, 0, 32, 32],
            ),
            (
                'viewBox="4 4 16 16"',
                '<rect x="5" y="5" width="14" height="14"/>',
                "pass",
                [0, 0, 32, 32],
            ),
        )
        with TemporaryDirectory() as folder:
            root = Path(folder)
            svg = root / "viewport.svg"
            for attributes, body, status, bounds in fixtures:
                with self.subTest(attributes=attributes):
                    source = (
                        f'<svg xmlns="http://www.w3.org/2000/svg" {attributes} '
                        'fill="none" stroke="currentColor" stroke-width="2" '
                        f'stroke-linejoin="round">{body}</svg>'
                    )
                    svg.write_text(source)
                    result = self.module.process(svg, root, 64, 2 / 64, "square-32", "sub")
                    self.assertEqual(result["status"], status)
                    self.assertEqual(result["paintedBoundsDesign"], bounds)
                    self.assertEqual(svg.read_text(), source)

    def test_container_circle_uses_64u_design_and_32px_ship_profile(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            svg = root / "container.svg"
            svg.write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" '
                'fill="none" stroke="currentColor" stroke-width="2">'
                '<circle cx="16" cy="16" r="14"/></svg>'
            )
            result = self.module.process(
                svg,
                root,
                64,
                2 / 64,
                "circle-60",
                "container",
            )
            self.assertEqual(result["status"], "pass")
            self.assertEqual(result["iconType"], "container")
            self.assertEqual((result["designCanvas"], result["shipCanvas"]), (64, 32))

    def test_cli_returns_failure_status_for_keyshape_violation(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            svg = root / "icon.svg"
            svg.write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" '
                'fill="none" stroke="currentColor" stroke-width="2">'
                '<rect x="2" y="2" width="20" height="20"/></svg>'
            )
            (root / "icon.json").write_text(json.dumps({"keyfitCheck": {"targetToken": "circle-44"}}))
            result = subprocess.run(
                [sys.executable, str(self.script), str(svg), "--expected-editable-dir", str(root), "--output-dir", str(root / "qa")],
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
