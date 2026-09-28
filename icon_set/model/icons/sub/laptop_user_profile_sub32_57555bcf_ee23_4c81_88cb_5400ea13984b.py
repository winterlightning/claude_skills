"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '57555bcf-ee23-4c81-88cb-5400ea13984b'
SOURCE_PATH = 'pictographic-primitives/symbol/laptop person_57555bcf-ee23-4c81-88cb-5400ea13984b.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rounded laptop screen', 'circular outlined user head', 'open curved shoulders', 'trapezoidal laptop base')

class Drawing(Sub32):
    icon_id = 'laptop-user-profile-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    keywords = ('laptop', 'user', 'profile')
    STROKE_WIDTH = 4
    PATH_STROKE_WIDTHS = {'screen': 4, 'base': 4}
    COMPACT_EXCEPTION = 'User requested uniform 4px strokes on a 32px canvas. Spacing and grid findings are retained for review.'
    def to_record(self):
        record=super().to_record()
        record['style']['path_stroke_widths']=dict(self.PATH_STROKE_WIDTHS)
        record['compact_exception']=self.COMPACT_EXCEPTION
        return record

    def build(self):
        self.box('screen',4,4,28,23,2)
        self.circle('head',16,10,3)
        self.add_bezier('shoulders',(10,20),((10,16),(22,16),(22,20)))
        # Base shares the screen bottom endpoints; no keyboard or extra marks added.
        self.add_line('base-left',(4,23),(2,27))
        self.add_bezier('base-bottom',(2,27),((1,28),(2,28),(4,28)),((12,28),(20,28),(28,28)),((30,28),(31,28),(30,27)))
        self.add_line('base-right',(30,27),(28,23))
        self.add_contour('base','base-left','base-bottom','base-right')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self,name,left,top,right,bottom,r):
        points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        for i,a in enumerate(points):
            b=points[(i+1)%8]
            if i%2:self.add_arc(f'{name}-{i}',a,b,radius_x=r)
            else:self.add_line(f'{name}-{i}',a,b)
        self.add_contour(name,*[f'{name}-{i}' for i in range(8)],closed=True)

