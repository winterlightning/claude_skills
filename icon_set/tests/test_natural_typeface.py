"""Free-proportion lettering preserves curves and typographic measurements."""
import hashlib
import json
import string
from pathlib import Path
import unittest
from svgpathtools import parse_path
from icon_set.scripts.build_typeface import source_paths, bounds

ROOT=Path(__file__).resolve().parents[2]

class NaturalTypefaceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads((ROOT/'icon_set/typeface/glyphs.json').read_text())
        cls.glyphs=cls.data['glyphs']

    def test_complete_character_map_without_keyshape_constraints(self):
        self.assertEqual(self.data['geometry_policy'],'natural-proportions-no-keyshape')
        self.assertEqual(len(self.glyphs),97)
        self.assertEqual(len({g['character'] for g in self.glyphs if g['preferred']}),96)
        for g in self.glyphs:self.assertNotIn('keyshape',g)

    def test_original_aspect_ratios_are_preserved_by_uniform_transforms(self):
        for g in self.glyphs:
            if not g['source_path']:continue
            with self.subTest(glyph=g['icon_id']):
                source=ROOT/g['source_path']
                original=bounds(source_paths(source))
                new=g['bounds']
                if original[2]>original[0]:
                    self.assertAlmostEqual((original[2]-original[0])/(original[3]-original[1]),
                                           (new[2]-new[0])/(new[3]-new[1]),places=10)
                self.assertEqual(g['source_sha256'],hashlib.sha256(source.read_bytes()).hexdigest())

    def test_bounds_metrics_and_preview_do_not_clip_any_glyph(self):
        for g in self.glyphs:
            with self.subTest(glyph=g['icon_id']):
                actual=bounds([parse_path(d) for d in g['paths']])
                for a,b in zip(actual,g['bounds']):self.assertAlmostEqual(a,b,places=9)
                self.assertAlmostEqual(g['baseline']-g['body_top'],g['body_height'],places=9)
                self.assertAlmostEqual(g['body_height'],24 if g['kind'] in ('lowercase','symbol') else 24*52/36)
                x,y,w,h=g['preview_box']
                self.assertGreaterEqual(actual[0]-2,x)
                self.assertGreaterEqual(actual[1]-2,y)
                self.assertLessEqual(actual[2]+2,x+w)
                self.assertLessEqual(actual[3]+2,y+h)

    def test_source_curves_and_compact_shoulders_survive(self):
        by_id={g['icon_id']:g for g in self.glyphs}
        for name in ['letter-r','letter-s','letter-j','letter-e','digit-2']:
            self.assertTrue(any('C' in d for d in by_id[name]['paths']),name)
        r=by_id['letter-r'];j=by_id['letter-j'];s=by_id['letter-s']
        self.assertLess((r['bounds'][2]-r['bounds'][0])/r['body_height'],.4)
        self.assertLess((j['bounds'][2]-j['bounds'][0])/j['body_height'],.4)
        self.assertLess((s['bounds'][2]-s['bounds'][0])/s['body_height'],.8)

    def test_keyboard_symbols_share_typographic_band(self):
        symbols={g['character']:g for g in self.glyphs if g['kind']=='symbol'}
        self.assertEqual(set(symbols),set(string.punctuation)|{"“","⊆"})
        for char,g in symbols.items():
            self.assertIsNone(g['source_path'])
            self.assertEqual(g['body_height'],24)
            self.assertEqual(g['baseline']-g['body_top'],24)
        self.assertEqual(symbols['.']['bounds'][3],symbols['.']['baseline'])
        self.assertGreater(symbols[',']['bounds'][3],symbols[',']['baseline'])
        self.assertLess(symbols['"']['bounds'][3],symbols['"']['body_top'])
