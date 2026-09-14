"""Curvy large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c9e1073-40ac-499b-9c75-8c1fc2f12243'
SOURCE_PATH = 'icons-json/arrows/curvy large head_2c9e1073-40ac-499b-9c75-8c1fc2f12243.json'
AUTHOR = 'json_to_solo'

class CurvyLargeHeadArrows(Solo48):
    icon_id = 'curvy-large-head-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curvy', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (39, 8), (44, 13))
        self.add_line('e1', (20, 33), (20, 21))
        self.add_line('e2', (29, 13), (44, 13))
        self.add_line('e3', (39, 19), (44, 13))
        self.add_arc('e4-1', (4, 32), (12, 40), radius_x=8, sweep=False)
        self.add_line('e4-2', (12, 40), (18, 38))
        self.add_arc('e4-3', (18, 38), (20, 33), radius_x=8, sweep=False)
        self.add_arc('e5', (20, 21), (29, 13), radius_x=9)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e4-1', 'e4-2', 'e4-3', 'e1', 'e5', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
