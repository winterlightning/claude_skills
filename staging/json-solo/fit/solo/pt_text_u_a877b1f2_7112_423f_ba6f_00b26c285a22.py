"""Pt (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a877b1f2-7112-423f-ba6f-00b26c285a22'
SOURCE_PATH = 'icons-json/symbol/pt (text u)_a877b1f2-7112-423f-ba6f-00b26c285a22.json'
AUTHOR = 'json_to_solo'

class PtTextUSymbol(Solo48):
    icon_id = 'pt-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('pt', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 16), (15, 16))
        self.add_line('e1', (15, 4), (8, 4))
        self.add_line('e2', (8, 4), (8, 27))
        self.add_line('e3', (34, 4), (34, 20))
        self.add_line('e4', (30, 10), (38, 10))
        self.add_line('e5', (8, 44), (40, 44))
        self.add_arc('e6', (15, 16), (15, 4), radius_x=6, sweep=False)
        self.add_arc('e7-1', (34, 20), (36, 26), radius_x=7, sweep=False)
        self.add_arc('e7-2', (36, 26), (40, 27), radius_x=6, sweep=False)
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e2')
        self.add_contour('c1', 'e3', 'e7-1', 'e7-2')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
