"""A rounded case with small circular hub releases a folded tape; the narrow double ribbon is reduced to one coherent stroke."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c343118f-b51a-5b6a-8e51-fa898e3a785d'
SOURCE_PATH = 'pictographic-primitives/tools/measure construction_c343118f-b51a-5b6a-8e51-fa898e3a785d.svg'
AUTHOR = 'gpt-6'

class ExtendedTapeMeasure(Solo48):
    icon_id = 'extended-tape-measure'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('tape measure', 'measure', 'measuring tape', 'ruler', 'length', 'construction', 'tape', 'tool')

    def build(self) -> None:

        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def box(n,x,y,w,h,r=0):
            if not r:
                self.add_polyline(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
                return
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for j in range(8):
                a,b=pts[j],pts[(j+1)%8]
                if j%2:self.add_arc(n+str(j),a,b,radius_x=r)
                else:self.add_line(n+str(j),a,b)
            self.add_contour(n,*[n+str(j) for j in range(8)],closed=True)

        box('case',4,8,26,22,8)
        circle('hub',17,19,2)
        self.add_line('tape-start',(22,30),(39,30))
        self.add_arc('tape-turn',(39,30),(39,40),radius_x=5)
        self.add_line('tape-return',(39,40),(13,40))
        self.add_contour('tape','tape-start','tape-turn','tape-return')
        self.relate('connect','tape','case')
