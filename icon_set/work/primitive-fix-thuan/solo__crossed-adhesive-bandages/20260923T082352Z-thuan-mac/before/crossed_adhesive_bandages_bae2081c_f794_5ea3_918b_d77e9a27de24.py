"""Crossed Adhesive Bandages."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bae2081c-f794-5ea3-918b-d77e9a27de24'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/bandage_bae2081c-f794-5ea3-918b-d77e9a27de24.svg'
AUTHOR = 'gpt-6'


class CrossedAdhesiveBandages(Solo48):
    icon_id = 'crossed-adhesive-bandages'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('crossed', 'adhesive', 'bandages')

    def build(self):
        # Plan: A rounded diagonal bandage overlays a second strip; four broad rounded ends form an X. Extremes (6,6)-(42,42).
        # Reduction: Reduce the small pad marks to one central perforation dot; keep visible overlap boundaries.
        # Reference: Lucide bandage: rounded adhesive outline and sparse central detail.

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

        path('front-left',(6,30),(14,22),(22,14),(30,6),(36,6))
        arc('front-upper-cap',(36,6),(42,12),6)
        path('front-right',(42,12),(42,18),(34,26),(26,34),(18,42),(12,42))
        arc('front-lower-cap',(12,42),(6,36),6)
        line('front-close',(6,36),(6,30))
        contour('front','front-left','front-upper-cap','front-right','front-lower-cap','front-close',closed=True)
        path('back-upper-left',(14,22),(6,14),(6,12))
        arc('back-upper-cap',(6,12),(12,6),6)
        path('back-upper-right',(12,6),(14,6),(22,14))
        contour('back-upper','back-upper-left','back-upper-cap','back-upper-right')
        path('back-lower-left',(26,34),(34,42),(36,42))
        arc('back-lower-cap',(36,42),(42,36),6,sweep=False)
        path('back-lower-right',(42,36),(42,34),(34,26))
        contour('back-lower','back-lower-left','back-lower-cap','back-lower-right')
        line('pad-dot',(24,24),(24,24))
        contacts()
