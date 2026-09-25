"""Cupping Therapy Massage."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc104ccc-60b6-4f68-9ada-273268e4595f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/vacuum cup massage back_dc104ccc-60b6-4f68-9ada-273268e4595f.svg'
AUTHOR = 'gpt-6'


class CuppingTherapyOnPatient(Solo48):
    icon_id = 'cupping-therapy-on-patient'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ()
    keywords = ('cupping', 'therapy', 'massage')

    def build(self):
        # Plan: Two identical suction cups rest on a prone patient above a low table. Extremes (4,8)-(44,40).
        # Reduction: Reduce the body to a horizontal stroke and omit the blanket and arm seam; preserve two cups and their valves.
        # Reference: human_ref/full_body_ref.png: circular head and horizontal torso; Lucide bell for the cups.

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

        for i,x in enumerate((8,24)):
         line(f'valve-{i}',(x,8),(x,14))
         line(f'cup-left-{i}',(x-4,28),(x-4,18))
         arc(f'cup-top-left-{i}',(x-4,18),(x,14),4)
         arc(f'cup-top-right-{i}',(x,14),(x+4,18),4)
         line(f'cup-right-{i}',(x+4,18),(x+4,28))
         contour(f'cup-{i}',f'cup-left-{i}',f'cup-top-left-{i}',f'cup-top-right-{i}',f'cup-right-{i}')
        line('torso',(28,28),(20,28))
        path('body',(20,28),(12,28),(4,28))
        circle('head',40,28,4)
        path('table',(4,40),(4,36),(28,36),(28,40))
        self.mark_human_figure('patient',head='head',torso='torso',torso_junction='start')
        # Head-to-torso: 40-4-28=8 centerline units, exactly 4 ink units.
        # The torso extends horizontally through the head center.
        contacts()
