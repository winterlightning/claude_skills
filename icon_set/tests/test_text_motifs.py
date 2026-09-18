import unittest,xml.etree.ElementTree as ET
from svgpathtools import parse_path
from icon_set.scripts.build_text_motifs import compose

class TextMotifTests(unittest.TestCase):
    def test_motifs_preserve_text_size_and_trim_combined_ink(self):
        result={'width':20,'height':28,'placements':[{'glyph':{'paths':['M2 2H18V26H2Z']},'scale':1,'x':0,'y':0}]}
        for motif in ['flash','document','chart','table','height','width','format','wrench']:
            with self.subTest(motif=motif):
                r=compose({'name':'Example','motif':motif},result)
                root=ET.fromstring(r['document']);self.assertEqual(root.get('stroke-width'),'4')
                paths=[parse_path(x.get('d')) for x in root if x.tag.endswith('path')]
                bounds=[p.bbox() for p in paths];text=paths[0].bbox()
                self.assertAlmostEqual(text[3]-text[2]+4,28)
                self.assertAlmostEqual(min(b[0] for b in bounds)-2,0)
                self.assertAlmostEqual(min(b[2] for b in bounds)-2,0)
                self.assertAlmostEqual(max(b[1] for b in bounds)+2,r['width'])
                self.assertAlmostEqual(max(b[3] for b in bounds)+2,r['height'])

    def test_unknown_motif_is_rejected(self):
        result={'width':20,'height':28,'placements':[{'glyph':{'paths':['M2 2H18V26']},'scale':1,'x':0,'y':0}]}
        with self.assertRaises(ValueError):compose({'name':'Example','motif':'unknown'},result)

if __name__=='__main__':unittest.main()
