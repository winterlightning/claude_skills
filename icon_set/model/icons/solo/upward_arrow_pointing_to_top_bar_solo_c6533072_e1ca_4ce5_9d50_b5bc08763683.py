"""Upward Arrow Pointing To Top Bar. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'c6533072-e1ca-4ce5-9d50-b5bc08763683'
SOURCE_PATH = 'pictographic-primitives/other/move top_c6533072-e1ca-4ce5-9d50-b5bc08763683.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upward-arrow-pointing-to-top-bar-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('sub icon', 'upward arrow pointing to top bar')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_line('bar',(4,8),(44,8))
        self.add_line('shaft',(24,40),(24,17))
        self.add_polyline('head',(14,27),(24,17),(34,27))
        self.relate('connect','shaft','head')
