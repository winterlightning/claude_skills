"""Sideboard with Lamp and Vase."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cb91a90c-8a6b-4c96-b53f-406fe78a68c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/console lamp_cb91a90c-8a6b-4c96-b53f-406fe78a68c9.svg'
AUTHOR = 'gpt-6'


class SideboardLampVaseDisplay(Solo48):
    icon_id = 'sideboard-lamp-vase-display'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "furnitures"
    aliases = ()
    keywords = ('sideboard', 'with', 'lamp', 'and', 'vase')

    def build(self):
        # Plan: A left vase and right lamp sit on a two-door cabinet, with shared support nodes. Extremes (6,6)-(42,42).
        # Reduction: Omit small handles, leg splay, lamp base ornament and source sprig; retain vase, shade and two-door cabinet.
        # Reference: Lucide lamp: trapezoidal shade above a shared central stem.

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

        path('shade',(30,6),(38,6),(42,16),(34,16),(26,16),closed=True)
        line('lamp-stem',(34,16),(34,26))
        path('vase-mouth',(6,12),(18,12),(18,20))
        arc('vase-round-right',(18,20),(12,26),6)
        arc('vase-round-left',(12,26),(6,20),6)
        line('vase-left',(6,20),(6,12))
        self.contours = [c for c in self.contours if c.contour_id != 'vase-mouth']
        self.add_contour('vase','vase-mouth-1','vase-mouth-2','vase-round-right','vase-round-left','vase-left',closed=True)
        nodes['vase']=((6,12),(18,12),(12,26))
        for part in ('vase-mouth','vase-round-right','vase-round-left','vase-left'):
            nodes.pop(part)
        path('cabinet',(6,26),(12,26),(24,26),(34,26),(42,26),(42,34),(36,34),(24,34),(12,34),(6,34),closed=True)
        line('door-seam',(24,26),(24,34))
        line('left-leg',(12,34),(12,42));line('right-leg',(36,34),(36,42))
        contacts()
