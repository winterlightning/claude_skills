"""Three Drawer Dresser."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eab7240d-0a70-5dd1-8557-4f65c7ed8837'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/dresser drawers_eab7240d-0a70-5dd1-8557-4f65c7ed8837.svg'
AUTHOR = 'gpt-6'


class ThreeDrawerDresserHorizontalPulls(Solo48):
    icon_id = 'three-drawer-dresser-horizontal-pulls'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "furnitures"
    categories = ("furnitures", "primitives")
    aliases = ()
    keywords = ('three', 'drawer', 'dresser')

    def build(self):
        # Plan: Three equal drawer fronts within one softly rounded cabinet; two equal legs. Extremes (6,6)-(42,42).
        # Reduction: Omit all three tiny pulls: three detached pulls and their six clearances cannot fit a 40-unit body. Preserve exactly three drawers.
        # Reference: Lucide bed-single: rounded shell with shared horizontal rails.

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

        l,t,r,b,foot = (8,4,40,40,44) if False else (6,6,42,36,42)
        step=(b-t)//3
        rounded('body',l,t,r,b,2,left=(t+step,t+2*step),right=(t+step,t+2*step),bottom=(l+4,r-4))
        for i in (1,2):line(f'divider-{i}',(l,t+i*step),(r,t+i*step))
        for x in (l+4,r-4):line(f'leg-{x}',(x,b),(x,foot))
        contacts()
