"""Fork (food), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0d4755a-cca4-5ee7-aa11-660d6df57a19'
SOURCE_PATH = 'icons-json/food/fork_a0d4755a-cca4-5ee7-aa11-660d6df57a19.json'
AUTHOR = 'json_to_solo'

class ForkFood(Solo48):
    icon_id = 'fork-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('fork', 'food')

    def build(self):
        self.add_line('sym-e0', (24, 4), (24, 21))
        self.add_line('sym-e1', (24, 21), (24, 44))
        self.add_arc('sym-e2', (24, 21), (20, 21), radius_x=30)
        self.add_arc('sym-e3', (20, 21), (17, 21), radius_x=28)
        self.add_arc('sym-e4', (17, 21), (8, 16), radius_x=9)
        self.add_line('sym-e6', (8, 16), (8, 4))
        self.add_arc('sym-e7', (24, 21), (28, 21), radius_x=30, sweep=False)
        self.add_line('sym-e8', (28, 21), (31, 21))
        self.add_arc('sym-e9', (31, 21), (40, 16), radius_x=9, sweep=False)
        self.add_line('sym-e11', (40, 16), (40, 4))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e11')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
