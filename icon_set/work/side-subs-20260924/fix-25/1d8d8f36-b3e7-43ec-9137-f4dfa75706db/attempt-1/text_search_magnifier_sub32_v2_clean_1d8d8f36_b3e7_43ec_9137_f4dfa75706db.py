"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '1d8d8f36-b3e7-43ec-9137-f4dfa75706db'
SOURCE_PATH = 'pictographic-primitives/other/magnifying glass t_1d8d8f36-b3e7-43ec-9137-f4dfa75706db.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('circular magnifier lens', 'lower-right handle', 'uppercase T with source-style horizontal caps')
class Drawing(Sub32):
    icon_id = 'text-search-magnifier-sub32-v2-clean'
    variant_of = 'text-search-magnifier-sub32-v2'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Text Search Magnifying Glass', 'core_parts': ('circular magnifier lens', 'lower-right handle', 'uppercase T with source-style horizontal caps'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Move the full serif T inward, shorten the side caps and lift the foot away from the lens.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    TYPEFACE_GLYPH_IDS = ('letter-t-uppercase',)
    def build(self):
        self.circle('frame',14,14,12)
        join=14+12/(2**0.5)
        self.add_line('handle',(join,join),(30,30))
        self.relate('connect','handle','frame-bottom')
        self.add_line('glyph-T-bar',(9,10),(19,10))
        self.add_line('glyph-T-stem',(14,10),(14,18))
        self.add_line('serif-left',(9,10),(9,12))
        self.add_line('serif-right',(19,10),(19,12))
        self.add_line('serif-foot',(12,18),(16,18))
        self.relate('connect','glyph-T-bar','serif-left','serif-right','glyph-T-stem')
        self.relate('connect','glyph-T-stem','serif-foot')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

