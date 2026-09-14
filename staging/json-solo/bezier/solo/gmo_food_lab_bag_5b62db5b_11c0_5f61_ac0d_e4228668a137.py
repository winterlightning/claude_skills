"""Gmo food lab bag (science), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b62db5b-11c0-5f61-ac0d-e4228668a137'
SOURCE_PATH = 'icons-json/science/gmo food lab bag_5b62db5b-11c0-5f61-ac0d-e4228668a137.json'
AUTHOR = 'json_to_solo'

class GmoFoodLabBagScience(Solo48):
    icon_id = 'gmo-food-lab-bag-science'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('gmo', 'food', 'lab', 'bag', 'science')

    def build(self):
        self.add_line('sym-e0', (24, 22), (33, 22))
        self.add_line('sym-e1', (32, 4), (27, 4))
        self.add_line('sym-e2', (27, 4), (24, 4))
        self.add_line('sym-e3', (24, 4), (21, 4))
        self.add_line('sym-e4', (21, 4), (16, 4))
        self.add_line('sym-e5', (16, 4), (18, 7))
        self.add_line('sym-e6', (18, 7), (18, 15))
        self.add_bezier('sym-e7', (18, 15), ((18, 15.609), (18.05, 16.382), (18, 17)))
        self.add_line('sym-e8', (18, 17), (9, 34))
        self.add_bezier('sym-e9', (9, 34), ((8.59, 34.782), (8, 36.136), (8, 37)))
        self.add_bezier('sym-e10', (8, 37), ((8, 37.073), (8, 36.918), (8, 37)))
        self.add_bezier('sym-e11', (8, 37), ((8, 37.155), (8, 37.845), (8, 38)))
        self.add_bezier('sym-e12', (8, 38), ((8, 41.364), (11.36, 44), (15, 44)))
        self.add_bezier('sym-e13', (15, 44), ((15.26, 44), (15.74, 44), (16, 44)))
        self.add_line('sym-e14', (16, 44), (24, 44))
        self.add_line('sym-e15', (24, 44), (32, 44))
        self.add_bezier('sym-e16', (32, 44), ((32.26, 44), (32.74, 44), (33, 44)))
        self.add_bezier('sym-e17', (33, 44), ((36.64, 44), (40, 41.364), (40, 38)))
        self.add_bezier('sym-e18', (40, 38), ((40, 37.845), (40, 37.155), (40, 37)))
        self.add_bezier('sym-e19', (40, 37), ((40, 36.918), (40, 37.073), (40, 37)))
        self.add_bezier('sym-e20', (40, 37), ((40, 36.136), (39.41, 34.782), (39, 34)))
        self.add_line('sym-e21', (39, 34), (30, 17))
        self.add_bezier('sym-e22', (30, 17), ((29.95, 16.382), (30, 15.609), (30, 15)))
        self.add_line('sym-e23', (30, 15), (30, 7))
        self.add_line('sym-e24', (30, 7), (32, 4))
        self.add_line('sym-e25', (24, 22), (15, 22))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', closed=True)
        self.add_contour('sym-c2', 'sym-e25')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
