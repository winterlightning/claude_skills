"""Upward Growth Trend. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '53e82e45-ef3e-43ae-b6e0-83e2e67c469d'
SOURCE_PATH = 'pictographic-primitives/other/circle arrow trend up_53e82e45-ef3e-43ae-b6e0-83e2e67c469d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upward-growth-trend-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'upward growth trend')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        circle(self,'outline',24,24,20)
        self.add_polyline('trend',(14,28),(21,21),(27,27),(33,20))
        self.add_polyline('head',(26,20),(33,20),(33,27))
        self.relate('connect','trend','head')
