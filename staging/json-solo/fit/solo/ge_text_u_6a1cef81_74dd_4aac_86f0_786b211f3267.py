"""Ge (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a1cef81-74dd-4aac-86f0-786b211f3267'
SOURCE_PATH = 'icons-json/symbol/ge (text u)_6a1cef81-74dd-4aac-86f0-786b211f3267.json'
AUTHOR = 'json_to_solo'

class GeTextUSymbol(Solo48):
    icon_id = 'ge-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('ge', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (21, 19), (21, 16))
        self.add_line('e1', (21, 16), (16, 16))
        self.add_line('e2', (8, 44), (40, 44))
        self.add_arc('e3-1', (21, 8), (16, 4), radius_x=6, sweep=False)
        self.add_line('e3-2', (16, 4), (12, 5))
        self.add_arc('e3-3', (12, 5), (9, 9), radius_x=7, sweep=False)
        self.add_line('e3-4', (9, 9), (8, 16))
        self.add_line('e3-5', (8, 16), (9, 22))
        self.add_arc('e3-6', (9, 22), (13, 26), radius_x=6, sweep=False)
        self.add_arc('e3-7', (13, 26), (21, 19), radius_x=6, sweep=False)
        self.add_arc('e4-1', (30, 19), (40, 17), radius_x=7, sweep=False)
        self.add_arc('e4-2', (40, 17), (30, 17), radius_x=5, sweep=False)
        self.add_arc('e4-3', (30, 17), (33, 26), radius_x=8, sweep=False)
        self.add_arc('e4-4', (33, 26), (40, 23), radius_x=5, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e0', 'e1')
        self.add_contour('c1', 'e4-1', 'e4-2', 'e4-3', 'e4-4')
        self.add_contour('c2', 'e2')
