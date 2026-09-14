"""SOLO48 parallel straight clearance is blocking, including inside one path."""
import unittest

from icon_set.model.icons.base import Icon
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.validation.parallel_straight import check_parallel_straight
from icon_set.validation.library_qa import inspect_icon


def fixture(gap):
    icon = Icon("parallel-test", Profile.SOLO48, semantic_role="MAIN", keyshape=Keyshape.SQUARE)
    icon.family = "solo"
    icon.semantic_kind = "noun"
    icon.add_polyline("u", (10, 30), (10, 10), (10 + gap, 10), (10 + gap, 30))
    return icon


class ParallelStraightTests(unittest.TestCase):
    def test_contract_is_four_ink_eight_centerline(self):
        self.assertEqual(Profile.SOLO48.spec.mic, 4)
        self.assertEqual(Profile.SOLO48.spec.equal_stroke_centerline_min, 8)

    def test_exact_threshold_same_contour(self):
        for gap, expected in ((7, 1), (8, 0), (9, 0)):
            with self.subTest(gap=gap):
                icon = fixture(gap)
                findings = check_parallel_straight(icon, icon.draw())
                self.assertEqual(len(findings), expected)
                mic = [f for f in icon.validate_icon().findings if f.check == "mic"]
                self.assertEqual(len(mic), expected)
                if findings:
                    self.assertEqual(findings[0].detail["ink_gap"], 3)

    def test_diagonal_distance_is_perpendicular(self):
        icon = fixture(8)
        icon.primitives.clear(); icon.contours.clear()
        icon.add_polyline("u", (10, 10), (30, 30), (26, 34), (6, 14))
        finding, = check_parallel_straight(icon, icon.draw())
        self.assertAlmostEqual(finding.detail["centerline_distance"], 32 ** .5)

    def test_separate_paths_use_the_same_threshold(self):
        for gap, expected in ((7, True), (8, False)):
            icon = fixture(gap)
            icon.primitives.clear(); icon.contours.clear()
            icon.add_line('left', (10, 10), (10, 30))
            icon.add_line('right', (10 + gap, 10), (10 + gap, 30))
            failures = [f for f in icon.validate_icon().findings if f.check == 'mic']
            self.assertEqual(bool(failures), expected)

    def test_end_to_end_parallel_runs_are_not_opposing_edges(self):
        icon = fixture(8)
        icon.primitives.clear(); icon.contours.clear()
        icon.add_polyline("step", (2, 2), (12, 2), (14, 6), (24, 6))
        self.assertEqual(check_parallel_straight(icon, icon.draw()), [])

    def test_near_parallel_excluded_and_all_profiles_use_eight(self):
        icon = fixture(7)
        icon.profile = Profile.SUB32
        self.assertEqual(len(check_parallel_straight(icon, icon.draw())), 1)
        icon = fixture(7)
        icon.primitives.clear(); icon.contours.clear()
        icon.add_polyline("taper", (10, 30), (10, 10), (17, 10), (18, 30))
        self.assertEqual(check_parallel_straight(icon, icon.draw()), [])

    def test_connected_hand_finger_gap_is_blocking(self):
        icon = fixture(8)
        icon.primitives.clear(); icon.contours.clear()
        icon.add_line('outer-finger', (28, 23), (36, 31))
        icon.add_line('thumb', (26, 28), (32, 34))
        icon.relate('connect', 'outer-finger', 'thumb')
        finding, = check_parallel_straight(icon, icon.draw())
        self.assertAlmostEqual(finding.detail['centerline_distance'], 7 / (2 ** .5))
        self.assertTrue(any(f.detail.get('rule') == 'parallel_straight'
                            for f in icon.validate_icon().findings))

    def test_midpoint_blind_spot_blocks_full_pipeline(self):
        icon = fixture(8)
        icon.primitives.clear(); icon.contours.clear()
        icon.add_line('a', (0, 0), (10, 0))
        icon.add_line('b', (8, 7), (18, 7))
        finding, = check_parallel_straight(icon, icon.draw())
        self.assertEqual(finding.detail['method'], 'overlap-fallback')
        row = inspect_icon(icon)
        self.assertEqual(row['status'], 'fail')
        self.assertTrue(any('overlap-fallback' in error for error in row['errors']))

    def test_parallel_check_reaches_full_qa_report(self):
        row = inspect_icon(fixture(7))
        self.assertEqual(row['status'], 'fail')
        self.assertTrue(any('parallel straight edges' in error for error in row['errors']))
        self.assertTrue(row['rules']['internal_parallel_straight']['blocking'])


if __name__ == '__main__':
    unittest.main()
