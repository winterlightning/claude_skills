"""Symmetric almond eye with diagonal obscuring slash; smooth cubic arcs have shared slash attachment knots.
Keyshape HRECT_M. Lucide eye-off: smooth almond contour and coherent diagonal; original specifies a complete lens.
Omissions: No omissions."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2f48fc2c-5ebe-4a21-b259-42ee5c3ca129'
SOURCE_PATH = 'pictographic-primitives/symbol/hidden_2f48fc2c-5ebe-4a21-b259-42ee5c3ca129.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'hidden'
    keyshape = Keyshape.HRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases=()
    keywords=('hidden',)

    def build(self):

        def path(n, start, steps, closed=False):
            members=[]; here=start
            for i,(kind,end,*a) in enumerate(steps):
                if here==end: continue
                tag=f'{n}-{i}'
                if kind=='L': self.add_line(tag,here,end)
                elif kind=='A': self.add_arc(tag,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C': self.add_bezier(tag,here,(a[0],a[1],end))
                members.append(tag); here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,q=4):
            path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('outline',(4,24),[('C',(14,13),(7,19),(10,15)),('C',(24,10),(18,11),(21,10)),('C',(44,24),(32,10),(39,17)),('C',(34,35),(41,29),(38,33)),('C',(24,38),(30,37),(27,38)),('C',(4,24),(16,38),(9,31))],True)
        line('slash',(14,13),(34,35));join('slash','outline')

