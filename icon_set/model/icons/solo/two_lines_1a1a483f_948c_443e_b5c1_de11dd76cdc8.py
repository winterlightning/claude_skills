"""Two lines (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a1a483f-948c-443e-b5c1-de11dd76cdc8'
SOURCE_PATH = 'pictographic-primitives/symbol/two lines_1a1a483f-948c-443e-b5c1-de11dd76cdc8.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class TwoLines(Solo48):
    icon_id = 'two-lines'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('two', 'lines', 'symbol')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (40, 4), (40, 44))
        self.add_line('e1', (40, 44), (8, 44))
        self.add_contour('c0', 'e0', 'e1', closed=False)
