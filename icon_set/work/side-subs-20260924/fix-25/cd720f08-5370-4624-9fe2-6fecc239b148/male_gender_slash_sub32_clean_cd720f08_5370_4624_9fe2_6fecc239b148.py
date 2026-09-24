"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = 'cd720f08-5370-4624-9fe2-6fecc239b148'
SOURCE_PATH = 'pictographic-primitives/pets/male stablization_cd720f08-5370-4624-9fe2-6fecc239b148.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('lower-left circle', 'upper-right arrow with two-stroke head', 'diagonal upper-left to lower-right slash')
class Drawing(Sub32):
    icon_id = 'male-gender-slash-sub32-clean'
    variant_of = 'male-gender-slash-sub32'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Male Gender Symbol with Slash', 'core_parts': ('lower-left circle', 'upper-right arrow with two-stroke head', 'diagonal upper-left to lower-right slash'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Extend both arrowhead arms evenly while preserving the circle and diagonal slash.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    TYPEFACE_GLYPH_IDS = ()
    def build(self):
        self.circle('circle',12,20,10)
        self.add_line('shaft',(18,12),(30,2))
        self.add_polyline('arrowhead',(22,2),(30,2),(30,10))
        self.relate('connect','shaft','arrowhead-1','arrowhead-2','circle-top')
        self.add_line('slash',(2,10),(22,30))
        self.relate('connect','slash','circle')
        self.relate('connect','shaft','circle')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

