"""Pathfinder intersect (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c1403de-6b64-47bf-92a2-5713a99fc2c0'
SOURCE_PATH = 'pictographic-primitives/design/pathfinder intersect_1c1403de-6b64-47bf-92a2-5713a99fc2c0.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class PathfinderIntersect(Solo48):
    icon_id = 'pathfinder-intersect'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('pathfinder', 'intersect', 'design')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (18, 31), (18, 17))
        self.add_line('e1', (18, 17), (31, 17))
        self.add_line('e2', (31, 17), (31, 31))
        self.add_line('e3', (31, 31), (18, 31))
        self.add_line('e4', (18, 31), (18, 42))
        self.add_line('e5', (18, 42), (42, 42))
        self.add_line('e6', (42, 42), (42, 17))
        self.add_line('e7', (42, 17), (31, 17))
        self.add_line('e8', (31, 17), (31, 6))
        self.add_line('e9', (31, 6), (6, 6))
        self.add_line('e10', (6, 6), (6, 31))
        self.add_line('e11', (6, 31), (18, 31))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', closed=True)
        self.add_contour('c1', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', closed=True)
        self.relate('connect', 'c0', 'c1')
