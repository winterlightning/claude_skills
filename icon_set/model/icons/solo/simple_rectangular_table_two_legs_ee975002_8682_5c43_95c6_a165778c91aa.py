"""Simple Rectangular Table."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ee975002-8682-5c43-95c6-a165778c91aa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/console table_ee975002-8682-5c43-95c6-a165778c91aa.svg'
AUTHOR = 'gpt-6'


class SimpleRectangularTableTwoLegs(Solo48):
    icon_id = 'simple-rectangular-table-two-legs'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "furnitures"
    aliases = ()
    keywords = ('simple', 'rectangular', 'table')

    def build(self):
        # Plan: A rounded tabletop owns two equal broad legs mirrored around x24. Extremes (4,8)-(44,40).
        # Reduction: Keep both broad legs; omit no structural parts.
        # Reference: Lucide bed-single: rounded rail and shared support joints.

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

        rounded('top',4,8,44,16,2,bottom=(8,16,32,40))
        for i,x in enumerate((8,32)):path(f'leg-{i}',(x,16),(x,40),(x+8,40),(x+8,16))
        contacts()
