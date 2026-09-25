"""Bird Footprint Symbol. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'ac9f5eb0-9ca6-4ae8-b650-3216bba2d023'
SOURCE_PATH = 'pictographic-primitives/other/bird print_ac9f5eb0-9ca6-4ae8-b650-3216bba2d023.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bird-footprint-symbol-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('sub icon', 'bird footprint symbol')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_polyline('stem',(24,4),(24,26),(24,44))
        self.add_polyline('toes',(8,14),(24,26),(40,14))
        self.relate('connect','stem','toes')
