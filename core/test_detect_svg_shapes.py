import unittest
from importlib.util import find_spec
from pathlib import Path
from tempfile import TemporaryDirectory

from detect_svg_shapes import analyze_svg, parse_path, render_detection_plot

MATPLOTLIB_AVAILABLE = find_spec("matplotlib") is not None


class ShapeDetectorTests(unittest.TestCase):
    def test_report_uses_current_centered_keyshapes(self):
        report = analyze_svg('<svg viewBox="0 0 48 48"><circle cx="24" cy="24" r="20"/></svg>')
        self.assertEqual(report["targetSpec"]["grid"], {"minor": 1, "major": 4})
        self.assertEqual(
            [item["name"] for item in report["targetSpec"]["keyshapes"]],
            ["circle-44", "square-40", "portrait-36x44", "landscape-44x36"],
        )

    def test_relative_and_absolute_path_commands(self):
        segments = parse_path("M 1 2 h 4 v 5 l -4 0 z")
        self.assertEqual([segment["type"] for segment in segments], ["M", "L", "L", "L", "Z"])
        self.assertEqual(segments[-1]["to"].as_dict(), {"x": 1.0, "y": 2.0})

    def test_native_primitives_and_spec_warnings(self):
        report = analyze_svg('''<svg viewBox="0 0 48 48">
          <circle cx="12" cy="12" r="6"/><rect x="20" y="4" width="20" height="8" rx="4"/>
          <line x1="4" y1="30" x2="20" y2="30"/><line x1="4" y1="40" x2="20" y2="37"/>
        </svg>''')
        self.assertEqual([item["classification"]["kind"] for item in report["elements"]], ["circle", "pill", "straight-line", "straight-line"])
        self.assertTrue(any("15° grid" in issue["message"] for issue in report["elements"][3]["specIssues"]))

    def test_token_rounded_rectangle_maps_to_the_rounded_rectangle_atom(self):
        report = analyze_svg('<svg viewBox="0 0 48 48"><rect x="8" y="4" width="32" height="40" rx="4"/></svg>')
        classification = report["elements"][0]["classification"]
        self.assertEqual(classification["kind"], "rounded-rectangle")
        self.assertEqual(classification["atomicShape"], "rounded-rectangle")
        self.assertEqual(report["makerPreflight"]["manualReview"], [])

    def test_path_curve_types_and_arc_bounds(self):
        report = analyze_svg('''<svg viewBox="0 0 48 48">
          <path d="M 4 4 L 20 4"/><path d="M 4 20 A 8 8 0 0 1 20 20"/>
          <path d="M 4 30 Q 12 20 20 30"/><path d="M 24 30 C 28 20 32 20 36 30"/>
          <path d="M 32 4 A 6 6 0 1 0 32 16 A 6 6 0 1 0 32 4 Z"/>
        </svg>''')
        self.assertEqual([item["classification"]["kind"] for item in report["elements"]], ["straight-line", "arc", "quadratic-curve", "cubic-curve", "circle"])
        self.assertEqual(report["elements"][4]["normalizedBounds"], {"x": 26, "y": 4, "width": 12, "height": 12})
        self.assertEqual(report["summary"]["errorCount"], 1)

    def test_polygons(self):
        report = analyze_svg('''<svg viewBox="0 0 48 48">
          <polygon points="4,4 12,4 12,12 4,12"/><path d="M 20 4 L 28 12 L 20 20 L 12 12 Z"/>
        </svg>''')
        self.assertEqual(report["elements"][0]["classification"]["kind"], "square")
        self.assertEqual(report["elements"][1]["classification"]["kind"], "diamond")

    def test_gable_pentagons_map_to_the_gable_atom(self):
        report = analyze_svg('''<svg viewBox="0 0 48 48">
          <path d="M 4 44 L 4 12 L 12 4 L 20 12 L 20 44 Z"/>
          <path d="M 44 24 L 12 24 L 4 32 L 12 40 L 44 40 Z"/>
          <path d="M 24 44 L 24 12 L 26 4 L 40 12 L 40 44 Z"/>
        </svg>''')
        kinds = [item["classification"]["kind"] for item in report["elements"]]
        # Upright and side-on gables are the same family; an off-centre apex is not.
        self.assertEqual(kinds, ["gable", "gable", "polygon"])
        self.assertEqual(report["elements"][0]["classification"]["atomicShape"], "gable")
        self.assertIsNone(report["elements"][2]["classification"]["atomicShape"])

    def test_cut_corner_pentagons_map_to_the_cut_corner_box_atom(self):
        report = analyze_svg('''<svg viewBox="0 0 48 48">
          <path d="M 4 14 L 14 4 L 24 4 L 24 24 L 4 24 Z"/>
          <path d="M 44 24 L 44 44 L 24 44 L 24 34 L 34 24 Z"/>
          <path d="M 4 34 L 14 28 L 20 28 L 20 44 L 4 44 Z"/>
        </svg>''')
        kinds = [item["classification"]["kind"] for item in report["elements"]]
        # Any corner is the same family under flips and rotation; a cut that is
        # not 45 degrees is a plain pentagon.
        self.assertEqual(kinds, ["cut-corner-box", "cut-corner-box", "polygon"])
        self.assertEqual(report["elements"][0]["classification"]["atomicShape"], "cut-corner-box")
        self.assertIsNone(report["elements"][2]["classification"]["atomicShape"])

    def test_quadratic_cloud_maps_to_the_cloud_atom(self):
        report = analyze_svg('''<svg viewBox="0 0 48 48">
          <path d="M 4 24 Q 4 16 12 16 Q 14 6 24 6 Q 34 6 36 16 Q 44 16 44 24 Q 44 34 36.8 34 L 11.2 34 Q 4 34 4 24 Z"/>
        </svg>''')
        element = report["elements"][0]
        self.assertEqual(element["classification"]["kind"], "cloud")
        self.assertEqual(element["classification"]["atomicShape"], "cloud")
        self.assertEqual(report["makerPreflight"]["manualReview"], [])

    def test_fifteen_degree_sloped_quadrilateral_maps_to_sloped_box(self):
        report = analyze_svg('''<svg viewBox="0 0 48 48">
          <path d="M 8 16.038 L 38 8 L 38 40 L 8 40 Z"/>
        </svg>''')
        element = report["elements"][0]
        self.assertEqual(element["classification"]["kind"], "sloped-box")
        self.assertEqual(element["classification"]["atomicShape"], "sloped-box")
        self.assertEqual(report["makerPreflight"]["manualReview"], [])

    def test_arch_paths_map_to_the_arch_atom(self):
        report = analyze_svg("""<svg viewBox="0 0 48 48">
          <path d="M 14 42 L 14 16 A 10 10 0 0 1 34 16 L 34 42"/>
          <path d="M 20 42 L 20 26 A 4 4 0 0 1 28 26 L 28 42"/>
          <path d="M 4 44 L 10 30 A 8 8 0 0 1 24 30 L 30 44"/>
        </svg>""")
        kinds = [item["classification"]["kind"] for item in report["elements"]]
        self.assertEqual(kinds, ["arch", "arch", "compound-line-arc"])
        self.assertEqual(report["elements"][0]["classification"]["atomicShape"], "arch")
        self.assertEqual(report["makerPreflight"]["manualReview"], [2])

    def test_open_rectangles_map_to_the_open_rectangle_atom(self):
        report = analyze_svg("""<svg viewBox="0 0 48 48">
          <path d="M 6 44 L 6 28 L 18 28 L 18 44"/>
          <path d="M 44 6 L 28 6 L 28 18 L 44 18"/>
          <path d="M 6 4 L 6 20 L 18 20"/>
          <path d="M 30 44 L 30 28 L 42 28 L 42 36"/>
          <path d="M 6 44 L 6 28 L 12 28 L 18 28 L 18 44"/>
        </svg>""")
        kinds = [item["classification"]["kind"] for item in report["elements"]]
        # Down-opening and side-opening are the same family, and a head broken
        # at a midpoint vertex is still one head; an L-bend and a three-sided
        # figure with unequal jambs are not.
        self.assertEqual(kinds, ["open-rectangle", "open-rectangle", "polyline", "polyline", "open-rectangle"])
        self.assertEqual(report["elements"][0]["classification"]["atomicShape"], "open-rectangle")
        self.assertIsNone(report["elements"][3]["classification"]["atomicShape"])
        self.assertEqual(report["makerPreflight"]["manualReview"], [2, 3])

    def test_open_gables_map_to_the_open_gable_atom(self):
        report = analyze_svg("""<svg viewBox="0 0 48 48">
          <path d="M 12 40 L 12 20 L 24 8 L 36 20 L 36 40"/>
          <path d="M 12 40 L 12 20 L 18 14 L 24 8 L 36 20 L 36 40"/>
          <path d="M 12 40 L 12 20 L 24 8 L 36 20 L 36 30"/>
          <path d="M 12 40 L 12 20 L 30 8 L 36 20 L 36 40"/>
          <path d="M 12 40 L 12 20 L 24 8 L 36 20 L 36 40 Z"/>
        </svg>""")
        kinds = [item["classification"]["kind"] for item in report["elements"]]
        # A roof edge broken at a midpoint vertex is still one edge; unequal
        # walls, an apex off the centre, and the closed outline are not open
        # gables — the last one is the closed `gable` the atom is derived from.
        self.assertEqual(kinds, ["open-gable", "open-gable", "polyline", "polyline", "gable"])
        self.assertEqual(report["elements"][0]["classification"]["atomicShape"], "open-gable")
        self.assertIsNone(report["elements"][2]["classification"]["atomicShape"])
        self.assertEqual(report["makerPreflight"]["manualReview"], [2, 3])

    def test_j_hook_maps_to_the_hook_atom_instead_of_arch(self):
        report = analyze_svg('<svg viewBox="0 0 48 48"><path d="M 12 8 L 12 28 A 4 4 0 0 0 20 28 L 20 24"/></svg>')
        classification = report["elements"][0]["classification"]
        self.assertEqual(classification["kind"], "hook")
        self.assertEqual(classification["atomicShape"], "hook")
        self.assertEqual(report["makerPreflight"]["manualReview"], [])

    def test_water_drop_maps_to_the_water_drop_atom(self):
        report = analyze_svg('<svg viewBox="0 0 48 48"><path d="M 12 4 Q 20 12 20 18 Q 20 24 12 24 Q 4 24 4 18 Q 4 12 12 4 Z"/></svg>')
        classification = report["elements"][0]["classification"]
        self.assertEqual((classification["kind"],classification["atomicShape"]),("water-drop","water-drop"))
        self.assertEqual(report["makerPreflight"]["manualReview"], [])

    def test_tapered_spire_maps_to_the_tapered_spire_atom(self):
        report = analyze_svg('<svg viewBox="0 0 48 48"><path d="M 24 4 Q 8 32 8 44 L 40 44 Q 40 32 24 4 Z"/></svg>')
        classification = report["elements"][0]["classification"]
        self.assertEqual((classification["kind"], classification["atomicShape"]), ("tapered-spire", "tapered-spire"))
        self.assertEqual(report["makerPreflight"]["manualReview"], [])

    def test_open_symmetric_quadratic_globe_maps_to_bulb_outline(self):
        report = analyze_svg('<svg viewBox="0 0 48 48"><path d="M 16 36 Q 16 28 12 24 Q 8 20 8 16 Q 8 4 20 4 Q 32 4 32 16 Q 32 20 28 24 Q 24 28 24 36"/></svg>')
        classification = report["elements"][0]["classification"]
        self.assertEqual((classification["kind"],classification["atomicShape"]),("bulb-outline","bulb-outline"))
        self.assertEqual(report["makerPreflight"]["manualReview"], [])

    def test_faucet_maps_to_the_faucet_atom(self):
        report = analyze_svg('<svg viewBox="0 0 48 48"><path d="M 4 20 L 28 20 A 8 8 0 0 1 36 28 L 36 36 M 15 20 L 15 8 M 10 8 L 20 8"/></svg>')
        classification = report["elements"][0]["classification"]
        self.assertEqual((classification["kind"],classification["atomicShape"]),("faucet","faucet"))
        self.assertEqual(report["makerPreflight"]["manualReview"], [])

    def test_ring_handle_open_jaw_maps_to_open_end_wrench(self):
        report = analyze_svg('<svg viewBox="0 0 48 48"><path d="M 8 8 A 4 4 0 1 1 8 16 A 4 4 0 1 1 8 8 M 12 12 L 28 12 M 28 12 L 32 8 M 28 12 L 32 16"/></svg>')
        classification = report["elements"][0]["classification"]
        self.assertEqual((classification["kind"],classification["atomicShape"]),("open-end-wrench","open-end-wrench"))
        self.assertEqual(report["makerPreflight"]["manualReview"], [])

    def test_broken_box_perimeter_maps_to_dashed_rectangle(self):
        report = analyze_svg('''<svg viewBox="0 0 48 48"><path d="M 8 8 L 12 8 M 16 8 L 20 8 M 20 12 L 20 16 M 20 20 L 20 24 M 20 28 L 16 28 M 12 28 L 8 28 M 8 24 L 8 20 M 8 16 L 8 12"/></svg>''')
        classification = report["elements"][0]["classification"]
        self.assertEqual(classification["kind"], "dashed-rectangle")
        self.assertEqual(classification["atomicShape"], "dashed-rectangle")
        self.assertEqual(report["makerPreflight"]["manualReview"], [])

    def test_closed_twin_gable_maps_to_the_twin_gable_atom(self):
        report = analyze_svg("""<svg viewBox="0 0 48 48">
          <path d="M 4 40 L 4 18 L 14 8 L 24 18 L 34 8 L 44 18 L 44 40 Z"/>
          <path d="M 4 40 L 4 18 L 16 8 L 24 18 L 34 8 L 44 18 L 44 40 Z"/>
        </svg>""")
        kinds = [item["classification"]["kind"] for item in report["elements"]]
        self.assertEqual(kinds, ["twin-gable", "polygon"])
        self.assertEqual(report["elements"][0]["classification"]["atomicShape"], "twin-gable")
        self.assertEqual(report["makerPreflight"]["manualReview"], [1])

    def test_open_arc_sweep_separates_arc_from_quarter_arc(self):
        report = analyze_svg("""<svg viewBox="0 0 48 48">
          <path d="M 4 20 A 8 8 0 0 1 20 20"/>
          <path d="M 4 34 A 8 8 0 0 1 12 42"/>
          <path d="M 44 34 A 8 8 0 0 0 36 42"/>
          <path d="M 4 30 A 12 10 0 0 1 20 40"/>
        </svg>""")
        kinds = [item["classification"]["kind"] for item in report["elements"]]
        self.assertEqual(kinds, ["arc", "quarter-arc", "quarter-arc", "quarter-arc"])
        atoms = [item["shapeId"] for item in report["makerPreflight"]["suggestedAtoms"]]
        self.assertEqual(atoms, ["arc", "quarter-arc", "quarter-arc", "quarter-arc"])
        self.assertEqual(report["makerPreflight"]["manualReview"], [])

    def test_two_arc_cusped_outline_maps_to_the_lens_atom(self):
        report = analyze_svg("""<svg viewBox="0 0 48 48">
          <path d="M 4 24 A 11.333 11.333 0 0 1 24 24 A 11.333 11.333 0 0 1 4 24 Z"/>
          <path d="M 30 18 A 6 6 0 0 1 42 18 A 6 6 0 0 1 30 18 Z"/>
        </svg>""")
        kinds = [item["classification"]["kind"] for item in report["elements"]]
        # The first path is a lens: its two junctions are 20 apart, short of the
        # 22.67 diameter, so the arcs meet at cusps. The second is the same
        # construction with the junctions exactly a diameter apart, which is a
        # circle and must not be reported as a lens.
        self.assertEqual(kinds, ["lens", "circle"])
        self.assertEqual(report["elements"][0]["classification"]["atomicShape"], "lens")
        self.assertEqual(report["makerPreflight"]["suggestedAtoms"][0]["shapeId"], "lens")
        self.assertEqual(report["makerPreflight"]["manualReview"], [])

    def test_two_opposite_quarter_arcs_map_to_s_bend(self):
        report = analyze_svg("""<svg viewBox="0 0 48 48">
          <path d="M 8 8 A 16 16 0 0 1 24 24 A 16 16 0 0 0 40 40"/>
        </svg>""")
        classification = report["elements"][0]["classification"]
        self.assertEqual(classification["kind"], "s-bend")
        self.assertEqual(classification["atomicShape"], "s-bend")
        self.assertEqual(report["makerPreflight"]["suggestedAtoms"][0]["shapeId"], "s-bend")
        self.assertEqual(report["makerPreflight"]["manualReview"], [])

    def test_closed_arc_shape_still_needs_manual_review(self):
        report = analyze_svg('<svg viewBox="0 0 48 48"><path d="M 4 34 A 8 8 0 0 1 12 42 Z"/></svg>')
        self.assertEqual(report["elements"][0]["classification"]["kind"], "closed-arc-shape")
        self.assertIsNone(report["elements"][0]["classification"]["atomicShape"])

    def test_transforms_require_manual_review(self):
        report = analyze_svg('<svg viewBox="0 0 48 48"><g transform="rotate(15 24 24)"><line x1="4" y1="24" x2="20" y2="24"/></g></svg>')
        self.assertEqual(report["makerPreflight"]["manualReview"], [0])
        self.assertFalse(report["summary"]["readyForIconMaker"])

    def test_gapped_rounded_box_maps_to_the_gapped_rounded_rectangle_atom(self):
        report = analyze_svg('<svg viewBox="0 0 48 48"><path d="M 32 8 L 36 8 A 4 4 0 0 1 40 12 '
                             'L 40 40 A 4 4 0 0 1 36 44 L 12 44 A 4 4 0 0 1 8 40 L 8 12 '
                             'A 4 4 0 0 1 12 8 L 16 8"/></svg>')
        classification = report["elements"][0]["classification"]
        self.assertEqual(classification["kind"], "gapped-rounded-rectangle")
        self.assertEqual(classification["atomicShape"], "gapped-rounded-rectangle")
        self.assertEqual(classification["inferredRadius"], 4.0)
        self.assertEqual(report["makerPreflight"]["manualReview"], [])
        self.assertTrue(report["summary"]["readyForIconMaker"])

    def test_off_centre_head_break_is_not_a_gapped_rounded_rectangle(self):
        # Same nine segments, but the head runs are 4u and 12u, so the opening is
        # not centred and the path stays a compound for the agent to resolve.
        report = analyze_svg('<svg viewBox="0 0 48 48"><path d="M 24 8 L 36 8 A 4 4 0 0 1 40 12 '
                             'L 40 40 A 4 4 0 0 1 36 44 L 12 44 A 4 4 0 0 1 8 40 L 8 12 '
                             'A 4 4 0 0 1 12 8 L 16 8"/></svg>')
        self.assertEqual(report["elements"][0]["classification"]["kind"], "compound-line-arc")
        self.assertIsNone(report["elements"][0]["classification"]["atomicShape"])

    @unittest.skipUnless(MATPLOTLIB_AVAILABLE, "Matplotlib is optional and not installed for this interpreter")
    def test_matplotlib_plot_is_written(self):
        svg = '<svg viewBox="0 0 48 48"><circle cx="24" cy="24" r="12"/><path d="M 4 40 Q 24 20 44 40"/></svg>'
        report = analyze_svg(svg, "plot-test.svg")
        with TemporaryDirectory() as directory:
            output = Path(directory) / "preflight.png"
            render_detection_plot(svg, report, output_path=output)
            self.assertTrue(output.exists())
            self.assertGreater(output.stat().st_size, 10_000)


if __name__ == "__main__":
    unittest.main()
