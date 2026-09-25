"""Hidden Visibility Eye Symbol. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.
Preserve the diagonal hidden-visibility slash and eye contour.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '90c55c1b-6141-40f9-8dfb-e0b9bed3cb5e'
SOURCE_PATH = 'pictographic-primitives/other/eye slash_90c55c1b-6141-40f9-8dfb-e0b9bed3cb5e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hidden-visibility-eye-symbol-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('sub icon', 'hidden visibility eye symbol')
    def build(self):
        # Plan: Preserve the diagonal hidden-visibility slash and eye contour.
        self.add_bezier('upper',(4,24),((14,3),(34,3),(44,24)))
        self.add_bezier('lower',(44,24),((34,45),(14,45),(4,24)))
        self.add_contour('eye','upper','lower',closed=True)
        self.add_line('slash',(10,40),(38,8))
        self.relate('connect','eye','slash')
