"""Bag (photography), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0f5b2ebf-9ca8-4f74-bcf3-e9448134158b'
SOURCE_PATH = 'icons-json/photography/bag_0f5b2ebf-9ca8-4f74-bcf3-e9448134158b.json'
AUTHOR = 'json_to_solo'

class Bag0f5b2ebf(Solo48):
    icon_id = 'bag-0f5b2ebf'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('bag', 'photography')

    def build(self):
        self.add_line('sym-e0', (17, 15), (31, 15))
        self.add_line('sym-e1', (31, 15), (31, 19))
        self.add_line('sym-e2', (17, 19), (17, 15))
        self.add_line('sym-e3', (17, 15), (15, 15))
        self.add_arc('sym-e4', (15, 15), (11, 17), radius_x=4, sweep=False)
        self.add_line('sym-e5', (11, 17), (11, 18))
        self.add_line('sym-e6', (11, 18), (8, 39))
        self.add_arc('sym-e8', (8, 39), (11, 44), radius_x=6, sweep=False)
        self.add_arc('sym-e9', (11, 44), (12, 44), radius_x=2)
        self.add_line('sym-e10', (12, 44), (24, 44))
        self.add_line('sym-e11', (24, 44), (36, 44))
        self.add_arc('sym-e12', (36, 44), (37, 44), radius_x=2)
        self.add_arc('sym-e13', (37, 44), (40, 39), radius_x=6, sweep=False)
        self.add_line('sym-e15', (40, 39), (37, 18))
        self.add_line('sym-e16', (37, 18), (37, 17))
        self.add_arc('sym-e17', (37, 17), (33, 15), radius_x=4, sweep=False)
        self.add_line('sym-e18', (33, 15), (31, 15))
        self.add_line('sym-e19', (31, 15), (31, 11))
        self.add_arc('sym-e20', (31, 11), (24, 4), radius_x=7, sweep=False)
        self.add_arc('sym-e23', (24, 4), (17, 11), radius_x=7, sweep=False)
        self.add_arc('sym-e24', (17, 11), (17, 15), radius_x=24, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e23', 'sym-e24')
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
