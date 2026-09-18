"""Circular Minus Symbol. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'ab7a719f-7c4a-4ed8-8dfb-01e3bb127cb4'
SOURCE_PATH = 'pictographic-primitives/other/circle minus_ab7a719f-7c4a-4ed8-8dfb-01e3bb127cb4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-minus-symbol-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'circular minus symbol')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        circle(self,'outline',24,24,20)
        self.add_line('minus',(14,24),(34,24))
