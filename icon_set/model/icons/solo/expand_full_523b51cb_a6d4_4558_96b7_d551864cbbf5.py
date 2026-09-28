"""Expand full (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '523b51cb-a6d4-4558-96b7-d551864cbbf5'
SOURCE_PATH = 'pictographic-primitives/interface-essential/expand full_523b51cb-a6d4-4558-96b7-d551864cbbf5.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class ExpandFull(Solo48):
    icon_id = 'expand-full'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('expand', 'full', 'interface-essential')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (6, 14), (6, 6))
        self.add_line('e1', (6, 6), (14, 6))
        self.add_line('e2', (34, 6), (42, 6))
        self.add_line('e3', (42, 6), (42, 14))
        self.add_line('e4', (6, 35), (6, 42))
        self.add_line('e5', (6, 42), (14, 42))
        self.add_line('e6', (34, 42), (42, 42))
        self.add_line('e7', (42, 42), (42, 35))
        self.add_line('e8', (33, 30), (15, 30))
        self.add_line('e9', (15, 30), (15, 18))
        self.add_line('e10', (15, 18), (33, 18))
        self.add_line('e11', (33, 18), (33, 30))
        self.add_contour('c0', 'e0', 'e1', closed=False)
        self.add_contour('c1', 'e2', 'e3', closed=False)
        self.add_contour('c2', 'e4', 'e5', closed=False)
        self.add_contour('c3', 'e6', 'e7', closed=False)
        self.add_contour('c4', 'e8', 'e9', 'e10', 'e11', closed=True)
