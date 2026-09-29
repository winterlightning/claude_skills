"""dentistry tooth hook.
The grip became a short polygon and the hook an upright J. Restore the long diagonal rounded grip, diagonal neck and curling dental tip.
Lucide search: a clean joined handle; source owns tool shape.
Plan: subject-specific coherent contours; repeated members share dimensions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4009081f-4b9a-47f8-99bd-9ffa8ebc399a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dental-hook-tool-looped-tip/20260928T164738Z-thuan-mac/reference/dentistry tooth hook_4009081f-4b9a-47f8-99bd-9ffa8ebc399a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dental-hook-tool-looped-tip'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'health'
    aliases = ()
    keywords = ('dental', 'hook', 'tool', 'looped', 'tip')

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
        path('grip',(22,25),('L',(17,20)),('L',(34,3)),('A',(42,11),6,6,True),('L',(25,28)),('L',(22,25)),closed=True)
        path('hook',(22,25),('L',(14,33)),('A',(5,42),7,7,True),('A',(5,32),7,7,True))
        join('grip','hook')
