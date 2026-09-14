"""Casino chip 1 (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c7cef94c-7b9b-4df7-b935-546150f20188'
SOURCE_PATH = 'icons-json/symbol/casino chip 1_c7cef94c-7b9b-4df7-b935-546150f20188.json'
AUTHOR = 'json_to_solo'

class CasinoChip1Symbol(Solo48):
    icon_id = 'casino-chip-1-symbol'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('casino', 'chip', 'symbol')

    def build(self):
        self.add_line('e0', (17, 31), (10, 38))
        self.add_line('e1', (38, 38), (31, 31))
        self.add_line('e2', (31, 17), (38, 10))
        self.add_line('e3', (17, 17), (10, 10))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e5-top', (14, 24), (34, 24), radius_x=10)
        self.add_arc('e5-bottom', (34, 24), (14, 24), radius_x=10)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c0', 'e5')
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c1', 'e5')
        self.relate('connect', 'c2', 'e5')
        self.relate('connect', 'c2', 'e4')
        self.relate('connect', 'c3', 'e5')
        self.relate('connect', 'c3', 'e4')
