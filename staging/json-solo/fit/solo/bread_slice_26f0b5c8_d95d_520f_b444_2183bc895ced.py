"""Bread slice (food), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '26f0b5c8-d95d-520f-b444-2183bc895ced'
SOURCE_PATH = 'icons-json/food/bread slice_26f0b5c8-d95d-520f-b444-2183bc895ced.json'
AUTHOR = 'json_to_solo'

class BreadSlice26f0b5c8(Solo48):
    icon_id = 'bread-slice-26f0b5c8'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('bread', 'slice', 'food')

    def build(self):
        self.add_line('e0', (40, 21), (40, 38))
        self.add_line('e1', (35, 42), (13, 42))
        self.add_line('e2', (9, 38), (9, 22))
        self.add_arc('e3-1', (40, 38), (36, 42), radius_x=5)
        self.add_line('e3-2', (36, 42), (35, 42))
        self.add_arc('e4', (13, 42), (9, 38), radius_x=4)
        self.add_line('e5-1', (9, 22), (6, 15))
        self.add_arc('e5-2', (6, 15), (9, 10), radius_x=8)
        self.add_arc('e5-3', (9, 10), (16, 7), radius_x=18)
        self.add_arc('e5-4', (16, 7), (24, 6), radius_x=33)
        self.add_line('e5-5', (24, 6), (32, 7))
        self.add_arc('e5-6', (32, 7), (39, 10), radius_x=20)
        self.add_arc('e5-7', (39, 10), (42, 15), radius_x=6)
        self.add_line('e5-8', (42, 15), (40, 21))
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e1', 'e4', 'e2', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', 'e5-8', closed=True)
