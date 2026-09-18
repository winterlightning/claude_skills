"""Three Star Rating Symbol. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'b6bc6078-6461-4815-9bb2-19bfae693e42'
SOURCE_PATH = 'pictographic-primitives/other/three stars_b6bc6078-6461-4815-9bb2-19bfae693e42.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-star-rating-symbol-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'three star rating symbol')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        def star(name,cx,cy):
         self.add_polyline(name,(cx,cy-6),(cx+2,cy-2),(cx+6,cy-2),(cx+3,cy+1),(cx+4,cy+6),(cx,cy+3),(cx-4,cy+6),(cx-3,cy+1),(cx-6,cy-2),(cx-2,cy-2),closed=True)
        star('top',24,14)
        star('left',10,34)
        star('right',38,34)
