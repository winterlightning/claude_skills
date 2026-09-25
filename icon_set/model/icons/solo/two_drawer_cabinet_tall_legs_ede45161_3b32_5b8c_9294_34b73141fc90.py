"""Two Drawer Storage Cabinet."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ede45161-3b32-5b8c-9294-34b73141fc90'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/dresser drawers_ede45161-3b32-5b8c-9294-34b73141fc90.svg'
AUTHOR = 'gpt-6'


class TwoDrawerCabinetTallLegs(Solo48):
    icon_id = 'two-drawer-cabinet-tall-legs'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "furnitures"
    categories = ("furnitures", "primitives")
    aliases = ()
    keywords = ('two', 'drawer', 'storage', 'cabinet')

    def build(self):
        # Plan: Two equal drawer bays centered on x24, repeated horizontal pulls, and shared legs. Extremes (8,4)-(40,44).
        # Reduction: Retain both pulls and drawer count; use a full-height body to reserve clearance for both pulls.
        # Reference: Lucide bed-single: rounded shell and split structural rails.

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

        rounded('body',8,4,40,38,2,left=(21,),right=(21,),bottom=(12,36))
        line('divider',(8,21),(40,21))
        for i,y in enumerate((13,29)):line(f'pull-{i}',(20,y),(28,y))
        for x in (12,36):line(f'leg-{x}',(x,38),(x,44))
        contacts()
