"""Symbol armor (war), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '874f7bd6-cdff-431b-9907-a5c3452b8113'
SOURCE_PATH = 'icons-json/war/symbol armor_874f7bd6-cdff-431b-9907-a5c3452b8113.json'
AUTHOR = 'json_to_solo'

class SymbolArmorWar(Solo48):
    icon_id = 'symbol-armor-war'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('symbol', 'armor', 'war')

    def build(self):
        self.add_line('e0', (44, 14), (32, 14))
        self.add_line('e1', (10, 40), (37, 40))
        self.add_line('e2', (13, 22), (34, 22))
        self.add_line('e3', (13, 22), (15, 12))
        self.add_line('e4', (18, 8), (29, 8))
        self.add_line('e5', (32, 12), (32, 14))
        self.add_line('e6', (34, 22), (32, 14))
        self.add_arc('e7-1', (13, 22), (8, 22), radius_x=13, sweep=False)
        self.add_arc('e7-2', (8, 22), (4, 29), radius_x=9, sweep=False)
        self.add_line('e7-3', (4, 29), (6, 36))
        self.add_arc('e7-4', (6, 36), (10, 40), radius_x=8, sweep=False)
        self.add_arc('e8-1', (37, 40), (43, 28), radius_x=12, sweep=False)
        self.add_arc('e8-2', (43, 28), (34, 22), radius_x=7, sweep=False)
        self.add_arc('e9', (15, 12), (18, 8), radius_x=4)
        self.add_arc('e10', (29, 8), (32, 12), radius_x=4)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e1', 'e8-1', 'e8-2')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e9', 'e4', 'e10', 'e5')
        self.add_contour('c4', 'e6')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
