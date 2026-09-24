from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='8f58894e-3584-4d7e-9183-ffe9e81333d8'
SOURCE_PATH='pictographic-primitives/war/tools tear gas_8f58894e-3584-4d7e-9183-ffe9e81333d8.svg'
AUTHOR='gpt-6'
PLAN='Cry eye with pupil and lower lid, full hanging tear, puffy gas above horizontal canister. HRECT_L4,8–44,40; joins have shared nodes. Lucide eye/droplet/spray-can construction; tiny gas dot and canister stripe omitted.'
class Drawing(Solo48):
    icon_id='tools-tear-gas'
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
        self.add_arc('eye-upper',(4,16),(22,16),radius_x=9,radius_y=8)
        self.add_bezier('eye-lower',(22,16),((22,18),(21,20),(20,21)))
        self.add_contour('eye','eye-upper','eye-lower')
        self.add_dot('pupil',(13,17))
        self.add_line('tear-stem',(4,16),(4,24));self.relate('connect','tear-stem','eye')
        self.add_bezier('tear',(4,24),((4,27),(4,30),(4,32)),((4,40),(16,40),(16,32)),((16,28),(9,26),(4,24)))
        self.add_contour('drop','tear',closed=True);self.relate('connect','tear-stem','drop')
        self.add_bezier('gas',(32,18),((30,18),(30,14),(33,14)),((32,8),(38,8),(40,10)),((44,12),(44,15),(44,18)))
        pts=[(29,28),(39,28),(42,31),(42,34),(42,37),(39,40),(29,40),(26,37),(26,31),(29,28)]
        ids=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
         n=f'canister-{i}';ids.append(n)
         if i in [1,4,6,8]:self.add_arc(n,a,b,radius_x=3)
         else:self.add_line(n,a,b)
        self.add_contour('canister',*ids,closed=True)
        self.add_line('nozzle',(42,34),(44,34));self.relate('connect','nozzle','canister')
