"""Meal can (food), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a9327102-c668-47fb-88c0-07e9b814ac8a'
SOURCE_PATH = 'icons-json/food/meal can_a9327102-c668-47fb-88c0-07e9b814ac8a.json'
AUTHOR = 'json_to_solo'

class MealCan(Solo48):
    icon_id = 'meal-can'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('meal', 'can', 'food')

    def build(self):
        self.add_arc('sym-e0', (24, 16), (12, 14), radius_x=32)
        self.add_arc('sym-e1', (12, 14), (8, 11), radius_x=21)
        self.add_line('sym-e2', (8, 11), (8, 38))
        self.add_arc('sym-e3', (8, 38), (9, 40), radius_x=5, sweep=False)
        self.add_line('sym-e4-1', (9, 40), (15, 43))
        self.add_arc('sym-e4-2', (15, 43), (23, 44), radius_x=33, sweep=False)
        self.add_line('sym-e5', (23, 44), (24, 44))
        self.add_arc('sym-e6', (24, 44), (25, 44), radius_x=29)
        self.add_arc('sym-e7-1', (25, 44), (33, 43), radius_x=34, sweep=False)
        self.add_line('sym-e7-2', (33, 43), (39, 40))
        self.add_line('sym-e8', (39, 40), (40, 38))
        self.add_line('sym-e9', (40, 38), (40, 11))
        self.add_line('sym-e10', (40, 11), (36, 14))
        self.add_arc('sym-e11', (36, 14), (24, 16), radius_x=32)
        self.add_line('sym-e12', (24, 4), (23, 4))
        self.add_line('sym-e13', (23, 4), (11, 6))
        self.add_arc('sym-e14', (11, 6), (8, 10), radius_x=6, sweep=False)
        self.add_line('sym-e15', (8, 10), (8, 11))
        self.add_line('sym-e17', (16, 23), (24, 24))
        self.add_line('sym-e18', (24, 24), (32, 23))
        self.add_line('sym-e19', (32, 23), (32, 35))
        self.add_line('sym-e20', (32, 35), (24, 36))
        self.add_line('sym-e21', (24, 36), (16, 35))
        self.add_line('sym-e22', (16, 35), (16, 23))
        self.add_arc('sym-e23', (24, 4), (25, 4), radius_x=76, sweep=False)
        self.add_line('sym-e24', (25, 4), (37, 6))
        self.add_arc('sym-e25', (37, 6), (40, 10), radius_x=6)
        self.add_arc('sym-e26', (40, 10), (40, 11), radius_x=21, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4-1', 'sym-e4-2', 'sym-e5', 'sym-e6', 'sym-e7-1', 'sym-e7-2', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', closed=True)
        self.add_contour('sym-c1', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
        self.add_contour('sym-c2', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', closed=True)
        self.add_contour('sym-c3', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
