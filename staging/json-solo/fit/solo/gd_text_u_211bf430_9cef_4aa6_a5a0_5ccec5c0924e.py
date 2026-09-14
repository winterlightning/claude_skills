"""Gd (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '211bf430-9cef-4aa6-a5a0-5ccec5c0924e'
SOURCE_PATH = 'icons-json/symbol/gd (text u)_211bf430-9cef-4aa6-a5a0-5ccec5c0924e.json'
AUTHOR = 'json_to_solo'

class GdTextUSymbol(Solo48):
    icon_id = 'gd-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('gd', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (21, 19), (21, 16))
        self.add_line('e1', (21, 16), (16, 16))
        self.add_line('e2', (40, 4), (40, 23))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_line('e4-1', (21, 8), (19, 5))
        self.add_line('e4-2', (19, 5), (15, 4))
        self.add_arc('e4-3', (15, 4), (9, 8), radius_x=7, sweep=False)
        self.add_line('e4-4', (9, 8), (8, 16))
        self.add_line('e4-5', (8, 16), (10, 24))
        self.add_arc('e4-6', (10, 24), (13, 26), radius_x=6, sweep=False)
        self.add_arc('e4-7', (13, 26), (21, 19), radius_x=6, sweep=False)
        self.add_arc('e5-1', (40, 23), (33, 26), radius_x=5)
        self.add_arc('e5-2', (33, 26), (29, 19), radius_x=7)
        self.add_arc('e5-3', (29, 19), (33, 12), radius_x=8)
        self.add_arc('e5-4', (33, 12), (40, 14), radius_x=6)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e5-1', 'e5-2', 'e5-3', 'e5-4')
        self.add_contour('c2', 'e3')
