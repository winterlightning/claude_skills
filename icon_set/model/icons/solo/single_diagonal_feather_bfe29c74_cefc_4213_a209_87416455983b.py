"""Diagonal feather vane owns two coherent sides and one deliberate notch; straight quill passes through shared base point.
Construction: Lucide feather original/atomic-debug: diagonal quill and vane seam; source supplies pointed tip and notch.
Omissions: Fine barb texture omitted; a single notch restores feather identity.
Keyshape SQUARE: exact contract extremes, stroke 4.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bfe29c74-cefc-4213-a209-87416455983b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/plume_bfe29c74-cefc-4213-a209-87416455983b.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='single-diagonal-feather'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('single', 'diagonal', 'feather')
    def build(self):
        self.path('vane',(12,36),[('C',(6,25),(8,34),(6,31)),('C',(42,6),(6,12),(27,6)),('C',(36,24),(42,13),(40,19)),('L',(31,26)),('L',(34,28)),('C',(12,36),(28,35),(20,40))],True)
        self.poly('quill',(6,42),(12,36),(28,20));self.join('vane','quill')

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
