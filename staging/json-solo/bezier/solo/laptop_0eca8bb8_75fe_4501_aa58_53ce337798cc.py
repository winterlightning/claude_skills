"""Batch-01/laptop (computers), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0eca8bb8-75fe-4501-aa58-53ce337798cc'
SOURCE_PATH = 'icons-json/computers/batch-01/laptop_0eca8bb8-75fe-4501-aa58-53ce337798cc.json'
AUTHOR = 'json_to_solo'

class Batch01Laptop0eca8bb8(Solo48):
    icon_id = 'batch-01-laptop-0eca8bb8'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ()
    keywords = ('batch', 'laptop', 'computers')

    def build(self):
        self.add_line('sym-e0', (7, 32), (41, 32))
        self.add_bezier('sym-e1', (41, 32), ((41.991, 33.56), (42.291, 34.46), (43, 36)))
        self.add_bezier('sym-e2', (43, 36), ((43.245, 36.53), (44, 37.37), (44, 38)))
        self.add_bezier('sym-e3', (44, 38), ((44, 38.03), (44, 37.97), (44, 38)))
        self.add_bezier('sym-e4', (44, 38), ((44, 38.03), (44, 37.97), (44, 38)))
        self.add_bezier('sym-e5', (44, 38), ((44, 38.75), (42.473, 39.74), (42, 40)))
        self.add_line('sym-e6', (42, 40), (24, 40))
        self.add_line('sym-e7', (24, 40), (6, 40))
        self.add_bezier('sym-e8', (6, 40), ((5.527, 39.74), (4, 38.75), (4, 38)))
        self.add_bezier('sym-e9', (4, 38), ((4, 37.97), (4, 38.03), (4, 38)))
        self.add_bezier('sym-e10', (4, 38), ((4, 37.97), (4, 38.03), (4, 38)))
        self.add_bezier('sym-e11', (4, 38), ((4, 37.37), (4.755, 36.53), (5, 36)))
        self.add_bezier('sym-e12', (5, 36), ((5.709, 34.46), (6.009, 33.56), (7, 32)))
        self.add_line('sym-e13', (7, 32), (7, 10))
        self.add_bezier('sym-e14', (7, 10), ((7.573, 8.81), (7.927, 8.61), (9, 8)))
        self.add_line('sym-e15', (9, 8), (24, 8))
        self.add_line('sym-e16', (24, 8), (39, 8))
        self.add_bezier('sym-e17', (39, 8), ((40.073, 8.61), (40.427, 8.81), (41, 10)))
        self.add_line('sym-e18', (41, 10), (41, 32))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18')
