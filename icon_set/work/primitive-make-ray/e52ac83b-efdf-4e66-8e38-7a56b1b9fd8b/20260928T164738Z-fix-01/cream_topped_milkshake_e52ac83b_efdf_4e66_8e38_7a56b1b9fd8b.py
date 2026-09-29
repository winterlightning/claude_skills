"""bubble tea wipcream.
The whipped topping read as a flame and the straw as a V. Restore a rounded swirl, right-angle straw bend and rounded cup with a wavy liquid line.
Lucide cup-soda: cup, projecting rim and wavy liquid level.
Plan: subject-specific coherent contours; repeated members share dimensions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e52ac83b-efdf-4e66-8e38-7a56b1b9fd8b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cream-topped-milkshake/20260928T164738Z-thuan-mac/reference/bubble tea wipcream_e52ac83b-efdf-4e66-8e38-7a56b1b9fd8b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cream-topped-milkshake'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('cream', 'topped', 'milkshake')

    def build(self):

        def path(n,start,*commands,closed=False):
            pt=start; members=[]
            for i,c in enumerate(commands):
                mid=f'{n}-{i}'
                if c[0]=='L': self.add_line(mid,pt,c[1]); end=c[1]
                elif c[0]=='A':
                    _,end,rx,ry,sweep=c
                    self.add_arc(mid,pt,end,radius_x=rx,radius_y=ry,sweep=sweep)
                elif c[0]=='C':
                    _,a,b,end=c; self.add_bezier(mid,pt,(a,b,end))
                pt=end;members.append(mid)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x,y-r),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True),closed=True)
        def box(n,l,t,r,b,rad=2):
            path(n,(l+rad,t),('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True),closed=True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def bez(n,start,*s): self.add_bezier(n,start,*s)
        def join(a,b): self.relate('connect',a,b)
        path('cup',(9,24),('L',(12,39)),('C',(13,43),(17,44),(21,44)),('L',(27,44)),('C',(31,44),(35,43),(36,39)),('L',(39,24)))
        poly('rim',(8,24),(9,24),(12,24),(34,24),(39,24),(40,24));join('cup','rim')
        bez('cream',(12,24),((9,19),(14,13),(19,13)),((16,9),(24,10),(25,4)),((30,7),(31,12),(28,15)),((34,15),(36,20),(34,24)))
        poly('straw',(34,15),(37,5),(42,5));join('cream','straw');join('rim','cream')
        bez('liquid',(11,33),((21,28),(27,38),(37,33)));join('liquid','cup')
