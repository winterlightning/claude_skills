"""Female User Profile Icon. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '7e7928dc-c2b2-4979-be45-5ca674afd12d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__female-user-profile-icon-solo/20260927T151732Z-thuan-mac-1/reference/full body women_7e7928dc-c2b2-4979-be45-5ca674afd12d.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'female-user-profile-icon-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('sub icon', 'female user profile icon')
    def build(self):
        # Round head and a long flared dress echo the full-body source.
        circle(self,'head',24,10,6)
        self.add_polyline('dress',(18,24),(30,24),(34,28),(40,38),
                          (31,38),(29,44),(19,44),(17,38),(8,38),
                          (14,28),closed=True)
