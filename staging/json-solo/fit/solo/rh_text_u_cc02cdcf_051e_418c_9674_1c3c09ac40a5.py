"""Rh (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc02cdcf-051e-418c-9674-1c3c09ac40a5'
SOURCE_PATH = 'icons-json/symbol/rh (text u)_cc02cdcf-051e-418c-9674-1c3c09ac40a5.json'
AUTHOR = 'json_to_solo'

class RhTextUSymbol(Solo48):
    icon_id = 'rh-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('rh', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 16), (16, 16))
        self.add_line('e1', (16, 4), (9, 4))
        self.add_line('e2', (8, 5), (8, 27))
        self.add_line('e3', (21, 27), (16, 16))
        self.add_line('e4', (30, 4), (30, 27))
        self.add_line('e5', (40, 19), (40, 27))
        self.add_line('e6', (8, 44), (40, 44))
        self.add_arc('e7-1', (16, 16), (21, 12), radius_x=5, sweep=False)
        self.add_arc('e7-2', (21, 12), (16, 4), radius_x=6, sweep=False)
        self.add_arc('e8', (9, 4), (8, 5), radius_x=1, sweep=False)
        self.add_arc('e9-1', (30, 15), (37, 12), radius_x=5)
        self.add_arc('e9-2', (37, 12), (39, 14), radius_x=4)
        self.add_line('e9-3', (39, 14), (40, 18))
        self.add_line('e9-4', (40, 18), (40, 19))
        self.add_contour('c0', 'e0', 'e7-1', 'e7-2', 'e1', 'e8', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e9-1', 'e9-2', 'e9-3', 'e9-4', 'e5')
        self.add_contour('c4', 'e6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c2')
