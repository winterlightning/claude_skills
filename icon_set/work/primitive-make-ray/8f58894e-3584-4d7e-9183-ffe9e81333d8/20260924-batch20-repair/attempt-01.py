from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='8f58894e-3584-4d7e-9183-ffe9e81333d8'
SOURCE_PATH='pictographic-primitives/war/tools tear gas_8f58894e-3584-4d7e-9183-ffe9e81333d8.svg'
AUTHOR='gpt-6'
PLAN='Tear gas: upper-left eye joins full falling tear, open gas plume above horizontal canister at right. HRECT_L4,8–44,40. Pupil, lower eyelid and small gas dot omitted for clearance; Lucide eye/droplet/spray-can geometric construction.'
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
        self.add_arc('eye',(4,16),(22,16),radius_x=9,radius_y=8)
        self.add_bezier('tear',(4,16),((4,22),(4,27),(4,30)),((4,38),(16,38),(16,30)),((16,24),(9,21),(4,16)))
        self.add_contour('drop','tear',closed=True);self.relate('connect','eye','drop')
        self.add_arc('gas',(32,18),(44,18),radius_x=6,radius_y=10)
        self.box('canister',26,28,42,40,3)
        self.add_line('nozzle',(42,34),(44,34));self.relate('connect','nozzle','canister')
