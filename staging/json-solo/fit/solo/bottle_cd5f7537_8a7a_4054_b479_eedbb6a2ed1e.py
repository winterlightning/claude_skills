"""Batch-01/bottle (decoration), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd5f7537-8a7a-4054-b479-eedbb6a2ed1e'
SOURCE_PATH = 'icons-json/decoration/batch-01/bottle_cd5f7537-8a7a-4054-b479-eedbb6a2ed1e.json'
AUTHOR = 'json_to_solo'

class Batch01BottleDecoration(Solo48):
    icon_id = 'batch-01-bottle-decoration'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    aliases = ()
    keywords = ('batch', 'bottle', 'decoration')

    def build(self):
        self.add_line('sym-e0', (35, 5), (35, 7))
        self.add_arc('sym-e1', (35, 7), (32, 9), radius_x=27, sweep=False)
        self.add_arc('sym-e2', (32, 9), (31, 18), radius_x=7, sweep=False)
        self.add_line('sym-e3', (31, 18), (37, 25))
        self.add_arc('sym-e4', (37, 25), (40, 32), radius_x=13)
        self.add_line('sym-e5', (40, 32), (40, 33))
        self.add_line('sym-e6', (40, 33), (40, 34))
        self.add_arc('sym-e7', (40, 34), (32, 44), radius_x=11)
        self.add_line('sym-e8', (32, 44), (30, 44))
        self.add_line('sym-e9', (30, 44), (24, 44))
        self.add_line('sym-e10', (24, 44), (18, 44))
        self.add_line('sym-e11', (18, 44), (16, 44))
        self.add_arc('sym-e12', (16, 44), (8, 34), radius_x=11)
        self.add_line('sym-e13', (8, 34), (8, 33))
        self.add_line('sym-e14', (8, 33), (8, 32))
        self.add_arc('sym-e15', (8, 32), (11, 25), radius_x=13)
        self.add_line('sym-e16', (11, 25), (17, 18))
        self.add_arc('sym-e17', (17, 18), (16, 9), radius_x=7, sweep=False)
        self.add_arc('sym-e18', (16, 9), (13, 7), radius_x=26, sweep=False)
        self.add_line('sym-e19', (13, 7), (13, 5))
        self.add_arc('sym-e20', (13, 5), (14, 4), radius_x=17)
        self.add_line('sym-e21', (14, 4), (24, 4))
        self.add_line('sym-e22', (24, 4), (34, 4))
        self.add_arc('sym-e23', (34, 4), (35, 5), radius_x=17)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
