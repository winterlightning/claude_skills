"""Square Horizontal Exchange Arrows. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '78aaab68-fc23-4751-a93d-0e4f746ad065'
SOURCE_PATH = 'pictographic-primitives/other/square arrow opposite_78aaab68-fc23-4751-a93d-0e4f746ad065.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-horizontal-exchange-arrows-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('sub icon', 'square horizontal exchange arrows')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        rounded_rect(self,'outline',6,6,42,42,5)
        self.add_polyline('top',(32,19),(16,19),(20,15))
        self.add_polyline('bottom',(16,29),(32,29),(28,33))
