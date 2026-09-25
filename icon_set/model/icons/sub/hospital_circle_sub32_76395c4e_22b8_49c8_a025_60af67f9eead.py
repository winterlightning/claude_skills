"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '76395c4e-22b8-49c8-a025-60af67f9eead'
SOURCE_PATH = 'pictographic-primitives/transportation/hospital_76395c4e-22b8-49c8-a025-60af67f9eead.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('complete circular frame', 'uppercase H hospital symbol')

class Drawing(Sub32):
    icon_id = 'hospital-circle-sub32'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    keywords = ('hospital', 'symbol', 'in', 'circle')
    TYPEFACE_GLYPH_IDS = ('letter-h-uppercase',)

    def build(self):
        self.circle('frame',16,16,14)
        self.add_line('text-H-0-0-0-0',(11, 10),(11, 22))
        self.add_line('text-H-0-1-0-0',(21, 10),(21, 22))
        self.add_line('text-H-0-2-0-0',(11, 16),(21, 16))

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

