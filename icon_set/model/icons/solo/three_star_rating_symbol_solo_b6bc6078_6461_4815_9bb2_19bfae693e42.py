"""Three equal outlined stars in a triangular rating cluster.
Lucide star original and atomic-debug inform the five-point contours.
Shared widened vertices preserve open centers; HRECT_L extrema (4,8)-(44,40).
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
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('sub icon', 'three star rating symbol')
    def build(self):
        # Three equal five-point stars, shared local vertices; top and lower pair
        # meet HRECT_L extrema (4,8)-(44,40). Lucide star informs open centers.
        points=((0,-7),(3,-3),(8,-2),(5,2),(5,7),(0,4),(-5,7),(-5,2),(-8,-2),(-3,-3))
        for name,cx,cy in [('top',24,15),('left',12,33),('right',36,33)]:
            self.add_polyline(name,*[(cx+x,cy+y) for x,y in points],closed=True)
