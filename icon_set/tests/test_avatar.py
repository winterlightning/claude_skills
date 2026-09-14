"""Avatar output keeps the reference's detached head and exact requested spacing."""
import unittest
from icon_set.model.icons.registry import create, icons_in
from icon_set.model.icons.avatar._base import HEAD_BODY_INK_GAP, HEAD_BODY_CENTERLINE_GAP
from icon_set.validation.envelope import centerline_bounds, visible_bounds
from icon_set.validation.svg_reader import parse_svg


class AvatarTests(unittest.TestCase):
    def test_reference_avatar_geometry_and_export(self):
        icon = create('user-avatar')
        report = icon.validate_icon()
        self.assertEqual(report.status, 'valid', report.describe())
        head = [p for p in icon.primitives if p.element_id.startswith('head-')]
        body = [p for p in icon.primitives if not p.element_id.startswith('head-')]
        self.assertEqual(centerline_bounds(body)[1] - centerline_bounds(head)[3], HEAD_BODY_CENTERLINE_GAP)
        self.assertEqual(visible_bounds(body)[1] - visible_bounds(head)[3], HEAD_BODY_INK_GAP)
        # The head's bottom is on the flat shoulder span, so this vertical
        # separation is the nearest gap, not merely a bounding-box estimate.
        shoulder = next(p for p in body if p.element_id == 'shoulder-top')
        head_box = centerline_bounds(head)
        self.assertLessEqual(shoulder.start.x, (head_box[0]+head_box[2])/2)
        self.assertGreaterEqual(shoulder.end.x, (head_box[0]+head_box[2])/2)
        svg = parse_svg(icon.to_svg())
        self.assertEqual(svg.view_box, (0,0,48,48))
        self.assertEqual(svg.style['stroke-width'], '4')
        self.assertEqual(len(svg.paths), 2)
        self.assertNotIn('content-top-left', icon.anchors)

    def test_all_avatars_export_at_48_with_exact_head_body_gap(self):
        for icon in icons_in('avatar'):
            with self.subTest(icon=icon.icon_id):
                report = icon.validate_icon()
                self.assertEqual(report.status, 'valid', report.describe())
                self.assertEqual(report.warnings, ())
                self.assertEqual(parse_svg(icon.to_svg()).view_box, (0, 0, 48, 48))
                if icon.icon_id == 'user-avatar':
                    head = [p for p in icon.primitives if p.element_id.startswith('head-')]
                else:
                    head = [p for p in icon.primitives if not p.element_id.startswith('body-')]
                body = [p for p in icon.primitives if p not in head]
                self.assertEqual(visible_bounds(body)[1] - visible_bounds(head)[3], 4)
                # Every lowest head point includes a jaw/circle extremum on x24,
                # directly above the flat shoulder plateau at its minimum y.
                shoulder_id = 'shoulder-top' if icon.icon_id == 'user-avatar' else 'body-top'
                shoulder = next(p for p in body if p.element_id == shoulder_id)
                self.assertLessEqual(shoulder.start.x, 24)
                self.assertGreaterEqual(shoulder.end.x, 24)
