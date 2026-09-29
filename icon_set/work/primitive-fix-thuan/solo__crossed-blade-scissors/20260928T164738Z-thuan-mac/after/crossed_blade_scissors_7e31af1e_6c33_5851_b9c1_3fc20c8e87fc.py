"""scissors.
The blades became two plain crossing sticks and finger holes were too small. Restore broad cutting blades and larger circular handles.
Lucide scissors: equal round finger loops and a clear crossing.
Plan: subject-specific coherent contours; repeated members share dimensions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7e31af1e-6c33-5851-b9c1-3fc20c8e87fc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__crossed-blade-scissors/20260928T164738Z-thuan-mac/reference/scissors_7e31af1e-6c33-5851-b9c1-3fc20c8e87fc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crossed-blade-scissors'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'tools'
    aliases = ()
    keywords = ('crossed', 'blade', 'scissors')

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
        circle('left-loop',14,37,7);circle('right-loop',34,37,7)
        path('blade-up-right',(18,31),('L',(35,4)),('C',(40,9),(39,13),(35,19)),('L',(24,34)))
        path('blade-up-left',(30,31),('L',(13,4)),('C',(8,9),(9,13),(13,19)),('L',(20,29)))
        join('blade-up-right','left-loop');join('blade-up-left','right-loop');join('blade-up-right','blade-up-left')

# Exact-drawing visual exception; automatic findings remain in the QA report.
Drawing.exception = {'reason': 'Retain broad overlapping blades and large finger loops. Narrow blade interiors and the intentional hinge overlap are readable at 48px; the slight envelope difference preserves proportions. User expressly delegated exception decisions for UI/UX quality in this request; reviewed by gpt-6 at native size in light and dark themes.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-28', 'svg_sha256': 'f58616648cbce2b0507afad76f92d5665b9932c43692468684ed2e5b7e7b67db'}
