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
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'three star rating symbol')
    def build(self):
        # Three matching five-point outlines in a triangular rating group.
        def star(name,cx,cy):
            points=[(0,-8),(3,-3),(8,-3),(4,2),(5,8),(0,5),(-5,8),(-4,2),(-8,-3),(-3,-3)]
            self.add_polyline(name,*[(cx+x,cy+y) for x,y in points],closed=True)
        star('top',24,14)
        star('left',14,34)
        star('right',34,34)
