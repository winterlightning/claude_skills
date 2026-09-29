"""mailbox house.
The handle met the lens at an awkward angle and was too short. Use a smaller circular lens and a longer radially aligned handle.
Lucide search: true circular lens and radial handle.
Plan: subject-specific coherent contours; repeated members share dimensions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5a48ce49-6ce4-48c1-90af-512b716eb5e1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__compact-magnifying-glass-with-extended-handle/20260928T164738Z-thuan-mac/reference/mailbox house_5a48ce49-6ce4-48c1-90af-512b716eb5e1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'compact-magnifying-glass-with-extended-handle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('compact', 'magnifying', 'glass', 'with', 'extended', 'handle')

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
        # 9-12-15 triangle puts the attachment exactly on the radius.
        path('lens',(6,21),('A',(21,6),15,15,True),('A',(30,33),15,15,True),('A',(6,21),15,15,True),closed=True)
        line('handle',(30,33),(39,45));join('lens','handle')
