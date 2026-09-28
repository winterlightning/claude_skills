"""Helmet (protection), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd5b67122-8eaa-475e-8ad0-0d51c15807ab'
SOURCE_PATH = 'pictographic-primitives/protection/helmet_d5b67122-8eaa-475e-8ad0-0d51c15807ab.svg'
AUTHOR = 'gpt-6'

class HelmetD5b67122(Solo48):
    icon_id = 'helmet-d5b67122'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    categories = ('protection', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('helmet', 'protection')

    def build(self):
        self.add_line('sym-e0', (44, 40), (4, 40))
        self.add_line('sym-e3', (28, 8), (20, 8))
        self.add_line('sym-e4', (20, 8), (19, 13))
        self.add_line('sym-e5', (19, 13), (19, 14))
        self.add_arc('sym-e6', (19, 14), (8, 31), radius_x=24, radius_y=24, large_arc=False, sweep=False)
        self.add_arc('sym-e7', (8, 31), (8, 40), radius_x=59, radius_y=59, large_arc=False, sweep=False)
        self.add_line('sym-e8', (19, 29), (19, 14))
        self.add_arc('sym-e9', (29, 14), (40, 31), radius_x=24, radius_y=24, large_arc=False, sweep=True)
        self.add_arc('sym-e10', (40, 31), (40, 40), radius_x=59, radius_y=59, large_arc=False, sweep=True)
        self.add_line('sym-e11', (29, 29), (29, 13))
        self.add_line('sym-e13', (29, 13), (28, 8))
        self.add_contour('sym-c0', 'sym-e0', closed=False)
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', closed=False)
        self.add_contour('sym-c2', 'sym-e8', closed=False)
        self.add_contour('sym-c3', 'sym-e9', 'sym-e10', closed=False)
        self.add_contour('sym-c4', 'sym-e11', 'sym-e13', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
