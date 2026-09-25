"""Two Seater Living Room Sofa."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd397dedb-6edb-4b65-8c34-4895798f59fa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/sofa double_d397dedb-6edb-4b65-8c34-4895798f59fa.svg'
AUTHOR = 'gpt-6'


class TwoSeatSofaCentralSeam(Solo48):
    icon_id = 'two-seat-sofa-central-seam'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "furnitures"
    aliases = ()
    keywords = ('two', 'seater', 'living', 'room', 'sofa')

    def build(self):
        # Plan: Mirrored round arms frame a two-seat back with axial seam and shared short legs. Extremes (4,8)-(44,40).
        # Reduction: Omit separate cushion outlines; preserve central seam, rounded arms and front rail.
        # Reference: Lucide sofa: rounded arm-front contour and divided back.

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

        path('back-top',(12,20),(12,12))
        arc('back-left',(12,12),(16,8),4)
        path('back-rail',(16,8),(24,8),(32,8))
        arc('back-right',(32,8),(36,12),4)
        line('back-side',(36,12),(36,20))
        self.contours = [c for c in self.contours if c.contour_id not in ('back-top','back-rail')]
        self.add_contour('back','back-top-1','back-left','back-rail-1','back-rail-2','back-right','back-side')
        nodes={'back':((12,20),(24,8),(36,20))}
        arc('arm-left',(4,20),(12,20),4)
        path('seat',(12,20),(12,26),(24,26),(36,26),(36,20))
        arc('arm-right',(36,20),(44,20),4)
        path('front',(44,20),(44,34),(36,34),(12,34),(4,34),(4,20))
        line('seam',(24,8),(24,26))
        for x in (12,36):line(f'leg-{x}',(x,34),(x,40))
        contacts()
