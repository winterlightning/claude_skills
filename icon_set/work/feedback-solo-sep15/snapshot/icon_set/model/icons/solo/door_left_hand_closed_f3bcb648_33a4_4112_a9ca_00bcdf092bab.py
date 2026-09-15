"""Door left hand closed (building), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3bcb648-33a4-4112-a9ca-00bcdf092bab'
SOURCE_PATH = 'pictographic-primitives/building/door left hand closed_f3bcb648-33a4-4112-a9ca-00bcdf092bab.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class DoorLeftHandClosed(Solo48):
    icon_id = 'door-left-hand-closed'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('door', 'left', 'hand', 'closed', 'building')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (6, 42), (10, 42))
        self.add_line('e1', (42, 42), (37, 42))
        self.add_line('e2', (10, 42), (10, 6))
        self.add_line('e3', (10, 6), (37, 6))
        self.add_line('e4', (37, 6), (37, 42))
        self.add_line('e5', (10, 42), (37, 42))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', 'e3', 'e4', closed=False)
        self.add_contour('c3', 'e5', closed=False)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
