from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='7a8b5b6b-d72f-42df-9379-3389fd1e33fd'
SOURCE_PATH='pictographic-primitives/_uncategorized_33/self driving car_7a8b5b6b-d72f-42df-9379-3389fd1e33fd.svg'
AUTHOR='gpt-6'
PLAN='Front car retains roof, fascia and wheels; simplify radio to one broad arc and omit crowded headlights. Mirrored about x24; Lucide car-front joined construction. SQUARE extremes6,6–42,42.'
class Drawing(Solo48):
    icon_id='self-driving-car'
    keyshape=Keyshape.SQUARE
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
        self.box('body',6,26,42,36,4)
        self.add_polyline('roof',(12,26),(16,18),(32,18),(36,26));self.relate('connect','body','roof')
        for i,x in enumerate((12,36)):
         self.add_line(f'wheel-{i}',(x,36),(x,42));self.relate('connect','body',f'wheel-{i}')
        self.add_arc('radio-outer',(14,10),(34,10),radius_x=10,radius_y=4)
