"""Copper Intrauterine Device."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a3b31c3-a30d-46a8-90d3-db6b6580d6ed'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/copper iud_8a3b31c3-a30d-46a8-90d3-db6b6580d6ed.svg'
AUTHOR = 'gpt-6'


class CopperIudRoundedArms(Solo48):
    icon_id = 'copper-iud-rounded-arms'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('copper', 'intrauterine', 'device')

    def build(self):
        # Plan: Mirrored broad curved arms meet an axial banded stem and a circular terminal. Extremes (6,6)-(42,42).
        # Reduction: Reduce three internal bands to two plus the lower stem edge; preserve curled arms and round tip.
        # Reference: Lucide bell: shared smooth circular arcs and axial attachment.

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

        for n,mirror in [('left',lambda p:p),('right',lambda p:(48-p[0],p[1]))]:
         sweep=n=='left'
         arc(n+'-curl',mirror((12,18)),mirror((6,12)),6,sweep=sweep)
         arc(n+'-top',mirror((6,12)),mirror((12,6)),6,sweep=sweep)
         bez(n+'-shoulder',mirror((12,6)),(mirror((18,6)),mirror((21,8)),mirror((24,14))))
         contour(n+'-arm',n+'-curl',n+'-top',n+'-shoulder')
        path('stem',(20,14),(24,14),(28,14),(28,22),(28,30),(28,38),(24,38),(20,38),(20,30),(20,22),closed=True)
        for y in (22,30):line(f'band-{y}',(20,y),(28,y))
        circle('terminal',24,40,2)
        contacts()
