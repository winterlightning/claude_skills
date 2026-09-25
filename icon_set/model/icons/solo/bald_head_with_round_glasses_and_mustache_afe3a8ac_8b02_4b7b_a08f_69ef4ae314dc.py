"""Circular bald face owns mirrored round spectacles and a smooth symmetric moustache. Shared axis x24.
Construction: Lucide glasses original and atomic-debug: equal circular lenses linked by a bridge.
Omissions: Ears and enclosed moustache outline omitted; bald face and spectacles retained.
Keyshape CIRCLE: exact contract extremes, stroke 4.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'afe3a8ac-8b02-4b7b-a08f-69ef4ae314dc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/great grandfather_afe3a8ac-8b02-4b7b-a08f-69ef4ae314dc.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='bald-head-with-round-glasses-and-mustache'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('bald', 'head', 'with', 'round', 'glasses', 'and', 'mustache')
    def build(self):
        self.circle('head',24,24,20)
        for side in (-1,1):self.circle('lens-'+str(side),24+side*7,19,3)
        self.line('bridge',(20,19),(28,19))
        for side in (-1,1):self.join('bridge','lens-'+str(side))
        self.path('mustache',(17,32),[('C',(24,32),(19,28),(22,32)),('C',(31,32),(26,32),(29,28))])

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
