"""Sideboard with Drawers and Shelf."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2b93d079-db33-43b5-8437-9b6a69107589'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/shelf drawers_2b93d079-db33-43b5-8437-9b6a69107589.svg'
AUTHOR = 'gpt-6'


class SideboardTwoDoorsOpenUpperShelf(Solo48):
    icon_id = 'sideboard-two-doors-open-upper-shelf'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/furniture"
    aliases = ()
    keywords = ('sideboard', 'with', 'drawers', 'and', 'shelf')

    def build(self):
        # Plan: Cabinet and shelf share upright posts; equal doors meet at x24. Extremes (4,8)-(44,40).
        # Reduction: Reduce thick top to one rail and omit tiny hardware.
        # Reference: Lucide bed-single: shared structural rails and uprights.

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

        path('top',(4,8),(8,8),(40,8),(44,8))
        for x in (8,40):line(f'post-{x}',(x,8),(x,20))
        path('cabinet',(4,20),(8,20),(24,20),(40,20),(44,20),(44,32),(40,32),(24,32),(8,32),(4,32),closed=True)
        line('seam',(24,20),(24,32))
        for x in (8,40):line(f'leg-{x}',(x,32),(x,40))
        contacts()
