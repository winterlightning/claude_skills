"""Upward Pointing Chevron. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '93e589ef-a49d-4782-8494-d3c593234d3c'
SOURCE_PATH = 'pictographic-primitives/other/double arrow up 1_93e589ef-a49d-4782-8494-d3c593234d3c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upward-pointing-chevron-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'upward pointing chevron')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_polyline('chevron',(4,24),(24,8),(44,24),(44,40),(24,24),(4,40),closed=True)
