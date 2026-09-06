#!/usr/bin/env python3
"""Pure SVG-ingest and review-required profile adaptation regression tests."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from icon_geometry import parse_path, primitive_commands, resolve_icon
from icon_profiles import get_profile
from profile_adaptation import adapt_geometry, read_design_svg


class ProfileAdaptationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.path = Path(self.temporary.name) / "input-design.svg"
        self.normal, self.sub = get_profile("normal"), get_profile("sub")

    def read(self, children='<path d="M 4 24 L 44 24"/>', *, attributes="", prefix="", suffix=""):
        self.path.write_text(prefix + '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" '
            'fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" '
            + attributes + ">" + children + "</svg>" + suffix, encoding="utf-8")
        return read_design_svg(self.path)

    def source(self, *paths):
        return {"canvas": 48, "strokeWidth": 4, "elements": [
            {"id": f"shape-{index}", "tag": "path", "attrs": {"d": path}}
            for index, path in enumerate(paths)]}

    def token(self, profile, orientation):
        return next(token for token in profile["keyshapes"] if token["orientation"] == orientation)

    def adapt(self, source, orientation="square", target=None):
        target = target or self.sub
        return adapt_geometry(source, self.normal, target,
            self.token(self.normal, orientation), self.token(target, orientation))

    def commands(self, result, index=0):
        return parse_path(result["elements"][index]["attrs"]["d"])

    def test_reads_all_seven_geometry_tags_without_silent_geometry_loss(self):
        primitives = [
            ("path", {"d": "M 4 4 H 12 V 12 Z"}),
            ("line", {"x1": "4", "y1": "20", "x2": "12", "y2": "20"}),
            ("circle", {"cx": "24", "cy": "24", "r": "8"}),
            ("ellipse", {"cx": "24", "cy": "12", "rx": "8", "ry": "4"}),
            ("rect", {"x": "4", "y": "4", "width": "40", "height": "40", "rx": "4"}),
            ("polyline", {"points": "4,4 24,24 44,4"}),
            ("polygon", {"points": "4,44 24,4 44,44"}),
        ]
        children = "".join(f'<{tag} id="{tag}" ' + " ".join(f'{key}="{value}"' for key, value in attrs.items()) + "/>"
                           for tag, attrs in primitives)
        source = self.read(children, attributes='width="48px" height="48"')
        self.assertEqual((source["canvas"], source["strokeWidth"]), (48, 4))
        self.assertEqual(len(source["elements"]), 7)
        for element, (tag, attrs) in zip(source["elements"], primitives):
            self.assertEqual(set(element), {"id", "tag", "attrs"})
            self.assertEqual(element["tag"], "path")
            self.assertEqual(self.commands({"elements": [element]}), primitive_commands(tag, attrs))

    def test_relative_shorthand_and_arc_precision_are_preserved(self):
        geometry = "m 8 8 h 4 v 4 q 2 4 4 0 t 4 0 c 1 2 3 4 4 2 s 3 -2 4 0 a 3 4 12.123456789 0 1 4 4 z"
        source = self.read(f'<path d="{geometry}"/>')
        self.assertEqual(self.commands(source), parse_path(geometry))
        self.assertIn("12.123456789", source["elements"][0]["attrs"]["d"])

    def test_matching_child_paint_is_checked_then_removed(self):
        source = self.read('<line x1="4" y1="24" x2="44" y2="24" fill="none" stroke="currentColor" '
                           'stroke-width="4.0" stroke-linecap="round" stroke-linejoin="round"/>')
        self.assertEqual(set(source["elements"][0]["attrs"]), {"d"})
        self.assertNotIn("stroke", source["elements"][0]["attrs"]["d"])

    def test_missing_dimensions_and_xml_declaration_are_supported(self):
        source = self.read(prefix='<?xml version="1.0" encoding="UTF-8"?>\n')
        self.assertEqual(source["canvas"], 48)
        self.assertEqual(source["elements"][0]["id"], "element-001")

    def test_explicit_ids_survive_and_generated_ids_do_not_collide(self):
        source = self.read('<path d="M4 4L8 8"/><path id="element-001" d="M12 12L16 16"/>')
        self.assertEqual([element["id"] for element in source["elements"]], ["element-001-auto", "element-001"])
        self.assertEqual(read_design_svg(self.path), source)

    def test_rejects_unsafe_root_attributes_and_intrinsic_size_mismatch(self):
        for attributes in ('transform="scale(2)"', 'style="width:24px"', 'onload="alert(1)"',
                           'width="24"', 'height="100%"', 'class="icon"', 'opacity=".5"'):
            with self.subTest(attributes=attributes), self.assertRaises(ValueError):
                self.read(attributes=attributes)

    def test_rejects_paint_changes_and_mixed_strokes(self):
        for attribute in ('fill="black"', 'stroke="red"', 'stroke="url(#paint)"', 'stroke-width="2"',
                          'stroke-linecap="butt"', 'stroke-linejoin="bevel"', 'stroke-width="4px"'):
            with self.subTest(attribute=attribute), self.assertRaises(ValueError):
                self.read(f'<path d="M4 4L44 44" {attribute}/>')
        self.read()
        self.path.write_text(self.path.read_text().replace('fill="none"', 'fill="black"'))
        with self.assertRaisesRegex(ValueError, "fill"):
            read_design_svg(self.path)

    def test_rejects_unknown_nodes_attributes_text_and_namespaces(self):
        children = ('<g><path d="M4 4L44 44"/></g>', '<script>alert(1)</script>', '<style>path{fill:red}</style>',
                    '<use href="#x"/>', '<image href="https://example.invalid/image"/>', '<title>Title</title>',
                    '<path d="M4 4L44 44" transform="translate(1)"/>', '<path d="M4 4L44 44" data-id="x"/>',
                    '<path d="M4 4L44 44"><animate/></path>', '<path d="M4 4L44 44"/>text',
                    'text<path d="M4 4L44 44"/>', '<x:path xmlns:x="urn:other" d="M4 4L44 44"/>',
                    '<path xmlns:xlink="http://www.w3.org/1999/xlink" d="M4 4L44 44"/>')
        for child in children:
            with self.subTest(child=child), self.assertRaises(ValueError):
                self.read(child)

    def test_rejects_comments_processing_instructions_dtd_and_entities(self):
        for prefix in ('<!--comment-->', '<?xml-stylesheet href="remote.css"?>',
                       '<!DOCTYPE svg [<!ENTITY x "x">]>'):
            with self.subTest(prefix=prefix), self.assertRaises(ValueError):
                self.read(prefix=prefix)
        with self.assertRaises(ValueError):
            self.read('<path d="M4 4L44 44"/><!--comment-->')
        with self.assertRaises(ValueError):
            self.read(suffix='<!--comment-->')

    def test_rejects_invalid_or_duplicate_ids_and_invalid_geometry(self):
        children = ('<path id="x" d="M4 4L8 8"/><path id="x" d="M12 12L16 16"/>',
                    '<path id="1bad" d="M4 4L8 8"/>', '<path d="M4 4LNaN 8"/>', '<path d="M4 4L1e999 8"/>',
                    '<path d="M4 4A4 4 0 2 0 8 8"/>', '<path d="M4 4L8"/>', '<path d="M4 4R8 8"/>',
                    '<circle cx="24" cy="24" r="-4"/>', '<path d="M4 4"/>', '')
        for child in children:
            with self.subTest(child=child), self.assertRaises(ValueError):
                self.read(child)

    def test_rejects_non_square_offset_or_nonfinite_canvas_and_malformed_xml(self):
        self.read()
        valid = self.path.read_text()
        for viewbox in ("0 0 48 32", "1 0 48 48", "0 0 0 0", "0 0 NaN NaN", "0,,0,48,48", "0 0 48"):
            self.path.write_text(valid.replace("0 0 48 48", viewbox))
            with self.subTest(viewbox=viewbox), self.assertRaises(ValueError):
                read_design_svg(self.path)
        self.path.write_text("<svg>")
        with self.assertRaisesRegex(ValueError, "XML"):
            read_design_svg(self.path)
        self.path.write_bytes(b"\xff")
        with self.assertRaisesRegex(ValueError, "UTF-8"):
            read_design_svg(self.path)

    def test_rejects_unbounded_or_numerically_unstable_sampling_input(self):
        for path in ("M0 0L10000000 0", "M4 4A1e-200 4 0 0 1 8 8", "M4 4A.00001 4 0 0 1 44 44"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                self.read(f'<path d="{path}"/>')

    def test_square_fit_compensates_stroke_and_preserves_source(self):
        source = self.source("M6 6H42V42H6Z")
        before = deepcopy(source)
        result = self.adapt(source)
        self.assertEqual(source, before)
        self.assertAlmostEqual(result["metrics"]["uniformScale"], 28 / 36)
        self.assertEqual(result["metrics"]["targetStrokeWidth"], 4)
        self.assertEqual(result["metrics"]["adaptedPaintedBounds"], [0, 0, 32, 32])
        self.assertTrue(result["metrics"]["requiresReview"])
        self.assertNotIn("status", result)
        self.assertEqual(result, self.adapt(source))
        json.dumps(result, allow_nan=False)

    def test_rectangular_token_uses_uniform_limiting_dimension(self):
        result = self.adapt(self.source("M4 8L44 40"), "landscape")
        self.assertAlmostEqual(result["metrics"]["uniformScale"], .7)
        self.assertEqual(result["metrics"]["uniformPaintedBounds"], [0, 2.8000000000000007, 32, 29.2])
        self.assertEqual(result["metrics"]["adaptedPaintedBounds"], [0, 3, 32, 29])

    def test_half_grid_ties_are_symmetric_around_target_center(self):
        result = self.adapt(self.source("M23.5 24L24.5 24", "M24 23.5L24 24.5"), target=self.normal)
        first, second = self.commands(result), self.commands(result, 1)
        self.assertEqual([command.points[0] for command in first], [(23, 24), (25, 24)])
        self.assertEqual([command.points[0] for command in second], [(24, 23), (24, 25)])

    def test_shared_coordinates_axis_lines_subpaths_and_dots_are_preserved(self):
        result = self.adapt(self.source("M10 24L10 24 M24 24L24 24 M38 24L38 24", "M24 4V44"), "landscape")
        commands = self.commands(result)
        self.assertEqual([command.type for command in commands], ["M", "L", "M", "L", "M", "L"])
        self.assertEqual(result["metrics"]["preservedDotCount"], 3)
        self.assertEqual(result["metrics"]["collapsedSegments"], [])
        xs = [commands[index].points[0][0] for index in (0, 2, 4)]
        self.assertEqual(xs[0] + xs[2], 32)
        self.assertEqual(xs[1], 16)
        self.assertTrue(all(point[0] == 16 for command in self.commands(result, 1) for point in command.points))

    def test_full_circle_is_reconstructed_without_lens_deformation(self):
        result = self.adapt(self.source("M24 4A20 20 0 1 1 24 44A20 20 0 1 1 24 4Z"), "circle")
        self.assertEqual(result["metrics"]["reconstructedEllipseCount"], 1)
        self.assertEqual(result["metrics"]["adaptedPaintedBounds"], [0, 0, 32, 32])
        arcs = [command for command in self.commands(result) if command.type == "A"]
        self.assertEqual([command.arc for command in arcs], [(14, 14, 0, 1, 1)] * 2)
        self.assertEqual(result["metrics"]["implicitArcExpansions"], [])

    def test_off_center_full_circle_keeps_circle_and_shared_axis(self):
        result = self.adapt(self.source("M24 4A8 8 0 1 1 24 20A8 8 0 1 1 24 4Z", "M24 20L24 44"), "portrait")
        self.assertEqual(result["metrics"]["reconstructedEllipseCount"], 1)
        commands = self.commands(result)
        radius = commands[1].arc[0]
        self.assertEqual(abs(commands[0].points[0][1] - commands[1].points[0][1]), 2 * radius)
        self.assertEqual(commands[1].points[0], self.commands(result, 1)[0].points[0])
        self.assertEqual(result["metrics"]["implicitArcExpansions"], [])

    def test_full_ellipse_preserves_coherent_radii(self):
        result = self.adapt(self.source("M8 9A16 5 0 1 1 40 9A16 5 0 1 1 8 9Z"), "portrait")
        self.assertEqual(result["metrics"]["reconstructedEllipseCount"], 1)
        commands = self.commands(result)
        radius = commands[1].arc[0]
        self.assertEqual(abs(commands[0].points[0][0] - commands[1].points[0][0]), 2 * radius)
        self.assertEqual(commands[1].arc[:2], commands[2].arc[:2])

    def test_arc_flags_rotation_and_zero_radius_line_semantics_survive(self):
        result = self.adapt(self.source("M8 12A8 10 12.123456789 1 0 32 28A0 4 30 0 1 40 36"))
        arcs = [command.arc for command in self.commands(result) if command.type == "A"]
        self.assertEqual(arcs[0][2:], (12.123456789, 1, 0))
        self.assertEqual(arcs[1][0], 0)
        self.assertEqual(arcs[1][2:], (30, 0, 1))
        self.assertTrue(result["metrics"]["radiusAdjustments"])

    def test_fractional_anchors_curves_and_implicit_arc_expansion_are_flagged(self):
        result = self.adapt(self.source("M4.2 24A4 4 0 0 1 20.2 24Q24.1 8 28 24C32 40 38 8 44 24"))
        self.assertGreater(result["metrics"]["fractionalSourceCoordinateCount"], 0)
        self.assertEqual({item["type"] for item in result["metrics"]["curveDeformations"]}, {"A", "Q", "C"})
        self.assertTrue(result["metrics"]["implicitArcExpansions"])
        self.assertTrue(any("tangency" in warning for warning in result["warnings"]))

    def test_newly_collapsed_lines_and_curves_are_not_silently_repaired(self):
        result = self.adapt(self.source("M8 8L8.1 8.1", "M8 8Q8.1 8.1 8.2 8.2", "M8 8C8.1 8.1 8.2 8.2 8.3 8.3"))
        self.assertEqual({item["type"] for item in result["metrics"]["collapsedSegments"]}, {"L", "Q", "C"})
        self.assertTrue(result["metrics"]["coordinateMerges"])
        self.assertEqual(result["metrics"]["preservedDotCount"], 0)
        self.assertTrue(any("no semantic repair" in warning for warning in result["warnings"]))

    def test_painted_overflow_is_reported_not_hidden(self):
        result = self.adapt(self.source("M0 0L48 48"))
        self.assertGreater(max(result["metrics"]["paintedOverflow"]), 0)
        self.assertTrue(any("exceed" in warning for warning in result["warnings"]))

    def test_custom_grid_and_profile_stroke_are_honored(self):
        custom = {"canvas": 40, "strokeWidth": 3, "validation": {"gridStep": .5}}
        result = adapt_geometry(self.source("M6 6L42 42"), self.normal, custom,
            self.token(self.normal, "square"), {"name": "box", "width": 39, "height": 39})
        self.assertEqual(result["metrics"]["targetStrokeWidth"], 3)
        self.assertEqual(result["metrics"]["gridStep"], .5)
        self.assertEqual(result["metrics"]["uniformScale"], 1)
        self.assertEqual(result["metrics"]["adaptedPaintedBounds"], [.5, .5, 39.5, 39.5])

    def test_invalid_profiles_tokens_and_mismatched_source_are_rejected(self):
        source = self.source("M4 4L44 44")
        bad_sources = ({**source, "canvas": 24}, {**source, "strokeWidth": 2})
        for candidate in bad_sources:
            with self.assertRaisesRegex(ValueError, "source profile"):
                self.adapt(candidate)
        for custom in ({"canvas": 31, "strokeWidth": 4, "validation": {"gridStep": 1}},
                       {"canvas": 32, "strokeWidth": 32},
                       {"canvas": 32, "strokeWidth": 4, "validation": {"gridStep": 1e-320}}):
            with self.subTest(custom=custom), self.assertRaises(ValueError):
                adapt_geometry(source, self.normal, custom, self.token(self.normal, "square"), {"width": 28, "height": 28})
        for token in ({"width": 4, "height": 32}, {"width": 33, "height": 32}, {"width": "NaN", "height": 32}):
            with self.subTest(token=token), self.assertRaises(ValueError):
                adapt_geometry(source, self.normal, self.sub, self.token(self.normal, "square"), token)

    def test_source_file_bytes_and_element_roles_are_unchanged(self):
        source = self.read()
        original = self.path.read_bytes()
        source["elements"][0]["role"] = "single-divider"
        result = self.adapt(source, "landscape")
        self.assertEqual(self.path.read_bytes(), original)
        self.assertEqual(result["elements"][0]["role"], "single-divider")
        self.assertEqual(len(resolve_icon({"schemaVersion": 2, "elements": result["elements"]})), 1)


if __name__ == "__main__":
    unittest.main()
