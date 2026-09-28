"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '638f0a9f-914c-4078-b32c-13c8ec4aacf6'
SOURCE_PATH = 'pictographic-primitives/other/battery 1_638f0a9f-914c-4078-b32c-13c8ec4aacf6.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rounded rectangular battery body', 'separate right terminal', 'centered zigzag lightning bolt')
class Drawing(Sub32):
    icon_id = 'charging-battery-sub32-clean'
    variant_of = 'charging-battery-sub32'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Charging Battery Symbol', 'core_parts': ('rounded rectangular battery body', 'separate right terminal', 'centered zigzag lightning bolt'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Widen the open lightning zigzag to distinguish both bends and recenter it within the battery.'}
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    TYPEFACE_GLYPH_IDS = ()
    def build(self):
        self.box('body',2,6,24,26,3)
        self.add_line('terminal',(30,12),(30,20))
        self.add_polyline('bolt',(16,11),(10,16),(16,16),(10,21))

    def box(self,name,left,top,right,bottom,r):
        points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        for i,a in enumerate(points):
            b=points[(i+1)%8]
            if i%2:self.add_arc(f'{name}-{i}',a,b,radius_x=r)
            else:self.add_line(f'{name}-{i}',a,b)
        self.add_contour(name,*[f'{name}-{i}' for i in range(8)],closed=True)

