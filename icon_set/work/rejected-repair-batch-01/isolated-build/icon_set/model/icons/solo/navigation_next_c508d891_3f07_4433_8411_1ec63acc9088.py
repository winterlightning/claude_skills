"""Navigation next (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c508d891-3f07-4433-8411-1ec63acc9088'
SOURCE_PATH = 'pictographic-primitives/interface-essential/navigation next_c508d891-3f07-4433-8411-1ec63acc9088.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class NavigationNext(Solo48):
    icon_id = 'navigation-next'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'next', 'interface-essential')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (37, 8), (42, 14))
        self.add_line('e1', (42, 14), (44, 16))
        self.add_line('e2', (26, 16), (44, 16))
        self.add_line('e3', (37, 25), (44, 16))
        self.add_line('e4', (25, 8), (4, 8))
        self.add_line('e5', (4, 8), (4, 40))
        self.add_line('e6', (4, 40), (28, 40))
        self.add_line('e7', (28, 40), (28, 26))
        self.add_arc('e8', (18, 31), (26, 16), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_contour('c0', 'e0', 'e1', closed=False)
        self.add_contour('c1', 'e8', 'e2', closed=False)
        self.add_contour('c2', 'e3', closed=False)
        self.add_contour('c3', 'e4', 'e5', 'e6', 'e7', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
