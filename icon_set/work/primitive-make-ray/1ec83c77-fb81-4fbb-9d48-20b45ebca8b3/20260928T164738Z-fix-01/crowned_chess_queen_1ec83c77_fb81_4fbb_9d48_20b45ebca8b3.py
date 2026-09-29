"""chess king.
The crown merged into its base and lost the tall tapered stem. Restore the chess-piece proportions, separate collar, flared stem and broad foot.
Original crown and chess stem; no useful exact Lucide match.
Plan: subject-specific coherent contours; repeated members share dimensions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1ec83c77-fb81-4fbb-9d48-20b45ebca8b3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__crowned-chess-queen/20260928T164738Z-thuan-mac/reference/chess king_1ec83c77-fb81-4fbb-9d48-20b45ebca8b3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crowned-chess-queen'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hobbies'
    aliases = ()
    keywords = ('crowned', 'chess', 'queen')

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
        circle('finial',24,6,2)
        poly('crown',(10,12),(16,18),(24,10),(32,18),(38,12),(32,24),(16,24),(10,12))
        line('neck',(24,8),(24,10));join('neck','finial');join('neck','crown')
        line('collar',(16,24),(32,24));join('collar','crown')
        path('stem-left',(19,24),('C',(19,29),(18,34),(15,38)))
        path('stem-right',(29,24),('C',(29,29),(30,34),(33,38)))
        join('collar','stem-left');join('collar','stem-right')
        box('base',10,38,38,44,2);join('stem-left','base');join('stem-right','base')
