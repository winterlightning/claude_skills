from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='c9a32a88-1037-4cb5-8b11-265935d5449f'
SOURCE_PATH='pictographic-primitives/weather/visibility_c9a32a88-1037-4cb5-8b11-265935d5449f.svg'
AUTHOR='gpt-6'
PLAN='Visibility: closed left-facing triangle over clear100, two horizontal range dashes. SQUARE6,6–42,42. Equal rounded zeros9×11 with9-unit gaps; numeral1 serif/base and third dash omitted. Source arrangement retained; no useful exact Lucide match.'
class Drawing(Solo48):
    icon_id='visibility'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "weather"
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
        self.add_polyline('triangle',(6,14),(18,6),(18,22),closed=True)
        self.add_line('dash-0',(27,14),(29,14));self.add_line('dash-1',(38,14),(42,14))
        self.add_line('one',(6,31),(6,42))
        for i,x in enumerate((15,33)):self.box(f'zero-{i}',x,31,x+9,42,4)
