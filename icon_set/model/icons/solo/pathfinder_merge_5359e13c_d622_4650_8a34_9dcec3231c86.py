"""Pathfinder merge (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5359e13c-d622-4650-8a34-9dcec3231c86'
SOURCE_PATH = 'pictographic-primitives/design/pathfinder merge_5359e13c-d622-4650-8a34-9dcec3231c86.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class PathfinderMerge(Solo48):
    icon_id = 'pathfinder-merge'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pathfinder', 'merge', 'design')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (17, 30), (4, 30))
        self.add_line('e1', (4, 30), (4, 8))
        self.add_line('e2', (4, 8), (29, 8))
        self.add_line('e3', (29, 8), (29, 18))
        self.add_line('e4', (29, 18), (44, 18))
        self.add_line('e5', (44, 18), (44, 40))
        self.add_line('e6', (44, 40), (17, 40))
        self.add_line('e7', (17, 40), (17, 30))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', closed=True)
