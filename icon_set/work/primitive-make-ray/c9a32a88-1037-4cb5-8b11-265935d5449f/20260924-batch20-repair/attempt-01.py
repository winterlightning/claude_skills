from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='c9a32a88-1037-4cb5-8b11-265935d5449f'
SOURCE_PATH='pictographic-primitives/weather/visibility_c9a32a88-1037-4cb5-8b11-265935d5449f.svg'
AUTHOR='gpt-6'
PLAN='Visibility mark with closed left triangle, dashed range and100 below. HRECT_L4,8–44,40 opens digit counters and gaps. Dash count reduced from3 to2, numeral1 serif/base omitted; all three digits retained. No useful exact Lucide match.'
class Drawing(Solo48):
    icon_id='visibility'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
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
        self.add_polyline('triangle',(4,16),(16,8),(16,24),closed=True)
        self.add_line('dash-0',(25,16),(29,16));self.add_line('dash-1',(38,16),(44,16))
        self.add_line('one',(4,28),(4,40))
        for i,x in enumerate((12,32)):
         self.box(f'zero-{i}',x,28,x+12,40,4)
