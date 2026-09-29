"""cough.
The face was overly blocky and added unexplained detached marks. Restore the smooth head profile, nose, jaw and neck; retain two short cough rays to clarify the concept.
Shared human reference for smooth head/neck vocabulary; source profile owns anatomy.
Plan: subject-specific coherent contours; repeated members share dimensions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'bc3ea9f7-36ca-4b3a-a099-e36c89039b41'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cough/20260928T164738Z-thuan-mac/reference/cough_bc3ea9f7-36ca-4b3a-a099-e36c89039b41.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cough'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'health'
    aliases = ()
    keywords = ('cough',)

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
        path('profile',(19,44),('L',(19,36)),('L',(15,36)),('A',(11,32),4,4,True),('L',(11,24)),('L',(6,24)),('L',(10,13)),('C',(12,6),(18,4),(24,4)),('C',(35,4),(40,12),(40,21)),('C',(40,29),(34,33),(34,37)),('L',(34,44)))
        line('cough-upper',(3,31),(5,32));line('cough-lower',(3,40),(6,38))
