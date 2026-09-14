"""Batch-01/laptop (computers), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '96bd0a70-5265-56a5-8f8c-7df6339b6c49'
SOURCE_PATH = 'icons-json/computers/batch-01/laptop_96bd0a70-5265-56a5-8f8c-7df6339b6c49.json'
AUTHOR = 'json_to_solo'

class Batch01Laptop(Solo48):
    icon_id = 'batch-01-laptop'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ()
    keywords = ('batch', 'laptop', 'computers')

    def build(self):
        self.add_line('sym-e0', (41, 32), (7, 32))
        self.add_bezier('sym-e1', (7, 32), ((6.391, 33.09), (4, 36.97), (4, 38)))
        self.add_bezier('sym-e2', (4, 38), ((4, 38.07), (4, 37.93), (4, 38)))
        self.add_bezier('sym-e3', (4, 38), ((4, 39), (5.218, 40), (6, 40)))
        self.add_line('sym-e4', (6, 40), (24, 40))
        self.add_line('sym-e5', (24, 40), (42, 40))
        self.add_bezier('sym-e6', (42, 40), ((42.782, 40), (44, 39), (44, 38)))
        self.add_bezier('sym-e7', (44, 38), ((44, 37.93), (44, 38.07), (44, 38)))
        self.add_bezier('sym-e8', (44, 38), ((44, 36.97), (41.609, 33.09), (41, 32)))
        self.add_line('sym-e9', (41, 32), (41, 11))
        self.add_bezier('sym-e10', (41, 11), ((41, 9.58), (40.427, 8), (39, 8)))
        self.add_bezier('sym-e11', (39, 8), ((38.864, 8), (39.145, 8), (39, 8)))
        self.add_line('sym-e12', (39, 8), (24, 8))
        self.add_line('sym-e13', (24, 8), (9, 8))
        self.add_bezier('sym-e14', (9, 8), ((8.855, 8), (9.136, 8), (9, 8)))
        self.add_bezier('sym-e15', (9, 8), ((7.573, 8), (7, 9.58), (7, 11)))
        self.add_line('sym-e16', (7, 11), (7, 32))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16')
