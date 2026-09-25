"""Sweating grin with a coherent circular face arc and a symmetric droplet. Smooth closed smile and one happy eye; upper-right face rim opens behind sweat.
Construction: No useful exact Lucide match; source arrangement and geometric primitives.
Omissions: Right eye and tooth divisions omitted for sweat clearance; wide closed grin retained.
Keyshape CIRCLE: exact contract extremes, stroke 4.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5a09584a-4888-47cb-81af-7c5eb6f78a57'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/41-5a09584a-4888-47cb-81af-7c5eb6f78a57.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='toothy-grin-with-sweat-droplet'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('toothy', 'grin', 'with', 'sweat', 'droplet')
    def build(self):
        self.path('face',(24,4),[('A',(4,24),20,20,False),('A',(24,44),20,20,False),('A',(40,36),20,20,False)])
        self.path('sweat',(36,8),[('C',(32,16),(34,12),(32,14)),('A',(40,16),4,4,False),('C',(36,8),(40,14),(38,12))],True)
        self.path('eye',(14,19),[('C',(22,19),(16,15),(20,15))])
        self.path('mouth',(14,28),[('L',(30,28)),('A',(14,28),8,7,True)],True)

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
