"""Artificial Leg Prosthesis."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd94d67b4-475c-5da4-9a6b-467f0ced79ef'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/prosthetic leg_d94d67b4-475c-5da4-9a6b-467f0ced79ef.svg'
AUTHOR = 'gpt-6'


class ArtificialLegProsthesisJoint(Solo48):
    icon_id = 'artificial-leg-prosthesis-joint'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ()
    keywords = ('artificial', 'leg', 'prosthesis')

    def build(self):
        # Plan: Socket, circular knee, narrow shaft and right-pointing foot share axial attachment nodes. Extremes (10,4)-(38,44).
        # Reduction: Reduce lower shaft to one stroke and omit surface detail.
        # Reference: Lucide rounded mechanical construction; shared human reference inspected for limb context.

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

        path('socket-top',(10,8),(10,4),(30,4),(30,8))
        arc('socket-right',(30,8),(20,18),10)
        arc('socket-left',(20,18),(10,8),10)
        contour('socket','socket-top','socket-right','socket-left',closed=True)
        circle('knee',20,23,5)
        line('shaft',(20,28),(20,36))
        path('foot-top',(10,36),(20,36),(34,36))
        arc('toe-top',(34,36),(38,40),4)
        arc('toe-bottom',(38,40),(34,44),4)
        path('sole',(34,44),(10,44),(10,36))
        contour('foot','foot-top','toe-top','toe-bottom','sole',closed=True)
        contacts()
