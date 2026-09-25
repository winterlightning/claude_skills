"""User Profile with Plus Symbol. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '5c48e4cd-7e6c-4903-8a9d-8562b0e49909'
SOURCE_PATH = 'pictographic-primitives/other/doctor_5c48e4cd-7e6c-4903-8a9d-8562b0e49909.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'user-profile-with-plus-symbol-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('sub icon', 'user profile with plus symbol')
    human_construction = 'bust'
    def build(self):
        circle(self,'head',24,14,8)
        self.add_arc('body',(6,42),(42,42),radius_x=18,radius_y=16)
        self.relate('connect','head','body')
        self.add_polyline('h',(18,38),(24,38),(30,38))
        self.add_polyline('v',(24,35),(24,38),(24,42))
        self.relate('connect','h','v')
