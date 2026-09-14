"""Cu (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd2287aae-54a7-4e4c-9033-5df0a68ec4c5'
SOURCE_PATH = 'icons-json/symbol/cu (text u)_d2287aae-54a7-4e4c-9033-5df0a68ec4c5.json'
AUTHOR = 'json_to_solo'

class CuTextUSymbol(Solo48):
    icon_id = 'cu-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('cu', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 9), (8, 21))
        self.add_line('e1', (29, 12), (29, 22))
        self.add_line('e2', (40, 12), (40, 27))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_arc('e4-1', (20, 8), (14, 4), radius_x=7, sweep=False)
        self.add_arc('e4-2', (14, 4), (11, 5), radius_x=6, sweep=False)
        self.add_arc('e4-3', (11, 5), (8, 9), radius_x=5, sweep=False)
        self.add_arc('e5-1', (8, 21), (12, 26), radius_x=6, sweep=False)
        self.add_arc('e5-2', (12, 26), (20, 23), radius_x=6, sweep=False)
        self.add_arc('e6-1', (29, 22), (36, 26), radius_x=5, sweep=False)
        self.add_arc('e6-2', (36, 26), (40, 22), radius_x=4, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e0', 'e5-1', 'e5-2')
        self.add_contour('c1', 'e1', 'e6-1', 'e6-2')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.relate('connect', 'c1', 'c2')
