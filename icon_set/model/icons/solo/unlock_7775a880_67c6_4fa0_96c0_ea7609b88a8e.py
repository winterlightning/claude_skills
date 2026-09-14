"""Unlock (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7775a880-67c6-4fa0-96c0-ea7609b88a8e'
SOURCE_PATH = 'icons-json/symbol/unlock_7775a880-67c6-4fa0-96c0-ea7609b88a8e.json'
AUTHOR = 'json_to_solo'

class UnlockSymbol(Solo48):
    icon_id = 'unlock-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('unlock', 'symbol')

    def build(self):
        self.add_line('e0', (27, 14), (27, 22))
        self.add_line('e1', (17, 25), (17, 39))
        self.add_line('e2', (22, 44), (36, 44))
        self.add_line('e3', (40, 40), (40, 25))
        self.add_line('e4', (37, 22), (21, 22))
        self.add_line('e5-1', (8, 19), (8, 13))
        self.add_arc('e5-2', (8, 13), (13, 5), radius_x=11)
        self.add_line('e5-3', (13, 5), (17, 4))
        self.add_arc('e5-4', (17, 4), (27, 14), radius_x=10)
        self.add_arc('e6', (21, 22), (17, 25), radius_x=4, sweep=False)
        self.add_arc('e7', (17, 39), (22, 44), radius_x=5, sweep=False)
        self.add_arc('e8', (36, 44), (40, 40), radius_x=4, sweep=False)
        self.add_arc('e9', (40, 25), (37, 22), radius_x=3, sweep=False)
        self.add_contour('c0', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e0')
        self.add_contour('c1', 'e6', 'e1', 'e7', 'e2', 'e8', 'e3', 'e9', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
