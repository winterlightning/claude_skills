"""Dollar (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c47b147-c2f7-4c49-8513-824a167aa784'
SOURCE_PATH = 'icons-json/symbol/dollar_2c47b147-c2f7-4c49-8513-824a167aa784.json'
AUTHOR = 'json_to_solo'

class DollarSymbol(Solo48):
    icon_id = 'dollar-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('dollar', 'symbol')

    def build(self):
        self.add_line('e0', (29, 25), (21, 24))
        self.add_line('e1', (24, 8), (24, 4))
        self.add_line('e2', (24, 44), (24, 8))
        self.add_arc('e3-1', (8, 33), (24, 41), radius_x=18, sweep=False)
        self.add_arc('e3-2', (24, 41), (35, 38), radius_x=26, sweep=False)
        self.add_arc('e3-3', (35, 38), (40, 32), radius_x=7, sweep=False)
        self.add_arc('e3-4', (40, 32), (29, 25), radius_x=10, sweep=False)
        self.add_arc('e4-1', (21, 24), (11, 21), radius_x=26)
        self.add_arc('e4-2', (11, 21), (8, 17), radius_x=5)
        self.add_line('e4-3', (8, 17), (8, 16))
        self.add_arc('e4-4', (8, 16), (24, 8), radius_x=16)
        self.add_arc('e5', (24, 8), (38, 16), radius_x=14)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e1')
        self.add_contour('c1', 'e2', 'e5')
