"""Computer Mouse Arrow Cursor. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '1b142e96-a7ca-4d29-b690-c751a7da7802'
SOURCE_PATH = 'pictographic-primitives/other/cursor left 2_1b142e96-a7ca-4d29-b690-c751a7da7802.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'computer-mouse-arrow-cursor-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('sub icon', 'computer mouse arrow cursor')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_polyline('pointer',(6,6),(42,20),(30,27),(40,37),(33,42),(23,32),(20,42),closed=True)
