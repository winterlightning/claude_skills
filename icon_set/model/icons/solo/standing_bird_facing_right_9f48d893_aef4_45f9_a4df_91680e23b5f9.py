"""Right-facing bird has a round head, continuous back and breast, pointed tail, curved wing and paired feet. All belly attachments are explicit.
Construction: Lucide bird original/atomic-debug: flowing breast, pointed tail and single wing curve.
Omissions: Eye and feather hatching omitted; rightward asymmetry follows the source.
Keyshape SQUARE: exact contract extremes, stroke 4.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9f48d893-aef4-45f9-a4df-91680e23b5f9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/fowl_9f48d893-aef4-45f9-a4df-91680e23b5f9.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='standing-bird-facing-right'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('standing', 'bird', 'facing', 'right')
    def build(self):
        self.path('outline',(6,36),[('L',(14,28)),('L',(21,21)),('C',(25,13),(23,19),(25,17)),('A',(32,6),7,7,True),('A',(39,13),7,7,True),('L',(42,15)),('L',(39,17)),('C',(30,33),(39,26),(36,33)),('L',(20,33)),('C',(6,36),(16,33),(12,36))],True)
        self.path('wing',(14,28),[('C',(27,18),(25,28),(30,24))]);self.join('outline','wing')
        for j,x in enumerate((20,30)):
         self.line('leg'+str(j),(x,33),(x+2,42));self.join('leg'+str(j),'outline')
         self.line('foot'+str(j),(x-1,42),(x+5,42));self.join('leg'+str(j),'foot'+str(j))

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
