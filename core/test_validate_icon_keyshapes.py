"""Regressions for the mandatory native-canvas and painted-keyshape gate.

These exercise the SVG that would actually ship, not duplicated editable
geometry or a bounds estimate based only on control points.
"""

from importlib.util import find_spec
import json
import os
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import icon_profiles
import validate_icon_keyshapes as gate


RASTER_AVAILABLE = all(find_spec(name) is not None for name in ("cairosvg", "numpy", "PIL"))
SCRIPT = Path(__file__).with_name("validate_icon_keyshapes.py")


def document(token="square-40", icon_type="normal", **extra):
    profile = icon_profiles.get_profile(icon_type)
    return {
        "schemaVersion": 2,
        "iconType": icon_type,
        "canvas": profile["canvas"],
        "strokeWidth": profile["strokeWidth"],
        "keyfitCheck": {"targetToken": token},
        **extra,
    }


def drawing(body='<rect x="6" y="6" width="36" height="36"/>', *, canvas=48, stroke=4):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas}" height="{canvas}" '
        f'viewBox="0 0 {canvas} {canvas}" fill="none" stroke="currentColor" '
        f'stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round">'
        f'{body}</svg>'
    )


@unittest.skipUnless(RASTER_AVAILABLE, "raster keyshape dependencies are unavailable")
class CanvasKeyshapeGateTests(unittest.TestCase):
    def check(self, source=None, metadata=None, **kwargs):
        return gate.check_drawing(
            source if source is not None else drawing(),
            document=document() if metadata is None else metadata,
            **kwargs,
        )

    def assertPass(self, result):
        self.assertTrue(result["ok"], result)
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["errors"], [])
        self.assertIsInstance(result["issues"], list)
        self.assertEqual(result["keyfit"]["status"], "pass")

    def assertFail(self, result):
        self.assertFalse(result["ok"], result)
        self.assertEqual(result["status"], "fail")
        self.assertTrue(result["errors"], result)
        self.assertIsInstance(result["issues"], list)

    def test_exact_painted_square_passes_without_duplicate_editable_geometry(self):
        result = self.check()
        self.assertPass(result)
        self.assertEqual(result["keyfit"]["paintedBoundsDesign"], [4, 4, 44, 44])

    def test_missing_metadata_never_infers_a_passing_keyshape(self):
        self.assertFail(gate.check_drawing(drawing()))

    def test_metadata_requires_v2_explicit_profile_canvas_stroke_and_target(self):
        for missing in ("schemaVersion", "iconType", "canvas", "strokeWidth", "keyfitCheck"):
            metadata = document()
            del metadata[missing]
            with self.subTest(missing=missing):
                self.assertFail(self.check(metadata=metadata))
        for malformed in ({}, {"targetToken": ""}, {"targetToken": "not-a-keyshape"}, {"targetToken": "square-40", "mode": "contain"}):
            with self.subTest(keyfit=malformed):
                self.assertFail(self.check(metadata=document(keyfitCheck=malformed)))
        for version in (1, True, "2"):
            with self.subTest(version=version):
                self.assertFail(self.check(metadata=document(schemaVersion=version)))

    def test_profile_mismatch_cannot_be_overridden_by_cli_hint(self):
        self.assertFail(self.check(icon_type="sub"))
        self.assertFail(self.check(metadata=document(canvas=32)))
        self.assertFail(self.check(metadata=document(strokeWidth=2)))
        self.assertFail(self.check(metadata=document(iconType="unknown")))

    def test_explicit_native_dimensions_are_mandatory(self):
        source = drawing()
        bad = (
            source.replace('width="48"', 'width="24"', 1),
            source.replace('height="48"', 'height="24"', 1),
            source.replace('width="48" ', "", 1),
            source.replace('height="48" ', "", 1),
            source.replace('viewBox="0 0 48 48" ', "", 1),
            source.replace('viewBox="0 0 48 48"', 'viewBox="0 0 24 24"'),
            source.replace('viewBox="0 0 48 48"', 'viewBox="1 0 48 48"'),
            source.replace('viewBox="0 0 48 48"', 'viewBox="0 0 48 32"'),
            source.replace('width="48"', 'width="100%"', 1),
            source.replace('width="48"', 'width="48em"', 1),
        )
        for svg in bad:
            with self.subTest(svg=svg):
                self.assertFail(self.check(svg))

    def test_native_px_units_are_accepted(self):
        svg = drawing().replace('width="48"', 'width="48px"', 1).replace('height="48"', 'height="48px"', 1)
        self.assertPass(self.check(svg))

    def test_all_seven_flat_geometry_tags_are_measured(self):
        bodies = (
            '<circle cx="24" cy="24" r="18"/>',
            '<ellipse cx="24" cy="24" rx="18" ry="18"/>',
            '<rect x="6" y="6" width="36" height="36"/>',
            '<line x1="6" y1="6" x2="42" y2="42"/>',
            '<polygon points="6,6 42,6 42,42"/>',
            '<polyline points="6,6 42,6 42,42"/>',
            '<path d="M6 6H42V42H6Z"/>',
        )
        for body in bodies:
            with self.subTest(body=body):
                self.assertPass(self.check(drawing(body)))

    def test_circle_primitive_and_two_arc_path_have_equivalent_verdicts(self):
        circle = self.check(drawing('<circle cx="24" cy="24" r="20"/>'), document("circle-44"))
        arcs = self.check(drawing('<path d="M44 24A20 20 0 1 0 4 24A20 20 0 1 0 44 24Z"/>'), document("circle-44"))
        self.assertPass(circle)
        self.assertPass(arcs)
        self.assertEqual(circle["keyfit"]["paintedBoundsDesign"], arcs["keyfit"]["paintedBoundsDesign"])

    def test_relative_cubic_quadratic_smooth_and_arc_commands_are_supported(self):
        source = drawing(
            '<rect x="6" y="6" width="36" height="36"/>'
            '<path d="m12 24c0 -6 6 -6 6 0s6 6 6 0q0 -4 4 0t4 0a2 2 0 0 1 2 2"/>'
        )
        self.assertPass(self.check(source))

    def test_normal_rectangle_uses_current_json_dimensions(self):
        self.assertPass(self.check(drawing('<rect x="4" y="8" width="40" height="32"/>'), document("landscape-44x36")))
        self.assertPass(self.check(drawing('<rect x="8" y="4" width="32" height="40"/>'), document("portrait-36x44")))

    def test_sub_circle_accepts_correct_stroke_inset_but_rejects_clipped_paint(self):
        metadata = document("circle-32", "sub")
        self.assertPass(self.check(drawing('<circle cx="16" cy="16" r="14"/>', canvas=32), metadata))
        result = self.check(drawing('<circle cx="16" cy="16" r="16"/>', canvas=32), metadata)
        self.assertFail(result)
        self.assertEqual(result["keyfit"]["paintedBoundsDesign"], [-2, -2, 34, 34])

    def test_tiny_centered_shape_is_not_an_exact_keyshape_fit(self):
        self.assertFail(self.check(drawing('<rect x="20" y="20" width="8" height="8"/>')))

    def test_centerline_fit_does_not_excuse_stroke_overflow(self):
        self.assertFail(self.check(drawing('<rect x="4" y="4" width="40" height="40"/>')))

    def test_circle_target_checks_radial_paint_not_just_bounding_box(self):
        result = self.check(drawing('<rect x="4" y="4" width="40" height="40"/>'), document("circle-44"))
        self.assertFail(result)
        self.assertEqual(result["keyfit"]["reason"], "paint-crosses-circle-keyshape")

    def test_smooth_quadratic_reflected_control_overflow_is_not_missed(self):
        # The T segment reflects the Q control and reaches y=64. Its endpoint
        # remains at y=24; endpoint-only and broken T estimates used to pass.
        result = self.check(drawing('<path d="M8 24Q16 -56 24 24T40 24"/>'))
        self.assertFail(result)

    def test_quadratic_controls_outside_canvas_do_not_imply_paint_overflow(self):
        # Quadratic extrema are at y=6 and 42, not at their -12/60 controls.
        result = self.check(drawing('<path d="M6 24Q24 -12 42 24Q24 60 6 24Z"/>'))
        self.assertPass(result)
        self.assertEqual(result["keyfit"]["paintedBoundsDesign"], [4, 4, 44, 44])

    def test_svg_stroke_and_paint_must_match_profile(self):
        source = drawing()
        replacements = (
            ('stroke-width="4"', 'stroke-width="2"'),
            ('stroke-width="4"', 'stroke-width="0"'),
            ('stroke-width="4"', 'stroke-width="nan"'),
            ('fill="none"', 'fill="black"'),
            ('stroke="currentColor"', 'stroke="black"'),
            ('stroke-linecap="round"', 'stroke-linecap="butt"'),
            ('stroke-linejoin="round"', 'stroke-linejoin="miter"'),
        )
        for before, after in replacements:
            with self.subTest(after=after):
                self.assertFail(self.check(source.replace(before, after)))
        self.assertFail(self.check(source.replace('<rect ', '<rect stroke-width="2" ', 1)))

    def test_unsupported_hidden_or_transformed_svg_is_rejected(self):
        bodies = (
            '<g><rect x="6" y="6" width="36" height="36"/></g>',
            '<g stroke-width="2"><rect x="6" y="6" width="36" height="36"/></g>',
            '<rect x="6" y="6" width="36" height="36" transform="translate(0 0)"/>',
            '<rect x="6" y="6" width="36" height="36" style="stroke-width:4"/>',
            '<rect x="6" y="6" width="36" height="36" display="none"/>',
            '<rect x="6" y="6" width="36" height="36" opacity="0"/>',
            '<defs><path id="shape" d="M6 6H42V42H6Z"/></defs><use href="#shape"/>',
            '<image href="https://example.invalid/icon.svg" width="48" height="48"/>',
            '<script>alert(1)</script><rect x="6" y="6" width="36" height="36"/>',
            '<rect x="6" y="6" width="36" height="36"/><foreignObject/>',
        )
        for body in bodies:
            with self.subTest(body=body):
                self.assertFail(self.check(drawing(body)))

    def test_malformed_geometry_cannot_be_partially_parsed_and_pass(self):
        bodies = (
            '<path d="M6 6H42V42H6Z garbage"/>',
            '<path d="M6 6H42V42H6Z M"/>',
            '<path d="M6 6H42V42H6Z R8 8"/>',
            '<path d="M6 6H42V42H6Z A2 2 0 2 1 6 6"/>',
            '<path d="M6 6H42V42H6Z Mnan 8"/>',
            '<rect x="6" y="6" width="36" height="36"/><path/>',
            '<rect x="6" y="6" width="36" height="36"/><path d="M1 1L2"/>',
        )
        for body in bodies:
            with self.subTest(body=body):
                self.assertFail(self.check(drawing(body)))
        self.assertFail(self.check(drawing()[:-6]))
        self.assertFail(self.check(drawing("")))
        self.assertFail(self.check('<!DOCTYPE svg [<!ENTITY shape "M6 6H42V42H6Z">]>' + drawing('<path d="&shape;"/>')))

    def test_optical_fit_requires_reasoned_fresh_painted_bounds(self):
        source = drawing('<rect x="16" y="6" width="16" height="36"/>')
        keyfit = {"targetToken": "square-40", "mode": "optical", "rationale": "Keep the intentionally narrow upright silhouette.", "paintedBounds": [14, 4, 34, 44]}
        self.assertPass(self.check(source, document(keyfitCheck=keyfit)))
        for change in ({"rationale": ""}, {"paintedBounds": [12, 4, 36, 44]}, {"paintedBounds": [0, 0, 48, 48]}):
            with self.subTest(change=change):
                self.assertFail(self.check(source, document(keyfitCheck={**keyfit, **change})))
        no_bounds = dict(keyfit)
        del no_bounds["paintedBounds"]
        self.assertFail(self.check(source, document(keyfitCheck=no_bounds)))

    def test_container_profile_requires_valid_slot_and_protects_it(self):
        source = drawing('<rect x="6" y="6" width="52" height="52"/>', canvas=64)
        metadata = document("square-56", "container")
        self.assertFail(self.check(source, metadata))
        metadata["containerSlot"] = {"x": 16, "y": 16, "w": 32, "h": 32, "acceptedKeyshape": "square-32"}
        self.assertPass(self.check(source, metadata))
        colliding = source.replace('</svg>', '<line x1="20" y1="32" x2="44" y2="32"/></svg>')
        self.assertFail(self.check(colliding, metadata))
        metadata["containerSlot"]["x"] = 15
        self.assertFail(self.check(source, metadata))

    def test_custom_profile_uses_resolved_json_dimensions_stroke_and_token(self):
        source = icon_profiles.source_document()
        source["profiles"]["badge"] = {
            "label": "Badge", "canvas": 40, "strokeWidth": 2,
            "keyshapes": [{"name": "badge-square", "orientation": "square", "shape": "rect", "width": 32, "height": 32}],
        }
        profiles = icon_profiles.resolve_profiles(source)
        with patch.object(icon_profiles, "_PROFILES", profiles):
            metadata = document("badge-square", "badge")
            self.assertPass(self.check(drawing('<rect x="5" y="5" width="30" height="30"/>', canvas=40, stroke=2), metadata))
            self.assertFail(self.check(drawing('<rect x="5" y="5" width="30" height="30"/>', canvas=40, stroke=4), metadata))
            slightly_inset = drawing('<rect x="5.125" y="5.125" width="29.75" height="29.75"/>', canvas=40, stroke=2)
            profiles["badge"]["validation"]["keyshapeTolerance"] = .2
            self.assertPass(self.check(slightly_inset, metadata))
            profiles["badge"]["validation"]["keyshapeTolerance"] = .01
            self.assertFail(self.check(slightly_inset, metadata))

    def test_check_file_preserves_source_and_metadata_and_uses_actual_svg(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            svg = root / "square.svg"
            editable = root / "square.json"
            svg.write_text(drawing())
            metadata = document(elements=[{"not": "trusted as SVG geometry"}])
            editable.write_text(json.dumps(metadata))
            before = {path.name: path.read_bytes() for path in root.iterdir()}
            self.assertPass(gate.check_file(svg, editable=editable))
            self.assertPass(gate.check_file(svg, editable=metadata))
            self.assertEqual(before, {path.name: path.read_bytes() for path in root.iterdir()})
            svg.write_text(drawing('<rect x="20" y="20" width="8" height="8"/>'))
            self.assertFail(gate.check_file(svg, editable=editable))

    def test_check_file_read_errors_are_failed_results(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            missing = root / "missing.svg"
            self.assertFail(gate.check_file(missing, editable=document()))
            svg = root / "square.svg"
            svg.write_text(drawing())
            self.assertFail(gate.check_file(svg))
            self.assertFail(gate.check_file(svg, editable=root / "missing.json"))
            malformed = root / "square.json"
            malformed.write_text("not JSON")
            self.assertFail(gate.check_file(svg, editable=malformed))
            svg.write_bytes(b"\xff\xfe\x00")
            self.assertFail(gate.check_file(svg, editable=document()))

    def test_missing_raster_dependency_cannot_grant_a_pass(self):
        with patch.dict(sys.modules, {"check_keyfit": None}):
            result = self.check()
        self.assertFail(result)
        self.assertIsNone(result["keyfit"])

    def test_rerun_uses_fresh_evidence_not_an_old_passing_report(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / "square.svg"
            output = root / "qa"
            source.write_text(drawing())
            first = gate.check_file(source, editable=document(), output_dir=output)
            self.assertPass(first)
            old_report = Path(first["keyfitReport"])
            old_data = old_report.read_bytes()
            source.write_text(drawing('<rect x="20" y="20" width="8" height="8"/>'))
            second = gate.check_file(source, editable=document(), output_dir=output)
            self.assertFail(second)
            self.assertNotEqual(first["evidenceDirectory"], second["evidenceDirectory"])
            self.assertNotEqual(first["keyfitReport"], second["keyfitReport"])
            self.assertEqual(old_report.read_bytes(), old_data)
            self.assertEqual(json.loads(Path(second["keyfitReport"]).read_text())["status"], "fail")


@unittest.skipUnless(RASTER_AVAILABLE, "raster keyshape dependencies are unavailable")
class CanvasKeyshapeCliTests(unittest.TestCase):
    def run_gate(self, *args):
        return subprocess.run([sys.executable, "-B", str(SCRIPT), *map(str, args)], text=True, capture_output=True)

    def fixture(self, root, name="square"):
        source = root / f"{name}.svg"
        metadata = root / f"{name}.json"
        source.write_text(drawing())
        metadata.write_text(json.dumps(document()))
        return source, metadata

    def test_single_file_explicit_metadata_writes_machine_readable_summary(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            svg, metadata = self.fixture(root)
            output = root / "qa"
            result = self.run_gate(svg, "--editable", metadata, "--output-dir", output, "--json")
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            json.loads(result.stdout)
            summary = json.loads((output / "canvas-keyshape-results.json").read_text())
            self.assertEqual((summary["checked"], summary["failed"], summary["ok"]), (1, 0, True))
            self.assertEqual(len(summary["rows"]), 1)

    def test_folder_checks_canonical_and_design_alias_with_same_metadata(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            svg_dir = root / "output"
            svg_dir.mkdir()
            metadata_dir = root / "editable"
            metadata_dir.mkdir()
            (svg_dir / "square.svg").write_text(drawing())
            (svg_dir / "square-design.svg").write_text(drawing())
            (metadata_dir / "square.json").write_text(json.dumps(document()))
            output = root / "qa"
            result = self.run_gate(svg_dir, "--expected-editable-dir", metadata_dir, "--output-dir", output, "--quiet")
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(result.stdout, "")
            summary = json.loads((output / "canvas-keyshape-results.json").read_text())
            self.assertEqual((summary["checked"], summary["failed"]), (2, 0))

    def test_missing_metadata_empty_folder_and_missing_path_fail(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            svg, metadata = self.fixture(root)
            empty = root / "empty"
            empty.mkdir()
            missing = root / "missing.svg"
            for args in ((svg,), (empty, "--expected-editable-dir", root), (missing, "--editable", metadata)):
                with self.subTest(args=args):
                    result = self.run_gate(*args)
                    self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                    self.assertNotIn("Traceback", result.stderr)

    def test_mixed_valid_and_missing_inputs_do_not_silently_skip_failure(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            svg, _ = self.fixture(root)
            output = root / "qa"
            result = self.run_gate(svg, root / "missing.svg", "--expected-editable-dir", root, "--output-dir", output)
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            summary = json.loads((output / "canvas-keyshape-results.json").read_text())
            self.assertFalse(summary["ok"])
            self.assertGreaterEqual(summary["failed"], 1)
            self.assertGreaterEqual(summary["checked"], 2)

    def test_numeric_violation_is_nonzero_even_in_quiet_mode(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            svg, metadata = self.fixture(root)
            svg.write_text(drawing().replace('width="48"', 'width="24"', 1))
            result = self.run_gate(svg, "--editable", metadata, "--quiet")
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertEqual(result.stdout, "")

    def test_report_cannot_overwrite_editable_even_with_tilde_path(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / "square.svg"
            source.write_text(drawing())
            editable = root / "canvas-keyshape-results.json"
            original = json.dumps(document()).encode()
            editable.write_bytes(original)
            tilde_path = "~/" + os.path.relpath(editable, Path.home())
            for metadata_path in (editable, tilde_path):
                with self.subTest(metadata_path=metadata_path):
                    result = self.run_gate(source, "--editable", metadata_path, "--output-dir", root)
                    self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                    self.assertEqual(editable.read_bytes(), original)

    def test_cli_misuse_has_exit_status_two(self):
        self.assertEqual(self.run_gate().returncode, 2)
        with TemporaryDirectory() as folder:
            root = Path(folder)
            svg, metadata = self.fixture(root)
            other, _ = self.fixture(root, "other")
            cases = (
                (svg, "--editable", metadata, "--expected-editable-dir", root),
                (svg, other, "--editable", metadata),
            )
            for args in cases:
                with self.subTest(args=args):
                    result = self.run_gate(*args)
                    self.assertEqual(result.returncode, 2, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
