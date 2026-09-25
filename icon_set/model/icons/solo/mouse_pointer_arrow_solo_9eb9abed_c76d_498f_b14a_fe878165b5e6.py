"""Mouse Pointer Arrow. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.
One directional pointer contour; asymmetric triangular cursor.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '9eb9abed-c76d-498f-b14a-fe878165b5e6'
SOURCE_PATH = 'pictographic-primitives/other/cursor left_9eb9abed-c76d-498f-b14a-fe878165b5e6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mouse-pointer-arrow-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('sub icon', 'mouse pointer arrow')
    def build(self):
        # Plan: One directional pointer contour; asymmetric triangular cursor.
        self.add_polyline('pointer',(8,4),(40,27),(24,31),(16,44),closed=True)
