"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '57555bcf-ee23-4c81-88cb-5400ea13984b'
SOURCE_PATH = 'pictographic-primitives/symbol/laptop person_57555bcf-ee23-4c81-88cb-5400ea13984b.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rounded laptop screen', 'circular outlined user head', 'open curved shoulders', 'trapezoidal laptop base')
class Drawing(Sub32):
    exception = {'reason': 'User-approved complete reference composition; accept remaining visual/grid/spacing findings while preserving 32x32 and uniform 4px strokes.', 'approved_by': 'user', 'approved_on': '2026-09-24', 'svg_sha256': 'b4ea2d8d9979a68a2332ddd5be9f096405460fd43ff376c92deebfe4fce25dd6'}
    icon_id = 'laptop-user-profile-sub32-v2-clean'
    variant_of = 'laptop-user-profile-sub32-v2'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Laptop User Profile', 'core_parts': ('rounded laptop screen', 'circular outlined user head', 'open curved shoulders', 'trapezoidal laptop base'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Give the laptop base a full gap and restore a curved shoulder arch; retain the circular head.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    TYPEFACE_GLYPH_IDS = ()
    def build(self):
        self.box('screen',4,2,28,24,2)
        self.circle('head',16,9,3)
        self.add_bezier('shoulders',(10,19),((10,15),(22,15),(22,19)))
        self.add_polyline('base',(4,24),(2,30),(30,30),(28,24))
        self.relate('connect','base-1','screen-4')
        self.relate('connect','base-3','screen-4')

    def box(self,name,left,top,right,bottom,r):
        points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        for i,a in enumerate(points):
            b=points[(i+1)%8]
            if i%2:self.add_arc(f'{name}-{i}',a,b,radius_x=r)
            else:self.add_line(f'{name}-{i}',a,b)
        self.add_contour(name,*[f'{name}-{i}' for i in range(8)],closed=True)

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

