"""Bag (shopping), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '44d13a4d-0f14-45d6-b151-8ea1e0eb4903'
SOURCE_PATH = 'icons-json/shopping/bag_44d13a4d-0f14-45d6-b151-8ea1e0eb4903.json'
AUTHOR = 'json_to_solo'

class Bag(Solo48):
    icon_id = 'bag'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('bag', 'shopping')

    def build(self):
        self.add_line('sym-e0', (17, 15), (31, 15))
        self.add_line('sym-e1', (31, 15), (31, 19))
        self.add_line('sym-e2', (17, 19), (17, 15))
        self.add_line('sym-e3', (17, 15), (15, 15))
        self.add_bezier('sym-e4', (15, 15), ((12.954, 15.173), (11.893, 15.855), (11, 18)))
        self.add_line('sym-e5', (11, 18), (8, 39))
        self.add_bezier('sym-e6', (8, 39), ((8, 39.1), (8, 38.9), (8, 39)))
        self.add_bezier('sym-e7', (8, 39), ((8, 41.209), (10.223, 43.218), (12, 44)))
        self.add_bezier('sym-e8', (12, 44), ((12.271, 44), (11.962, 44), (12, 44)))
        self.add_bezier('sym-e9', (12, 44), ((12.099, 44), (11.446, 43.763), (12, 44)))
        self.add_line('sym-e10', (12, 44), (24, 44))
        self.add_line('sym-e11', (24, 44), (36, 44))
        self.add_bezier('sym-e12', (36, 44), ((36.554, 43.763), (35.901, 44), (36, 44)))
        self.add_bezier('sym-e13', (36, 44), ((36.038, 44), (35.729, 44), (36, 44)))
        self.add_bezier('sym-e14', (36, 44), ((37.777, 43.218), (40, 41.209), (40, 39)))
        self.add_bezier('sym-e15', (40, 39), ((40, 38.9), (40, 39.1), (40, 39)))
        self.add_line('sym-e16', (40, 39), (37, 18))
        self.add_bezier('sym-e17', (37, 18), ((36.107, 15.855), (35.046, 15.173), (33, 15)))
        self.add_line('sym-e18', (33, 15), (31, 15))
        self.add_bezier('sym-e19', (31, 15), ((31, 13.527), (31.227, 12.455), (31, 11)))
        self.add_bezier('sym-e20', (31, 11), ((30.461, 7.591), (27.402, 4), (24, 4)))
        self.add_bezier('sym-e21', (24, 4), ((23.962, 4), (24.037, 4), (24, 4)))
        self.add_bezier('sym-e22', (24, 4), ((23.981, 4), (24.019, 4), (24, 4)))
        self.add_bezier('sym-e23', (24, 4), ((23.981, 4), (24.019, 4), (24, 4)))
        self.add_bezier('sym-e24', (24, 4), ((23.963, 4), (24.038, 4), (24, 4)))
        self.add_bezier('sym-e25', (24, 4), ((20.598, 4), (17.539, 7.591), (17, 11)))
        self.add_bezier('sym-e26', (17, 11), ((16.773, 12.455), (17, 13.527), (17, 15)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26')
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
