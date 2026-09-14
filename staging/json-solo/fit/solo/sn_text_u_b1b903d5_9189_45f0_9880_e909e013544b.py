"""Sn (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b1b903d5-9189-45f0-9880-e909e013544b'
SOURCE_PATH = 'icons-json/symbol/sn (text u)_b1b903d5-9189-45f0-9880-e909e013544b.json'
AUTHOR = 'json_to_solo'

class SnTextUSymbol(Solo48):
    icon_id = 'sn-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('sn', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (16, 16), (12, 14))
        self.add_line('e1', (30, 12), (30, 27))
        self.add_line('e2', (40, 17), (40, 27))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_arc('e4-1', (8, 23), (19, 25), radius_x=8, sweep=False)
        self.add_arc('e4-2', (19, 25), (16, 16), radius_x=5, sweep=False)
        self.add_arc('e5-1', (12, 14), (9, 11), radius_x=8)
        self.add_arc('e5-2', (9, 11), (14, 4), radius_x=6)
        self.add_arc('e5-3', (14, 4), (20, 7), radius_x=9)
        self.add_arc('e6-1', (30, 16), (38, 13), radius_x=6)
        self.add_line('e6-2', (38, 13), (40, 17))
        self.add_contour('c0', 'e4-1', 'e4-2', 'e0', 'e5-1', 'e5-2', 'e5-3')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e6-1', 'e6-2', 'e2')
        self.add_contour('c3', 'e3')
        self.relate('connect', 'c2', 'c1')
