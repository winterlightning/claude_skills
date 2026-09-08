"""Release integrity regressions discovered in the architecture review."""
import hashlib
import importlib.util
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from icon_set.model.icons.registry import create
from icon_set.model.primitives import Arc, Point
from icon_set.renderers.svg import build_paths

_SPEC = importlib.util.spec_from_file_location(
    'icon_build_review', Path(__file__).resolve().parents[1] / 'scripts/build.py'
)
builder = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(builder)


class GeometryIntegrityTests(unittest.TestCase):
    def test_duplicate_contours_cannot_hide_a_square(self):
        icon = create('square')
        icon.add_line('extra', (12, 16), (20, 16))
        icon.add_contour('outline', 'extra')
        self.assertFalse(icon.validate_icon().ok)
        with self.assertRaisesRegex(ValueError, 'duplicate contour'):
            icon.to_svg()

    def test_loose_path_cannot_hide_a_contour_in_either_order(self):
        for loose_first in (True, False):
            with self.subTest(loose_first=loose_first):
                icon = create('square')
                icon.add_line('outline', (12, 16), (20, 16))
                if loose_first:
                    icon.primitives.insert(0, icon.primitives.pop())
                with self.assertRaisesRegex(ValueError, 'conflicting emitted path'):
                    build_paths(icon.draw())
                self.assertFalse(icon.validate_icon().ok)

    def test_emission_covers_every_primitive_once(self):
        from icon_set.model.icons.registry import all_icons
        from collections import Counter
        for icon in all_icons():
            with self.subTest(icon=icon.icon_id):
                drawing = icon.draw()
                emitted = [m for p in build_paths(drawing) for m in p['members']]
                self.assertEqual(Counter(emitted), Counter(p.element_id for p in drawing.primitives))

    def test_namespaced_standalone_paths_still_require_spacing(self):
        icon = create('square')
        icon.primitives.clear()
        icon.contours.clear()
        left, top, right, bottom = icon.keyshape_bounds()
        icon.add_polyline('0:fake:outline', (left + 2, top + 2), (right - 2, top + 2),
                          (right - 2, bottom - 2), (left + 2, bottom - 2), closed=True)
        icon.add_line('0:fake:near', (left + 8, top + 3), (right - 8, top + 3))
        report = icon.validate_icon()
        self.assertTrue(any(e.startswith('mic') for e in report.errors), report.describe())


class StructuralValidationTests(unittest.TestCase):
    def test_invalid_metadata_returns_a_report(self):
        cases = [('profile', 'SUB32'), ('keyshape', 'SQUARE'), ('family', []),
                 ('category', 123), ('category', ''), ('aliases', 'alias'),
                 ('keywords', [123]), ('semantic_kind', 'other'),
                 ('icon_id', '../escaped'), ('icon_id', '/absolute'),
                 ('icon_id', 'square\n')]
        for field, value in cases:
            with self.subTest(field=field, value=value):
                icon = create('square')
                setattr(icon, field, value)
                report = icon.validate_icon()
                self.assertFalse(report.ok)
                self.assertTrue(any(e.startswith('schema/profile') for e in report.errors))

    def test_malformed_geometry_returns_a_report(self):
        for primitive in [object(), Arc('bad', Point(2, 16), Point(30, 16), '14', 14),
                          Arc('bad', Point(float('nan'), 16), Point(30, 16), 14, 14),
                          Arc('bad', Point(2, 16), Point(30, 16), 14, 14, 2, True)]:
            with self.subTest(primitive=primitive):
                icon = create('square')
                icon.primitives.append(primitive)
                self.assertFalse(icon.validate_icon().ok)

    def test_unknown_relationship_member_is_rejected(self):
        icon = create('square')
        icon.relate('connect', 'outline', 'missing')
        self.assertFalse(icon.validate_icon().ok)


class BuildIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.dist = self.root / 'dist'
        self.png = self.root / 'png'
        for root in (self.dist, self.png):
            for family in ('sub32', 'solo48'):
                folder = root / family
                folder.mkdir(parents=True)
                for name in ('square.svg', 'stale.svg', 'square.png', 'manifest.json'):
                    (folder / name).write_bytes(b'previous release')
        self.before = self.snapshot()

    def snapshot(self):
        return {str(p.relative_to(self.root)): p.read_bytes()
                for p in self.root.rglob('*') if p.is_file()}

    def test_invalid_icon_preserves_previous_family(self):
        good, bad = create('square'), create('plus')
        bad.STROKE_WIDTH = 99
        with patch.object(builder, 'icons_in', return_value=[good, bad]):
            self.assertEqual(builder.build_family('sub', self.dist, self.png, write_png=False, report=False), (0, 1))
        self.assertEqual(self.snapshot(), self.before)

    def test_failure_in_later_family_preserves_all_outputs(self):
        bad = create('smartwatch')
        bad.STROKE_WIDTH = 99
        with patch.object(builder, 'icons_in', side_effect=lambda f: [create('square')] if f == 'sub' else [bad]):
            self.assertEqual(builder.build(self.dist, self.png, write_png=False, only=['sub', 'solo'], report=False), 1)
        self.assertEqual(self.snapshot(), self.before)

    def test_png_failure_preserves_svgs_manifests_and_previews(self):
        with patch.object(builder, 'icons_in', return_value=[create('square')]), \
                patch.object(builder, 'render_png', side_effect=RuntimeError('renderer unavailable')):
            self.assertEqual(builder.build_family('sub', self.dist, self.png,
                                                   write_png=True, report=False), (0, 1))
        self.assertEqual(self.snapshot(), self.before)

    def test_publish_failure_rolls_back_prior_swaps(self):
        original = builder.os.replace
        def fail_once(src, dst):
            if Path(src).name == 'sub32' and Path(dst) == self.png / 'sub32':
                raise OSError('simulated publication failure')
            return original(src, dst)
        with patch.object(builder, 'icons_in', return_value=[create('square')]), \
                patch.object(builder, 'render_png', return_value=b'new png'), \
                patch.object(builder.os, 'replace', side_effect=fail_once):
            with self.assertRaisesRegex(OSError, 'publication failure'):
                builder.build_family('sub', self.dist, self.png, write_png=True, report=False)
        self.assertEqual(self.snapshot(), self.before)

    def test_success_publishes_matching_manifest_and_prunes_only_selected_family(self):
        with patch.object(builder, 'icons_in', return_value=[create('square')]):
            self.assertEqual(builder.build_family('sub', self.dist, self.png, write_png=False, report=False), (1, 0))
        manifest = json.loads((self.dist / 'sub32/manifest.json').read_text())
        svg = self.dist / 'sub32/square.svg'
        record = manifest['icons'][0]
        self.assertEqual(record['svg_sha256'], hashlib.sha256(svg.read_bytes()).hexdigest())
        self.assertEqual((builder.PACKAGE_ROOT / record['svg_path']).resolve(), svg)
        self.assertFalse((self.dist / 'sub32/stale.svg').exists())
        self.assertEqual((self.dist / 'solo48/stale.svg').read_bytes(), b'previous release')
        self.assertEqual((self.png / 'sub32/square.png').read_bytes(), b'previous release')
        after = self.snapshot()
        with patch.object(builder, 'icons_in', return_value=[create('square')]):
            builder.build_family('sub', self.dist, self.png, write_png=False, report=False)
        self.assertEqual(self.snapshot(), after)

    def test_invalid_id_cannot_escape_output_directory(self):
        icon = create('square')
        icon.icon_id = '../escaped'
        with patch.object(builder, 'icons_in', return_value=[icon]):
            self.assertEqual(builder.build_family('sub', self.dist, self.png, write_png=False, report=False), (0, 1))
        self.assertEqual(self.snapshot(), self.before)
