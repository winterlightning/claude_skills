"""Brightness (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0683af89-a794-45d7-baf4-2a77d813dbe0'
SOURCE_PATH = 'icons-json/interface-essential/brightness_0683af89-a794-45d7-baf4-2a77d813dbe0.json'
AUTHOR = 'json_to_solo'

class Brightness(Solo48):
    icon_id = 'brightness'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('brightness', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 6), (24, 11))
        self.add_line('e1', (12, 12), (15, 15))
        self.add_line('e2', (33, 15), (36, 12))
        self.add_line('e3', (6, 24), (11, 24))
        self.add_line('e4', (37, 24), (42, 24))
        self.add_line('e5', (12, 36), (15, 33))
        self.add_line('e6', (33, 33), (36, 36))
        self.add_line('e7', (24, 42), (24, 37))
        self.add_arc('e8-top', (17, 24), (31, 24), radius_x=7)
        self.add_arc('e8-bottom', (31, 24), (17, 24), radius_x=7)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
