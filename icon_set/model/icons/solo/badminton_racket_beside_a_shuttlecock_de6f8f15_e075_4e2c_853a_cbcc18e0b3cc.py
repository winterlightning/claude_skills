"""Circular racket with aligned cross strings and diagonal handle; shuttle feather wedge and round cork share one contour.
Construction: No useful exact Lucide match; source arrangement and geometric primitives.
Omissions: Dense string mesh reduced to a centered cross; individual shuttle feathers omitted.
Keyshape HRECT_L: exact contract extremes, stroke 4.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "de6f8f15-e075-4e2c-853a-cbcc18e0b3cc"
SOURCE_PATH = "pictographic-primitives/_uncategorized_05/badminton shuttlecock racquet_de6f8f15-e075-4e2c-853a-cbcc18e0b3cc.svg"
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='badminton-racket-beside-a-shuttlecock'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('badminton', 'racket', 'beside', 'a', 'shuttlecock')
    def build(self):
        # Handle attachment is an exact 6-8-10 point on the rim.
        self.path('rim',(34,8),[('A',(44,18),10,10,True),('A',(34,28),10,10,True),('A',(28,26),10,10,True),('A',(24,18),10,10,True),('A',(34,8),10,10,True)],True)
        self.line('handle',(28,26),(10,40)); self.join('rim','handle')
        self.line('string-v',(34,8),(34,28));self.line('string-h',(24,18),(44,18))
        for s in ('string-v','string-h'):self.join('rim',s)
        self.path('shuttle',(4,8),[('L',(16,8)),('L',(14,19)),('C',(10,23),(13.6,21.2),(12,23)),('C',(6,19),(8,23),(6.4,21.2)),('L',(4,8))],True)

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
