"""Twin Bell Alarm Clock — batch 51."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b861b25e-362d-558f-9c20-00dab6f0971a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/alarm clock_b861b25e-362d-558f-9c20-00dab6f0971a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'twin-bell-alarm-clock-reference-b861b25e-362d-558f-9c20-00dab6f0971a'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('twin', 'bell', 'alarm', 'clock', 'reference')

    def build(self):
        # Plan: round dial, paired curved bell strokes and diagonal feet.
        # SQUARE extremes6,6,42,42. Lucide alarm-clock informs simplified bells and feet.
        # Omit closed bell undersides to preserve clearance; keep both ringing silhouettes.
        self.circle('dial',24,27,15,attachments=((15,39),(33,39)))
        self.add_arc('bell-left',(6,12),(12,6),radius_x=6)
        self.add_arc('bell-right',(36,6),(42,12),radius_x=6)
        for n,a,z in [('left-foot',(15,39),(12,42)),('right-foot',(33,39),(36,42))]:
            self.add_line(n,a,z);self.relate('connect',n,'dial')
        self.add_polyline('hands',(24,21),(24,27),(29,27))


    def circle(self,n,x,y,r,attachments=()):
        from math import atan2
        pts=list(dict.fromkeys([(x+r,y),(x,y+r),(x-r,y),(x,y-r)]+list(attachments)))
        pts.sort(key=lambda p:atan2(p[1]-y,p[0]-x))
        for j in range(len(pts)):self.add_arc(f'{n}-{j}',pts[j],pts[(j+1)%len(pts)],radius_x=r)
        self.add_contour(n,*[f'{n}-{j}' for j in range(len(pts))],closed=True)

    def box(self,n,x,y,w,h,attachments=()):
        corners=[(x,y),(x+w,y),(x+w,y+h),(x,y+h)];nodes=[]
        for a,z in zip(corners,corners[1:]+corners[:1]):
            dx,dy=z[0]-a[0],z[1]-a[1]
            inside=[p for p in attachments if (p[0]-a[0])*dy==(p[1]-a[1])*dx and 0<(p[0]-a[0])*dx+(p[1]-a[1])*dy<dx*dx+dy*dy]
            inside.sort(key=lambda p:(p[0]-a[0])*dx+(p[1]-a[1])*dy);nodes.extend([a]+inside)
        self.add_polyline(n,*nodes,closed=True)

