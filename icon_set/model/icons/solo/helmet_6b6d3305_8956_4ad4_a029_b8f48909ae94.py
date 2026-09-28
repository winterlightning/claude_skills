"""Helmet (protection), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b6d3305-8956-4ad4-a029-b8f48909ae94'
SOURCE_PATH = 'pictographic-primitives/protection/helmet_6b6d3305-8956-4ad4-a029-b8f48909ae94.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Helmet6b6d3305(Solo48):
    icon_id = 'helmet-6b6d3305'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    categories = ('protection', 'primitives')
    aliases = ()
    keywords = ('helmet', 'protection')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (29, 29), (29, 13))
        self.add_line('e1', (19, 29), (19, 10))
        self.add_line('e2', (29, 10), (29, 13))
        self.add_line('e3', (4, 29), (44, 29))
        self.add_line('e4', (44, 29), (44, 40))
        self.add_line('e5', (44, 40), (4, 40))
        self.add_arc('e6', (40, 29), (29, 13), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_line('e7-1', (19, 10), (23, 8))
        self.add_line('e7-2', (23, 8), (26, 8))
        self.add_line('e7-3', (26, 8), (29, 10))
        self.add_arc('e8', (8, 29), (19, 13), radius_x=17, radius_y=17, large_arc=False, sweep=True)
        self.add_line('e11-3', (4, 40), (4, 29))
        self.add_contour('c0', 'e6', closed=False)
        self.add_contour('c1', 'e0', closed=False)
        self.add_contour('c2', 'e1', 'e7-1', 'e7-2', 'e7-3', 'e2', closed=False)
        self.add_contour('c3', 'e8', closed=False)
        self.add_contour('c4', 'e3', 'e4', 'e5', 'e11-3', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c2')
