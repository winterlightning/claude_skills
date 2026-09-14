"""Honeycomb (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f0c353b7-a354-469a-90f8-2f8b8d4edac1'
SOURCE_PATH = 'icons-json/symbol/honeycomb_f0c353b7-a354-469a-90f8-2f8b8d4edac1.json'
AUTHOR = 'json_to_solo'

class Honeycomb(Solo48):
    icon_id = 'honeycomb'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('honeycomb', 'symbol')

    def build(self):
        self.add_line('e0', (33, 22), (42, 26))
        self.add_line('e1', (42, 26), (42, 37))
        self.add_line('e2', (42, 37), (33, 42))
        self.add_line('e3', (33, 42), (24, 37))
        self.add_line('e4', (33, 22), (24, 26))
        self.add_line('e5', (33, 22), (33, 11))
        self.add_line('e6', (33, 11), (24, 6))
        self.add_line('e7', (24, 6), (15, 11))
        self.add_line('e8', (15, 11), (15, 22))
        self.add_line('e9', (24, 37), (24, 26))
        self.add_line('e10', (24, 37), (15, 42))
        self.add_line('e11', (11, 40), (6, 37))
        self.add_line('e12', (6, 37), (6, 26))
        self.add_line('e13', (6, 26), (15, 22))
        self.add_line('e14', (24, 26), (15, 22))
        self.add_arc('e15', (15, 42), (11, 40), radius_x=8)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e5', 'e6', 'e7', 'e8')
        self.add_contour('c3', 'e9')
        self.add_contour('c4', 'e10', 'e15', 'e11', 'e12', 'e13')
        self.add_contour('c5', 'e14')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
