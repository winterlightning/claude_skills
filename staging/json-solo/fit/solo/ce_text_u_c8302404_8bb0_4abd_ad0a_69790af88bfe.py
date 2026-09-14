"""Ce (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8302404-8bb0-4abd-ad0a-69790af88bfe'
SOURCE_PATH = 'icons-json/symbol/ce (text u)_c8302404-8bb0-4abd-ad0a-69790af88bfe.json'
AUTHOR = 'json_to_solo'

class CeTextUSymbol(Solo48):
    icon_id = 'ce-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('ce', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 9), (8, 21))
        self.add_line('e1', (8, 44), (40, 44))
        self.add_arc('e2-1', (19, 8), (14, 4), radius_x=6, sweep=False)
        self.add_arc('e2-2', (14, 4), (13, 4), radius_x=11)
        self.add_arc('e2-3', (13, 4), (8, 9), radius_x=5, sweep=False)
        self.add_arc('e3-1', (8, 21), (11, 26), radius_x=6, sweep=False)
        self.add_arc('e3-2', (11, 26), (20, 23), radius_x=7, sweep=False)
        self.add_arc('e4-1', (29, 19), (40, 17), radius_x=8, sweep=False)
        self.add_arc('e4-2', (40, 17), (30, 14), radius_x=6, sweep=False)
        self.add_arc('e4-3', (30, 14), (32, 26), radius_x=9, sweep=False)
        self.add_arc('e4-4', (32, 26), (40, 23), radius_x=6, sweep=False)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e0', 'e3-1', 'e3-2')
        self.add_contour('c1', 'e4-1', 'e4-2', 'e4-3', 'e4-4')
        self.add_contour('c2', 'e1')
