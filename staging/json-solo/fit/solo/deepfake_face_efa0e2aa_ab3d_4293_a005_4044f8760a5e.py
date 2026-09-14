"""Deepfake face (artificial-intelligence), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'efa0e2aa-ab3d-4293-a005-4044f8760a5e'
SOURCE_PATH = 'icons-json/artificial-intelligence/deepfake face_efa0e2aa-ab3d-4293-a005-4044f8760a5e.json'
AUTHOR = 'json_to_solo'

class DeepfakeFaceEfa0e2aa(Solo48):
    icon_id = 'deepfake-face-efa0e2aa'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('deepfake', 'face', 'artificial-intelligence')

    def build(self):
        self.add_line('e0', (40, 19), (8, 19))
        self.add_line('e1', (24, 28), (24, 4))
        self.add_line('e2', (40, 26), (40, 12))
        self.add_line('e3', (8, 19), (8, 29))
        self.add_arc('e4', (16, 30), (32, 30), radius_x=9, sweep=False)
        self.add_arc('e5-1', (40, 12), (36, 6), radius_x=11, sweep=False)
        self.add_arc('e5-2', (36, 6), (31, 4), radius_x=10, sweep=False)
        self.add_line('e5-3', (31, 4), (24, 4))
        self.add_line('e5-4', (24, 4), (17, 4))
        self.add_arc('e5-5', (17, 4), (12, 6), radius_x=9, sweep=False)
        self.add_arc('e5-6', (12, 6), (9, 10), radius_x=11, sweep=False)
        self.add_line('e5-7', (9, 10), (8, 17))
        self.add_line('e5-8', (8, 17), (8, 19))
        self.add_arc('e6-1', (8, 29), (24, 44), radius_x=17, sweep=False)
        self.add_arc('e6-2', (24, 44), (36, 38), radius_x=15, sweep=False)
        self.add_arc('e6-3', (36, 38), (40, 26), radius_x=20, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e2', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', 'e5-8', 'e3', 'e6-1', 'e6-2', 'e6-3', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
