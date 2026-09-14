"""Sr (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ae3aaea-c96d-4420-a757-abdfc64cfd21'
SOURCE_PATH = 'icons-json/symbol/sr (text u)_2ae3aaea-c96d-4420-a757-abdfc64cfd21.json'
AUTHOR = 'json_to_solo'

class SrTextU(Solo48):
    icon_id = 'sr-text-u'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('sr', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (16, 16), (12, 14))
        self.add_line('e1', (31, 13), (31, 27))
        self.add_line('e2', (8, 44), (40, 44))
        self.add_arc('e3-1', (8, 23), (18, 26), radius_x=9, sweep=False)
        self.add_arc('e3-2', (18, 26), (21, 19), radius_x=5, sweep=False)
        self.add_arc('e3-3', (21, 19), (16, 16), radius_x=10, sweep=False)
        self.add_arc('e4-1', (12, 14), (9, 7), radius_x=5)
        self.add_arc('e4-2', (9, 7), (11, 5), radius_x=5)
        self.add_line('e4-3', (11, 5), (15, 4))
        self.add_arc('e4-4', (15, 4), (21, 7), radius_x=9)
        self.add_arc('e5', (40, 13), (31, 17), radius_x=6, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e4-4')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e5')
        self.add_contour('c3', 'e2')
        self.relate('connect', 'c2', 'c1')
