"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '15e4830e-dce1-452c-9f05-87646ea11df9'
SOURCE_PATH = 'pictographic-primitives/romance/love gift box heart_15e4830e-dce1-452c-9f05-87646ea11df9.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rectangular gift box', 'two bow loops above the box', 'heart outline on the box')

class Drawing(Sub32):
    icon_id = 'heart-gift-box-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    keywords = ('heart', 'gift', 'box')


    def build(self):
        self.box('box',2,11,30,30,1)
        self.add_bezier('bow-left',(16,11),((12,1),(4,0),(4,5)),((4,10),(11,11),(16,11)))
        self.add_bezier('bow-right',(16,11),((20,1),(28,0),(28,5)),((28,10),(21,11),(16,11)))
        self.relate('connect','bow-left','bow-right','box-0')
        self.add_bezier('heart',(16,19),((12,14),(7,18),(11,22)),((13,24),(14,25),(16,27)),((18,25),(19,24),(21,22)),((25,18),(20,14),(16,19)))

    def box(self,name,left,top,right,bottom,r):
        points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        for i,a in enumerate(points):
            b=points[(i+1)%8]
            if i%2:self.add_arc(f'{name}-{i}',a,b,radius_x=r)
            else:self.add_line(f'{name}-{i}',a,b)
        self.add_contour(name,*[f'{name}-{i}' for i in range(8)],closed=True)

