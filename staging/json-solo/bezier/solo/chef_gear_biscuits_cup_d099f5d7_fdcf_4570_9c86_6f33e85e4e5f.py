"""Chef gear biscuits cup (food), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd099f5d7-fdcf-4570-9c86-6f33e85e4e5f'
SOURCE_PATH = 'icons-json/food/chef gear biscuits cup_d099f5d7-fdcf-4570-9c86-6f33e85e4e5f.json'
AUTHOR = 'json_to_solo'

class ChefGearBiscuitsCupFood(Solo48):
    icon_id = 'chef-gear-biscuits-cup-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('chef', 'gear', 'biscuits', 'cup', 'food')

    def build(self):
        self.add_line('sym-e0', (25, 20), (23, 20))
        self.add_line('sym-e1', (23, 20), (18, 7))
        self.add_bezier('sym-e2', (18, 7), ((17.569, 5.818), (14.698, 4), (13, 4)))
        self.add_bezier('sym-e3', (13, 4), ((12.914, 4), (13.086, 4), (13, 4)))
        self.add_bezier('sym-e4', (13, 4), ((12.877, 4), (13.135, 4), (13, 4)))
        self.add_bezier('sym-e5', (13, 4), ((10.612, 4), (8, 6.355), (8, 8)))
        self.add_bezier('sym-e6', (8, 8), ((8, 8.109), (8, 7.882), (8, 8)))
        self.add_bezier('sym-e7', (8, 8), ((8, 8.155), (8, 8.845), (8, 9)))
        self.add_line('sym-e8', (8, 9), (12, 20))
        self.add_line('sym-e9', (12, 20), (23, 20))
        self.add_line('sym-e10', (25, 20), (30, 7))
        self.add_bezier('sym-e11', (30, 7), ((30.431, 5.818), (33.302, 4), (35, 4)))
        self.add_bezier('sym-e12', (35, 4), ((35.086, 4), (34.914, 4), (35, 4)))
        self.add_bezier('sym-e13', (35, 4), ((35.123, 4), (34.865, 4), (35, 4)))
        self.add_bezier('sym-e14', (35, 4), ((37.388, 4), (40, 6.355), (40, 8)))
        self.add_bezier('sym-e15', (40, 8), ((40, 8.109), (40, 7.882), (40, 8)))
        self.add_bezier('sym-e16', (40, 8), ((40, 8.155), (40, 8.845), (40, 9)))
        self.add_line('sym-e17', (40, 9), (36, 20))
        self.add_line('sym-e18', (36, 20), (25, 20))
        self.add_line('sym-e19', (36, 20), (40, 20))
        self.add_line('sym-e20', (40, 20), (34, 43))
        self.add_bezier('sym-e21', (34, 43), ((33.778, 43.227), (33.32, 43.8), (33, 44)))
        self.add_bezier('sym-e22', (33, 44), ((32.815, 44), (33.185, 43.9), (33, 44)))
        self.add_line('sym-e23', (33, 44), (24, 44))
        self.add_line('sym-e24', (24, 44), (15, 44))
        self.add_bezier('sym-e25', (15, 44), ((14.815, 43.9), (15.185, 44), (15, 44)))
        self.add_bezier('sym-e26', (15, 44), ((14.68, 43.8), (14.222, 43.227), (14, 43)))
        self.add_line('sym-e27', (14, 43), (8, 20))
        self.add_line('sym-e28', (8, 20), (12, 20))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c1', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', closed=True)
        self.add_contour('sym-c2', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
