"""Symbol light recon (war), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2aaace93-e1e9-502b-b60c-566a934e76be'
SOURCE_PATH = 'pictographic-primitives/war/symbol light recon_2aaace93-e1e9-502b-b60c-566a934e76be.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class SymbolLightRecon(Solo48):
    icon_id = 'symbol-light-recon'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    categories = ('war', 'primitives')
    aliases = ()
    keywords = ('symbol', 'light', 'recon', 'war')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (4, 40), (4, 8))
        self.add_line('e1', (4, 8), (44, 8))
        self.add_line('e2', (44, 8), (5, 40))
        self.add_line('e3', (5, 40), (44, 40))
        self.add_line('e4', (44, 40), (44, 8))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', closed=False)
