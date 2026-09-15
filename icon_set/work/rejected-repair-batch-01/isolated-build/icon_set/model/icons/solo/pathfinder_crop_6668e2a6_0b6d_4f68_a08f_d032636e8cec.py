"""Pathfinder crop (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6668e2a6-0b6d-4f68-a08f-d032636e8cec'
SOURCE_PATH = 'pictographic-primitives/design/pathfinder crop_6668e2a6-0b6d-4f68-a08f-d032636e8cec.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class PathfinderCrop(Solo48):
    icon_id = 'pathfinder-crop'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pathfinder', 'crop', 'design')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (18, 31), (18, 17))
        self.add_line('e1', (18, 17), (30, 17))
        self.add_line('e2', (18, 31), (30, 31))
        self.add_line('e3', (30, 31), (30, 17))
        self.add_line('e4', (18, 31), (18, 42))
        self.add_line('e5', (18, 42), (42, 42))
        self.add_line('e6', (42, 42), (42, 17))
        self.add_line('e7', (42, 17), (30, 17))
        self.add_line('e8', (18, 31), (6, 31))
        self.add_line('e9', (6, 31), (6, 6))
        self.add_line('e10', (6, 6), (30, 6))
        self.add_line('e11', (30, 6), (30, 17))
        self.add_contour('c0', 'e0', 'e1', closed=False)
        self.add_contour('c1', 'e2', 'e3', closed=False)
        self.add_contour('c2', 'e4', 'e5', 'e6', 'e7', closed=False)
        self.add_contour('c3', 'e8', 'e9', 'e10', 'e11', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
