"""Focus close (photography), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7619190d-943a-49eb-bd67-270ef4c1b668'
SOURCE_PATH = 'pictographic-primitives/photography/focus close_7619190d-943a-49eb-bd67-270ef4c1b668.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class FocusClose(Solo48):
    icon_id = 'focus-close'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    categories = ('photography', 'primitives')
    aliases = ()
    keywords = ('focus', 'close', 'photography')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (6, 13), (6, 6))
        self.add_line('e1', (6, 6), (13, 6))
        self.add_line('e2', (35, 6), (42, 6))
        self.add_line('e3', (42, 6), (42, 13))
        self.add_line('e4', (35, 42), (42, 42))
        self.add_line('e5', (42, 42), (42, 35))
        self.add_line('e6', (6, 35), (6, 42))
        self.add_line('e7', (6, 42), (13, 42))
        self.add_arc('e8-top', (13, 24), (35, 24), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('e8-bottom', (35, 24), (13, 24), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_contour('c0', 'e0', 'e1', closed=False)
        self.add_contour('c1', 'e2', 'e3', closed=False)
        self.add_contour('c2', 'e4', 'e5', closed=False)
        self.add_contour('c3', 'e6', 'e7', closed=False)
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
