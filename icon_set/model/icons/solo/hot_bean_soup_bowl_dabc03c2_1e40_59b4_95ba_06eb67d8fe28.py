"""Broad bowl with two separated curved steam wisps and one recognizable bean. Smooth bowl contour and large bean opening.
Keyshape HRECT_L. Lucide soup: simple smooth bowl and long coherent steam strokes.
Omissions: One bean, rear rim and foot omitted to preserve spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dabc03c2-1e40-59b4-95ba-06eb67d8fe28'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/bean soup_dabc03c2-1e40-59b4-95ba-06eb67d8fe28.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'hot-bean-soup-bowl'
    keyshape = Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/food"
    aliases=()
    keywords=('hot', 'bean', 'soup', 'bowl')

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

        path('bowl',(4,23),[('A',(24,40),20,17,False),('A',(44,23),20,17,False)])
        path('bean',(20,21),[('C',(31,25),(27,18),(31,20)),('C',(23,31),(31,30),(27,32)),('C',(18,27),(19,31),(17,29)),('C',(20,21),(22,27),(23,24))],True)
        for x in (11,38):path(f'steam-{x}',(x,8),[('C',(x,14),(x-3,10),(x+3,12))])

