"""Phone with starburst (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9ee0961-b35e-48ac-b567-d69d398bf9fc'
SOURCE_PATH = 'icons-json/symbol/phone with starburst_c9ee0961-b35e-48ac-b567-d69d398bf9fc.json'
AUTHOR = 'json_to_solo'

class PhoneWithStarburstSymbol(Solo48):
    icon_id = 'phone-with-starburst-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('phone', 'with', 'starburst', 'symbol')

    def build(self):
        self.add_line('e0', (24, 14), (24, 8))
        self.add_line('e1', (35, 15), (37, 10))
        self.add_line('e2', (11, 10), (14, 15))
        self.add_line('e3', (37, 40), (41, 40))
        self.add_line('e4', (7, 40), (15, 39))
        self.add_line('e5-1', (41, 40), (44, 38))
        self.add_line('e5-2', (44, 38), (44, 35))
        self.add_line('e5-3', (44, 35), (43, 30))
        self.add_arc('e5-4', (43, 30), (38, 25), radius_x=10, sweep=False)
        self.add_arc('e5-5', (38, 25), (20, 23), radius_x=47, sweep=False)
        self.add_arc('e5-6', (20, 23), (7, 27), radius_x=21, sweep=False)
        self.add_arc('e5-7', (7, 27), (5, 30), radius_x=9, sweep=False)
        self.add_line('e5-8', (5, 30), (4, 37))
        self.add_arc('e5-9', (4, 37), (7, 40), radius_x=3, sweep=False)
        self.add_arc('e6-1', (15, 39), (17, 33), radius_x=7, sweep=False)
        self.add_arc('e6-2', (17, 33), (31, 33), radius_x=56)
        self.add_arc('e6-3', (31, 33), (33, 39), radius_x=9, sweep=False)
        self.add_line('e6-4', (33, 39), (37, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', 'e5-8', 'e5-9', 'e4', 'e6-1', 'e6-2', 'e6-3', 'e6-4', closed=True)
