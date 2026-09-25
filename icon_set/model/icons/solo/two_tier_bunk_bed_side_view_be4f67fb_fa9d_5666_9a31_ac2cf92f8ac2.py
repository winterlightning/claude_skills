"""Two Tier Bunk Bed."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be4f67fb-fa9d-5666-9a31-ac2cf92f8ac2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/bed bunk_be4f67fb-fa9d-5666-9a31-ac2cf92f8ac2.svg'
AUTHOR = 'gpt-6'


class TwoTierBunkBedSideView(Solo48):
    icon_id = 'two-tier-bunk-bed-side-view'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "furnitures"
    aliases = ()
    keywords = ('two', 'tier', 'bunk', 'bed')

    def build(self):
        # Plan: Two mattress rails and repeated left pillows connect tall side posts. Extremes (6,6)-(42,42).
        # Reduction: Reduce each mattress to one rail; preserve two separate pillow forms.
        # Reference: Lucide bed-single: coherent rounded pillow and mattress support.

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

        for x in (6,42):path(f'post-{x}',(x,6),(x,10),(x,18),(x,26),(x,34),(x,42))
        for i,y in enumerate((18,34)):
         path(f'mattress-{i}',(6,y),(18,y),(42,y))
         line(f'pillow-top-{i}',(6,y-8),(14,y-8))
         arc(f'pillow-corner-{i}',(14,y-8),(18,y-4),4)
         line(f'pillow-side-{i}',(18,y-4),(18,y))
         self.add_contour(f'pillow-{i}',f'pillow-top-{i}',f'pillow-corner-{i}',f'pillow-side-{i}')
         nodes[f'pillow-{i}']=nodes.pop(f'pillow-top-{i}')+nodes.pop(f'pillow-corner-{i}')+nodes.pop(f'pillow-side-{i}')
        contacts()
