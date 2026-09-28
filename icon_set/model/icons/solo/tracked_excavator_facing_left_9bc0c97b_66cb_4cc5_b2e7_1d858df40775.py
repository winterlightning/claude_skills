"""Excavator has a rounded cab and track, articulated straight boom and smooth scooping bucket. Track is a capsule with true semicircular ends.
Construction: No useful exact Lucide match; source arrangement and geometric primitives.
Omissions: Track rollers, glazing division and narrow double boom omitted.
Keyshape HRECT_L: exact contract extremes, stroke 4.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9bc0c97b-66cb-4cc5-b2e7-1d858df40775'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/excavator 1_9bc0c97b-66cb-4cc5-b2e7-1d858df40775.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='tracked-excavator-facing-left'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "construction"
    categories = ("construction", "primitive", "primitives")
    aliases=()
    keywords=('tracked', 'excavator', 'facing', 'left')
    def build(self):
        self.path('track',(26,32),[('L',(40,32)),('A',(40,40),4,4,True),('L',(26,40)),('A',(26,32),4,4,True)],True)
        self.path('cab',(26,32),[('L',(26,24)),('L',(26,10)),('A',(28,8),2,2,True),('L',(36,8)),('A',(38,10),2,2,True),('L',(38,32))]);self.join('cab','track')
        self.poly('boom',(26,24),(16,14),(8,18));self.join('boom','cab')
        self.path('bucket',(8,18),[('L',(5,24)),('C',(4,27),(4,26),(4,26)),('C',(13,31),(4,31),(10,31))]);self.join('bucket','boom')

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
