"""Circular Down Right Arrow. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '3965b3cb-3cad-4439-8fe1-ea32aefe85a5'
SOURCE_PATH = 'pictographic-primitives/other/circle arrow down right_3965b3cb-3cad-4439-8fe1-ea32aefe85a5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-down-right-arrow-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('sub icon', 'circular down right arrow')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        circle(self,'outline',24,24,20)
        self.add_line('shaft',(16,16),(31,31))
        self.add_polyline('head',(22,31),(31,31),(31,22))
        self.relate('connect','shaft','head')
