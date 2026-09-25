"""Layout 5 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00a510ed-d94a-4187-aafa-6dd3cdcc5eed'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout 5_00a510ed-d94a-4187-aafa-6dd3cdcc5eed.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Layout5(Solo48):
    icon_id = 'layout-5'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('layout', 'interface-essential')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (24, 32), (44, 32))
        self.add_line('e1', (24, 32), (24, 40))
        self.add_line('e2', (24, 32), (24, 24))
        self.add_line('e3', (24, 24), (44, 24))
        self.add_line('e4', (24, 24), (24, 16))
        self.add_line('e5', (44, 24), (44, 32))
        self.add_line('e6', (44, 24), (44, 16))
        self.add_line('e7', (24, 16), (44, 16))
        self.add_line('e8', (24, 16), (24, 8))
        self.add_line('e9', (44, 32), (44, 40))
        self.add_line('e10', (44, 40), (24, 40))
        self.add_line('e11', (24, 40), (4, 40))
        self.add_line('e12', (4, 40), (4, 8))
        self.add_line('e13', (4, 8), (24, 8))
        self.add_line('e14', (44, 16), (44, 8))
        self.add_line('e15', (44, 8), (24, 8))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', closed=False)
        self.add_contour('c3', 'e3', closed=False)
        self.add_contour('c4', 'e4', closed=False)
        self.add_contour('c5', 'e5', closed=False)
        self.add_contour('c6', 'e6', closed=False)
        self.add_contour('c7', 'e7', closed=False)
        self.add_contour('c8', 'e8', closed=False)
        self.add_contour('c9', 'e9', 'e10', closed=False)
        self.add_contour('c10', 'e11', 'e12', 'e13', closed=False)
        self.add_contour('c11', 'e14', 'e15', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c9')
        self.relate('connect', 'c5', 'c9')
        self.relate('connect', 'c1', 'c10')
        self.relate('connect', 'c1', 'c9')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c11', 'c6')
        self.relate('connect', 'c11', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c10', 'c11')
        self.relate('connect', 'c10', 'c8')
        self.relate('connect', 'c11', 'c8')
