"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '52524fee-82eb-4342-93ba-4c710b3efdd0'
SOURCE_PATH = 'pictographic-primitives/other/circle skull xmark_52524fee-82eb-4342-93ba-4c710b3efdd0.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('outer circle', 'skull cranium and closed jaw', 'two eye dots', 'one central jaw divider', 'four diagonal marks behind skull')
class Drawing(Sub32):
    icon_id = 'circle-skull-crossbones-sub32-v2-clean'
    variant_of = 'circle-skull-crossbones-sub32-v2'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Skull and Crossbones Danger Circle', 'core_parts': ('outer circle', 'skull cranium and closed jaw', 'two eye dots', 'one central jaw divider', 'four diagonal marks behind skull'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Redraw the skull with a wider jaw, shorter central tooth and higher eyes; retain all four diagonal bones.'}
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    TYPEFACE_GLYPH_IDS = ()
    def build(self):
        self.circle('frame',16,16,14)
        for name,a,b in [('bone-tl',(8,8),(10,10)),('bone-tr',(24,8),(22,10)),('bone-bl',(8,24),(11,21)),('bone-br',(24,24),(21,21))]:self.add_line(name,a,b)
        self.skull()

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def skull(self,open_jaw=False):
        self.add_bezier('cranium',(11,23),((11,20),(11,19),(9,18)),((7,16),(8,11),(10,9)),((12,7),(20,7),(22,9)),((24,11),(25,16),(23,18)),((21,19),(21,20),(21,23)))
        if not open_jaw:
            self.add_line('jaw',(21,23),(11,23))
            self.add_contour('skull','cranium','jaw',closed=True)
        self.add_dot('eye-left',(13,14))
        self.add_dot('eye-right',(19,14))
        self.add_line('tooth',(16,21),(16,23))
        if not open_jaw:self.relate('connect','tooth','jaw')

