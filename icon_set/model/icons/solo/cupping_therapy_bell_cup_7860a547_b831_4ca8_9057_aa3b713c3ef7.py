"""Cupping Therapy Massage Tool."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7860a547-b831-4ca8-9057-aa3b713c3ef7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/vacuum cup massage_7860a547-b831-4ca8-9057-aa3b713c3ef7.svg'
AUTHOR = 'gpt-6'


class CuppingTherapyBellCup(Solo48):
    icon_id = 'cupping-therapy-bell-cup'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ()
    keywords = ('cupping', 'therapy', 'massage', 'tool')

    def build(self):
        # Plan: A broad glass bell cup has a narrow top valve, rounded shoulders and thick lower flange. Extremes (8,4)-(40,44).
        # Reduction: Retain one curved highlight; omit no defining structural parts.
        # Reference: Lucide bell: smooth shoulders and broad base, without its clapper.

        nodes = {}
        def line(n, a, b):
            self.add_line(n, a, b); nodes[n] = (a, b)
        def path(n, *pts, closed=False):
            self.add_polyline(n, *pts, closed=closed); nodes[n] = pts
        def arc(n, a, b, r, ry=None, sweep=True):
            self.add_arc(n, a, b, radius_x=r, radius_y=r if ry is None else ry, sweep=sweep); nodes[n] = (a,b)
        def bez(n, start, *segments):
            self.add_bezier(n,start,*segments); nodes[n]=(start,*(s[2] for s in segments))
        def contour(n,*parts,closed=False):
            members=[];points=[]
            for part in parts:
                existing=next((c for c in self.contours if c.contour_id==part),None)
                if existing:
                    members.extend(existing.members);self.contours.remove(existing)
                else:members.append(part)
                points.extend(nodes.pop(part))
            self.add_contour(n,*members,closed=closed);nodes[n]=tuple(points)
        def circle(n,x,y,r):
            for suffix,a,z in [('t',(x-r,y),(x,y-r)),('r',(x,y-r),(x+r,y)),('b',(x+r,y),(x,y+r)),('l',(x,y+r),(x-r,y))]:arc(n+suffix,a,z,r)
            contour(n,*(n+s for s in 'trbl'),closed=True)
        def rounded(n,l,t,r,b,radius=2,top=(),bottom=(),left=(),right=()):
            parts=[]
            sides=[((l+radius,t),(r-radius,t),sorted(top),0),((r,t+radius),(r,b-radius),sorted(right),1),((r-radius,b),(l+radius,b),sorted(bottom,reverse=True),2),((l,b-radius),(l,t+radius),sorted(left,reverse=True),3)]
            for start,end,vals,side in sides:
                pts=[start]+[(v,t) if side==0 else (r,v) if side==1 else (v,b) if side==2 else (l,v) for v in vals]+[end]
                for i,(a,z) in enumerate(zip(pts,pts[1:])):
                    if a!=z:
                        part=f'{n}-s{side}-{i}';line(part,a,z);parts.append(part)
                part=f'{n}-c{side}';arc(part,end,sides[(side+1)%4][0],radius);parts.append(part)
            contour(n,*parts,closed=True)
        def contacts():
            names=list(nodes)
            for i,a in enumerate(names):
                for b in names[i+1:]:
                    if set(nodes[a]) & set(nodes[b]):self.relate('connect',a,b)

        path('valve',(20,14),(20,4),(28,4),(28,14))
        line('body-top',(20,14),(28,14))
        arc('body-right-shoulder',(28,14),(36,22),8)
        path('body-right',(36,22),(36,36),(12,36),(12,22))
        arc('body-left-shoulder',(12,22),(20,14),8)
        contour('body','body-top','body-right-shoulder','body-right','body-left-shoulder',closed=True)
        rounded('rim',8,36,40,44,4,top=(12,36))
        arc('highlight',(24,23),(27,26),3)
        contacts()
