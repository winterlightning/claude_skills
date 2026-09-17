"""Dental Extraction Forceps."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9bcc56f-bc17-4b53-9088-582efa893f7d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/instrument tooth_c9bcc56f-bc17-4b53-9088-582efa893f7d.svg'
AUTHOR = 'gpt-6'


class DentalExtractionForcepsOpenJaws(Solo48):
    icon_id = 'dental-extraction-forceps-open-jaws'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('dental', 'extraction', 'forceps')

    def build(self):
        # Plan: Two mirrored curved jaws meet at a shared pivot above spreading handles. Extremes (8,4)-(40,44).
        # Reduction: Reorient the forceps upright for a clearer tool silhouette; reduce thickness to coherent strokes and omit the tiny pivot seam.
        # Reference: Lucide scissors: two functional arms joined at one exact pivot.

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

        # Both jaw/handle pairs derive from the common pivot and axis x24.
        pivot=(24,22)
        for name,mirror in [('left',lambda p:p),('right',lambda p:(48-p[0],p[1]))]:
            bez(name+'-jaw',mirror((18,4)),(mirror((12,4)),mirror((12,8)),mirror((12,12))),(mirror((12,17)),mirror((18,20)),pivot))
            line(name+'-handle',pivot,mirror((40,44)))
            contour(name+'-arm',name+'-jaw',name+'-handle')
        contacts()
