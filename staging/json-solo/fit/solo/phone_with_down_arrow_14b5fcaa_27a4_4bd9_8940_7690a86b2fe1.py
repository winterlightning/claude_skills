"""Phone with down arrow (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14b5fcaa-27a4-4bd9-8940-7690a86b2fe1'
SOURCE_PATH = 'icons-json/symbol/phone with down arrow_14b5fcaa-27a4-4bd9-8940-7690a86b2fe1.json'
AUTHOR = 'json_to_solo'

class PhoneWithDownArrowSymbol(Solo48):
    icon_id = 'phone-with-down-arrow-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('phone', 'with', 'down', 'arrow', 'symbol')

    def build(self):
        self.add_line('e0', (42, 6), (31, 18))
        self.add_line('e1', (31, 18), (40, 18))
        self.add_line('e2', (31, 8), (31, 18))
        self.add_line('e3', (35, 31), (39, 34))
        self.add_line('e4', (13, 7), (17, 11))
        self.add_line('e5', (17, 16), (10, 22))
        self.add_line('e6-1', (24, 37), (31, 30))
        self.add_arc('e6-2', (31, 30), (35, 31), radius_x=3)
        self.add_arc('e7-1', (39, 34), (33, 42), radius_x=7)
        self.add_arc('e7-2', (33, 42), (6, 13), radius_x=50)
        self.add_arc('e7-3', (6, 13), (11, 6), radius_x=8)
        self.add_arc('e7-4', (11, 6), (13, 7), radius_x=3)
        self.add_arc('e8', (17, 11), (17, 16), radius_x=3)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e6-1', 'e6-2', 'e3', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e4', 'e8', 'e5')
