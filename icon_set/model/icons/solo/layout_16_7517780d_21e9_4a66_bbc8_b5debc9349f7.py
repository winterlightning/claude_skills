"""Layout 16 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7517780d-21e9-4a66-bbc8-b5debc9349f7'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout 16_7517780d-21e9-4a66-bbc8-b5debc9349f7.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Layout16(Solo48):
    icon_id = 'layout-16'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (31, 16), (31, 42))
        self.add_line('e1', (31, 16), (42, 16))
        self.add_line('e2', (31, 16), (6, 16))
        self.add_line('e3', (42, 16), (42, 42))
        self.add_line('e4', (42, 42), (31, 42))
        self.add_line('e5', (42, 16), (42, 6))
        self.add_line('e6', (42, 6), (6, 6))
        self.add_line('e7', (6, 6), (6, 16))
        self.add_line('e8', (31, 42), (6, 42))
        self.add_line('e9', (6, 42), (6, 16))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', closed=False)
        self.add_contour('c3', 'e3', 'e4', closed=False)
        self.add_contour('c4', 'e5', 'e6', 'e7', closed=False)
        self.add_contour('c5', 'e8', 'e9', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
