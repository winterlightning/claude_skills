"""Circular Check Mark Symbol. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'e827e098-b2c1-4c9d-a347-ed197ce977ef'
SOURCE_PATH = 'pictographic-primitives/other/circle check 1_e827e098-b2c1-4c9d-a347-ed197ce977ef.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-check-mark-symbol-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('sub icon', 'circular check mark symbol')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_arc('open-circle',(44,24),(24,4),radius_x=20,large_arc=True)
        self.add_polyline('check',(16,23),(24,31),(40,14))
