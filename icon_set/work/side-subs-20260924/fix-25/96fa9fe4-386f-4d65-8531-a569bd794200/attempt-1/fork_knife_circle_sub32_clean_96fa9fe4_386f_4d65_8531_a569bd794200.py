"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '96fa9fe4-386f-4d65-8531-a569bd794200'
SOURCE_PATH = 'pictographic-primitives/state/circle fork knife_96fa9fe4-386f-4d65-8531-a569bd794200.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('circle frame', 'three-tined fork with bowl and handle', 'curved knife blade and handle')
class Drawing(Sub32):
    icon_id = 'fork-knife-circle-sub32-clean'
    variant_of = 'fork-knife-circle-sub32'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Fork and Knife Dining Symbol', 'core_parts': ('circle frame', 'three-tined fork with bowl and handle', 'curved knife blade and handle'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Shorten the blade and raise its heel; compress the fork bowl vertically while retaining all three tines.'}
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    TYPEFACE_GLYPH_IDS = ()
    def build(self):
        self.circle('frame',16,16,14)
        self.add_line('fork-left',(7,10),(7,14))
        self.add_bezier('cup',(7,14),((7,19),(16,19),(16,14)))
        self.add_line('fork-right',(16,14),(16,10))
        self.add_contour('fork','fork-left','cup','fork-right')
        self.add_line('fork-center',(11,10),(11,24))
        self.relate('connect','fork-center','cup')
        self.add_line('knife-back',(22,10),(22,23))
        self.add_bezier('blade',(22,10),((26,12),(27,15),(27,17)))
        self.add_line('heel',(27,17),(22,17))
        self.add_contour('knife-edge','blade','heel')
        self.relate('connect','knife-back','blade','heel')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

