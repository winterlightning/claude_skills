"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '15fc1905-26f1-420c-9167-f58df5f29604'
SOURCE_PATH = 'pictographic-primitives/other/magnifying glass pill_15fc1905-26f1-420c-9167-f58df5f29604.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('circular magnifier lens', 'lower-right handle', 'diagonal capsule outline', 'one transverse divider')
class Drawing(Sub32):
    icon_id = 'medicine-search-sub32-clean'
    variant_of = 'medicine-search-sub32'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Medicine Search Magnifying Glass', 'core_parts': ('circular magnifier lens', 'lower-right handle', 'diagonal capsule outline', 'one transverse divider'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Retain the balanced diagonal pill construction and replace the legacy stroke override with the plain 4px SUB32 profile.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    TYPEFACE_GLYPH_IDS = ()
    def build(self):
        self.circle('lens',14,14,12)
        join=14+12/(2**0.5)
        self.add_line('handle',(join,join),(30,30))
        self.relate('connect','lens-bottom','handle')
        self.add_line('pill-left',(8,13),(13,8))
        self.add_bezier('pill-top',(13,8),((17,4),(23,10),(19,14)))
        self.add_line('pill-right',(19,14),(14,19))
        self.add_bezier('pill-bottom',(14,19),((10,23),(4,17),(8,13)))
        self.add_contour('capsule','pill-left','pill-top','pill-right','pill-bottom',closed=True)
        self.add_line('divider',(10,11),(16,17))
        self.relate('connect','divider','pill-left','pill-right')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

