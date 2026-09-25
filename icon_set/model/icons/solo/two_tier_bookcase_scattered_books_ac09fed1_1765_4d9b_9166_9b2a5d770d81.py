"""Two Tier Bookshelf with Books."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac09fed1-1765-4d9b-9166-9b2a5d770d81'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/shelf books 1_ac09fed1-1765-4d9b-9166-9b2a5d770d81.svg'
AUTHOR = 'gpt-6'


class TwoTierBookcaseScatteredBooks(Solo48):
    icon_id = 'two-tier-bookcase-scattered-books'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "furnitures"
    aliases = ()
    keywords = ('two', 'tier', 'bookshelf', 'with', 'books')

    def build(self):
        # Plan: Two shelf bays with upright upper books and leaning lower books. Extremes (6,6)-(42,42).
        # Reduction: Reduce each group from three outlined books to two distinct spines, preserving opposite group placement and lean.
        # Reference: Lucide bed-single: split frame rails; no useful local bookcase match.

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

        path('frame',(6,6),(42,6),(42,24),(42,42),(29,42),(19,42),(6,42),(6,24),closed=True)
        path('shelf',(6,24),(14,24),(24,24),(42,24))
        for x in (14,24):line(f'upper-book-{x}',(x,14),(x,24))
        for x in (23,33):line(f'lower-book-{x}',(x,32),(x-4,42))
        contacts()
