"""Bread slice (food), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b472d03a-9580-4867-bfce-5a72716c4d4f'
SOURCE_PATH = 'icons-json/food/bread slice_b472d03a-9580-4867-bfce-5a72716c4d4f.json'
AUTHOR = 'json_to_solo'

class BreadSliceFood(Solo48):
    icon_id = 'bread-slice-food'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('bread', 'slice', 'food')

    def build(self):
        self.add_line('sym-e0', (24, 42), (13, 42))
        self.add_arc('sym-e1', (13, 42), (12, 42), radius_x=1, sweep=False)
        self.add_line('sym-e2', (12, 42), (9, 39))
        self.add_line('sym-e3', (9, 39), (9, 19))
        self.add_line('sym-e4', (9, 19), (9, 18))
        self.add_arc('sym-e5', (9, 18), (8, 17), radius_x=7)
        self.add_line('sym-e6', (8, 17), (6, 14))
        self.add_line('sym-e7', (6, 14), (6, 13))
        self.add_arc('sym-e9', (6, 13), (10, 8), radius_x=6)
        self.add_line('sym-e10', (10, 8), (22, 6))
        self.add_line('sym-e12', (22, 6), (24, 6))
        self.add_line('sym-e13', (24, 6), (26, 6))
        self.add_line('sym-e15', (26, 6), (38, 8))
        self.add_arc('sym-e16', (38, 8), (42, 13), radius_x=6)
        self.add_arc('sym-e18', (42, 13), (42, 14), radius_x=23, sweep=False)
        self.add_line('sym-e19', (42, 14), (40, 17))
        self.add_line('sym-e20', (40, 17), (39, 18))
        self.add_line('sym-e21', (39, 18), (39, 19))
        self.add_line('sym-e22', (39, 19), (39, 39))
        self.add_line('sym-e23', (39, 39), (36, 42))
        self.add_line('sym-e24', (36, 42), (35, 42))
        self.add_line('sym-e25', (35, 42), (24, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e10', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
