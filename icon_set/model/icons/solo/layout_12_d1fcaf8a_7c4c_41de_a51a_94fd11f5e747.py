"""Layout 12 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd1fcaf8a-7c4c-41de-a51a-94fd11f5e747'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout 12_d1fcaf8a-7c4c-41de-a51a-94fd11f5e747.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Layout12(Solo48):
    icon_id = 'layout-12'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (24, 27), (42, 27))
        self.add_line('e1', (24, 27), (24, 42))
        self.add_line('e2', (24, 27), (24, 17))
        self.add_line('e3', (42, 27), (42, 42))
        self.add_line('e4', (42, 42), (24, 42))
        self.add_line('e5', (42, 27), (42, 17))
        self.add_line('e6', (24, 17), (42, 17))
        self.add_line('e7', (24, 17), (24, 6))
        self.add_line('e8', (24, 42), (6, 42))
        self.add_line('e9', (6, 42), (6, 6))
        self.add_line('e10', (6, 6), (24, 6))
        self.add_line('e11', (42, 17), (42, 6))
        self.add_line('e12', (42, 6), (24, 6))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', closed=False)
        self.add_contour('c3', 'e3', 'e4', closed=False)
        self.add_contour('c4', 'e5', closed=False)
        self.add_contour('c5', 'e6', closed=False)
        self.add_contour('c6', 'e7', closed=False)
        self.add_contour('c7', 'e8', 'e9', 'e10', closed=False)
        self.add_contour('c8', 'e11', 'e12', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c7')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c5', 'c8')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c7', 'c8')
