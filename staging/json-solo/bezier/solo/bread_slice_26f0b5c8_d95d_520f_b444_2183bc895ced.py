"""Bread slice (food), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e3', (40, 38), ((40, 39.726), (37.68, 41.984), (35.847, 41.984)), ((35.782, 41.992), (35.716, 41.992), (35.651, 42)), ((35.585, 42), (35.065, 42), (35, 42)))
        self.add_bezier('e4', (13, 42), ((10.766, 42), (9, 39.955), (9, 38)))
        self.add_bezier('e5', (9, 22), ((9, 20.928), (8.168, 19.852), (7.538, 19.14)), ((6.671, 18.166), (6.008, 16.743), (6.008, 15.417)), ((6.008, 15.361), (6, 15.305), (6, 15.248)), ((6, 15.247), (6, 15.246), (6, 15.245)), ((6, 12.955), (7.71, 10.934), (9.477, 9.682)), ((13.028, 7.178), (18.886, 6.016), (23.174, 6.016)), ((23.504, 6.016), (23.826, 6), (24.156, 6)), ((24.161, 6), (24.167, 6), (24.172, 6)), ((24.507, 6), (24.835, 6.016), (25.17, 6.016)), ((29.482, 6.016), (34.743, 7.137), (38.367, 9.543)), ((40.184, 10.745), (41.992, 12.783), (41.992, 15.098)), ((42, 15.219), (42, 15.332), (42, 15.445)), ((42, 15.446), (42, 15.448), (42, 15.45)), ((42, 15.712), (41.984, 15.965), (41.984, 16.219)), ((41.984, 18.183), (40.933, 19.478), (40, 21)))
        self.add_contour('c0', 'e0', 'e3', 'e1', 'e4', 'e2', 'e5', closed=True)
