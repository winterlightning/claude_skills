"""Diagnostic reflections must preserve geometry and leave verdicts to reviewers."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from icon_set.model.icons.base import Icon
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.scripts.prepare_icon_review import prepare, reflection_matrix


def transform(matrix, point):
    a, b, c, d, e, f = matrix
    x, y = point
    return a*x+c*y+e, b*x+d*y+f


class ReviewEvidenceTests(unittest.TestCase):
    def test_shuttlecock_axis_pairs_attachments(self):
        matrix = reflection_matrix((14, 34, 30, 18))
        for point, expected in [((14, 26), (22, 34)), ((18, 10), (38, 30)), ((14, 34), (14, 34))]:
            for actual, wanted in zip(transform(matrix, point), expected):
                self.assertAlmostEqual(actual, wanted)

    def test_arbitrary_reflection_is_involution_and_fixes_axis(self):
        for axis in [(3, 2, 3, 9), (1, 8, 9, 8), (-2, 5, 7, 9)]:
            matrix = reflection_matrix(axis)
            for point in [(4, -7), axis[:2], axis[2:]]:
                restored = transform(matrix, transform(matrix, point))
                for actual, expected in zip(restored, point):
                    self.assertAlmostEqual(actual, expected)
            for point in [axis[:2], axis[2:]]:
                for actual, expected in zip(transform(matrix, point), point):
                    self.assertAlmostEqual(actual, expected)

    def test_bad_axis_rejected_before_output(self):
        with TemporaryDirectory() as folder:
            output = Path(folder)/'evidence'
            for axis in [(1, 1, 1, 1), (0, 0, float('nan'), 1), (0, 0, float('inf'), 1)]:
                with self.assertRaises(ValueError):
                    prepare('unused', output, axis)
                self.assertFalse(output.exists())

    def test_profile_native_sizes_and_no_visual_verdict(self):
        from PIL import Image
        for profile in Profile:
            with self.subTest(profile=profile.name), TemporaryDirectory() as folder:
                icon = Icon('review-fixture', profile, semantic_role='MAIN', keyshape=Keyshape.SQUARE)
                icon.add_line('stroke', (8, 8), (16, 16))
                original = icon.to_svg()
                with patch('icon_set.model.icons.registry.create', return_value=icon):
                    evidence = prepare('review-fixture', Path(folder), (0, 0, 1, 1))
                self.assertEqual(icon.to_svg(), original)
                self.assertEqual((Path(folder)/'current.svg').read_text(), original)
                with Image.open(Path(folder)/'light-native.png') as rendered:
                    self.assertEqual(rendered.size, (profile.spec.canvas_size,)*2)
                self.assertEqual(evidence['visual_review'], 'not_performed')
                self.assertNotEqual(evidence['qa']['status'], 'pass')
                saved = json.loads((Path(folder)/'evidence.json').read_text())
                self.assertEqual(saved['qa']['status'], evidence['qa']['status'])
                self.assertTrue((Path(folder)/'mirror.png').is_file())


if __name__ == '__main__':
    unittest.main()
