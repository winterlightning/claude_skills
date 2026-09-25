"""Independent full icon-solo drawing from the original batch-04 brief."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cf0d9970-8b38-5723-b109-a3be9696acdb'
SOURCE_PATH = 'pictographic-primitives/rating/rating star three_cf0d9970-8b38-5723-b109-a3be9696acdb.svg'
AUTHOR = 'gpt-6'


class IndependentSolo(Solo48):
    icon_id = 'three-star-rating-row-v3'
    variant_of = 'three-star-rating-row'
    variant_label = 'Independent icon-solo; original reference only'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rating'
    aliases = ()
    keywords = ('three', 'star', 'rating', 'row')

    def build(self):
        # Plan: three identical upright stars in one centered horizontal series.
        # HRECT_M requested extremes (4,10)-(44,38). A faithful shallow row cannot
        # reach the vertical extremes: retain that keyshape blocker, never stretch stars.
        # Lucide star informs the alternating tips and valleys of each coherent contour.
        for i,cx in enumerate((10,24,38)):
            points=[(0,-7),(2,-2),(6,-2),(3,2),(4,7),(0,4),(-4,7),(-3,2),(-6,-2),(-2,-2)]
            self.add_polyline(f'star-{i}',*((cx+x,24+y) for x,y in points),closed=True)
