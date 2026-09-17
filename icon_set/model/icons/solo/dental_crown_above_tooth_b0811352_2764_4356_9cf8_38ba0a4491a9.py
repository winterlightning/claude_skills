"""Dental Crown Procedure."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0811352-2764-4356-9cf8-38ba0a4491a9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/dental crown_b0811352-2764-4356-9cf8-38ba0a4491a9.svg'
AUTHOR = 'gpt-6'


class DentalCrownAboveTooth(Solo48):
    icon_id = 'dental-crown-above-tooth'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('dental', 'crown', 'procedure')

    def build(self):
        # Plan: A notched crown floats above a matching two-root tooth, both centered on x24. Extremes (8,4)-(40,44).
        # Reduction: Simplify the crown and root notches while preserving the two separate aligned pieces.
        # Reference: No useful local Lucide tooth match; paired circular and smooth mirrored anatomical contours.

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

        arc('crown-left',(8,12),(16,4),8)
        bez('crown-notch-left',(16,4),((20,4),(22,6),(24,7)))
        bez('crown-notch-right',(24,7),((26,6),(28,4),(32,4)))
        arc('crown-right',(32,4),(40,12),8)
        path('crown-bottom',(40,12),(38,20),(30,20),(28,16),(20,16),(18,20),(10,20),(8,12))
        contour('crown','crown-left','crown-notch-left','crown-notch-right','crown-right','crown-bottom',closed=True)
        line('tooth-top',(8,29),(40,29))
        bez('tooth-right',(40,29),((40,37),(40,44),(34,44)))
        line('root-right',(34,44),(30,44))
        bez('root-notch-right',(30,44),((27,44),(28,38),(24,38)))
        bez('root-notch-left',(24,38),((20,38),(21,44),(18,44)))
        line('root-left',(18,44),(14,44))
        bez('tooth-left',(14,44),((8,44),(8,37),(8,29)))
        contour('tooth','tooth-top','tooth-right','root-right','root-notch-right','root-notch-left','root-left','tooth-left',closed=True)
        contacts()
