"""Only the fixed centerline size is exported, with constant stroke 4."""
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
        cls.glyphs=json.loads((Path(__file__).resolve().parents[1]/'typeface/glyphs.json').read_text())['glyphs']

    def test_exported_geometry_and_single_size_bundle(self):
        ns={'s':'http://www.w3.org/2000/svg'}
        self.assertEqual(HEIGHTS,(24,))
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            manifest=stage_sizes(root,self.glyphs)
            self.assertEqual(manifest['heights'],[24])
            self.assertEqual(len(list(root.glob('*/*.svg'))),107)
            for glyph,entry in zip(self.glyphs,manifest['glyphs']):
                self.assertEqual(len(entry['sizes']),1)
                record=entry['sizes'][0]
                doc=(root/record['file']).read_bytes()
                self.assertEqual(hashlib.sha256(doc).hexdigest(),record['svg_sha256'])
                svg=ET.fromstring(doc)
                self.assertEqual(svg.get('viewBox'),f"0 0 {glyph['canvas_width']} 24")
                self.assertEqual(svg.get('width'),str(glyph['canvas_width']))
                self.assertEqual(svg.get('height'),'24')
                group=svg.find('s:g',ns)
                self.assertEqual(group.get('stroke-width'),'4')
                self.assertFalse(any(el.get('transform') for el in svg.iter()))
                box=bounds([parse_path(el.get('d')) for el in group.findall('s:path',ns)])
                self.assertAlmostEqual(box[2]-box[0],glyph['centerline_width'],places=7)
                self.assertAlmostEqual(box[3]-box[1],glyph['centerline_height'],places=7)
                self.assertGreaterEqual(box[0]-2,-1e-7)
                self.assertGreaterEqual(box[1]-2,-1e-7)
                self.assertLessEqual(box[2]+2,glyph['canvas_width']+1e-7)
                self.assertLessEqual(box[3]+2,24+1e-7)
            with ZipFile(root/'typeface-6x20.zip') as archive:
                self.assertEqual(len(archive.namelist()),109)
                self.assertIsNone(archive.testzip())
            self.assertNotIn('__SIZE_DATA__',(root/'index.html').read_text())

    def test_retired_sizes_are_rejected(self):
        for height in [*range(12,24),*range(25,33),24.0,True,'24']:
            with self.assertRaises(ValueError):size_record(self.glyphs[0],height)
