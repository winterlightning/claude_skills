"""Left distance (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b849307-bb16-5026-8873-7c0f5b6aa752'
SOURCE_PATH = 'pictographic-primitives/design/left distance_1b849307-bb16-5026-8873-7c0f5b6aa752.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class LeftDistance(Solo48):
    icon_id = 'left-distance'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('left', 'distance', 'design')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (4, 8), (4, 40))
        self.add_line('e1', (26, 24), (12, 24))
        self.add_line('e2', (12, 24), (18, 19))
        self.add_line('e3', (12, 24), (18, 29))
        self.add_line('e4', (27, 16), (44, 16))
        self.add_line('e5', (44, 16), (44, 32))
        self.add_line('e6', (44, 32), (26, 32))
        self.add_line('e7', (26, 32), (26, 20))
        self.add_arc('e8', (26, 20), (27, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', 'e2', closed=False)
        self.add_contour('c2', 'e3', closed=False)
        self.add_contour('c3', 'e8', 'e4', 'e5', 'e6', 'e7', closed=True)
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
