"""icing.
The frosting had sharp joins and crowded scallops. Restore a smooth cloudlike dome and three clear, unequal drips above a rounded wrapper.
Original dome and flowing icing; no exact Lucide cupcake match.
Plan: subject-specific coherent contours; repeated members share dimensions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '156c4fd4-cbf2-4e71-83f1-9eefe3e7f03c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cupcake-with-dripping-frosting/20260928T164738Z-thuan-mac/reference/icing_156c4fd4-cbf2-4e71-83f1-9eefe3e7f03c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cupcake-with-dripping-frosting'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('cupcake', 'with', 'dripping', 'frosting')

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
        bez('frosting',(8,25),((7,18),(11,14),(15,13)),((16,1),(32,1),(33,13)),((39,14),(42,20),(40,25)),((38,29),(34,29),(32,26)),((30,22),(29,29),(29,31)),((29,36),(21,36),(21,30)),((21,23),(18,25),(17,27)),((14,31),(8,30),(8,25)))
        path('wrapper',(10,30),('L',(12,40)),('A',(16,44),4,4,False),('L',(32,44)),('A',(36,40),4,4,False),('L',(38,29)))
        join('wrapper','frosting')
