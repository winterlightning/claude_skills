"""Hidden Visibility Eye Symbol. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.
Preserve the diagonal hidden-visibility slash and eye contour.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '90c55c1b-6141-40f9-8dfb-e0b9bed3cb5e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hidden-visibility-eye-symbol-solo/20260927T151732Z-thuan-mac-1/reference/eye slash_90c55c1b-6141-40f9-8dfb-e0b9bed3cb5e.svg'
AUTHOR = "gpt-6"

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
        self.add_bezier('upper',(4,24),((13,4),(35,4),(44,24)))
        self.add_bezier('lower',(44,24),((35,44),(13,44),(4,24)))
        self.add_contour('eye','upper','lower',closed=True)
        # The diagonal now projects beyond the eye at both ends, as in the source.
        self.add_line('slash',(8,40),(40,8))
        self.relate('connect','eye','slash')
