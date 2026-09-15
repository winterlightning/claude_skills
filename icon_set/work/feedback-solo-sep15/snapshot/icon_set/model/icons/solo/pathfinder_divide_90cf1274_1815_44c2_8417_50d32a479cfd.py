"""Pathfinder divide (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90cf1274-1815-44c2-8417-50d32a479cfd'
SOURCE_PATH = 'pictographic-primitives/design/pathfinder divide_90cf1274-1815-44c2-8417-50d32a479cfd.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class PathfinderDivide(Solo48):
    icon_id = 'pathfinder-divide'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pathfinder', 'divide', 'design')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (18, 30), (18, 18))
        self.add_line('e1', (18, 18), (30, 18))
        self.add_line('e2', (18, 30), (30, 30))
        self.add_line('e3', (30, 30), (30, 18))
        self.add_line('e4', (18, 30), (18, 40))
        self.add_line('e5', (18, 40), (44, 40))
        self.add_line('e6', (44, 40), (44, 18))
        self.add_line('e7', (44, 18), (30, 18))
        self.add_line('e8', (18, 30), (4, 30))
        self.add_line('e9', (4, 30), (4, 8))
        self.add_line('e10', (4, 8), (30, 8))
        self.add_line('e11', (30, 8), (30, 18))
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
