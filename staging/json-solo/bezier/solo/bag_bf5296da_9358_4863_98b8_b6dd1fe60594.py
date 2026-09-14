"""Bag (photography), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bf5296da-9358-4863-98b8-b6dd1fe60594'
SOURCE_PATH = 'icons-json/photography/bag_bf5296da-9358-4863-98b8-b6dd1fe60594.json'
AUTHOR = 'json_to_solo'

class Bag(Solo48):
    icon_id = 'bag'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('bag', 'photography')

    def build(self):
        self.add_line('sym-e0', (17, 15), (31, 15))
        self.add_line('sym-e1', (31, 15), (31, 19))
        self.add_line('sym-e2', (17, 19), (17, 15))
        self.add_line('sym-e3', (17, 15), (15, 15))
        self.add_bezier('sym-e4', (15, 15), ((13.518, 15.127), (11.867, 15.527), (11, 17)))
        self.add_bezier('sym-e5', (11, 17), ((10.865, 17.227), (11.034, 17.727), (11, 18)))
        self.add_line('sym-e6', (11, 18), (8, 39))
        self.add_bezier('sym-e7', (8, 39), ((8, 39.1), (8, 38.9), (8, 39)))
        self.add_bezier('sym-e8', (8, 39), ((8, 41.082), (9.417, 43.1), (11, 44)))
        self.add_bezier('sym-e9', (11, 44), ((11.354, 44), (11.587, 44), (12, 44)))
        self.add_line('sym-e10', (12, 44), (24, 44))
        self.add_line('sym-e11', (24, 44), (36, 44))
        self.add_bezier('sym-e12', (36, 44), ((36.413, 44), (36.646, 44), (37, 44)))
        self.add_bezier('sym-e13', (37, 44), ((38.583, 43.1), (40, 41.082), (40, 39)))
        self.add_bezier('sym-e14', (40, 39), ((40, 38.9), (40, 39.1), (40, 39)))
        self.add_line('sym-e15', (40, 39), (37, 18))
        self.add_bezier('sym-e16', (37, 18), ((36.966, 17.727), (37.135, 17.227), (37, 17)))
        self.add_bezier('sym-e17', (37, 17), ((36.133, 15.527), (34.482, 15.127), (33, 15)))
        self.add_line('sym-e18', (33, 15), (31, 15))
        self.add_bezier('sym-e19', (31, 15), ((31, 13.527), (31.227, 12.455), (31, 11)))
        self.add_bezier('sym-e20', (31, 11), ((30.461, 7.591), (27.402, 4), (24, 4)))
        self.add_bezier('sym-e21', (24, 4), ((23.943, 4), (24.056, 4), (24, 4)))
        self.add_bezier('sym-e22', (24, 4), ((23.944, 4), (24.057, 4), (24, 4)))
        self.add_bezier('sym-e23', (24, 4), ((20.598, 4), (17.539, 7.591), (17, 11)))
        self.add_bezier('sym-e24', (17, 11), ((16.773, 12.455), (17, 13.527), (17, 15)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
