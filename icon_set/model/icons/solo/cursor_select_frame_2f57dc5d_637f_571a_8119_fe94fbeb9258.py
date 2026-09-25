"""Cursor select frame (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f57dc5d-637f-571a-8119-fe94fbeb9258'
SOURCE_PATH = 'pictographic-primitives/interface-essential/cursor select frame_2f57dc5d-637f-571a-8119-fe94fbeb9258.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class CursorSelectFrame(Solo48):
    icon_id = 'cursor-select-frame'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('cursor', 'select', 'frame', 'interface-essential')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('sym-e0', (6, 16), (6, 6))
        self.add_line('sym-e5', (6, 6), (17, 6))
        self.add_line('sym-e6', (31, 6), (42, 6))
        self.add_line('sym-e11', (42, 6), (42, 16))
        self.add_line('sym-e12', (6, 32), (6, 42))
        self.add_line('sym-e17', (6, 42), (17, 42))
        self.add_line('sym-e18', (31, 42), (42, 42))
        self.add_line('sym-e23', (42, 42), (42, 32))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e5', closed=False)
        self.add_contour('sym-c1', 'sym-e6', 'sym-e11', closed=False)
        self.add_contour('sym-c2', 'sym-e12', 'sym-e17', closed=False)
        self.add_contour('sym-c3', 'sym-e18', 'sym-e23', closed=False)
