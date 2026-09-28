"""Double Upward Chevron Arrow. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'c97fe46d-5a12-431f-8533-e38efec4ac69'
SOURCE_PATH = 'pictographic-primitives/other/double arrow up_c97fe46d-5a12-431f-8533-e38efec4ac69.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'double-upward-chevron-arrow-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('sub icon', 'double upward chevron arrow')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_polyline('outline',(6,18),(24,6),(42,18),(42,42),(24,30),(6,42),closed=True)
        self.add_polyline('divider',(6,30),(24,18),(42,30))
        self.relate('connect','outline','divider')
