"""Keyboard arrow return (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '32978e5f-dd58-5a85-96df-67457d537f63'
SOURCE_PATH = 'pictographic-primitives/interface-essential/keyboard arrow return_32978e5f-dd58-5a85-96df-67457d537f63.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class KeyboardArrowReturn(Solo48):
    icon_id = 'keyboard-arrow-return'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'return', 'interface-essential')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (6, 34), (39, 34))
        self.add_line('e1', (42, 30), (42, 6))
        self.add_line('e2', (42, 6), (24, 6))
        self.add_line('e3', (6, 34), (15, 26))
        self.add_line('e4', (6, 34), (15, 42))
        self.add_line('e5-1', (39, 34), (41, 33))
        self.add_arc('e5-2', (41, 33), (42, 30), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e1', 'e2', closed=False)
        self.add_contour('c1', 'e3', closed=False)
        self.add_contour('c2', 'e4', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
