from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='d19fe7af-bf3f-4193-8210-2e69b664727e'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/side road angle right 2_d19fe7af-bf3f-4193-8210-2e69b664727e.svg'
AUTHOR='gpt-6'
PLAN='Diamond sign with upward road arrow and lower right branch. Radial CIRCLE envelope20; shared true branch node24,25. Shorter branch keeps full source arrangement.'
class Drawing(Solo48):
    icon_id='side-road-angle-right-2'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "Uncategorized"
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,l,t,r,b,q=3):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)

    def build(self):
        self.add_polyline('diamond',(24,4),(44,24),(24,44),(4,24),closed=True)
        self.add_polyline('shaft',(24,31),(24,25),(24,17))
        self.add_polyline('head',(20,21),(24,17),(28,21));self.relate('connect','shaft','head')
        self.add_line('branch',(24,25),(27,29));self.relate('connect','branch','shaft')
