"""Breast Surgery with Scalpel."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd056bc28-eda5-5f75-af36-97d411db3644'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/surgery breast surgery_d056bc28-eda5-5f75-af36-97d411db3644.svg'
AUTHOR = 'gpt-6'


class BreastSurgeryScalpelVariant(Solo48):
    icon_id = 'breast-surgery-scalpel-variant'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('breast', 'surgery', 'with', 'scalpel')

    def build(self):
        # Plan: A diagonal scalpel contacts the upper breast; a rounded lower lobe provides room beneath its blade. Extremes (6,6)-(42,42).
        # Reduction: Omit the tiny nipple, separate incision mark and lower torso stub; preserve the blade contacting the breast.
        # Reference: Shared human reference and supplied anatomical source; Lucide syringe diagonal construction.

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

        path('handle',(26,16),(36,6),(42,6),(42,12),(32,22),closed=True)
        line('blade-back',(26,16),(18,24))
        bez('blade-tip',(18,24),((17,27),(15,30),(14,32)))
        bez('blade-edge',(14,32),((22,32),(28,28),(32,22)))
        line('blade-neck',(32,22),(26,16))
        contour('blade','blade-back','blade-tip','blade-edge','blade-neck',closed=True)
        bez('upper-chest',(16,6),((16,10),(20,14),(26,16)))
        bez('breast',(6,22),((6,35),(11,42),(20,42)),((34,42),(40,28),(32,22)))
        contacts()
