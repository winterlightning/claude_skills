"""Applying Contact Lens to Eye."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cb8db406-8145-4754-be32-27d400cedbc9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/ophthalmic contact lens 1_cb8db406-8145-4754-be32-27d400cedbc9.svg'
AUTHOR = 'gpt-6'


class ContactLensAppliedToEye(Solo48):
    icon_id = 'contact-lens-applied-to-eye'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ()
    keywords = ('applying', 'contact', 'lens', 'to', 'eye')

    def build(self):
        # Plan: An open almond eye at right faces a contact lens resting on a rounded fingertip at left. Extremes (6,6)-(42,42).
        # Reduction: Open the lower-left eye contour for the lens; keep a rounded fingertip holding the lens and simplify the iris to a small circle.
        # Reference: Lucide eye and hand; shared human reference inspected for consistent anatomy.

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

        bez('eye-top',(10,17),((15,10),(19,6),(26,6)),((33,6),(37,10),(42,17)))
        bez('eye-bottom',(42,17),((37,24),(33,28),(26,28)),((24,28),(23,28),(22,27)))
        contour('eye','eye-top','eye-bottom')
        circle('iris',26,17,2)
        circle('lens',10,29,3)
        line('finger-left',(6,42),(6,36))
        arc('finger-tip-left',(6,36),(10,32),4)
        arc('finger-tip-right',(10,32),(14,36),4)
        line('finger-right',(14,36),(14,42))
        contour('finger','finger-left','finger-tip-left','finger-tip-right','finger-right')
        contacts()
