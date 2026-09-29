"""Hill (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '05b90623-0dc3-40f3-b859-59417f7a43d8'
SOURCE_PATH = 'pictographic-primitives/transportation/hill_05b90623-0dc3-40f3-b859-59417f7a43d8.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Hill(Solo48):
    icon_id = 'hill'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('hill', 'transportation')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (4, 40), (4, 9))
        self.add_line('e1', (6, 8), (43, 38))
        self.add_line('e2', (43, 40), (4, 40))
        self.add_line('e3', (4, 9), (6, 8))
        self.add_arc('e4-1', (43, 38), (44, 39), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_arc('e4-2', (44, 39), (43, 40), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_contour('c0', 'e0', 'e3', 'e1', 'e4-1', 'e4-2', 'e2', closed=True)
