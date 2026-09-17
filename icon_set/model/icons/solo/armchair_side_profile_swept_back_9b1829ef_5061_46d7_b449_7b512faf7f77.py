"""Side View Armchair."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b1829ef-5061-46d7-b449-7b512faf7f77'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/seat_9b1829ef-5061-46d7-b449-7b512faf7f77.svg'
AUTHOR = 'gpt-6'


class ArmchairSideProfileSweptBack(Solo48):
    icon_id = 'armchair-side-profile-swept-back'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/furniture"
    aliases = ()
    keywords = ('side', 'view', 'armchair')

    def build(self):
        # Plan: One asymmetric swept shell, a horizontal seat and two splayed legs. Extremes (8,4)-(40,44).
        # Reduction: Omit upholstery thickness; retain the forward-facing seat and sweeping shell.
        # Reference: Lucide armchair: a coherent rounded shell with shared leg attachments.

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

        line('back',(8,4),(12,26))
        arc('heel',(12,26),(20,34),8,sweep=False)
        path('bottom',(20,34),(32,34),(36,34))
        arc('front',(36,34),(40,30),4,sweep=False)
        arc('seat-tip',(40,30),(34,24),6,sweep=False)
        line('seat',(34,24),(22,24))
        self.contours = [c for c in self.contours if c.contour_id != 'bottom']
        self.add_contour('shell','back','heel','bottom-1','bottom-2','front','seat-tip','seat')
        # Replace helper records with this continuous shell's attachment nodes.
        nodes={'shell':((8,4),(20,34),(32,34),(22,24))}
        line('leg-left',(20,34),(16,44));line('leg-right',(32,34),(36,44))
        contacts()
