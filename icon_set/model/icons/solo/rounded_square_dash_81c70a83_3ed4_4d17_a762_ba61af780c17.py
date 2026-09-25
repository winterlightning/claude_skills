from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81c70a83-3ed4-4d17-a762-ba61af780c17'
SOURCE_PATH = 'icon_set/work/todo-references/rounded square dash_81c70a83-3ed4-4d17-a762-ba61af780c17.svg'
AUTHOR = 'gpt-6'
# Plan: Dashed rounded square using four matching quarter-circle corners and four centered short dashes.
# Reference: square-dashed: equal repeated corner geometry and separated marks.
# Reduction: Reduced dash count to maintain 8-unit centerline gaps.

class AuthoredIcon(Solo48):
    icon_id = 'rounded-square-dash'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('rounded', 'square', 'dash')

    def build(self):
        for n,a,b in [('tl',(6,14),(14,6)),('tr',(34,6),(42,14)),('br',(42,34),(34,42)),('bl',(14,42),(6,34))]:
            self.add_arc(n,a,b,radius_x=8)
        for n,a,b in [('top',(23,6),(25,6)),('right',(42,23),(42,25)),('bottom',(25,42),(23,42)),('left',(6,25),(6,23))]: self.add_line(n,a,b)

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
