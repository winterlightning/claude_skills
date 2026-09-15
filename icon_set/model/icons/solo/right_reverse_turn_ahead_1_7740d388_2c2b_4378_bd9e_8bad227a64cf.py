"""Right reverse turn ahead 1 (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7740d388-2c2b-4378-bd9e-8bad227a64cf'
SOURCE_PATH = 'pictographic-primitives/symbol/right reverse turn ahead 1_7740d388-2c2b-4378-bd9e-8bad227a64cf.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class RightReverseTurnAhead1(Solo48):
    icon_id = 'right-reverse-turn-ahead-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('right', 'reverse', 'turn', 'ahead', 'symbol')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (8, 44), (8, 23))
        self.add_line('e1', (8, 23), (30, 23))
        self.add_line('e2', (30, 23), (30, 4))
        self.add_line('e3', (30, 4), (21, 12))
        self.add_line('e4', (30, 4), (40, 12))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', closed=False)
        self.add_contour('c1', 'e4', closed=False)
        self.relate('connect', 'c0', 'c1')
