"""Dental Mouth Mirror."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ad26951-3ebc-43be-a582-43053440b4d2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/dentistry tooth mirror_7ad26951-3ebc-43be-a582-43053440b4d2.svg'
AUTHOR = 'gpt-6'


class DentalMouthMirrorAngledHandle(Solo48):
    icon_id = 'dental-mouth-mirror-angled-handle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('dental', 'mouth', 'mirror')

    def build(self):
        # Plan: An oval reflective head at lower left connects to a long diagonal grip rising right. Extremes (6,6)-(42,42).
        # Reduction: Keep the oval head, narrow neck and broad grip; omit reflective marks.
        # Reference: Lucide search: a handle attaches to a clean circular head; use the source oval instead of a circle.

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

        arc('mirror-top',(6,36),(22,36),8,6)
        arc('mirror-bottom',(22,36),(6,36),8,6)
        contour('mirror','mirror-top','mirror-bottom',closed=True)
        line('shaft',(22,36),(27,27))
        path('grip-left',(24,24),(34,6),(38,6))
        arc('grip-cap',(38,6),(42,10),4)
        path('grip-right',(42,10),(42,14),(30,30),(27,27),(24,24))
        contour('grip','grip-left','grip-cap','grip-right',closed=True)
        contacts()
