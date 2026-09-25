"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.primitives import Bezier, Point
SOURCE_ICON_ID = '1d8d8f36-b3e7-43ec-9137-f4dfa75706db'
SOURCE_PATH = 'pictographic-primitives/other/magnifying glass t_1d8d8f36-b3e7-43ec-9137-f4dfa75706db.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('circular magnifier lens', 'lower-right handle', 'uppercase T with source-style horizontal caps')
class Drawing(Sub32):
    icon_id = 'text-search-magnifier-sub32-v2-clean'
    variant_of = 'text-search-magnifier-sub32-v2'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Text Search Magnifying Glass', 'core_parts': ('circular magnifier lens', 'lower-right handle', 'uppercase T with source-style horizontal caps'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Enlarge the magnifier lens, center the complete inner symbol and use an integer handle joint within the painted circle stroke.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('other', 'state', 'primitives-generate')
    TYPEFACE_GLYPH_IDS = ('letter-t-uppercase',)
    def build(self):
        self.circle('frame',15,15,13)
        # The integer handle begins within the circle's painted stroke,
        # so its overlap forms a continuous joint with no visible inner stub.
        join=24
        self.add_line('handle',(join,join),(30,30))
        self.relate('connect','handle','frame')
        self.add_line('glyph-T-bar',(9,12),(21,12))
        self.add_line('glyph-T-stem',(15,12),(15,20))
        self.add_line('serif-left',(9,12),(9,14))
        self.add_line('serif-right',(21,12),(21,14))
        self.add_line('serif-foot',(13,20),(17,20))
        self.relate('connect','glyph-T-bar','serif-left','serif-right','glyph-T-stem')
        self.relate('connect','glyph-T-stem','serif-foot')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

