"""Vase on Display Stand."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47586b25-f4af-4946-808f-5f086ef3d61b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/museum art_47586b25-f4af-4946-808f-5f086ef3d61b.svg'
AUTHOR = 'gpt-6'


class VaseOnDisplayPedestal(Solo48):
    icon_id = 'vase-on-display-pedestal'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "furnitures"
    categories = ("furnitures", "primitives")
    aliases = ()
    keywords = ('vase', 'on', 'display', 'stand')

    def build(self):
        # Plan: A mirrored flared vase sits on a broad pedestal with two short legs. Extremes (8,4)-(40,44).
        # Reduction: Omit painted wavy decoration and pedestal lower stretcher to keep the vase silhouette open.
        # Reference: Lucide lamp: axial object supported by a shared pedestal; no useful vase match.

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

        path('mouth',(14,4),(34,4))
        # Paired concave necks flow into a broad elliptical body.
        arc('neck-right',(34,4),(30,12),10,sweep=False)
        arc('belly-right',(30,12),(30,30),12,12)
        line('base-right',(30,30),(18,30))
        arc('belly-left',(18,30),(18,12),12,12)
        arc('neck-left',(18,12),(14,4),10,sweep=False)
        self.contours = [c for c in self.contours if c.contour_id != 'mouth']
        self.add_contour('vase','mouth-1','neck-right','belly-right','base-right','belly-left','neck-left',closed=True)
        nodes={'vase':((18,30),(30,30))}
        path('pedestal',(8,30),(18,30),(30,30),(40,30),(40,38),(34,38),(14,38),(8,38),closed=True)
        for x in (14,34):line(f'leg-{x}',(x,38),(x,44))
        contacts()
