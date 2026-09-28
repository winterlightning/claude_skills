"""Cannabis Marijuana Leaf."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '23aeb601-bfa8-482a-bf2e-7c341bd3a965'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/drugs cannabis_23aeb601-bfa8-482a-bf2e-7c341bd3a965.svg'
AUTHOR = 'gpt-6'


class CannabisLeafSevenLobes(Solo48):
    icon_id = 'cannabis-leaf-seven-lobes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "state")
    aliases = ()
    keywords = ('cannabis', 'marijuana', 'leaf')

    def build(self):
        # Plan: Seven pointed lobes mirror around x24 and join a short central stem. Extremes (6,6)-(42,42).
        # Reduction: Omit serrations and veins while retaining all seven lobes.
        # Reference: Lucide cannabis: seven-lobed mirrored silhouette without interior detail.

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

        # Right-half cubic definitions own the curvature; mirror them about x24.
        right=[((24,6),(27,11),(28,16),(28,20)),
               ((28,20),(31,16),(36,12),(40,12)),
               ((40,12),(39,17),(37,21),(34,24)),
               ((34,24),(37,24),(40,26),(42,28)),
               ((42,28),(39,30),(35,32),(32,32)),
               ((32,32),(33,34),(34,36),(34,38)),
               ((34,38),(30,38),(27,36),(24,34))]
        parts=[]
        for i,(a,c1,c2,z) in enumerate(right):
            n=f'right-{i}';bez(n,a,(c1,c2,z));parts.append(n)
        for i,(a,c1,c2,z) in enumerate(reversed(right)):
            n=f'left-{i}';mirror=lambda p:(48-p[0],p[1])
            bez(n,mirror(z),(mirror(c2),mirror(c1),mirror(a)));parts.append(n)
        contour('leaf',*parts,closed=True)
        line('stem',(24,34),(24,42))
        contacts()
