"""Skull and Crossbones Danger Circle. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '52524fee-82eb-4342-93ba-4c710b3efdd0'
SOURCE_PATH = 'pictographic-primitives/other/circle skull xmark_52524fee-82eb-4342-93ba-4c710b3efdd0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'skull-and-crossbones-danger-circle-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('sub icon', 'skull and crossbones danger circle')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        circle(self,'outline',24,24,20)
        self.add_bezier('skull',(19,27),((9,15),(19,10),(24,12)),((29,10),(39,15),(29,27)),((29,31),(29,32),(24,32)),((19,32),(19,31),(19,27)))
        self.add_contour('skull-shape','skull',closed=True)
        self.add_dot('eye-left',(20,21))
        self.add_dot('eye-right',(28,21))
        self.add_line('bone-a',(12,12),(35,35))
        self.add_line('bone-b',(12,35),(35,12))
        self.relate('connect','bone-a','bone-b','skull-shape')
