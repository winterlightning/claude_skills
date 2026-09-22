"""The complete glyph envelope fits the 24-unit base grid."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from svgpathtools import parse_path
from icon_set.scripts.build_typeface import bounds, canonical, fit_base_grid
from icon_set.scripts.typeface_gallery import stage_typeface

ROOT = Path(__file__).resolve().parents[2]

class NaturalTypefaceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT/'icon_set/typeface/glyphs.json').read_text())
        cls.glyphs = cls.data['glyphs']

    def test_complete_character_map(self):
        self.assertEqual(self.data['geometry_policy'], 'fixed-centerline-6x20')
        self.assertEqual(len(self.glyphs), 96)
        self.assertEqual(len({g['character'] for g in self.glyphs if g['preferred']}), 95)

    def test_only_keyboard_text_is_typeface(self):
        from icon_set.typeface.classification import is_typeface_character
        for char in '$€£¥₿₹₩₴₭₤℞⊆':
            self.assertFalse(is_typeface_character(char))
        for char in 'Aa09!?@#%&*+-=“°':
            self.assertTrue(is_typeface_character(char))
        self.assertTrue(all(is_typeface_character(g['character']) for g in self.glyphs))

    def test_every_actual_envelope_fits_integer_grid(self):
        for g in self.glyphs:
            with self.subTest(glyph=g['icon_id']):
                actual = bounds([parse_path(d) for d in g['paths']])
                half = g['stroke_width']/2
                for a,b in zip(actual, g['bounds']):
                    self.assertAlmostEqual(a,b,places=8)
                self.assertAlmostEqual(actual[0]-half, g['ink_left'], places=8)
                self.assertAlmostEqual(actual[1]-half, g['ink_top'], places=8)
                self.assertAlmostEqual(actual[2]+half, g['ink_left']+g['ink_width'], places=8)
                self.assertAlmostEqual(actual[3]+half, g['ink_top']+g['ink_height'], places=8)
                self.assertEqual(g['stroke_width'],4)
                self.assertIn(g['centerline_width'],(0,6,16,28))
                self.assertIn(g['centerline_height'],(0,20))
                self.assertEqual(g['ink_width'], round(g['ink_width']))
                self.assertEqual(g['preview_box'], [0,0,g['canvas_width'],24])
                self.assertAlmostEqual(g['baseline']-g['body_top'],g['body_height'],places=8)

    def test_original_source_provenance_retained(self):
        for g in self.glyphs:
            if g['source_path']:
                self.assertEqual(g['source_sha256'], hashlib.sha256((ROOT/g['source_path']).read_bytes()).hexdigest())

    def test_curves_survive_and_normalization_is_stable(self):
        for g in self.glyphs:
            refit = fit_base_grid(g)
            self.assertEqual(refit['ink_width'],g['ink_width'])
            for a,b in zip(refit['bounds'],g['bounds']):
                self.assertAlmostEqual(a,b,places=8)
        by_char = {g['character']:g for g in self.glyphs if g['preferred']}
        self.assertTrue(any('A' in d for d in by_char['C']['paths']))
        self.assertEqual(by_char['C']['ink_width'],10)
        self.assertEqual(by_char['.']['stroke_width'],4)
        self.assertEqual(by_char['.']['ink_width'],4)
        self.assertEqual(by_char['i']['ink_width'],4)

    def test_currency_rebuild_is_reproducible(self):
        from icon_set.scripts.typeface_symbols import SYMBOLS
        symbols=json.loads((ROOT/'icon_set/typeface/symbol-glyphs.json').read_text())['glyphs']
        by_char={g['character']:g for g in symbols if g['preferred']}
        for char in '₿£¥₴₭₤₹₩℞':
            name,paths=SYMBOLS[char]
            rebuilt=fit_base_grid(canonical('symbol-'+name,char,'symbol',[parse_path(d) for d in paths],(18,42)))
            self.assertEqual(by_char[char],rebuilt)

    def test_reexport_removes_retired_symbols_and_downloads(self):
        from icon_set.scripts.typeface_gallery import export_glyphs
        from icon_set.scripts.typeface_sizes import stage_sizes
        from zipfile import ZipFile
        symbols=json.loads((ROOT/'icon_set/typeface/symbol-glyphs.json').read_text())['glyphs']
        with tempfile.TemporaryDirectory() as folder:
            target=Path(folder)
            export_glyphs(target/'typeface', {'glyphs': self.glyphs+symbols})
            stage_sizes(target/'typeface/sizes', self.glyphs+symbols)
            stage_typeface(target, [], {})
            for glyph in symbols:
                self.assertFalse((target/'typeface'/(glyph['icon_id']+'.svg')).exists())
                self.assertFalse((target/'typeface/sizes/24'/(glyph['icon_id']+'.svg')).exists())
            with ZipFile(target/'typeface/sizes/typeface-6x20.zip') as archive:
                for glyph in symbols:
                    self.assertNotIn('24/'+glyph['icon_id']+'.svg', archive.namelist())

    def test_export_uses_actual_base_canvas_and_stroke(self):
        import xml.etree.ElementTree as ET
        with tempfile.TemporaryDirectory() as folder:
            target=Path(folder)
            stage_typeface(target,[],{})
            for g in self.glyphs:
                svg=ET.parse(target/'typeface'/(g['icon_id']+'.svg')).getroot()
                self.assertEqual(float(svg.get('width')),g['canvas_width'])
                self.assertEqual(float(svg.get('height')),24)
                self.assertEqual(float(svg.get('stroke-width')),g['stroke_width'])


class NaturalTypefaceV2Tests(unittest.TestCase):
    """v2 fits UPPER and Numbers to a grid-snapped 15-unit centerline and 19-unit ink."""
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT/'icon_set/typeface/glyphs-v2.json').read_text())
        cls.glyphs = cls.data['glyphs']
        cls.by_char = {g['character']: g for g in cls.glyphs}

    def test_uppercase_and_digit_catalog(self):
        self.assertEqual(self.data['geometry_policy'], 'grid-centerline-15x19')
        self.assertEqual(self.data['case_policy'], 'uppercase')
        self.assertEqual(self.data['fallback'], 'v1')
        self.assertEqual(len(self.glyphs), 36)
        self.assertEqual(len(self.by_char), 36)
        for g in self.glyphs:
            with self.subTest(char=g['character']):
                self.assertIn(g['kind'], ('uppercase', 'digit'))
                self.assertTrue(g['preferred'])
                expected = ('letter-'+g['character'].lower()+'-uppercase'
                            if g['kind']=='uppercase' else 'digit-'+g['character'])
                self.assertEqual(g['icon_id'], expected)
                self.assertAlmostEqual(g['body_top'], 2)
                self.assertAlmostEqual(g['baseline'], 17)
                self.assertAlmostEqual(g['body_height'], 15)
                self.assertEqual(g['stroke_width'], 4)
                self.assertEqual(g['ink_height'], 19)
                self.assertEqual(g['canvas_height'], 19)
                self.assertAlmostEqual(g['bounds'][3], 17, places=3)
                self.assertAlmostEqual(g['bounds'][1], 2, places=3)
                self.assertGreaterEqual(g['canvas_width']+1e-6, g['ink_width'])

    def test_every_path_point_is_on_the_integer_grid(self):
        from svgpathtools import Arc, CubicBezier, QuadraticBezier
        for g in self.glyphs:
            for path_data in g['paths']:
                for segment in parse_path(path_data):
                    self.assertNotIsInstance(segment, Arc)
                    points=[segment.start,segment.end]
                    if isinstance(segment,CubicBezier):points += [segment.control1,segment.control2]
                    elif isinstance(segment,QuadraticBezier):points += [segment.control]
                    self.assertTrue(all(p.real==round(p.real) and p.imag==round(p.imag) for p in points),g['icon_id'])
                    self.assertGreater(segment.length(), 0, g['icon_id'])

    def test_widths_keep_source_proportions(self):
        self.assertGreater(self.by_char['W']['centerline_width'], self.by_char['I']['centerline_width'])
        self.assertGreater(self.by_char['0']['centerline_width'], self.by_char['1']['centerline_width'])

    def test_source_provenance_and_digests(self):
        for g in self.glyphs:
            with self.subTest(char=g['character']):
                expected = 'Letters/UPPER/' if g['kind']=='uppercase' else 'Letters/Numbers/'
                self.assertTrue(g['source_path'].startswith(expected))
                self.assertEqual(g['source_sha256'], hashlib.sha256((ROOT/g['source_path']).read_bytes()).hexdigest())
                digest = hashlib.sha256(json.dumps(g['paths'], separators=(',',':')).encode()).hexdigest()
                self.assertEqual(digest, g['svg_sha256'])

    def test_q_tail_is_a_stroke(self):
        q = self.by_char['Q']
        self.assertEqual(len(q['paths']), 2)
        self.assertGreaterEqual(q['centerline_width'], self.by_char['O']['centerline_width'])
