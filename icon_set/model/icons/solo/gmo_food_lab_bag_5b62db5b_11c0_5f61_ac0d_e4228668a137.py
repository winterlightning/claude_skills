"""Gmo food lab bag (science), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5b62db5b-11c0-5f61-ac0d-e4228668a137'
SOURCE_PATH = 'icons-json/science/gmo food lab bag_5b62db5b-11c0-5f61-ac0d-e4228668a137.json'
AUTHOR = 'gpt-6'

class GmoFoodLabBag(Solo48):
    icon_id = 'gmo-food-lab-bag'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('gmo', 'food', 'lab', 'bag', 'science')

    def build(self):
        self.add_line('sym-e0', (24, 22), (33, 22))
        self.add_line('sym-e1', (32, 4), (16, 4))
        self.add_line('sym-e5', (16, 4), (18, 7))
        self.add_line('sym-e6', (18, 7), (18, 15))
        self.add_arc('sym-e7', (18, 15), (18, 17), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_line('sym-e8', (18, 17), (9, 34))
        self.add_arc('sym-e9', (9, 34), (8, 37), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('sym-e11', (8, 37), (8, 38))
        self.add_arc('sym-e12', (8, 38), (15, 44), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('sym-e13', (15, 44), (16, 44), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('sym-e14', (16, 44), (33, 44))
        self.add_arc('sym-e17', (33, 44), (40, 38), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('sym-e18', (40, 38), (40, 37))
        self.add_arc('sym-e20', (40, 37), (39, 34), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('sym-e21', (39, 34), (30, 17))
        self.add_arc('sym-e22', (30, 17), (30, 15), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_line('sym-e23', (30, 15), (30, 7))
        self.add_line('sym-e24', (30, 7), (32, 4))
        self.add_line('sym-e25', (24, 22), (15, 22))
        self.add_contour('sym-c0', 'sym-e0', closed=False)
        self.add_contour('sym-c1', 'sym-e1', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e17', 'sym-e18', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', closed=True)
        self.add_contour('sym-c2', 'sym-e25', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
