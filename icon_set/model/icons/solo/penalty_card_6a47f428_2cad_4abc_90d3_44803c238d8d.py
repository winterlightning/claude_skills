"""Penalty card (sports), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a47f428-2cad-4abc-90d3-44803c238d8d'
SOURCE_PATH = 'pictographic-primitives/sports/penalty card_6a47f428-2cad-4abc-90d3-44803c238d8d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class PenaltyCard(Solo48):
    icon_id = 'penalty-card'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('penalty', 'card', 'sports')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (34, 35), (31, 33))
        self.add_line('e1', (42, 42), (42, 34))
        self.add_line('e2', (26, 36), (6, 36))
        self.add_line('e3', (6, 36), (6, 6))
        self.add_line('e4', (6, 6), (31, 6))
        self.add_line('e5', (31, 6), (31, 23))
        self.add_line('e6', (31, 33), (31, 23))
        self.add_arc('e7', (34, 42), (26, 36), radius_x=19, radius_y=19, large_arc=False, sweep=True)
        self.add_arc('e8', (42, 34), (31, 23), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('e12-1', (26, 36), (25, 31), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e12-2', (25, 31), (31, 33), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('c0', 'e7', closed=False)
        self.add_contour('c1', 'e0', closed=False)
        self.add_contour('c2', 'e1', 'e8', closed=False)
        self.add_contour('c3', 'e2', 'e3', 'e4', 'e5', closed=False)
        self.add_contour('c4', 'e12-1', 'e12-2', closed=False)
        self.add_contour('c5', 'e6', closed=False)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c5')
