"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '15e4830e-dce1-452c-9f05-87646ea11df9'
SOURCE_PATH = 'pictographic-primitives/romance/love gift box heart_15e4830e-dce1-452c-9f05-87646ea11df9.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rectangular gift box', 'two bow loops above the box', 'heart outline on the box')
class Drawing(Sub32):
    exception = {'reason': 'User-approved complete reference composition; accept remaining visual/grid/spacing findings while preserving 32x32 and uniform 4px strokes.', 'approved_by': 'user', 'approved_on': '2026-09-24', 'svg_sha256': '92a28f2139c837d5a58c878073d0f1781dfb0227bd8b1a87d6584896654cfff2'}
    icon_id = 'heart-gift-box-sub32-clean'
    variant_of = 'heart-gift-box-sub32'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Heart Gift Box', 'core_parts': ('rectangular gift box', 'two bow loops above the box', 'heart outline on the box'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Use paired smoother bow loops and raise the heart tip away from the bottom of the gift box.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'romance'
    categories = ('primitives', 'romance')
    TYPEFACE_GLYPH_IDS = ()
    def build(self):
        self.box('box',2,11,30,30,1)
        self.add_bezier('bow-left',(16,11),((10,11),(4,9),(4,5)),((4,1),(10,1),(16,11)))
        self.add_bezier('bow-right',(16,11),((22,11),(28,9),(28,5)),((28,1),(22,1),(16,11)))
        self.relate('connect','bow-left','bow-right','box-0')
        self.add_bezier('heart',(16,19),((12,15),(8,19),(11,22)),((13,24),(14,25),(16,26)),((18,25),(19,24),(21,22)),((24,19),(20,15),(16,19)))

    def box(self,name,left,top,right,bottom,r):
        points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        for i,a in enumerate(points):
            b=points[(i+1)%8]
            if i%2:self.add_arc(f'{name}-{i}',a,b,radius_x=r)
            else:self.add_line(f'{name}-{i}',a,b)
        self.add_contour(name,*[f'{name}-{i}' for i in range(8)],closed=True)

