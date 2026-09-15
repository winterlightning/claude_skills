"""Dumbbell (sports), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c7617317-0663-433d-b73d-2bfd2f6407c8'
SOURCE_PATH = 'pictographic-primitives/sports/dumbbell_c7617317-0663-433d-b73d-2bfd2f6407c8.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class DumbbellSports(Solo48):
    icon_id = 'dumbbell-sports'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('dumbbell', 'sports')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (35, 24), (13, 24))
        self.add_line('e1', (4, 40), (4, 8))
        self.add_line('e2', (4, 8), (13, 8))
        self.add_line('e3', (13, 8), (13, 40))
        self.add_line('e4', (13, 40), (4, 40))
        self.add_line('e5', (35, 8), (44, 8))
        self.add_line('e6', (44, 8), (44, 40))
        self.add_line('e7', (44, 40), (35, 40))
        self.add_line('e8', (35, 40), (35, 8))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e4', closed=True)
        self.add_contour('c2', 'e5', 'e6', 'e7', 'e8', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c1')
