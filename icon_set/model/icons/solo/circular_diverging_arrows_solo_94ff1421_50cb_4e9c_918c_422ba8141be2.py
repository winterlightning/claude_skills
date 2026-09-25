"""Circular Diverging Arrows. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '94ff1421-50cb-4e9c-918c-422ba8141be2'
SOURCE_PATH = 'pictographic-primitives/other/circle split arrow_94ff1421-50cb-4e9c-918c-422ba8141be2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-diverging-arrows-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('sub icon', 'circular diverging arrows')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        circle(self,'outline',24,24,20)
        self.add_bezier('left',(24,34),((24,24),(20,20),(16,16)))
        self.add_bezier('right',(24,34),((24,24),(28,20),(32,16)))
        self.add_polyline('head-left',(16,23),(16,16),(23,16))
        self.add_polyline('head-right',(25,16),(32,16),(32,23))
        self.relate('connect','left','right')
        self.relate('connect','left','head-left')
        self.relate('connect','right','head-right')
