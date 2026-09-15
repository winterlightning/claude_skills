"""Pathfinder minus front (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb7d86f4-3ff3-47a3-aa50-7504fb0e5662'
SOURCE_PATH = 'pictographic-primitives/design/pathfinder minus front_eb7d86f4-3ff3-47a3-aa50-7504fb0e5662.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class PathfinderMinusFront(Solo48):
    icon_id = 'pathfinder-minus-front'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pathfinder', 'minus', 'front', 'design')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (18, 29), (18, 40))
        self.add_line('e1', (18, 40), (44, 40))
        self.add_line('e2', (44, 40), (44, 17))
        self.add_line('e3', (44, 17), (30, 17))
        self.add_line('e4', (18, 29), (18, 17))
        self.add_line('e5', (18, 17), (30, 17))
        self.add_line('e6', (18, 29), (4, 29))
        self.add_line('e7', (4, 29), (4, 8))
        self.add_line('e8', (4, 8), (30, 8))
        self.add_line('e9', (30, 8), (30, 17))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', closed=False)
        self.add_contour('c1', 'e4', 'e5', closed=False)
        self.add_contour('c2', 'e6', 'e7', 'e8', 'e9', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
