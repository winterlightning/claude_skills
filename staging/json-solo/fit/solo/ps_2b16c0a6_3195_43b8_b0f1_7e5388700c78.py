"""Ps (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2b16c0a6-3195-43b8-b0f1-7e5388700c78'
SOURCE_PATH = 'icons-json/symbol/Ps_2b16c0a6-3195-43b8-b0f1-7e5388700c78.json'
AUTHOR = 'json_to_solo'

class PsSymbol(Solo48):
    icon_id = 'ps-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('ps', 'symbol')

    def build(self):
        self.add_line('e0', (4, 25), (15, 25))
        self.add_line('e1', (15, 8), (4, 8))
        self.add_line('e2', (4, 8), (4, 40))
        self.add_arc('e3-1', (15, 25), (23, 16), radius_x=9, sweep=False)
        self.add_arc('e3-2', (23, 16), (15, 8), radius_x=9, sweep=False)
        self.add_arc('e4-1', (44, 25), (34, 21), radius_x=6, sweep=False)
        self.add_arc('e4-2', (34, 21), (33, 27), radius_x=5, sweep=False)
        self.add_arc('e4-3', (33, 27), (42, 32), radius_x=18, sweep=False)
        self.add_arc('e4-4', (42, 32), (44, 35), radius_x=4)
        self.add_arc('e4-5', (44, 35), (42, 39), radius_x=5)
        self.add_line('e4-6', (42, 39), (38, 40))
        self.add_line('e4-7', (38, 40), (34, 39))
        self.add_line('e4-8', (34, 39), (33, 36))
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e1', 'e2')
        self.add_contour('c1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7', 'e4-8')
