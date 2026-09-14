"""Arrow rectangle left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0805fb92-9e1a-592f-854d-f7c801587705'
SOURCE_PATH = 'icons-json/arrows/arrow rectangle left_0805fb92-9e1a-592f-854d-f7c801587705.json'
AUTHOR = 'json_to_solo'

class ArrowRectangleLeft0805fb92(Solo48):
    icon_id = 'arrow-rectangle-left-0805fb92'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'rectangle', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (25, 16), (18, 24))
        self.add_line('e1', (18, 24), (26, 32))
        self.add_line('e2', (42, 8), (7, 8))
        self.add_line('e3', (4, 12), (4, 37))
        self.add_line('e4', (8, 40), (41, 40))
        self.add_line('e5', (44, 37), (44, 9))
        self.add_arc('e6-1', (7, 8), (4, 11), radius_x=3, sweep=False)
        self.add_arc('e6-2', (4, 11), (4, 12), radius_x=18)
        self.add_arc('e7-1', (4, 37), (7, 40), radius_x=3, sweep=False)
        self.add_arc('e7-2', (7, 40), (8, 40), radius_x=21)
        self.add_line('e8-1', (41, 40), (44, 39))
        self.add_line('e8-2', (44, 39), (44, 38))
        self.add_arc('e8-3', (44, 38), (44, 37), radius_x=39)
        self.add_arc('e9', (44, 9), (42, 8), radius_x=3, sweep=False)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e6-1', 'e6-2', 'e3', 'e7-1', 'e7-2', 'e4', 'e8-1', 'e8-2', 'e8-3', 'e5', 'e9', closed=True)
