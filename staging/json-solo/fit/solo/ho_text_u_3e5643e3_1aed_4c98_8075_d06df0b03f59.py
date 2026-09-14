"""Ho (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e5643e3-1aed-4c98-8075-d06df0b03f59'
SOURCE_PATH = 'icons-json/symbol/ho (text u)_3e5643e3-1aed-4c98-8075-d06df0b03f59.json'
AUTHOR = 'json_to_solo'

class HoTextUSymbol(Solo48):
    icon_id = 'ho-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('ho', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (8, 27))
        self.add_line('e1', (21, 15), (8, 15))
        self.add_line('e2', (21, 27), (21, 4))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_arc('e4-1', (32, 12), (30, 23), radius_x=9, sweep=False)
        self.add_arc('e4-2', (30, 23), (37, 26), radius_x=5, sweep=False)
        self.add_arc('e4-3', (37, 26), (39, 24), radius_x=6, sweep=False)
        self.add_line('e4-4', (39, 24), (40, 19))
        self.add_arc('e4-5', (40, 19), (39, 15), radius_x=9, sweep=False)
        self.add_arc('e4-6', (39, 15), (32, 12), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', closed=True)
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c0')
