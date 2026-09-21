"""Every published size matches its real stroked geometry and the size proposal."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET
from zipfile import ZipFile

from svgpathtools import parse_path
from icon_set.scripts.build_typeface import bounds
from icon_set.scripts.typeface_sizes import HEIGHTS, size_record, stage_sizes


class TypefaceSizesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        source = Path(__file__).resolve().parents[1] / 'typeface/glyphs.json'
        cls.glyphs = json.loads(source.read_text())['glyphs']

    def test_all_exports_match_actual_geometry_and_integer_dimensions(self):
        before = json.dumps(self.glyphs, sort_keys=True)
        ns = {'s': 'http://www.w3.org/2000/svg'}
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder)
            manifest = stage_sizes(target, self.glyphs)
            self.assertEqual(manifest['heights'], list(range(12,33)))
            self.assertEqual(len(list(target.glob('*/*.svg'))), 107*21)
            for glyph, entry in zip(self.glyphs, manifest['glyphs']):
                for size in entry['sizes']:
                    with self.subTest(glyph=glyph['icon_id'], height=size['height']):
                        document = (target/size['file']).read_bytes()
                        self.assertEqual(hashlib.sha256(document).hexdigest(), size['svg_sha256'])
                        svg = ET.fromstring(document)
                        group = svg.find('s:g', ns)
                        self.assertIsNone(group.get('transform'))
                        self.assertEqual(group.get('stroke-width'),'4')
                        self.assertFalse(any(el.get('transform') for el in svg.iter()))
                        # Read the exported paths, stroke and transform rather than
                        # trusting the stored width or bounding-box metadata.
                        box = bounds([parse_path(p.get('d')) for p in group.findall('s:path', ns)])
                        half = float(group.get('stroke-width'))/2
                        ink = [box[0]-half, box[1]-half,
                               box[2]+half, box[3]+half]
                        h = size['height']
                        path_w = glyph['bounds'][2]-glyph['bounds'][0]
                        path_h = glyph['bounds'][3]-glyph['bounds'][1]
                        w = max(4,2*int(glyph['ink_width']*h/48+0.5)) if path_w > 1e-9 else 4
                        ink_h = h if path_h > 1e-9 else 4
                        top = (h-ink_h)/2
                        self.assertEqual(size['ink_height'],ink_h)
                        self.assertEqual(size['stroke_width'],4)
                        for actual,expected in zip(ink, [0,top,w,top+ink_h]):
                            self.assertAlmostEqual(actual,expected,places=7)
                        self.assertEqual(svg.get('viewBox'),f'0 0 {w} {h}')
                        self.assertEqual(svg.get('width'),str(w))
                        self.assertEqual(svg.get('height'),str(h))
                        self.assertEqual(size['width'],w)
                        self.assertEqual(w % 2,0)
            with ZipFile(target/'typeface-12-to-32.zip') as archive:
                self.assertEqual(len(archive.namelist()),107*21+2)
                self.assertEqual(json.loads(archive.read('manifest.json')),manifest)
                self.assertIsNone(archive.testzip())
            self.assertNotIn('__SIZE_DATA__',(target/'index.html').read_text())
        self.assertEqual(json.dumps(self.glyphs, sort_keys=True), before)

    def test_all_intermediate_sizes_and_narrow_stems(self):
        by_char = {g['character']:g for g in self.glyphs if g['preferred']}
        self.assertEqual([size_record(by_char['C'],h)['width'] for h in HEIGHTS],
                         [8,8,10,10,10,12,12,12,14,14,14,16,16,16,18,18,18,20,20,20,22])
        # Narrow stems cannot be narrower than the fixed stroke.
        size = size_record(by_char['i'],15)
        self.assertEqual(size['width'],4)
        self.assertEqual(size['stroke_width_x'],4)
        for h in HEIGHTS:
            self.assertEqual(size_record(by_char['.'],h)['width'],4)
            self.assertEqual(size_record(by_char['.'],h)['ink_height'],4)
            self.assertEqual(size_record(by_char['-'],h)['ink_height'],4)

    def test_even_width_ties_round_up(self):
        by_char = {g['character']:g for g in self.glyphs if g['preferred']}
        self.assertEqual(size_record(by_char['O'],12)['width'],10)  # 9 -> 10
        self.assertEqual(size_record(by_char['O'],28)['width'],22)  # 21 -> 22
        self.assertEqual(size_record(by_char['A'],24)['width'],20)  # 19 -> 20

    def test_invalid_sizes_are_rejected(self):
        for height in (11,33,12.5,True,'24'):
            with self.assertRaises(ValueError):
                size_record(self.glyphs[0],height)


if __name__ == '__main__':
    unittest.main()
