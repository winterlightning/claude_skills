"""User Profile in Circle. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.
Circular head and broad shoulder arc; detached head/body centerline gap 8.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '04ecc27d-03d8-408a-819d-858967c25768'
SOURCE_PATH = 'pictographic-primitives/other/person_04ecc27d-03d8-408a-819d-858967c25768.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'user-profile-circle-190-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('sub icon', 'user profile in circle')
    def build(self):
        # Plan: Circular head and broad shoulder arc; detached head/body centerline gap 8.
        circle(self,'outline',24,24,20)
        circle(self,'head',24,18,4)
        self.add_arc('shoulders',(17,32),(31,32),radius_x=7,radius_y=2)
