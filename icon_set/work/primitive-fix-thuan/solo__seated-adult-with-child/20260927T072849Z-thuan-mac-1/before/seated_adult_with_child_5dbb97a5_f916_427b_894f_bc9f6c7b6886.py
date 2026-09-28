"An adult sits on a curved-backed seat facing right with a smaller child on the lap. Both figures have circular heads and bent legs, with the child's feet projecting forward.\n\nConstruction: Adult and child sit side by side on a shared seat; head size distinguishes the child. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5dbb97a5-f916-427b-894f-bc9f6c7b6886'
SOURCE_PATH = 'pictographic-primitives/wayfinding/seat child_5dbb97a5-f916-427b-894f-bc9f6c7b6886.svg'
AUTHOR = 'gpt-6'

class SeatedAdultWithChild(Solo48):
    icon_id = 'seated-adult-with-child'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('adult', 'child', 'seated', 'lap', 'priority', 'seat')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('adult-head-top', (9, 11), (15, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('adult-head-bottom', (15, 11), (9, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('adult-body-1', (14, 23), (14, 32))
        self.add_line('adult-body-2', (14, 32), (22, 32))
        self.add_line('adult-body-3', (22, 32), (26, 40))
        self.add_arc('child-head-top', (30, 15), (34, 15), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('child-head-bottom', (34, 15), (30, 15), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('child-body-1', (30, 26), (34, 31))
        self.add_line('child-body-2', (34, 31), (38, 31))
        self.add_line('child-body-3', (38, 31), (44, 40))
        self.add_line('seat-1', (4, 24), (4, 40))
        self.add_line('seat-2', (4, 40), (16, 40))
        self.add_contour('adult-head', 'adult-head-top', 'adult-head-bottom', closed=True)
        self.add_contour('adult-body', 'adult-body-1', 'adult-body-2', 'adult-body-3', closed=False)
        self.add_contour('child-head', 'child-head-top', 'child-head-bottom', closed=True)
        self.add_contour('child-body', 'child-body-1', 'child-body-2', 'child-body-3', closed=False)
        self.add_contour('seat', 'seat-1', 'seat-2', closed=False)
