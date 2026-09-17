"""Back Massage Therapy."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '67bda00f-e94c-44cb-8e5d-0d74c282744a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/massage back_67bda00f-e94c-44cb-8e5d-0d74c282744a.svg'
AUTHOR = 'gpt-6'


class BackMassageTherapistPatient(Solo48):
    icon_id = 'back-massage-therapist-patient'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('back', 'massage', 'therapy')

    def build(self):
        # Plan: A standing therapist reaches a prone patient supported by the table. Extremes (6,6)-(42,42).
        # Reduction: Omit blanket outlines, extra fingers and lower therapist body; retain a separate tabletop. Both circular heads have radius 3.
        # Reference: human_ref/full_body_ref.png: coherent torso and round-ended limbs; exact detached head gaps.

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

        circle('therapist-head',12,9,3)
        line('therapist-torso',(12,20),(12,22))
        path('arm',(12,20),(22,20),(28,30))
        line('patient-torso',(28,30),(6,30))
        circle('patient-head',39,30,3)
        path('table',(6,40),(8,40),(30,40),(32,40))
        for x in (8,30):line(f'table-leg-{x}',(x,40),(x,42))
        self.mark_human_figure('therapist',head='therapist-head',torso='therapist-torso',torso_junction='start')
        self.mark_human_figure('patient',head='patient-head',torso='patient-torso',torso_junction='start')
        # Therapist 20-(9+3)=8; patient 39-3-28=8 centerline units.
        # Both gaps are exactly 4 visible units, and heads follow their torso axes.
        contacts()
