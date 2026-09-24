from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b60b81a4-9d88-4566-84d3-7931d6c1da67'
SOURCE_PATH = 'icon_set/work/todo-references/sass circle logo_b60b81a4-9d88-4566-84d3-7931d6c1da67.svg'
AUTHOR = 'gpt-6'
# Plan: Circular Sass logo with an open upper script loop and lower S loop, hand-authored as smooth cubics.
# Reference: No useful exact local Lucide logo match. Supplied Sass reference owns the calligraphic path.
# Reduction: Simplified small loop curvature to integer knots; retained both script loops.

class AuthoredIcon(Solo48):
    icon_id = 'sass-circle-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('sass', 'circle', 'logo')

    def build(self):
        self.circle('badge',24,24,20)
        self.add_bezier('script',(23,21),((30,24),(35,17),(29,15)),((25,13),(15,18),(15,22)),((14,26),(27,27),(24,34)),((22,40),(12,36),(17,32)),((22,28),(30,27),(31,31)),((32,33),(31,35),(30,35)))

    def circle(self, n, x, y, r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self, n, l, t, r, b, q=3):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)
