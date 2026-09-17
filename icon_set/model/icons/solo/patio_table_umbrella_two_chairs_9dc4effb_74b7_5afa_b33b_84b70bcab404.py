"""Table with Umbrella and Chairs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9dc4effb-74b7-5afa-b33b-84b70bcab404'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/table restaurant beach_9dc4effb-74b7-5afa-b33b-84b70bcab404.svg'
AUTHOR = 'gpt-6'


class PatioTableUmbrellaTwoChairs(Solo48):
    icon_id = 'patio-table-umbrella-two-chairs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/furniture"
    aliases = ()
    keywords = ('table', 'with', 'umbrella', 'and', 'chairs')

    def build(self):
        # Plan: A triangular canopy owns the central pole; two mirrored inward-facing chair strokes flank the table. Extremes (6,6)-(42,42).
        # Reduction: Reduce table to one top and pedestal, chairs to back-seat-leg strokes.
        # Reference: Lucide bed-single supports; no useful local umbrella dining-set match.

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

        path('canopy',(6,18),(24,6),(42,18),(24,18),closed=True)
        path('pole',(24,18),(24,26),(24,42))
        path('table',(16,26),(24,26),(32,26))
        for side in (-1,1):
         x=24+side*18; inside=24+side*10
         path(f'chair-{side}',(x,26),(x,34),(inside,34),(inside,42))
         line(f'outer-leg-{side}',(x,34),(x,42))
        contacts()
