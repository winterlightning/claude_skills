"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = 'b2e51317-7251-4abe-a7c5-6e845a33f1c5'
SOURCE_PATH = 'pictographic-primitives/other/square folk_b2e51317-7251-4abe-a7c5-6e845a33f1c5.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rounded square frame', 'circular spoon bowl', 'attached vertical spoon handle', 'upright knife with curved blade and horizontal heel', 'vertical knife handle')
class Drawing(Sub32):
    exception = {'reason': 'User-approved complete reference composition; accept remaining visual/grid/spacing findings while preserving 32x32 and uniform 4px strokes.', 'approved_by': 'user', 'approved_on': '2026-09-24', 'svg_sha256': '8c41eb48a8293142de1f472b8637ad98aae309dc742990c45645a15ff056fd99'}
    icon_id = 'square-spoon-knife-sub32-clean'
    variant_of = 'square-spoon-knife-sub32'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Square Spoon and Knife', 'core_parts': ('rounded square frame', 'circular spoon bowl', 'attached vertical spoon handle', 'upright knife with curved blade and horizontal heel', 'vertical knife handle'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Use a smaller circular spoon bowl with more space between utensils and a shorter curved knife blade.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    TYPEFACE_GLYPH_IDS = ()
    def build(self):
        self.box('frame',2,2,30,30,2)
        self.circle('bowl',10,12,4)
        self.add_line('spoon-handle',(10,16),(10,24))
        self.relate('connect','bowl','spoon-handle')
        self.add_line('knife-back',(20,9),(20,24))
        self.add_bezier('blade',(20,9),((24,11),(25,14),(25,17)))
        self.add_line('heel',(25,17),(20,17))
        self.add_contour('knife-edge','blade','heel')
        self.relate('connect','knife-back','blade','heel')

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

