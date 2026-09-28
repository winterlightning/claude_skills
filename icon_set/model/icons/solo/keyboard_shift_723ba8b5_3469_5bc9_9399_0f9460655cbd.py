"""Keyboard shift (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '723ba8b5-3469-5bc9-9399-0f9460655cbd'
SOURCE_PATH = 'pictographic-primitives/interface-essential/keyboard shift_723ba8b5-3469-5bc9-9399-0f9460655cbd.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class KeyboardShift(Solo48):
    icon_id = 'keyboard-shift'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('keyboard', 'shift', 'interface-essential')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (32, 22), (32, 44))
        self.add_line('e1', (32, 44), (16, 44))
        self.add_line('e2', (16, 44), (16, 22))
        self.add_line('e3', (16, 22), (8, 22))
        self.add_line('e4', (8, 22), (24, 4))
        self.add_line('e5', (24, 4), (40, 22))
        self.add_line('e6', (40, 22), (32, 22))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', closed=True)
