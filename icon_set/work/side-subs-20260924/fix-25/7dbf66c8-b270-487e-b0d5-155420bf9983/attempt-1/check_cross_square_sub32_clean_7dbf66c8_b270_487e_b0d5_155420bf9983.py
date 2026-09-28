"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '7dbf66c8-b270-487e-b0d5-155420bf9983'
SOURCE_PATH = 'pictographic-primitives/other/rectangle remove and check_7dbf66c8-b270-487e-b0d5-155420bf9983.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rounded square frame', 'upper-left checkmark', 'diagonal rising divider', 'lower-right cross')
class Drawing(Sub32):
    icon_id = 'check-cross-square-sub32-clean'
    variant_of = 'check-cross-square-sub32'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Check and Cross Square', 'core_parts': ('rounded square frame', 'upper-left checkmark', 'diagonal rising divider', 'lower-right cross'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Move the checkmark and cross inward and detach both ends of the divider from the frame.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    TYPEFACE_GLYPH_IDS = ()
    def build(self):
        self.box('frame',2,2,30,30,2)
        self.add_polyline('check',(7,12),(10,15),(14,8))
        self.add_line('divider',(10,26),(22,6))
        self.add_line('cross-a',(20,21),(25,26))
        self.add_line('cross-b',(25,21),(20,26))
        self.relate('connect','cross-a','cross-b')

    def box(self,name,left,top,right,bottom,r):
        points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        for i,a in enumerate(points):
            b=points[(i+1)%8]
            if i%2:self.add_arc(f'{name}-{i}',a,b,radius_x=r)
            else:self.add_line(f'{name}-{i}',a,b)
        self.add_contour(name,*[f'{name}-{i}' for i in range(8)],closed=True)

