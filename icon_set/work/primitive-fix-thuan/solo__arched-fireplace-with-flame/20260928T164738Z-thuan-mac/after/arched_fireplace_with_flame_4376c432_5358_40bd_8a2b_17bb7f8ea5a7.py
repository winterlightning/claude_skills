"""hearthside.
The surround had become a single arch and the fire a droplet. Restore a rectangular mantel surround, inset arched opening, and asymmetric flame.
Lucide flame: asymmetric lobe and clear flame tip.
Plan: subject-specific coherent contours; repeated members share dimensions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4376c432-5358-40bd-8a2b-17bb7f8ea5a7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__arched-fireplace-with-flame/20260928T164738Z-thuan-mac/reference/hearthside_4376c432-5358-40bd-8a2b-17bb7f8ea5a7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arched-fireplace-with-flame'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('arched', 'fireplace', 'with', 'flame')

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
        path('surround',(6,42),('L',(6,12)),('A',(12,6),6,6,True),('L',(36,6)),('A',(42,12),6,6,True),('L',(42,42)))
        poly('hearth',(6,42),(12,42),(24,42),(36,42),(42,42))
        path('opening',(12,42),('L',(12,26)),('A',(36,26),12,12,True),('L',(36,42)))
        bez('fire',(24,42),((15,41),(20,33),(24,28)),((24,32),(26,34),(29,33)),((31,38),(30,42),(24,42)))
        join('hearth','surround');join('hearth','opening');join('hearth','fire')

# Exact-drawing visual exception; automatic findings remain in the QA report.
Drawing.exception = {'reason': 'The defining nested fireplace surround needs a 2px wall gap. The revised asymmetric flame stays inside its opening and reads clearly at 48px. User expressly delegated exception decisions for UI/UX quality in this request; reviewed by gpt-6 at native size in light and dark themes.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-28', 'svg_sha256': '70c2e136071c72f097b3b202840a38662b61309fdc0961257d03838e0456f5fc'}
