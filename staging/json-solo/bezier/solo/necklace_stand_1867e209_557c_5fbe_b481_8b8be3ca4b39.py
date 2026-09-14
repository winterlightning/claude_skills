"""Batch-01/necklace stand (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1867e209-557c-5fbe-b481-8b8be3ca4b39'
SOURCE_PATH = 'icons-json/accessories/batch-01/necklace stand_1867e209-557c-5fbe-b481-8b8be3ca4b39.json'
AUTHOR = 'json_to_solo'

class Batch01NecklaceStand(Solo48):
    icon_id = 'batch-01-necklace-stand'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'necklace', 'stand', 'accessories')

    def build(self):
        self.add_line('sym-e0', (11, 40), (15, 40))
        self.add_line('sym-e1', (15, 40), (33, 40))
        self.add_line('sym-e2', (33, 40), (37, 40))
        self.add_bezier('sym-e3', (24, 26), ((28.054, 26.088), (31.663, 24.378), (34, 21)))
        self.add_bezier('sym-e4', (34, 21), ((35.182, 19.307), (36.291, 17.92), (37, 16)))
        self.add_line('sym-e5', (37, 16), (34, 17))
        self.add_bezier('sym-e6', (34, 17), ((31.093, 18.793), (27.534, 20), (24, 20)))
        self.add_bezier('sym-e7', (24, 20), ((20.466, 20), (16.907, 18.793), (14, 17)))
        self.add_line('sym-e8', (14, 17), (11, 16))
        self.add_bezier('sym-e9', (11, 16), ((11.709, 17.92), (12.818, 19.307), (14, 21)))
        self.add_bezier('sym-e10', (14, 21), ((16.337, 24.378), (19.946, 26.088), (24, 26)))
        self.add_bezier('sym-e11', (33, 40), ((33.809, 36.261), (35.9, 34.425), (39, 32)))
        self.add_bezier('sym-e12', (39, 32), ((40.755, 30.636), (44, 28.392), (44, 26)))
        self.add_bezier('sym-e13', (44, 26), ((44, 25.933), (44, 26.059), (44, 26)))
        self.add_bezier('sym-e14', (44, 26), ((44, 25.933), (44, 26.067), (44, 26)))
        self.add_line('sym-e15', (44, 26), (44, 20))
        self.add_bezier('sym-e16', (44, 20), ((44, 19.68), (44, 19.32), (44, 19)))
        self.add_bezier('sym-e17', (44, 19), ((44, 15.615), (39.236, 16.682), (37, 16)))
        self.add_bezier('sym-e18', (37, 16), ((36.645, 15.806), (36.355, 15.194), (36, 15)))
        self.add_bezier('sym-e19', (36, 15), ((34.7, 14.293), (33.527, 13.331), (33, 12)))
        self.add_bezier('sym-e20', (33, 12), ((32.509, 10.754), (32.373, 8.775), (31, 8)))
        self.add_bezier('sym-e21', (31, 8), ((30.782, 8), (30.227, 8.084), (30, 8)))
        self.add_line('sym-e22', (30, 8), (25, 8))
        self.add_bezier('sym-e23', (25, 8), ((24.697, 8), (24.303, 8), (24, 8)))
        self.add_bezier('sym-e24', (24, 8), ((23.697, 8), (23.303, 8), (23, 8)))
        self.add_line('sym-e25', (23, 8), (18, 8))
        self.add_bezier('sym-e26', (18, 8), ((17.773, 8.084), (17.218, 8), (17, 8)))
        self.add_bezier('sym-e27', (17, 8), ((15.627, 8.775), (15.491, 10.754), (15, 12)))
        self.add_bezier('sym-e28', (15, 12), ((14.473, 13.331), (13.3, 14.293), (12, 15)))
        self.add_bezier('sym-e29', (12, 15), ((11.645, 15.194), (11.355, 15.806), (11, 16)))
        self.add_bezier('sym-e30', (11, 16), ((8.764, 16.682), (4, 15.615), (4, 19)))
        self.add_bezier('sym-e31', (4, 19), ((4, 19.32), (4, 19.68), (4, 20)))
        self.add_line('sym-e32', (4, 20), (4, 26))
        self.add_bezier('sym-e33', (4, 26), ((4, 26.067), (4, 25.933), (4, 26)))
        self.add_bezier('sym-e34', (4, 26), ((4, 26.059), (4, 25.933), (4, 26)))
        self.add_bezier('sym-e35', (4, 26), ((4, 28.392), (7.245, 30.636), (9, 32)))
        self.add_bezier('sym-e36', (9, 32), ((12.1, 34.425), (14.191, 36.261), (15, 40)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', closed=True)
        self.add_contour('sym-c2', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
