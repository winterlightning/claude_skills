"""Grid-hinted typeface v2: even ink heights 18..40, stroke 4, keys on whole units."""
import hashlib
import json
from pathlib import Path
import unittest
from svgpathtools import parse_path
from icon_set.scripts.build_typeface import V2_SIZES, bounds

ROOT = Path(__file__).resolve().parents[2]


class TypefaceV2SizesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT/'icon_set/typeface/glyphs-v2-sizes.json').read_text())
        cls.native = json.loads((ROOT/'icon_set/typeface/glyphs-v2.json').read_text())['glyphs']

    def test_every_even_height_is_built(self):
        self.assertEqual(V2_SIZES, tuple(range(18, 41, 2)))
        self.assertEqual(sorted(map(int, self.data['sizes'])), list(V2_SIZES))
        ids = [g['icon_id'] for g in self.native]
        for glyphs in self.data['sizes'].values():
            self.assertEqual([g['icon_id'] for g in glyphs], ids)

    def test_geometry_snaps_to_grid(self):
        for height, glyphs in self.data['sizes'].items():
            height = int(height)
            for g in glyphs:
                with self.subTest(size=height, glyph=g['character']):
                    self.assertEqual(g['stroke_width'], 4)
                    self.assertEqual(g['hint_report']['merged_keys'], 0)
                    box = bounds([parse_path(d) for d in g['paths']])
                    for stored, parsed in zip(g['bounds'], box):
                        self.assertAlmostEqual(stored, parsed, places=6)
                    for v in box:
                        self.assertAlmostEqual(v, round(v), places=6)
                    for v in g['hint_report']['x_keys']+g['hint_report']['y_keys']:
                        self.assertEqual(v, int(v))
                    self.assertAlmostEqual(box[1], 2, places=6)
                    self.assertAlmostEqual(box[3], height-2, places=6)
                    self.assertAlmostEqual(g['ink_height'], height, places=6)
                    self.assertEqual(round(box[2]-box[0]) % 2, 0)
                    self.assertGreaterEqual(box[0]-2, -1e-6)
                    self.assertLessEqual(box[2]+2, height+1e-6)
                    digest = hashlib.sha256(json.dumps(g['paths'], separators=(',', ':')).encode()).hexdigest()
                    self.assertEqual(digest, g['svg_sha256'])

    def test_sources_are_current(self):
        for glyph in self.native:
            digest = hashlib.sha256((ROOT/glyph['source_path']).read_bytes()).hexdigest()
            self.assertEqual(digest, glyph['source_sha256'], glyph['source_path']+' changed; rebuild v2')
        native = {g['icon_id']: g['source_sha256'] for g in self.native}
        for glyphs in self.data['sizes'].values():
            for g in glyphs:
                self.assertEqual(g['source_sha256'], native[g['icon_id']])


if __name__ == '__main__':
    unittest.main()
