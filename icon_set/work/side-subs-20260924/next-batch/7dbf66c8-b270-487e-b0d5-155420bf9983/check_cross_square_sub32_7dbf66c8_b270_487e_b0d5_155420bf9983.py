"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7dbf66c8-b270-487e-b0d5-155420bf9983'
SOURCE_PATH = 'pictographic-primitives/other/rectangle remove and check_7dbf66c8-b270-487e-b0d5-155420bf9983.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rounded square frame', 'upper-left checkmark', 'diagonal rising divider', 'lower-right cross')

class Drawing(Sub32):
    icon_id = 'check-cross-square-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    keywords = ('check', 'and', 'cross', 'square')


    def build(self):
        self.box('frame',2,2,30,30,2)
        self.add_polyline('check',(6,12),(9,16),(14,8))
        self.add_line('divider',(11,27),(21,5))
        self.add_line('cross-a',(21,22),(26,27))
        self.add_line('cross-b',(26,22),(21,27))
        self.relate('connect','cross-a','cross-b')

    def box(self,name,left,top,right,bottom,r):
        points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        for i,a in enumerate(points):
            b=points[(i+1)%8]
            if i%2:self.add_arc(f'{name}-{i}',a,b,radius_x=r)
            else:self.add_line(f'{name}-{i}',a,b)
        self.add_contour(name,*[f'{name}-{i}' for i in range(8)],closed=True)

