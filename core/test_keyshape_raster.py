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
        result = self.check('<circle cx="24" cy="24" r="20"/>', "circle-44")
        self.assertEqual(result["status"], "pass")
        self.assertLessEqual(result["circleOverflowDesignU"], result["toleranceDesignUnits"])

    def test_inference_requires_a_dominant_large_circle(self):
        result = self.check('<circle cx="24" cy="24" r="20"/>')
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["assignedToken"]["name"], "circle-44")
        self.assertTrue(result["circleDetection"]["isDominantLargeCircle"])

    def test_house_silhouette_uses_rectangular_fallback(self):
        result = self.check(
            '<path d="M6.889 15.495V42.384H41.111V15.495"/>'
            '<path d="M2 18.317L24 5.616L46 18.317"/>'
            '<path d="M16.667 42.384V25.273H31.333V42.384"/>'
        )
        self.assertFalse(result["circleDetection"]["isDominantLargeCircle"])
        self.assertEqual(result["targetToken"]["name"], "landscape-44x36")

    def test_circle_rejects_corner_paint_with_same_rectangular_bounds(self):
        result = self.check('<rect x="4" y="4" width="40" height="40"/>', "circle-44")
        self.assertEqual(result["status"], "fail")
        self.assertEqual(result["reason"], "paint-crosses-circle-keyshape")

    def test_three_rectangular_keyshapes(self):
        fixtures = (
            ('<rect x="6" y="6" width="36" height="36"/>', "square-40"),
            ('<rect x="8" y="4" width="32" height="40"/>', "portrait-36x44"),
            ('<rect x="4" y="8" width="40" height="32"/>', "landscape-44x36"),
        )
        for body, token in fixtures:
            with self.subTest(token=token):
                self.assertEqual(self.check(body, token)["status"], "pass")

    def test_sub_circle_uses_native_32_profile(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            svg = root / "sub.svg"
            svg.write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" '
                'fill="none" stroke="currentColor" stroke-width="4">'
                '<circle cx="16" cy="16" r="14"/></svg>'
            )
            result = self.module.process(svg, root, 64, 2 / 64, "circle-32", "sub")
            self.assertEqual(result["status"], "pass")
            self.assertEqual(result["iconType"], "sub")
            self.assertEqual((result["designCanvas"], result["shipCanvas"]), (32, 32))
            self.assertEqual(result["assignedToken"]["name"], "circle-32")
            self.assertEqual(result["paintedBoundsDesign"], [0, 0, 32, 32])

    def test_sub_rectangular_keyshapes_include_stroke_at_canvas_edges(self):
        fixtures = (
            ('<rect x="2" y="2" width="28" height="28"/>', "square-32", [0, 0, 32, 32]),
            ('<rect x="4" y="2" width="24" height="28"/>', "portrait-28x32", [2, 0, 30, 32]),
            ('<rect x="2" y="4" width="28" height="24"/>', "landscape-32x28", [0, 2, 32, 30]),
        )
        for body, token, bounds in fixtures:
            with self.subTest(token=token):
                result = self.check(body, token, icon_type="sub")
                self.assertEqual(result["status"], "pass")
                self.assertEqual(result["assignedToken"]["name"], token)
                self.assertEqual(result["paintedBoundsDesign"], bounds)

    def test_sub_inference_disambiguates_equal_sized_circle_and_square(self):
        fixtures = (
            ('<circle cx="16" cy="16" r="14"/>', "circle-32", True),
            ('<rect x="2" y="2" width="28" height="28"/>', "square-32", False),
        )
        for body, token, circle_evidence in fixtures:
            with self.subTest(token=token):
                result = self.check(body, icon_type="sub")
                self.assertEqual(result["status"], "pass")
                self.assertEqual(result["assignedToken"]["name"], token)
                self.assertEqual(result["circleDetection"]["isDominantLargeCircle"], circle_evidence)

    def test_sub_declared_square_is_not_replaced_by_circle_inference(self):
        result = self.check(
            '<circle cx="16" cy="16" r="14"/>', "square-32", icon_type="sub"
        )
        self.assertTrue(result["circleDetection"]["isDominantLargeCircle"])
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["assignedToken"]["name"], "square-32")

    def test_sub_circle_rejects_corner_paint_with_shared_square_bounds(self):
        result = self.check(
            '<rect x="2" y="2" width="28" height="28"/>', "circle-32", icon_type="sub"
        )
        self.assertEqual(result["paintedBoundsDesign"], [0, 0, 32, 32])
        self.assertEqual(result["status"], "fail")
        self.assertEqual(result["reason"], "paint-crosses-circle-keyshape")

    def test_sub_keyshapes_reject_stroke_hidden_by_canvas_clipping(self):
        fixtures = (
            ('<rect x="0" y="0" width="32" height="32"/>', "square-32", [-2, -2, 34, 34]),
            ('<rect x="4" y="0" width="24" height="32"/>', "portrait-28x32", [2, -2, 30, 34]),
            ('<rect x="0" y="4" width="32" height="24"/>', "landscape-32x28", [-2, 2, 34, 30]),
            ('<circle cx="16" cy="16" r="16"/>', "circle-32", [-2, -2, 34, 34]),
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
        ship = self.check('<circle cx="16" cy="16" r="14"/>', "circle-32", icon_type="sub")
        self.assertEqual(design["status"], "pass")
        self.assertEqual(ship["status"], "pass")
        self.assertEqual(design["paintedBoundsDesign"], ship["paintedBoundsDesign"])

    def test_padded_measurement_preserves_viewport_mapping_and_source(self):
        fixtures = (
            (
                'viewBox="0 0 32 32" style="color:#008000;overflow:hidden !important"',
                '<rect x="0" y="0" width="32" height="32"/>',
                "fail",
                [-2, -2, 34, 34],
            ),
            (
                'viewBox="0 0 32 32"',
                '<rect x="6.25%" y="6.25%" width="87.5%" height="87.5%"/>',
                "pass",
                [0, 0, 32, 32],
            ),
            (
                'viewBox="8 8 32 32"',
                '<rect x="10" y="10" width="28" height="28"/>',
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
                        'fill="none" stroke="currentColor" stroke-width="4" '
                        f'stroke-linejoin="round">{body}</svg>'
                    )
                    svg.write_text(source)
                    result = self.module.process(svg, root, 64, 2 / 64, "square-32", "sub")
                    self.assertEqual(result["status"], status)
                    self.assertEqual(result["paintedBoundsDesign"], bounds)
                    self.assertEqual(svg.read_text(), source)

    def test_container_circle_uses_native_64_profile(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            svg = root / "container.svg"
            svg.write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" '
                'fill="none" stroke="currentColor" stroke-width="4">'
                '<circle cx="32" cy="32" r="28"/></svg>'
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
            self.assertEqual((result["designCanvas"], result["shipCanvas"]), (64, 64))

    def test_cli_returns_failure_status_for_keyshape_violation(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            svg = root / "icon.svg"
            svg.write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" '
                'fill="none" stroke="currentColor" stroke-width="4">'
                '<rect x="4" y="4" width="40" height="40"/></svg>'
            )
            (root / "icon.json").write_text(json.dumps({"keyfitCheck": {"targetToken": "circle-44"}}))
            result = subprocess.run(
                [sys.executable, str(self.script), str(svg), "--expected-editable-dir", str(root), "--output-dir", str(root / "qa")],
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)

    def test_raster_keyfit_rejects_reduced_source_or_intrinsic_size(self):
        for icon_type, canvas, radius, token in (("sub", 32, 14, "circle-32"), ("normal", 48, 20, "circle-44"), ("container", 64, 28, "circle-60")):
            for reduced_viewbox in (True, False):
                with self.subTest(icon_type=icon_type, reduced_viewbox=reduced_viewbox), TemporaryDirectory() as folder:
                    root = Path(folder)
                    source = root / "reduced.svg"
                    scale = .5 if reduced_viewbox else 1
                    source.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas // 2}" height="{canvas // 2}" viewBox="0 0 {canvas * scale:g} {canvas * scale:g}" fill="none" stroke="black" stroke-width="{4 * scale:g}"><circle cx="{canvas * scale / 2:g}" cy="{canvas * scale / 2:g}" r="{radius * scale:g}"/></svg>')
                    result = self.module.process(source, root, 4, .5, token, icon_type)
                    self.assertEqual(result["status"], "fail")
                    self.assertEqual(result["reason"], "non-native-svg-size")
                    self.assertTrue(result["nativeSizeIssues"])


@unittest.skipUnless(RASTER_AVAILABLE and find_spec("cv2"), "hole QA dependencies are unavailable")
class NativeHoleQaTests(unittest.TestCase):
    def test_native_hole_metrics_have_one_to_one_units_and_actual_svg_stroke_default(self):
        import qa_overlays as holes
        for icon_type, canvas in (("sub", 32), ("normal", 48), ("container", 64)):
            with self.subTest(icon_type=icon_type), TemporaryDirectory() as folder:
                root = Path(folder)
                source = root / "native.svg"
                source.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas}" height="{canvas}" viewBox="0 0 {canvas} {canvas}" fill="none" stroke="black" stroke-width="4"><circle cx="{canvas // 2}" cy="{canvas // 2}" r="10"/></svg>')
                result = holes.process(source, root, 4, 1, 0, icon_type)
                self.assertEqual(result["status"], "pass")
                self.assertEqual(result["normalizedCanvases"], {"designUnits": canvas, "shipPixels": canvas})
                self.assertEqual(len(result["holes"]), 1)
                metric = result["holes"][0]
                self.assertEqual(metric["bbox_design_u"], metric["bbox_ship_px"])
                for field in ("equivalent_diameter", "inscribed_diameter", "inscribed_radius"):
                    self.assertEqual(metric[f"{field}_design_u"], metric[f"{field}_ship_px"])
                self.assertEqual(holes.authored_stroke_design_u(source, (0, 0, canvas, canvas), canvas), 4)
                source.write_text(source.read_text().replace(' stroke-width="4"', ''))
                self.assertEqual(holes.authored_stroke_design_u(source, (0, 0, canvas, canvas), canvas), 1)

    def test_hole_gate_rejects_reduced_viewport_and_intrinsic_dimensions(self):
        import qa_overlays as holes
        for icon_type, canvas in (("sub", 32), ("normal", 48), ("container", 64)):
            for scale in (.5, 1):
                with self.subTest(icon_type=icon_type, scale=scale), TemporaryDirectory() as folder:
                    root = Path(folder)
                    source = root / "reduced.svg"
                    source.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas // 2}" height="{canvas // 2}" viewBox="0 0 {canvas * scale:g} {canvas * scale:g}" fill="none" stroke="black" stroke-width="{4 * scale:g}"><circle cx="{canvas * scale / 2:g}" cy="{canvas * scale / 2:g}" r="{10 * scale:g}"/></svg>')
                    result = holes.process(source, root, 4, 1, 0, icon_type)
                    self.assertEqual(result["status"], "fail")
                    self.assertTrue(result["nativeSizeIssues"])
                    holes.write_html_report([result], root, 1, 0)
                    report = (root / "hole-radius-report.html").read_text()
                    self.assertIn("must be native", report)
                    self.assertIn("1px at native size", report)


if __name__ == "__main__":
    unittest.main()
