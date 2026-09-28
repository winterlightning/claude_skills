"""Horizontal Measurement Markers. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '5e331499-062d-4a4a-965e-e100d55ce756'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horizontal-measurement-markers-solo/20260927T151732Z-thuan-mac-1/reference/measurement markers_5e331499-062d-4a4a-965e-e100d55ce756.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horizontal-measurement-markers-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('sub icon', 'horizontal measurement markers')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_polyline('top',(44,8),(23,8),(17,20),(8,20),(4,16),
                          (4,12),(8,8),(23,8))
        self.add_polyline('bottom',(44,40),(44,32),(23,32),(17,28),
                          (8,28),(4,32),(4,36),(8,40),(23,40))
        self.add_line('measure',(31,24),(44,24))
