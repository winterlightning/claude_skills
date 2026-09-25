"""Knotted bandana with equal pointed tie ends, round knot, curved neck fold and pointed hanging cloth; mirrored about x24.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction references: No useful local Lucide match; original reference informs construction.
Omissions: Secondary neck folds omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'da69e025-ec35-4e8e-b0d5-492782d18d44'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/bandana_da69e025-ec35-4e8e-b0d5-492782d18d44.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'knotted-triangular-neck-bandana'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bandana',)
    def build(self):

        def path(n, start, steps, closed=False):
            ids=[]; p=start
            for i,step in enumerate(steps):
                k=f'{n}-{i}';kind=step[0];q=step[1]
                if kind=='L': self.add_line(k,p,q)
                elif kind=='A': self.add_arc(k,p,q,radius_x=step[2],radius_y=step[3],sweep=step[4])
                elif kind=='B': self.add_bezier(k,p,(step[2],step[3],q))
                ids.append(k);p=q
            self.add_contour(n,*ids,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        circle('knot',24,15,5)
        path('cloth',(19,15),[('B',(8,6),(12,13),(9,9)),('B',(14,18),(8,11),(10,16)),('B',(6,26),(10,20),(7,23)),('B',(24,42),(7,32),(18,39)),('B',(42,26),(30,39),(41,32)),('B',(34,18),(41,23),(38,20)),('B',(40,6),(38,16),(40,11)),('B',(29,15),(39,9),(36,13))])
        join('knot','cloth')
        path('fold',(6,26),[('B',(42,26),(16,34),(32,34))]);join('fold','cloth')
