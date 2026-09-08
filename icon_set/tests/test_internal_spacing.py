"""Advisory internal clearance must find squeezes without blocking releases."""
import unittest
from tempfile import TemporaryDirectory
from pathlib import Path

from icon_set.model.icons.registry import create
from icon_set.validation.internal_spacing import analyze_internal_spacing
from icon_set.validation.library_qa import inspect_icon, save_evidence


def cramped_dress():
    from dataclasses import replace
    from icon_set.model.primitives import Point, Arc
    icon = create('dress')
    points = {(19,2):(17,2),(19,8):(17,8),(29,2):(31,2),(29,8):(31,8)}
    icon.primitives = [replace(p, start=Point(*points.get(p.start.as_tuple(),p.start.as_tuple())),
                              end=Point(*points.get(p.end.as_tuple(),p.end.as_tuple())),
                              **({'radius_x':7,'radius_y':7} if p.element_id=='neckline' else {}))
                       for p in icon.primitives]
    return icon


def cramped_wrench():
    from dataclasses import replace
    from icon_set.model.primitives import Point
    icon = create('open-end-maintenance-wrench')
    points = {(40,2):(38,2),(33,10):(30,10)}
    icon.primitives = [replace(p, start=Point(*points.get(p.start.as_tuple(),p.start.as_tuple())),
                              end=Point(*points.get(p.end.as_tuple(),p.end.as_tuple()))) for p in icon.primitives]
    return icon


class InternalSpacingTests(unittest.TestCase):
    def test_dress_reports_both_closed_shoulder_gaps(self):
        icon = cramped_dress()
        result = analyze_internal_spacing(icon, icon.draw())
        pairs = {tuple(f['elements']): f for f in result['findings']}
        for side in ('left', 'right'):
            finding = pairs[(f'strap-{side}-inner', f'strap-{side}-outer')]
            self.assertAlmostEqual(finding['ink_gap'], 0)
            self.assertGreaterEqual(finding['sustained_length'], 2)
        self.assertFalse(result['blocking'])

    def test_wrench_reports_opposing_jaw_edges(self):
        icon = cramped_wrench()
        result = analyze_internal_spacing(icon, icon.draw())
        self.assertTrue(any(f['elements'] == ['jaw-upper-inner', 'head-upper-belly'] for f in result['findings']))

    def test_closing_tip_normal_corners_and_circles_do_not_trigger(self):
        for name in ('paper-airplane-message-send', 'square', 'circle'):
            with self.subTest(icon=name):
                icon = create(name)
                self.assertEqual(analyze_internal_spacing(icon, icon.draw())['findings'], [])

    def test_widening_shoulders_removes_the_parallel_edge_findings(self):
        from dataclasses import replace
        from icon_set.model.primitives import Point
        icon = create('dress')
        # Isolate a pair in a fixture contour so unrelated neckline gaps do not
        # influence the assertion. The same shape is tested tight and wide.
        icon.primitives = []
        icon.contours = []
        icon.add_polyline('u', (10,20),(10,2),(18,2),(18,20))
        self.assertEqual(analyze_internal_spacing(icon,icon.draw())['findings'], [])
        icon.primitives = [replace(p, start=Point(14 if p.start.x==18 else p.start.x,p.start.y),
                                   end=Point(14 if p.end.x==18 else p.end.x,p.end.y)) for p in icon.primitives]
        self.assertTrue(analyze_internal_spacing(icon,icon.draw())['findings'])

    def test_advisory_is_visible_without_changing_release_status(self):
        with TemporaryDirectory() as temporary:
            root=Path(temporary)
            row=inspect_icon(cramped_dress(),debug_dir=root/'solo/dress')
            self.assertEqual(row['status'],'pass')
            self.assertTrue(row['needs_review'])
            row['_key']='solo/dress'
            save_evidence([row],root,debug=True,report=True)
            self.assertTrue((root/'solo/dress/internal-spacing.png').exists())
            html=(root/'index.html').read_text()
            self.assertIn('needs review',html)
            self.assertIn('strap-left-inner',html)
            self.assertIn('Advisory only',html)

    def test_repaired_dress_and_wrench_clear_both_qa_and_internal_spacing(self):
        for name in ('dress','open-end-maintenance-wrench'):
            with self.subTest(icon=name):
                row = inspect_icon(create(name))
                self.assertEqual(row['status'],'pass',row['errors'])
                self.assertFalse(row['needs_review'])
