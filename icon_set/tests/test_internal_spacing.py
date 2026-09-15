"""Sampled advisories coexist with exact blocking parallel-straight checks."""
import unittest
from tempfile import TemporaryDirectory
from pathlib import Path

from icon_set.model.icons.registry import create
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.validation.internal_spacing import analyze_internal_spacing
from icon_set.validation.library_qa import inspect_icon, save_evidence


class ConnectedChannel(Solo48):
    icon_id = 'connected-channel-fixture'
    keyshape = Keyshape.SQUARE
    inner_x = 36

    def build(self):
        self.add_polyline('outer', (6,42), (6,6), (42,6), (42,42))
        x = self.inner_x
        self.add_line('join', (42,42), (x,42))
        self.add_bezier('return', (x,42), ((x-1,34),(x-1,26),(x,18)))
        self.add_line('inner-top', (x,18), (16,18))
        self.add_line('inner-left', (16,18), (16,42))
        self.add_contour('inner','join','return','inner-top','inner-left')
        self.relate('connect', 'outer', 'inner')


# Retired library drawings, pinned here because the assertions below name their
# element ids and coordinates. Classes outside model/icons are never registered.
class DressFixture(Solo48):
    icon_id = 'dress'
    keyshape = Keyshape.VRECT_L

    def build(self) -> None:
        for name, start, end in (
                ('strap-left-top', (13, 2), (19, 2)), ('strap-left-inner', (19, 2), (19, 8))):
            self.add_line(name, start, end)
        self.add_arc('neckline', (19, 8), (29, 8), radius_x=5, sweep=False)
        for name, start, end in (
                ('strap-right-inner', (29, 8), (29, 2)), ('strap-right-top', (29, 2), (35, 2)),
                ('strap-right-outer', (35, 2), (35, 12)), ('bodice-right-upper', (35, 12), (34, 17)),
                ('bodice-right-lower', (34, 17), (31, 22)), ('skirt-right-upper', (31, 22), (36, 31)),
                ('skirt-right-lower', (36, 31), (40, 44))):
            self.add_line(name, start, end)
        self.add_arc('hem', (40, 44), (8, 44), radius_x=16, radius_y=2)
        for name, start, end in (
                ('skirt-left-lower', (8, 44), (12, 31)), ('skirt-left-upper', (12, 31), (17, 22)),
                ('bodice-left-lower', (17, 22), (14, 17)), ('bodice-left-upper', (14, 17), (13, 12)),
                ('strap-left-outer', (13, 12), (13, 2))):
            self.add_line(name, start, end)
        self.add_contour('outline', 'strap-left-top', 'strap-left-inner', 'neckline', 'strap-right-inner',
                         'strap-right-top', 'strap-right-outer', 'bodice-right-upper', 'bodice-right-lower',
                         'skirt-right-upper', 'skirt-right-lower', 'hem', 'skirt-left-lower', 'skirt-left-upper',
                         'bodice-left-lower', 'bodice-left-upper', 'strap-left-outer', closed=True)
        self.add_line('waist-seam', (17, 22), (31, 22))
        self.relate('connect', 'outline', 'waist-seam')


class WrenchFixture(Solo48):
    icon_id = 'open-end-maintenance-wrench'
    keyshape = Keyshape.SQUARE

    def build(self) -> None:
        self.add_line('jaw-upper-inner', (40, 2), (33, 10))
        self.add_arc('jaw-recess', (33, 10), (38, 18), radius_x=8, sweep=False)
        self.add_line('jaw-lower-inner', (38, 18), (46, 10))
        self.add_line('jaw-lower-tip', (46, 10), (46, 18))
        self.add_arc('head-lower-belly', (46, 18), (36, 24), radius_x=7)
        self.add_arc('head-lower-fillet', (36, 24), (30, 25), radius_x=5, sweep=False)
        self.add_line('shaft-lower', (30, 25), (9, 46))
        self.add_arc('butt', (9, 46), (2, 39), radius_x=7)
        self.add_line('shaft-upper', (2, 39), (25, 16))
        self.add_arc('head-upper-fillet', (25, 16), (26, 11), radius_x=5, sweep=False)
        self.add_arc('head-upper-belly', (26, 11), (33, 2), radius_x=8, radius_y=7)
        self.add_line('jaw-upper-tip', (33, 2), (40, 2))
        self.add_contour('wrench-outline', 'jaw-upper-inner', 'jaw-recess', 'jaw-lower-inner', 'jaw-lower-tip',
                         'head-lower-belly', 'head-lower-fillet', 'shaft-lower', 'butt', 'shaft-upper',
                         'head-upper-fillet', 'head-upper-belly', 'jaw-upper-tip', closed=True)


def cramped_dress():
    from dataclasses import replace
    from icon_set.model.primitives import Point, Arc
    icon = DressFixture()
    points = {(19,2):(17,2),(19,8):(17,8),(29,2):(31,2),(29,8):(31,8)}
    icon.primitives = [replace(p, start=Point(*points.get(p.start.as_tuple(),p.start.as_tuple())),
                              end=Point(*points.get(p.end.as_tuple(),p.end.as_tuple())),
                              **({'radius_x':7,'radius_y':7} if p.element_id=='neckline' else {}))
                       for p in icon.primitives]
    return icon


def cramped_wrench():
    from dataclasses import replace
    from icon_set.model.primitives import Point
    icon = WrenchFixture()
    points = {(40,2):(38,2),(33,10):(30,10)}
    icon.primitives = [replace(p, start=Point(*points.get(p.start.as_tuple(),p.start.as_tuple())),
                              end=Point(*points.get(p.end.as_tuple(),p.end.as_tuple()))) for p in icon.primitives]
    return icon


class InternalSpacingTests(unittest.TestCase):
    def test_real_connection_does_not_exempt_distant_crowding(self):
        icon = ConnectedChannel()
        self.assertTrue(icon.validate_icon().ok)
        row = inspect_icon(icon)
        self.assertEqual(row['status'], 'review')
        self.assertTrue(any(f['ink_gap'] < 4 for f in row['internal_spacing']['findings']))

        class WideChannel(ConnectedChannel):
            inner_x = 34
        row = inspect_icon(WideChannel())
        self.assertEqual(row['status'], 'pass', row['errors'] + row['warnings'])

    def test_unresolved_spacing_cannot_publish_and_remains_visible(self):
        import json
        from unittest.mock import patch
        from icon_set.scripts import build as builder
        from icon_set.scripts.failure_report import collect

        class WideChannel(ConnectedChannel):
            icon_id = 'wide-channel-fixture'
            inner_x = 34

        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            with patch.object(builder, 'icons_in', return_value=[ConnectedChannel(), WideChannel()]):
                self.assertEqual(builder.build_family('solo', root/'dist', root/'png',
                                                       write_png=False, report=False), (1,1))
            manifest = json.loads((root/'dist/solo48/manifest.json').read_text())
            self.assertEqual([r['icon_id'] for r in manifest['icons']], ['wide-channel-fixture'])
            failed_path = root/'dist/failed/solo48/manifest.json'
            failed = json.loads(failed_path.read_text())['icons'][0]
            self.assertEqual(failed['status'], 'review')
            self.assertTrue(failed['spacing_pairs'])
            # An unrelated error must not hide the spacing warning in the gallery.
            failed['errors'] = ['canvas/keyshape bounds: fixture failure']
            failed_path.write_text(json.dumps({'icons':[failed]}))
            report = collect([(failed_path, '')])
            self.assertEqual({i['rule'] for i in report['icons'][0]['issues']}, {'bounds','spacing'})

    def test_chained_curves_cannot_hide_crowding_or_ship_as_pass(self):
        class CurvedChannel(Solo48):
            icon_id = 'curved-channel-fixture'
            keyshape = Keyshape.SQUARE

            def build(self):
                points = ((6,42),(6,6),(42,6),(42,42),
                          (36,42),(36,18),(16,18),(16,42))
                segments = []
                for a, b in zip(points, points[1:]):
                    segments.append((
                        tuple(a[k] + (b[k]-a[k])/3 for k in (0,1)),
                        tuple(a[k] + 2*(b[k]-a[k])/3 for k in (0,1)), b))
                self.add_bezier('channel', points[0], *segments)
                self.add_contour('outline', 'channel')

        icon = CurvedChannel()
        result = analyze_internal_spacing(icon, icon.draw())
        self.assertTrue(result['findings'])
        self.assertTrue(any(f['ink_gap'] < 4 for f in result['findings']))
        row = inspect_icon(icon)
        self.assertNotEqual(row['status'], 'pass')
        self.assertTrue(any('internal-spacing' in w for w in row['warnings']))

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

    def test_advisory_remains_visible_when_exact_parallel_check_blocks(self):
        with TemporaryDirectory() as temporary:
            root=Path(temporary)
            row=inspect_icon(cramped_dress(),debug_dir=root/'solo/dress')
            self.assertEqual(row['status'],'fail')
            self.assertTrue(any('parallel straight edges' in error for error in row['errors']))
            self.assertTrue(row['needs_review'])
            row['_key']='solo/dress'
            save_evidence([row],root,debug=True,report=True)
            self.assertTrue((root/'solo/dress/internal-spacing.png').exists())
            html=(root/'index.html').read_text() + ''.join(p.read_text() for p in (root/'report').glob('*.js'))
            self.assertIn('Connected-edge spacing: review',html)
            self.assertIn('strap-left-inner',html)
            self.assertIn('Review required before release',html)

    def test_wide_contour_clears_both_qa_and_internal_spacing(self):
        from icon_set.model.keyshapes import Keyshape
        icon = create('dress')
        icon.primitives = []
        icon.contours = []
        icon.relationships = []
        icon.keyshape = Keyshape.SQUARE
        icon.add_polyline('u', (6,42), (6,6), (42,6), (42,42))
        row = inspect_icon(icon)
        self.assertEqual(row['status'],'pass',row['errors'])
        self.assertFalse(row['needs_review'])


class AvatarContactTests(unittest.TestCase):
    def test_only_exact_declared_avatar_contact_is_accepted(self):
        from dataclasses import replace
        from icon_set.model.primitives import Point
        icon = create('football-player-avatar')
        self.assertEqual(analyze_internal_spacing(icon, icon.draw())['findings'], [])
        icon.primitives = [replace(p, start=Point(p.start.x, p.start.y + 1),
                                  end=Point(p.end.x, p.end.y + 1))
                           if p.element_id in ('body-top', 'body-top-right') else p
                           for p in icon.primitives]
        self.assertTrue(analyze_internal_spacing(icon, icon.draw())['findings'])

    def test_non_avatar_contact_keeps_normal_review(self):
        icon = create('football-player-avatar')
        icon.category = 'test-other'
        self.assertTrue(analyze_internal_spacing(icon, icon.draw())['findings'])
