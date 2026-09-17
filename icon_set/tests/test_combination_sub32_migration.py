"""A rounded outer box must not substitute for grid-safe source geometry."""
import unittest
from icon_set.model.icons.registry import create
from icon_set.scripts.audit_combination_subs import proportional_candidate
from icon_set.scripts.combination_experiment import placement, POSITIONS
from icon_set.validation.envelope import centerline_bounds


class Sub32MigrationTests(unittest.TestCase):
    def test_fractional_robot_resize_requires_redraw(self):
        source = create('robot-head-with-twin-antennae')
        _, _, issues = proportional_candidate(source, source.keyshape)
        self.assertTrue(issues)
        report = create('robot-head-with-twin-antennae-sub32').validate_icon()
        self.assertEqual(report.status, 'valid')
        self.assertFalse(report.warnings)

    def test_native_default_placement_preserves_grid_in_all_positions(self):
        for uid in ('robot-head-with-twin-antennae', 'circle-add', 'ball', 'circle-symbol',
                    'plain-circular-rescue-ring-with-quarter-divisions',
                    'sparkle-four-point-rounded', 'add'):
            icon = create(uid + '-sub32')
            bounds = centerline_bounds(icon.draw().primitives)
            item = dict(bounds=bounds, canvas=32)
            for anchor in POSITIONS.values():
                with self.subTest(icon=uid, anchor=anchor):
                    p = placement(item, 32, anchor, (0, 0), size_lock='auto')
                    b = p['painted_box']
                    self.assertAlmostEqual(b['w'] - 4, bounds[2] - bounds[0])
                    self.assertAlmostEqual(b['h'] - 4, bounds[3] - bounds[1])
                    for offset in (b['x'] + 2 - bounds[0], b['y'] + 2 - bounds[1]):
                        self.assertAlmostEqual(offset, round(offset))
