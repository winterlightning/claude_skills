"""User Profile Selection Cursor. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '742a102d-2547-4878-9ea9-c64ad681d52b'
SOURCE_PATH = 'pictographic-primitives/other/cursor head_742a102d-2547-4878-9ea9-c64ad681d52b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'user-profile-selection-cursor-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('sub icon', 'user profile selection cursor')
    def build(self):
        self.add_arc('head-upper',(6,19),(32,19),radius_x=13)
        self.add_arc('head-lower',(19,32),(6,19),radius_x=13)
        self.add_contour('head','head-lower','head-upper')
        self.add_polyline('cursor',(26,25),(42,33),(35,35),(32,42),closed=True)
