"""Deepfake rotate (artificial-intelligence), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30e56ade-c3d8-5998-a5e2-8711b05ffd45'
SOURCE_PATH = 'icons-json/artificial-intelligence/deepfake rotate_30e56ade-c3d8-5998-a5e2-8711b05ffd45.json'
AUTHOR = 'json_to_solo'

class DeepfakeRotateArtificialIntelligence(Solo48):
    icon_id = 'deepfake-rotate-artificial-intelligence'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('deepfake', 'rotate', 'artificial-intelligence')

    def build(self):
        self.add_line('e0', (27, 9), (21, 4))
        self.add_line('e1', (27, 9), (21, 13))
        self.add_arc('e2-1', (34, 12), (39, 20), radius_x=21)
        self.add_line('e2-2', (39, 20), (40, 26))
        self.add_arc('e2-3', (40, 26), (34, 40), radius_x=20)
        self.add_arc('e2-4', (34, 40), (25, 44), radius_x=15)
        self.add_line('e2-5', (25, 44), (19, 43))
        self.add_arc('e2-6', (19, 43), (14, 40), radius_x=15)
        self.add_arc('e2-7', (14, 40), (10, 35), radius_x=19)
        self.add_line('e2-8', (10, 35), (8, 26))
        self.add_line('e2-9', (8, 26), (9, 20))
        self.add_arc('e2-10', (9, 20), (13, 13), radius_x=23)
        self.add_arc('e3-1', (38, 34), (15, 18), radius_x=27)
        self.add_arc('e3-2', (15, 18), (14, 12), radius_x=4)
        self.add_arc('e3-3', (14, 12), (27, 9), radius_x=16)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8', 'e2-9', 'e2-10')
        self.add_contour('c1', 'e3-1', 'e3-2', 'e3-3')
        self.add_contour('c2', 'e0')
        self.add_contour('c3', 'e1')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c0')
