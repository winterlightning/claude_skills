"""Wrapped Candy Sweet.

Horizontally wrapped candy with a broad central sweet and two triangular flared ends. Centerline extremes (4,10)-(44,38). Mirrored wrapper wings share the central body seam endpoints. Lucide candy informs integrated wrapper topology; omit decorative stripes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '65190295-301f-48c4-9b55-daa2e73e7886'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wrapped-candy-pointed-ends/20260927T082307Z-thuan-mac-1/reference/candy_65190295-301f-48c4-9b55-daa2e73e7886.svg'
AUTHOR = "gpt-6"

class WrappedCandyPointedEnds(Solo48):
    icon_id = 'wrapped-candy-pointed-ends'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('food', 'state')
    aliases = ()
    keywords = ('wrapped', 'candy', 'sweet')

    def build(self):
        # One oval sweet and two mirrored triangular wrapper ends.
        self.add_arc('sweet-top',(14,24),(34,24),radius_x=10,radius_y=14,sweep=True)
        self.add_arc('sweet-bottom',(34,24),(14,24),radius_x=10,radius_y=14,sweep=True)
        self.add_contour('sweet','sweet-top','sweet-bottom',closed=True)
        self.add_polyline('left-wrap',(14,24),(4,10),(4,38),closed=True)
        self.add_polyline('right-wrap',(34,24),(44,10),(44,38),closed=True)
        self.relate('connect','sweet','left-wrap')
        self.relate('connect','sweet','right-wrap')
