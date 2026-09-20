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
        self.assertEqual(self.data['geometry_policy'], 'grid-ink-height24')
        self.assertEqual(len(self.glyphs), 107)
        self.assertEqual(len({g['character'] for g in self.glyphs if g['preferred']}), 106)

    def test_every_actual_envelope_fits_integer_grid(self):
        for g in self.glyphs:
            with self.subTest(glyph=g['icon_id']):
                actual = bounds([parse_path(d) for d in g['paths']])
                half = g['stroke_width']/2
                for a,b in zip(actual, g['bounds']):
                    self.assertAlmostEqual(a,b,places=8)
                self.assertAlmostEqual(actual[0]-half, 0, places=8)
                self.assertAlmostEqual(actual[1]-half, 0, places=8)
                self.assertAlmostEqual(actual[2]+half, g['ink_width'], places=8)
                self.assertAlmostEqual(actual[3]+half, 24, places=8)
                self.assertEqual(g['ink_width'], round(g['ink_width']))
                self.assertEqual(g['preview_box'], [0,0,g['ink_width'],24])
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
        self.assertEqual(by_char['C']['ink_width'],16)
        self.assertEqual(by_char['.']['stroke_width'],24)
        self.assertEqual(by_char['.']['ink_width'],24)
        self.assertEqual(by_char['i']['ink_width'],4)

    def test_currency_rebuild_is_reproducible(self):
        from icon_set.scripts.typeface_symbols import SYMBOLS
        by_char={g['character']:g for g in self.glyphs if g['preferred']}
        for char in '₿£¥₴₭₤₹₩℞':
            name,paths=SYMBOLS[char]
            rebuilt=fit_base_grid(canonical('symbol-'+name,char,'symbol',[parse_path(d) for d in paths],(18,42)))
            self.assertEqual(by_char[char],rebuilt)

    def test_export_uses_actual_base_canvas_and_stroke(self):
        import xml.etree.ElementTree as ET
        with tempfile.TemporaryDirectory() as folder:
            target=Path(folder)
            stage_typeface(target,[],{})
            for g in self.glyphs:
                svg=ET.parse(target/'typeface'/(g['icon_id']+'.svg')).getroot()
                self.assertEqual(float(svg.get('width')),g['ink_width'])
                self.assertEqual(float(svg.get('height')),24)
                self.assertEqual(float(svg.get('stroke-width')),g['stroke_width'])
