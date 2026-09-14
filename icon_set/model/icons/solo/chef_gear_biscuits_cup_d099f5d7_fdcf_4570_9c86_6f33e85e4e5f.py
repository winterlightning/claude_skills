"""Chef gear biscuits cup (food), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd099f5d7-fdcf-4570-9c86-6f33e85e4e5f'
SOURCE_PATH = 'icons-json/food/chef gear biscuits cup_d099f5d7-fdcf-4570-9c86-6f33e85e4e5f.json'
AUTHOR = 'json_to_solo'

class ChefGearBiscuitsCup(Solo48):
    icon_id = 'chef-gear-biscuits-cup'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('chef', 'gear', 'biscuits', 'cup', 'food')

    def build(self):
        self.add_line('sym-e0', (25, 20), (23, 20))
        self.add_line('sym-e1', (23, 20), (18, 7))
        self.add_arc('sym-e2', (18, 7), (13, 4), radius_x=6, sweep=False)
        self.add_line('sym-e5-1', (13, 4), (10, 5))
        self.add_arc('sym-e5-2', (10, 5), (8, 8), radius_x=4, sweep=False)
        self.add_line('sym-e7', (8, 8), (8, 9))
        self.add_line('sym-e8', (8, 9), (12, 20))
        self.add_line('sym-e9', (12, 20), (23, 20))
        self.add_line('sym-e10', (25, 20), (30, 7))
        self.add_arc('sym-e11', (30, 7), (35, 4), radius_x=6)
        self.add_line('sym-e14-1', (35, 4), (38, 5))
        self.add_arc('sym-e14-2', (38, 5), (40, 8), radius_x=4)
        self.add_arc('sym-e16', (40, 8), (40, 9), radius_x=20, sweep=False)
        self.add_line('sym-e17', (40, 9), (36, 20))
        self.add_line('sym-e18', (36, 20), (25, 20))
        self.add_line('sym-e19', (36, 20), (40, 20))
        self.add_line('sym-e20', (40, 20), (34, 43))
        self.add_line('sym-e21', (34, 43), (33, 44))
        self.add_line('sym-e23', (33, 44), (24, 44))
        self.add_line('sym-e24', (24, 44), (15, 44))
        self.add_line('sym-e26', (15, 44), (14, 43))
        self.add_line('sym-e27', (14, 43), (8, 20))
        self.add_line('sym-e28', (8, 20), (12, 20))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e5-1', 'sym-e5-2', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c1', 'sym-e10', 'sym-e11', 'sym-e14-1', 'sym-e14-2', 'sym-e16', 'sym-e17', 'sym-e18', closed=True)
        self.add_contour('sym-c2', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e23', 'sym-e24', 'sym-e26', 'sym-e27', 'sym-e28')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
