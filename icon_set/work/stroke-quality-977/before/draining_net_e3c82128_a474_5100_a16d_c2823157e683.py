"""Draining net (food), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3c82128-a474-5100-a16d-c2823157e683'
SOURCE_PATH = 'pictographic-primitives/food/draining net_e3c82128-a474-5100-a16d-c2823157e683.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class DrainingNet(Solo48):
    icon_id = 'draining-net'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('draining', 'net', 'food')

    def build(self):
        self.add_line('sym-e0', (24, 44), (24, 44))
        self.add_line('sym-e1', (24, 4), (24, 4))
        self.add_arc('sym-e2', (24, 4), (19, 8), radius_x=6, sweep=False)
        self.add_line('sym-e4', (19, 8), (20, 23))
        self.add_arc('sym-e5', (20, 23), (9, 30), radius_x=16, sweep=False)
        self.add_line('sym-e6', (9, 30), (8, 32))
        self.add_line('sym-e7', (8, 32), (8, 33))
        self.add_line('sym-e8', (8, 33), (8, 34))
        self.add_arc('sym-e9-1', (8, 34), (13, 41), radius_x=10, sweep=False)
        self.add_arc('sym-e9-2', (13, 41), (23, 44), radius_x=19, sweep=False)
        self.add_line('sym-e10', (24, 44), (23, 44))
        self.add_line('sym-e11', (24, 44), (25, 44))
        self.add_arc('sym-e12-1', (25, 44), (35, 41), radius_x=19, sweep=False)
        self.add_arc('sym-e12-2', (35, 41), (40, 34), radius_x=10, sweep=False)
        self.add_line('sym-e13', (40, 34), (40, 33))
        self.add_line('sym-e14', (40, 33), (40, 32))
        self.add_line('sym-e15', (40, 32), (39, 30))
        self.add_arc('sym-e16', (39, 30), (28, 23), radius_x=15, sweep=False)
        self.add_line('sym-e17', (28, 23), (29, 8))
        self.add_arc('sym-e19', (29, 8), (24, 4), radius_x=6, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', closed=True)
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9-1', 'sym-e9-2')
        self.add_contour('sym-c2', 'sym-e10')
        self.add_contour('sym-c3', 'sym-e11')
        self.add_contour('sym-c4', 'sym-e12-1', 'sym-e12-2', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e19')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c2', 'sym-c3')
