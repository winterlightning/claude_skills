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

    def check(self, body: str, token: str | None = None) -> dict:
        with TemporaryDirectory() as folder:
            root = Path(folder)
            svg = root / "icon.svg"
            svg.write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" '
                'fill="none" stroke="currentColor" stroke-width="2" '
                f'stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
            )
            return self.module.process(svg, root, 64, 2 / 64, token)

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
