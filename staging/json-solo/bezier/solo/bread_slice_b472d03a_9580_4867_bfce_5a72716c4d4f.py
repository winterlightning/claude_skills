"""Bread slice (food), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b472d03a-9580-4867-bfce-5a72716c4d4f'
SOURCE_PATH = 'icons-json/food/bread slice_b472d03a-9580-4867-bfce-5a72716c4d4f.json'
AUTHOR = 'json_to_solo'

class BreadSliceB472d03a(Solo48):
    icon_id = 'bread-slice-b472d03a'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('bread', 'slice', 'food')

    def build(self):
        self.add_line('sym-e0', (24, 42), (13, 42))
        self.add_bezier('sym-e1', (13, 42), ((12.951, 41.992), (12.049, 42), (12, 42)))
        self.add_bezier('sym-e2', (12, 42), ((10.405, 42), (9.466, 40.227), (9, 39)))
        self.add_line('sym-e3', (9, 39), (9, 19))
        self.add_bezier('sym-e4', (9, 19), ((8.82, 18.624), (9.254, 18.344), (9, 18)))
        self.add_bezier('sym-e5', (9, 18), ((8.689, 17.566), (8.376, 17.376), (8, 17)))
        self.add_bezier('sym-e6', (8, 17), ((7.157, 16.149), (6, 15.227), (6, 14)))
        self.add_bezier('sym-e7', (6, 14), ((6, 13.926), (6, 13.074), (6, 13)))
        self.add_bezier('sym-e8', (6, 13), ((6, 12.926), (6, 13.074), (6, 13)))
        self.add_bezier('sym-e9', (6, 13), ((6, 10.873), (8.274, 8.941), (10, 8)))
        self.add_bezier('sym-e10', (10, 8), ((13.305, 6.192), (18.228, 6), (22, 6)))
        self.add_bezier('sym-e11', (22, 6), ((22.098, 6), (21.902, 6), (22, 6)))
        self.add_line('sym-e12', (22, 6), (24, 6))
        self.add_line('sym-e13', (24, 6), (26, 6))
        self.add_bezier('sym-e14', (26, 6), ((26.098, 6), (25.902, 6), (26, 6)))
        self.add_bezier('sym-e15', (26, 6), ((29.772, 6), (34.695, 6.192), (38, 8)))
        self.add_bezier('sym-e16', (38, 8), ((39.726, 8.941), (42, 10.873), (42, 13)))
        self.add_bezier('sym-e17', (42, 13), ((42, 13.074), (42, 12.926), (42, 13)))
        self.add_bezier('sym-e18', (42, 13), ((42, 13.074), (42, 13.926), (42, 14)))
        self.add_bezier('sym-e19', (42, 14), ((42, 15.227), (40.843, 16.149), (40, 17)))
        self.add_bezier('sym-e20', (40, 17), ((39.624, 17.376), (39.311, 17.566), (39, 18)))
        self.add_bezier('sym-e21', (39, 18), ((38.746, 18.344), (39.18, 18.624), (39, 19)))
        self.add_line('sym-e22', (39, 19), (39, 39))
        self.add_bezier('sym-e23', (39, 39), ((38.534, 40.227), (37.595, 42), (36, 42)))
        self.add_bezier('sym-e24', (36, 42), ((35.951, 42), (35.049, 41.992), (35, 42)))
        self.add_line('sym-e25', (35, 42), (24, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
