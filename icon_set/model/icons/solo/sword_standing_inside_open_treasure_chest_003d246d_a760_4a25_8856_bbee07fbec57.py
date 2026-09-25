"""Diagonal sword axis is straight through grip and blade; crossguard is perpendicular. Rounded chest has a centered top attachment and continuous lower corners.
Construction: No useful exact Lucide match; source arrangement and geometric primitives.
Omissions: Double chest rim and blade width reduced; pommel, straight sword and perpendicular guard retained.
Keyshape VRECT_L: exact contract extremes, stroke 4.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '003d246d-a760-4a25-8856-bbee07fbec57'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_26/loot box treasure chest reward 2_003d246d-a760-4a25-8856-bbee07fbec57.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='sword-standing-inside-open-treasure-chest'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "rewards"
    categories = ("rewards", "primitive", "primitives")
    aliases=()
    keywords=('sword', 'standing', 'inside', 'open', 'treasure', 'chest')
    def build(self):
        self.circle('pommel',32,7,3)
        self.line('grip',(32,10),(26,18))
        self.line('blade',(26,18),(20,26))
        self.poly('guard',(22,15),(26,18),(30,21))
        for a,b in [('pommel','grip'),('grip','blade'),('grip','guard'),('blade','guard')]:self.join(a,b)
        self.path('chest',(8,26),[('L',(20,26)),('L',(40,26)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,26))],True)
        self.join('chest','blade')

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
