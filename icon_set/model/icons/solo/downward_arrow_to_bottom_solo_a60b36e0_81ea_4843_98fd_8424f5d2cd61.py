"""Downward Arrow To Bottom. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'a60b36e0-81ea-4843-98fd-8424f5d2cd61'
SOURCE_PATH = 'pictographic-primitives/other/move bottom_a60b36e0-81ea-4843-98fd-8424f5d2cd61.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'downward-arrow-to-bottom-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'downward arrow to bottom')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_line('bar',(4,40),(44,40))
        self.add_line('shaft',(24,8),(24,31))
        self.add_polyline('head',(14,21),(24,31),(34,21))
        self.relate('connect','shaft','head')
