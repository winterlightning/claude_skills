"""Layout (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '309fb1e3-e1dd-4884-9491-8855823b712b'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout_309fb1e3-e1dd-4884-9491-8855823b712b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Layout(Solo48):
    icon_id = 'layout'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('layout', 'interface-essential')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (24, 25), (42, 25))
        self.add_line('e1', (24, 25), (24, 42))
        self.add_line('e2', (24, 25), (24, 6))
        self.add_line('e3', (42, 25), (42, 42))
        self.add_line('e4', (42, 42), (24, 42))
        self.add_line('e5', (42, 25), (42, 6))
        self.add_line('e6', (42, 6), (24, 6))
        self.add_line('e7', (24, 42), (6, 42))
        self.add_line('e8', (6, 42), (6, 6))
        self.add_line('e9', (6, 6), (24, 6))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', closed=False)
        self.add_contour('c3', 'e3', 'e4', closed=False)
        self.add_contour('c4', 'e5', 'e6', closed=False)
        self.add_contour('c5', 'e7', 'e8', 'e9', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
