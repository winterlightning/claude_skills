"""Arrow rectangle left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84253ba9-1f79-5e64-9fcc-510a1fc2dc89'
SOURCE_PATH = 'icons-json/arrows/arrow rectangle left_84253ba9-1f79-5e64-9fcc-510a1fc2dc89.json'
AUTHOR = 'json_to_solo'

class ArrowRectangleLeft(Solo48):
    icon_id = 'arrow-rectangle-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'rectangle', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (22, 8), (41, 8))
        self.add_line('e1', (44, 11), (44, 37))
        self.add_line('e2', (42, 40), (19, 40))
        self.add_line('e3', (12, 34), (5, 26))
        self.add_line('e4', (6, 22), (16, 10))
        self.add_line('e5', (30, 16), (23, 24))
        self.add_line('e6', (23, 24), (30, 32))
        self.add_arc('e7-1', (14, 12), (20, 8), radius_x=7)
        self.add_arc('e7-2', (20, 8), (22, 8), radius_x=32, sweep=False)
        self.add_arc('e8', (41, 8), (44, 11), radius_x=3)
        self.add_line('e9', (44, 37), (42, 40))
        self.add_arc('e10', (19, 40), (12, 34), radius_x=15)
        self.add_line('e11-1', (5, 26), (4, 25))
        self.add_arc('e11-2', (4, 25), (6, 22), radius_x=4)
        self.add_contour('c0', 'e7-1', 'e7-2', 'e0', 'e8', 'e1', 'e9', 'e2', 'e10', 'e3', 'e11-1', 'e11-2', 'e4')
        self.add_contour('c1', 'e5', 'e6')
