"""Circular Virus Cell."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a588702-8526-4903-87b5-af17b3a3bf1a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/virus_8a588702-8526-4903-87b5-af17b3a3bf1a.svg'
AUTHOR = 'gpt-6'


class CircularVirusCellProjections(Solo48):
    icon_id = 'circular-virus-cell-projections'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ()
    keywords = ('circular', 'virus', 'cell')

    def build(self):
        # Plan: A circular cell owns four axial stems and equal transverse caps. Extremes (6,6)-(42,42).
        # Reduction: Reduce two crowded internal squiggles to one short diagonal strand.
        # Reference: No useful direct Lucide virus match; shared circle and mirrored projection definitions.

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

        circle('cell',24,24,10)
        for n,a,z,cap in [('top',(24,14),(24,6),((20,6),(24,6),(28,6))),('right',(34,24),(42,24),((42,20),(42,24),(42,28))),('bottom',(24,34),(24,42),((20,42),(24,42),(28,42))),('left',(14,24),(6,24),((6,20),(6,24),(6,28)))]:
         line(n+'-stem',a,z);path(n+'-cap',*cap)
        line('strand',(23,23),(25,25))
        contacts()
