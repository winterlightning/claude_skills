import io
import unittest
import xml.etree.ElementTree as ET
import cairosvg
import numpy as np
from PIL import Image
from icon_set.scripts.combination_state_subs import engine_document

class StateSubBridgeTests(unittest.TestCase):
    def test_dot_conversion_preserves_painted_artwork(self):
        source='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" stroke="currentColor" stroke-width="4" fill="none" stroke-linecap="round"><circle cx="16" cy="16" r="14"/><path d="M16 8V17"/><circle cx="16" cy="24" r="2" fill="currentColor" stroke="none"/></svg>'
        converted=engine_document(source)
        images=[np.array(Image.open(io.BytesIO(cairosvg.svg2png(bytestring=s.encode(),output_width=256,output_height=256))).convert('RGBA'))[:,:,3] for s in (source,converted)]
        self.assertLess(np.abs(images[0].astype(int)-images[1].astype(int)).mean(),.03)
        root=ET.fromstring(converted)
        self.assertEqual(len(root.findall('{*}circle')),1)
        self.assertEqual(len(root.findall('{*}path')),2)

    def test_does_not_silently_thicken_or_remove_unsupported_fills(self):
        with self.assertRaises(ValueError):engine_document('<svg stroke-width="2"/>')
        with self.assertRaises(ValueError):engine_document('<svg stroke-width="4"><circle r="5" stroke="none"/></svg>')
