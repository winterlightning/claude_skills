"""Hand saw with clean straight blade edges and two repeated teeth. Rounded open grip replaces sharp square handle corners.
Construction: No useful exact Lucide match; source arrangement and geometric primitives.
Omissions: Grip hole reduced to open grip; tooth count reduced to two large teeth.
Keyshape HRECT_L: exact contract extremes, stroke 4.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fb9e5252-41fd-4313-ae36-6711e4c93e41'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/handsaw_fb9e5252-41fd-4313-ae36-6711e4c93e41.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='toothed-hand-saw-batch-064'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('toothed', 'hand', 'saw', 'batch', '064')
    def build(self):
        self.path('grip',(4,22),[('L',(4,36)),('A',(8,40),4,4,False),('L',(12,40)),('A',(16,36),4,4,False),('L',(16,18))])
        self.poly('blade',(16,18),(44,8),(44,20),(36,20),(32,28),(28,28),(24,36),(16,36))
        self.join('grip','blade')

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
