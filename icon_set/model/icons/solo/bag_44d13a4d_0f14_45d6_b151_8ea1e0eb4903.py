"""Bag (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '44d13a4d-0f14-45d6-b151-8ea1e0eb4903'
SOURCE_PATH = 'icons-json/shopping/bag_44d13a4d-0f14-45d6-b151-8ea1e0eb4903.json'
AUTHOR = 'json_to_solo'

class Bag44d13a4d(Solo48):
    icon_id = 'bag-44d13a4d'
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
        self.add_arc('sym-e4', (15, 15), (11, 18), radius_x=3, sweep=False)
        self.add_line('sym-e5', (11, 18), (8, 39))
        self.add_arc('sym-e7', (8, 39), (12, 44), radius_x=6, sweep=False)
        self.add_line('sym-e10', (12, 44), (24, 44))
        self.add_line('sym-e11', (24, 44), (36, 44))
        self.add_arc('sym-e14', (36, 44), (40, 39), radius_x=6, sweep=False)
        self.add_line('sym-e16', (40, 39), (37, 18))
        self.add_arc('sym-e17', (37, 18), (33, 15), radius_x=3, sweep=False)
        self.add_line('sym-e18', (33, 15), (31, 15))
        self.add_line('sym-e19', (31, 15), (31, 11))
        self.add_arc('sym-e20', (31, 11), (24, 4), radius_x=7, sweep=False)
        self.add_arc('sym-e25', (24, 4), (17, 11), radius_x=7, sweep=False)
        self.add_arc('sym-e26', (17, 11), (17, 15), radius_x=24, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e10', 'sym-e11', 'sym-e14', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e25', 'sym-e26')
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
