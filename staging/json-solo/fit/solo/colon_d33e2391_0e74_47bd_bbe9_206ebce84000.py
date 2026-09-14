"""Colon (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd33e2391-0e74-47bd-bbe9-206ebce84000'
SOURCE_PATH = 'icons-json/money/colon_d33e2391-0e74-47bd-bbe9-206ebce84000.json'
AUTHOR = 'json_to_solo'

class ColonMoney(Solo48):
    icon_id = 'colon-money'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('colon', 'money')

    def build(self):
        self.add_arc('e0-1', (31, 25), (36, 36), radius_x=9)
        self.add_arc('e0-2', (36, 36), (23, 44), radius_x=15)
        self.add_arc('e0-3', (23, 44), (15, 42), radius_x=22)
        self.add_line('e1', (33, 5), (32, 5))
        self.add_line('e2-1', (15, 42), (37, 18))
        self.add_arc('e2-2', (37, 18), (40, 12), radius_x=9, sweep=False)
        self.add_arc('e2-3', (40, 12), (32, 5), radius_x=8, sweep=False)
        self.add_arc('e3-1', (15, 42), (8, 34), radius_x=9)
        self.add_arc('e3-2', (8, 34), (15, 22), radius_x=16)
        self.add_line('e4', (32, 5), (15, 22))
        self.add_arc('e5-1', (32, 5), (26, 4), radius_x=24, sweep=False)
        self.add_arc('e5-2', (26, 4), (14, 8), radius_x=20, sweep=False)
        self.add_arc('e5-3', (14, 8), (15, 22), radius_x=8, sweep=False)
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2-1', 'e2-2', 'e2-3')
        self.add_contour('c3', 'e3-1', 'e3-2')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5-1', 'e5-2', 'e5-3')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
