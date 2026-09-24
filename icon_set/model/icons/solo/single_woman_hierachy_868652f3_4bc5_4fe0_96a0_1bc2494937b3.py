from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='868652f3-4bc5-4fe0-96a0-1bc2494937b3'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/single woman hierachy_868652f3-4bc5-4fe0-96a0-1bc2494937b3.svg'
AUTHOR='gpt-6'
PLAN='Woman plus three-node hierarchy. Human reference full_body_ref dress silhouette, head radius6 bottom18 to shoulder26 gives4 ink gap. Narrower body opens9-unit space beside spine and circle nodes. SQUARE6,6–42,42; Lucide network shared branch knots.'
class Drawing(Solo48):
    icon_id='single-woman-hierachy'
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
        self.circle('head',12,12,6)
        self.add_arc('shoulder-left',(8,28),(12,26),radius_x=4,radius_y=2)
        self.add_arc('shoulder-right',(12,26),(16,28),radius_x=4,radius_y=2)
        self.add_line('dress-right',(16,28),(18,36))
        self.add_line('hem-right',(18,36),(16,36))
        self.add_line('leg-right',(16,36),(16,42))
        self.add_line('feet',(16,42),(8,42))
        self.add_line('leg-left',(8,42),(8,36))
        self.add_line('hem-left',(8,36),(6,36))
        self.add_line('dress-left',(6,36),(8,28))
        self.add_contour('torso','shoulder-left','shoulder-right','dress-right','hem-right','leg-right','feet','leg-left','hem-left','dress-left',closed=True)
        ys=(9,24,39)
        self.add_polyline('spine',*((27,y) for y in ys))
        for i,y in enumerate(ys):
         self.circle(f'node-{i}',39,y,3)
         self.add_line(f'branch-{i}',(27,y),(36,y));self.relate('connect',f'branch-{i}','spine');self.relate('connect',f'branch-{i}',f'node-{i}')
