"""Nanobot (state), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dd990e4b-d221-4af4-82e5-519aa93fd2a1'
SOURCE_PATH = 'pictographic-primitives/state/nanobot_dd990e4b-d221-4af4-82e5-519aa93fd2a1.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Nanobot(Solo48):
    icon_id = 'nanobot'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('nanobot', 'state')

    def build(self):
        self.add_line('e0', (10, 28), (10, 13))
        self.add_line('e1', (11, 11), (23, 4))
        self.add_line('e2', (25, 4), (37, 11))
        self.add_line('e3', (38, 12), (38, 29))
        self.add_line('e4', (11, 30), (23, 38))
        self.add_line('e5', (26, 38), (37, 30))
        self.add_arc('e6-top', (19, 19), (29, 19), radius_x=5)
        self.add_arc('e6-bottom', (29, 19), (19, 19), radius_x=5)
        self.add_arc('e7-1', (37, 44), (40, 37), radius_x=10, sweep=False)
        self.add_arc('e7-2', (40, 37), (37, 30), radius_x=10, sweep=False)
        self.add_line('e8', (11, 30), (10, 28))
        self.add_line('e9', (10, 13), (11, 11))
        self.add_arc('e10', (23, 4), (25, 4), radius_x=73, sweep=False)
        self.add_arc('e11', (37, 11), (38, 12), radius_x=9)
        self.add_line('e12', (38, 29), (37, 30))
        self.add_line('e13', (23, 38), (26, 38))
        self.add_arc('e14-1', (11, 30), (8, 37), radius_x=12, sweep=False)
        self.add_line('e14-2', (8, 37), (9, 41))
        self.add_arc('e14-3', (9, 41), (11, 44), radius_x=21, sweep=False)
        self.add_contour('c0', 'e7-1', 'e7-2')
        self.add_contour('c1', 'e8', 'e0', 'e9', 'e1', 'e10', 'e2', 'e11', 'e3', 'e12')
        self.add_contour('c2', 'e4', 'e13', 'e5')
        self.add_contour('c3', 'e14-1', 'e14-2', 'e14-3')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
