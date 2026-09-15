"""Diving block weight (recreation), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '284b7c04-e252-4531-868f-398d3ef94159'
SOURCE_PATH = 'icons-json/recreation/diving block weight_284b7c04-e252-4531-868f-398d3ef94159.json'
AUTHOR = 'gpt-6'

class DivingBlockWeight(Solo48):
    icon_id = 'diving-block-weight'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'recreation'
    aliases = ()
    keywords = ('diving', 'block', 'weight', 'recreation')

    def build(self):
        self.add_line('sym-e0', (24, 29), (35, 28))
        self.add_line('sym-e1', (35, 28), (40, 26))
        self.add_line('sym-e2', (40, 26), (40, 38))
        self.add_line('sym-e3', (40, 38), (37, 41))
        self.add_line('sym-e4-1', (37, 41), (32, 43))
        self.add_line('sym-e4-2', (32, 43), (25, 44))
        self.add_line('sym-e5', (25, 44), (24, 44))
        self.add_arc('sym-e6', (24, 44), (23, 44), radius_x=28, radius_y=28, large_arc=False, sweep=False)
        self.add_line('sym-e7-1', (23, 44), (16, 43))
        self.add_line('sym-e7-2', (16, 43), (11, 41))
        self.add_line('sym-e8', (11, 41), (8, 38))
        self.add_line('sym-e9', (8, 38), (8, 26))
        self.add_line('sym-e10', (8, 26), (13, 28))
        self.add_line('sym-e11', (13, 28), (24, 29))
        self.add_line('sym-e12', (24, 4), (25, 4))
        self.add_line('sym-e13', (25, 4), (30, 5))
        self.add_arc('sym-e14', (30, 5), (40, 17), radius_x=16, radius_y=16, large_arc=False, sweep=True)
        self.add_line('sym-e15', (40, 17), (40, 26))
        self.add_arc('sym-e17', (24, 4), (23, 4), radius_x=70, radius_y=70, large_arc=False, sweep=True)
        self.add_line('sym-e18', (23, 4), (18, 5))
        self.add_arc('sym-e19', (18, 5), (8, 17), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_line('sym-e20', (8, 17), (8, 26))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4-1', 'sym-e4-2', 'sym-e5', 'sym-e6', 'sym-e7-1', 'sym-e7-2', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', closed=True)
        self.add_contour('sym-c1', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=False)
        self.add_contour('sym-c2', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
