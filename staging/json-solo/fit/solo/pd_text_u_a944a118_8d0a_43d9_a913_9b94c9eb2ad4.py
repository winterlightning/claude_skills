"""Pd (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a944a118-8d0a-43d9-a913-9b94c9eb2ad4'
SOURCE_PATH = 'icons-json/symbol/pd (text u)_a944a118-8d0a-43d9-a913-9b94c9eb2ad4.json'
AUTHOR = 'json_to_solo'

class PdTextUSymbol(Solo48):
    icon_id = 'pd-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('pd', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 16), (15, 16))
        self.add_line('e1', (15, 4), (8, 4))
        self.add_line('e2', (8, 4), (8, 27))
        self.add_line('e3', (40, 4), (40, 23))
        self.add_line('e4', (8, 44), (40, 44))
        self.add_arc('e5-1', (15, 16), (20, 10), radius_x=6, sweep=False)
        self.add_arc('e5-2', (20, 10), (15, 4), radius_x=6, sweep=False)
        self.add_arc('e6-1', (40, 23), (29, 22), radius_x=6)
        self.add_arc('e6-2', (29, 22), (33, 12), radius_x=8)
        self.add_arc('e6-3', (33, 12), (40, 14), radius_x=6)
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e1', 'e2')
        self.add_contour('c1', 'e3', 'e6-1', 'e6-2', 'e6-3')
        self.add_contour('c2', 'e4')
