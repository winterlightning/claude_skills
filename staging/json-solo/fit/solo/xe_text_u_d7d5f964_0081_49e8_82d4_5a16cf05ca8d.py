"""Xe (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd7d5f964-0081-49e8-82d4-5a16cf05ca8d'
SOURCE_PATH = 'icons-json/symbol/xe (text u)_d7d5f964-0081-49e8-82d4-5a16cf05ca8d.json'
AUTHOR = 'json_to_solo'

class XeTextUSymbol(Solo48):
    icon_id = 'xe-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('xe', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (23, 27))
        self.add_line('e1', (8, 27), (23, 4))
        self.add_line('e2', (8, 44), (40, 44))
        self.add_arc('e3-1', (31, 19), (40, 17), radius_x=6, sweep=False)
        self.add_arc('e3-2', (40, 17), (33, 13), radius_x=5, sweep=False)
        self.add_arc('e3-3', (33, 13), (32, 25), radius_x=9, sweep=False)
        self.add_arc('e3-4', (32, 25), (40, 23), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e3-1', 'e3-2', 'e3-3', 'e3-4')
        self.add_contour('c3', 'e2')
