"""Layout 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '63fa50d7-4f0b-438a-9923-2f535be24705'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout 1_63fa50d7-4f0b-438a-9923-2f535be24705.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Layout1(Solo48):
    icon_id = 'layout-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (42, 30), (30, 30))
        self.add_line('e1', (42, 30), (42, 42))
        self.add_line('e2', (42, 42), (30, 42))
        self.add_line('e3', (42, 30), (42, 17))
        self.add_line('e4', (30, 42), (30, 30))
        self.add_line('e5', (30, 42), (18, 42))
        self.add_line('e6', (18, 30), (18, 42))
        self.add_line('e7', (18, 30), (30, 30))
        self.add_line('e8', (18, 30), (6, 30))
        self.add_line('e9', (18, 42), (6, 42))
        self.add_line('e10', (6, 42), (6, 30))
        self.add_line('e11', (6, 30), (6, 6))
        self.add_line('e12', (6, 6), (30, 6))
        self.add_line('e13', (30, 6), (30, 17))
        self.add_line('e14', (30, 6), (42, 6))
        self.add_line('e15', (42, 6), (42, 17))
        self.add_line('e16', (30, 17), (42, 17))
        self.add_line('e17', (30, 17), (30, 30))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', 'e2', closed=False)
        self.add_contour('c2', 'e3', closed=False)
        self.add_contour('c3', 'e4', closed=False)
        self.add_contour('c4', 'e5', closed=False)
        self.add_contour('c5', 'e6', closed=False)
        self.add_contour('c6', 'e7', closed=False)
        self.add_contour('c7', 'e8', closed=False)
        self.add_contour('c8', 'e9', 'e10', closed=False)
        self.add_contour('c9', 'e11', 'e12', closed=False)
        self.add_contour('c10', 'e13', closed=False)
        self.add_contour('c11', 'e14', 'e15', closed=False)
        self.add_contour('c12', 'e16', closed=False)
        self.add_contour('c13', 'e17', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c13')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c13', 'c3')
        self.relate('connect', 'c13', 'c6')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c11', 'c12')
        self.relate('connect', 'c11', 'c2')
        self.relate('connect', 'c12', 'c2')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c5', 'c8')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c7', 'c9')
        self.relate('connect', 'c8', 'c9')
        self.relate('connect', 'c10', 'c11')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c11', 'c9')
        self.relate('connect', 'c10', 'c12')
        self.relate('connect', 'c10', 'c13')
        self.relate('connect', 'c12', 'c13')
