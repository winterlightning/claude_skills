"""Equal large wheels share y34 and radius6. Body corners use matched quarter arcs, cab roof is rounded and straight edges stay straight.
Construction: Lucide tractor: circular wheels and simplified raised cab.
Omissions: Wheel hubs and window divisions omitted.
Keyshape HRECT_L: exact contract extremes, stroke 4.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '87fdb6c4-b392-445f-b29f-1ee390cf87cd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/jeep_87fdb6c4-b392-445f-b29f-1ee390cf87cd.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='simple-off-road-vehicle'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/reference"
    aliases=()
    keywords=('simple', 'off', 'road', 'vehicle')
    def build(self):
        for n,x in [('rear-wheel',10),('front-wheel',38)]: self.circle(n,x,34,6)
        self.path('body',(4,34),[('L',(4,22)),('A',(6,20),2,2,True),('L',(16,20)),('L',(34,20)),('L',(42,20)),('A',(44,22),2,2,True),('L',(44,34))])
        self.path('cab',(16,20),[('L',(18,10)),('C',(20,8),(18.4,8),(19,8)),('L',(32,8)),('A',(34,10),2,2,True),('L',(34,20))])
        for n in ['rear-wheel','front-wheel','cab']:self.join('body',n)

    def path(self,n,p,steps,closed=False):
        ids=[]
        for j,step in enumerate(steps):
            k,q,*v=step; uid=f'{n}-{j}'
            if k=='L': self.add_line(uid,p,q)
            elif k=='A': self.add_arc(uid,p,q,radius_x=v[0],radius_y=v[1],sweep=v[2])
            elif k=='C': self.add_bezier(uid,p,(v[0],v[1],q))
            ids.append(uid);p=q
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,rad=2):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
    def line(self,n,a,b): self.add_line(n,a,b)
    def poly(self,n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
    def join(self,a,b): self.relate('connect',a,b)
