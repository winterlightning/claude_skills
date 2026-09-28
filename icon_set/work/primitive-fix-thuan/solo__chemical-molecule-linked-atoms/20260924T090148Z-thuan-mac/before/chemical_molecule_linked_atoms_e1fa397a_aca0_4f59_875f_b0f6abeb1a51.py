"""Chemical Molecular Structure."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e1fa397a-aca0-4f59-875f-b0f6abeb1a51'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/chemical hexagon_e1fa397a-aca0-4f59-875f-b0f6abeb1a51.svg'
AUTHOR = 'gpt-6'


class ChemicalMoleculeLinkedAtoms(Solo48):
    icon_id = 'chemical-molecule-linked-atoms'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('chemical', 'molecular', 'structure')

    def build(self):
        # Plan: Five circular atoms and a sixth bare corner form a hexagonal ring with one extended bond. Extremes (6,6)-(42,42).
        # Reduction: Omit the lower extension and simplify the upper-right terminal atom to a bond end.
        # Reference: No useful Lucide molecule match; shared circle definitions and explicit bond attachment nodes.

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

        for n,x,y in [('upper-left',9,17),('top',21,9),('upper-right',33,17),('bottom',21,39),('lower-left',9,31)]:circle(n,x,y,3)
        line('bond-upper-left',(12,17),(18,9))
        line('bond-upper-right',(24,9),(30,17))
        line('bond-left',(9,20),(9,28))
        path('bond-right',(33,20),(33,31),(24,39))
        line('bond-lower-left',(18,39),(12,31))
        path('extension',(36,17),(42,11),(42,6))
        contacts()
