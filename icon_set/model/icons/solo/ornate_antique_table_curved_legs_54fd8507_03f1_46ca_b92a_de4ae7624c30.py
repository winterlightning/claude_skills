"""Vintage Ornate Antique Table."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '54fd8507-03f1-46ca-b92a-de4ae7624c30'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/table retro_54fd8507-03f1-46ca-b92a-de4ae7624c30.svg'
AUTHOR = 'gpt-6'


class OrnateAntiqueTableCurvedLegs(Solo48):
    icon_id = 'ornate-antique-table-curved-legs'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "furnitures"
    categories = ("furnitures", "primitives")
    aliases = ()
    keywords = ('vintage', 'ornate', 'antique', 'table')

    def build(self):
        # Plan: Wide rounded top above a scalloped apron and mirrored bowed legs. Extremes (4,8)-(44,40).
        # Reduction: Reduce leg thickness to single curving strokes and apron to two broad scallops.
        # Reference: Lucide armchair: coherent curves with shared attachment nodes.

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

        rounded('top',4,8,44,16,4,bottom=(10,24,38))
        # A single pair of wide semicircular scallops below the top.
        arc('apron-left',(10,16),(24,16),7,6,sweep=False)
        arc('apron-right',(24,16),(38,16),7,6,sweep=False)
        for label,x,sign in [('left',10,-1),('right',38,1)]:
         self.add_bezier(f'leg-{label}',(x,16),((x+sign*9,25),(x-sign*3,33),(x,40)))
         nodes[f'leg-{label}']=((x,16),(x,40))
        contacts()
