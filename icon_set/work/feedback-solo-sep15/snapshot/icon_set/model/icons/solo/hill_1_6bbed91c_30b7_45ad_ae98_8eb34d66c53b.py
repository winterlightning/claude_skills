"""Hill 1 (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6bbed91c-30b7-45ad-ae98-8eb34d66c53b'
SOURCE_PATH = 'pictographic-primitives/symbol/hill 1_6bbed91c-30b7-45ad-ae98-8eb34d66c53b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Hill1(Solo48):
    icon_id = 'hill-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('hill', 'symbol')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (44, 40), (44, 9))
        self.add_line('e1', (42, 8), (5, 38))
        self.add_line('e2', (5, 40), (44, 40))
        self.add_line('e3', (44, 9), (42, 8))
        self.add_arc('e4-1', (5, 38), (4, 39), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('e4-2', (4, 39), (5, 40), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_contour('c0', 'e0', 'e3', 'e1', 'e4-1', 'e4-2', 'e2', closed=True)
