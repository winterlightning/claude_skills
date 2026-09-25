"""Table Lamp on Nightstand."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '54acb416-e4b3-5e07-9f33-daa1cb28e9e2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/night stand lamp_54acb416-e4b3-5e07-9f33-daa1cb28e9e2.svg'
AUTHOR = 'gpt-6'


class NightstandWithTallTableLamp(Solo48):
    icon_id = 'nightstand-with-tall-table-lamp'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "furnitures"
    aliases = ()
    keywords = ('table', 'lamp', 'on', 'nightstand')

    def build(self):
        # Plan: Centered tapered shade and stem above two broad cabinet panels. Extremes (8,4)-(40,44).
        # Reduction: Omit tiny lamp base; preserve shade, stem and drawer divider.
        # Reference: Lucide lamp: trapezoid and axial stem.

        nodes = {}
        def line(n, a, b):
            self.add_line(n, a, b)
            nodes[n] = (a, b)
        def path(n, *pts, closed=False):
            self.add_polyline(n, *pts, closed=closed)
            nodes[n] = pts
        def arc(n, a, b, r, ry=None, sweep=True):
            self.add_arc(n, a, b, radius_x=r, radius_y=r if ry is None else ry, sweep=sweep)
            nodes[n] = (a, b)
        def rounded(n, l, t, r, b, radius=2, top=(), bottom=(), left=(), right=()):
            # Rectangle owns equal corner radii and ordered attachment nodes.
            parts=[]
            corners=[((l+radius,t),(r-radius,t),sorted(top),0),
                     ((r,t+radius),(r,b-radius),sorted(right),1),
                     ((r-radius,b),(l+radius,b),sorted(bottom,reverse=True),2),
                     ((l,b-radius),(l,t+radius),sorted(left,reverse=True),3)]
            for start,end,values,side in corners:
                pts=[start]+[(v,t) if side==0 else (r,v) if side==1 else (v,b) if side==2 else (l,v) for v in values]+[end]
                for i,(a,z) in enumerate(zip(pts,pts[1:])):
                    if a!=z:
                        part=f'{n}-side-{side}-{i}';line(part,a,z);parts.append(part)
                dest=corners[(side+1)%4][0];part=f'{n}-corner-{side}'
                arc(part,end,dest,radius);parts.append(part)
            self.add_contour(n,*parts,closed=True)
            nodes[n]=tuple(p for part in parts for p in nodes.pop(part))
        def contacts():
            names=list(nodes)
            for i,a in enumerate(names):
                for b in names[i+1:]:
                    if set(nodes[a]) & set(nodes[b]):
                        self.relate('connect',a,b)

        path('shade',(18,4),(30,4),(34,16),(24,16),(14,16),closed=True)
        line('stem',(24,16),(24,26))
        rounded('cabinet',8,26,40,44,2,top=(24,),left=(35,),right=(35,))
        line('divider',(8,35),(40,35))
        contacts()
