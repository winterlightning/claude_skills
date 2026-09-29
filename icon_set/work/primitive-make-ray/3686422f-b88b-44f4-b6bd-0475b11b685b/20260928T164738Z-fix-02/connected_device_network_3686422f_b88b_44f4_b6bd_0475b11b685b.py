"""internet of thing graph service.
The center device became square, its cable disappeared, and side connections were truncated. Restore a tall center device and three descending cables.
Lucide network: rounded nodes with actual joined connectors.
Plan: subject-specific coherent contours; repeated members share dimensions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3686422f-b88b-44f4-b6bd-0475b11b685b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__connected-device-network/20260928T164738Z-thuan-mac/reference/internet of thing graph service_3686422f-b88b-44f4-b6bd-0475b11b685b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'connected-device-network'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'internet'
    aliases = ()
    keywords = ('connected', 'device', 'network')

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
        box('central',17,6,31,27,3)
        box('left',4,25,12,37,2);box('right',36,25,44,37,2)
        line('center-wire',(24,27),(24,44));join('central','center-wire')
        path('left-wire',(12,33),('L',(14,33)),('A',(18,37),4,4,True),('L',(18,44)))
        path('right-wire',(36,33),('L',(34,33)),('A',(30,37),4,4,False),('L',(30,44)))
        join('left','left-wire');join('right','right-wire')
        self.add_dot('button',(24,20))

# Exact-drawing visual exception; automatic findings remain in the QA report.
Drawing.exception = {'reason': 'Retain the tall device, button and three separate cables. Compact 2px cable gaps and small device corners remain visibly open; preserve the natural scene extent. User expressly delegated exception decisions for UI/UX quality in this request; reviewed by gpt-6 at native size in light and dark themes.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-28', 'svg_sha256': 'cb9c92a0aaab66fee8a2d66cb401811b27d7fd47954d55ecd5967e5501e17bfb'}
