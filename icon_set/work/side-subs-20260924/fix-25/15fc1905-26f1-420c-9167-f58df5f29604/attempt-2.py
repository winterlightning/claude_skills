"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.primitives import Bezier, Point
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
        self.circle('lens',15,15,13)
        # The integer handle begins within the circle's painted stroke,
        # so its overlap forms a continuous joint with no visible inner stub.
        join=24
        self.add_line('handle',(join,join),(30,30))
        self.relate('connect','lens','handle')
        self.add_line('pill-left',(10,14),(14,10))
        self.add_bezier('pill-top',(14,10),((17,7),(22,12),(19,15)))
        self.add_line('pill-right',(19,15),(15,19))
        self.add_bezier('pill-bottom',(15,19),((12,22),(7,17),(10,14)))
        self.add_contour('capsule','pill-left','pill-top','pill-right','pill-bottom',closed=True)
        self.add_line('divider',(12,12),(17,17))
        self.relate('connect','divider','pill-left','pill-right')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

