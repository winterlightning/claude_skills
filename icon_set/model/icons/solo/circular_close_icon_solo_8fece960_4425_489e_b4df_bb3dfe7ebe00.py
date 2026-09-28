"""Circular Close Icon. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '8fece960-4425-489e-b4df-bb3dfe7ebe00'
SOURCE_PATH = 'pictographic-primitives/other/circle remove_8fece960-4425-489e-b4df-bb3dfe7ebe00.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-close-icon-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('sub icon', 'circular close icon')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        circle(self,'outline',24,24,20)
        self.add_polyline('cross-a',(17,17),(24,24),(31,31))
        self.add_polyline('cross-b',(17,31),(24,24),(31,17))
        self.relate('connect','cross-a','cross-b')
