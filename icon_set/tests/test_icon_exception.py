"""Explicit acceptance keeps measurements and expires when a drawing changes."""
import hashlib
import io
import json
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape

class ExceptionFixture(Sub32):
    icon_id = 'exception-fixture'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    def build(self):
        self.add_polyline('frame', (2,2), (30,2), (30,30), (2,30), closed=True)
        self.add_polyline('tiny', (14,14), (18,14), (18,18), (14,18), closed=True)

def small_hole_icon():
    return ExceptionFixture()


class SoloExceptionFixture(Solo48):
    icon_id = 'solo-exception-fixture'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'

    def build(self):
        self.add_polyline('frame', (6, 6), (42, 6), (42, 42), (6, 42), closed=True)
        self.add_polyline('tiny', (20, 20), (21, 20), (21, 21), (20, 21), closed=True)

from icon_set.validation import library_qa as qa
from icon_set.scripts import build as builder


def approve(icon):
    icon.exception = {'reason': 'User accepts the complete reference at 4px.',
                      'approved_by': 'user',
                      'svg_sha256': hashlib.sha256(icon.to_svg().encode()).hexdigest()}
    return icon


class IconExceptionTests(unittest.TestCase):
    def test_solo_acceptance_retains_failures_and_expires_on_change(self):
        icon = approve(SoloExceptionFixture())
        row = qa.inspect_icon(icon)
        self.assertEqual(row['status'], 'pass')
        self.assertEqual(row['automatic_status'], 'fail')
        self.assertTrue(row['errors'])
        icon.add_line('change', (28, 20), (28, 22))
        self.assertEqual(qa.inspect_icon(icon)['status'], 'fail')

    def test_solo_wrong_canvas_cannot_be_accepted(self):
        icon = SoloExceptionFixture()
        svg = icon.to_svg().replace('viewBox="0 0 48 48"', 'viewBox="0 0 60 48"')
        with patch.object(icon, 'to_svg', return_value=svg):
            approve(icon)
            self.assertNotEqual(qa.inspect_icon(icon)['status'], 'pass')

    def test_acceptance_retains_actual_failures(self):
        icon = approve(small_hole_icon())
        row = qa.inspect_icon(icon)
        self.assertEqual(row['status'], 'pass')
        self.assertEqual(row['automatic_status'], 'fail')
        self.assertEqual(row['negative_space']['status'], 'fail')
        self.assertTrue(row['errors'])
        self.assertEqual(icon.to_record()['exception'], icon.exception)

    def test_changed_drawing_or_missing_reason_does_not_pass(self):
        for change in ('drawing', 'reason'):
            icon = approve(small_hole_icon())
            if change == 'drawing':
                icon.add_line('new', (8, 8), (8, 10))
            else:
                icon.exception['reason'] = ''
            row = qa.inspect_icon(icon)
            self.assertEqual(row['status'], 'fail')
            self.assertNotIn('automatic_status', row)

    def test_checker_errors_cannot_be_accepted(self):
        icon = approve(small_hole_icon())
        with patch.object(qa, 'measure_negative_space', side_effect=RuntimeError('broken checker')):
            row = qa.inspect_icon(icon)
        self.assertEqual(row['status'], 'error')

    def test_strict_check_does_not_confuse_acceptance_with_geometry_pass(self):
        from icon_set.scripts import fix_icon_sub
        icon = approve(small_hole_icon())
        with patch.object(fix_icon_sub, 'create', return_value=icon), patch.object(fix_icon_sub, 'module_path', return_value=Path(__file__).resolve()):
            row = fix_icon_sub.strict_check(icon.icon_id)
        self.assertEqual(row['strict_32'], 'fail')
        self.assertEqual(row['qa_status'], 'fail')
        self.assertTrue(row['failures'])

    def test_wrong_stroke_is_still_blocking(self):
        icon = small_hole_icon()
        icon.STROKE_WIDTH = 2
        approve(icon)
        self.assertNotEqual(qa.inspect_icon(icon)['status'], 'pass')

    def test_build_exports_exception_and_revocation_invalidates_cache(self):
        icon = approve(small_hole_icon())
        with TemporaryDirectory() as temporary, patch.object(builder, 'icons_in', return_value=[icon]), patch.object(builder, 'create', return_value=icon), redirect_stdout(io.StringIO()):
            root = Path(temporary)
            options = dict(write_png=False, only=['sub'], debug=False, report=False, changed_only=True)
            self.assertEqual(builder.build(root/'dist', root/'png', **options), 0)
            manifest = json.loads((root/'dist/sub32/manifest.json').read_text())
            records = manifest['icons']
            self.assertEqual(records[0]['validation']['automatic_status'], 'fail')
            self.assertEqual(records[0]['validation']['exception'], icon.exception)
            icon.exception = None
            self.assertEqual(builder.build(root/'dist', root/'png', **options), 1)


if __name__ == '__main__':
    unittest.main()
