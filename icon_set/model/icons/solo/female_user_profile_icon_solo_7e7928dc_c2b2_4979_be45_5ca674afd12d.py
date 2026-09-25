"""Female User Profile Icon. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '7e7928dc-c2b2-4979-be45-5ca674afd12d'
SOURCE_PATH = 'pictographic-primitives/other/full body women_7e7928dc-c2b2-4979-be45-5ca674afd12d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'female-user-profile-icon-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('sub icon', 'female user profile icon')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        circle(self,'head',24,10,6)
        self.add_polyline('dress',(18,24),(14,24),(8,36),(17,36),(19,44),(29,44),(31,36),(40,36),(34,24),(30,24),closed=True)
