"""Gavel block (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c48a60eb-d543-4958-b02f-1af524f7b1a0'
SOURCE_PATH = 'pictographic-primitives/state/gavel block_c48a60eb-d543-4958-b02f-1af524f7b1a0.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class GavelBlock(Solo48):
    icon_id = 'gavel-block'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('gavel', 'block', 'state')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (4, 8), (44, 8))
        self.add_line('e1', (44, 8), (44, 40))
        self.add_line('e2', (44, 40), (4, 40))
        self.add_line('e3', (4, 40), (4, 8))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', closed=True)
