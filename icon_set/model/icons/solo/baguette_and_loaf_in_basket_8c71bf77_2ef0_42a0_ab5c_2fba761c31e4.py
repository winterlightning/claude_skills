"""Diagonal baguette sits behind a rounded loaf in a basket. Loaf top deliberately receives the baguette at28,20; this is a visible overlap, not a squeezed gap.
Construction: No useful exact Lucide match; source arrangement and geometric primitives.
Omissions: Scoring omitted. Baguette is partly hidden by the round loaf, matching the source overlap.
Keyshape SQUARE: exact contract extremes, stroke 4.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8c71bf77-2ef0-42a0-ab5c-2fba761c31e4'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_08/bread baguette_8c71bf77-2ef0-42a0-ab5c-2fba761c31e4.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='baguette-and-loaf-in-basket'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('baguette', 'and', 'loaf', 'in', 'basket')
    def build(self):
        self.path('baguette',(6,28),[('L',(19,10)),('C',(26,6),(22,6),(23,6)),('C',(31,17),(34,6),(36,12)),('L',(28,20))])
        self.path('loaf',(24,28),[('C',(28,20),(24,24),(24,20)),('L',(34,20)),('C',(42,28),(38,20),(42,24))])
        self.path('basket',(6,28),[('L',(24,28)),('L',(42,28)),('C',(24,42),(42,37),(34,42)),('C',(6,28),(14,42),(6,37))],True)
        self.join('basket','baguette');self.join('basket','loaf');self.join('baguette','loaf')

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
