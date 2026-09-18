"""Upward Arrow Inside Circle. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '7bd3a2bd-439f-4018-b851-acf302ef01a5'
SOURCE_PATH = 'pictographic-primitives/other/circle arrow up_7bd3a2bd-439f-4018-b851-acf302ef01a5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upward-arrow-inside-circle-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'upward arrow inside circle')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        circle(self,'outline',24,24,20)
        self.add_line('shaft',(24,34),(24,16))
        self.add_polyline('head',(17,23),(24,16),(31,23))
        self.relate('connect','shaft','head')
