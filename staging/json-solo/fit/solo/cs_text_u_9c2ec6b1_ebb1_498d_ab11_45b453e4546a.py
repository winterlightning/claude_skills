"""Cs (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c2ec6b1-ebb1-498d-ab11-45b453e4546a'
SOURCE_PATH = 'icons-json/symbol/cs (text u)_9c2ec6b1-ebb1-498d-ab11-45b453e4546a.json'
AUTHOR = 'json_to_solo'

class CsTextUSymbol(Solo48):
    icon_id = 'cs-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('cs', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 9), (8, 21))
        self.add_line('e1', (8, 44), (40, 44))
        self.add_arc('e2-1', (21, 8), (15, 4), radius_x=7, sweep=False)
        self.add_line('e2-2', (15, 4), (11, 5))
        self.add_arc('e2-3', (11, 5), (8, 9), radius_x=5, sweep=False)
        self.add_arc('e3', (8, 21), (21, 23), radius_x=7, sweep=False)
        self.add_arc('e4-1', (40, 16), (35, 12), radius_x=5, sweep=False)
        self.add_arc('e4-2', (35, 12), (32, 18), radius_x=4, sweep=False)
        self.add_line('e4-3', (32, 18), (39, 21))
        self.add_arc('e4-4', (39, 21), (40, 23), radius_x=3)
        self.add_line('e4-5', (40, 23), (38, 26))
        self.add_arc('e4-6', (38, 26), (31, 23), radius_x=5)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e0', 'e3')
        self.add_contour('c1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6')
        self.add_contour('c2', 'e1')
