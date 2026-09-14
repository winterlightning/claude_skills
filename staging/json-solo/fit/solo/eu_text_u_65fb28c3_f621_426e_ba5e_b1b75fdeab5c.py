"""Eu (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65fb28c3-f621-426e-ba5e-b1b75fdeab5c'
SOURCE_PATH = 'icons-json/symbol/eu (text u)_65fb28c3-f621-426e-ba5e-b1b75fdeab5c.json'
AUTHOR = 'json_to_solo'

class EuTextUSymbol(Solo48):
    icon_id = 'eu-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('eu', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (21, 4), (9, 4))
        self.add_line('e1', (8, 5), (8, 26))
        self.add_line('e2', (9, 27), (21, 27))
        self.add_line('e3', (18, 15), (8, 15))
        self.add_line('e4', (30, 12), (30, 22))
        self.add_line('e5', (40, 12), (40, 27))
        self.add_line('e6', (8, 44), (40, 44))
        self.add_arc('e7', (9, 4), (8, 5), radius_x=1, sweep=False)
        self.add_line('e8', (8, 26), (9, 27))
        self.add_arc('e9', (30, 22), (40, 22), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e9')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c3')
