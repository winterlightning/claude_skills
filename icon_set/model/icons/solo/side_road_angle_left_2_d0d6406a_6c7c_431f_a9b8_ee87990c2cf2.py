from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='d0d6406a-6c7c-431f-a9b8-ee87990c2cf2'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/side road angle left 2_d0d6406a-6c7c-431f-a9b8-ee87990c2cf2.svg'
AUTHOR='gpt-6'
PLAN='Complete diamond sign and curved rightward arrow follow reference direction despite filename. Radial CIRCLE envelope reaches20 at four vertices. Rebalanced arrow; no defining parts omitted.'
class Drawing(Solo48):
    icon_id='side-road-angle-left-2'
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
        self.add_line('stem',(20,28),(20,27))
        self.add_arc('turn',(20,27),(26,21),radius_x=6)
        self.add_line('shaft',(26,21),(29,21));self.add_contour('road','stem','turn','shaft')
        self.add_polyline('head',(25,17),(29,21),(25,25));self.relate('connect','road','head')
