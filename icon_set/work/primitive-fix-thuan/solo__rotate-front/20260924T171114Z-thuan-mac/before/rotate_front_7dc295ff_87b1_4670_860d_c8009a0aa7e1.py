from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7dc295ff-87b1-4670-860d-c8009a0aa7e1'
SOURCE_PATH = 'icon_set/work/todo-references/rotate front_7dc295ff-87b1-4670-860d-c8009a0aa7e1.svg'
AUTHOR = 'gpt-6'
# Plan: Overlapping front and rear tiles with a clockwise rotation arc above the rear tile.
# Reference: rotate-cw: coherent curved arrow; rounded tile geometry.
# Reduction: No defining parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'rotate-front'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('rotate', 'front')

    def build(self):
        self.box('front',6,14,26,34)
        self.add_polyline('rear',(26,28),(42,28),(42,42),(16,42),(16,34))
        self.relate('connect','front','rear')
        self.add_arc('rotation',(30,6),(42,18),radius_x=12)
        self.add_polyline('start-head',(34,6),(30,6),(34,10))
        self.add_polyline('end-head',(36,14),(42,18),(42,10))
        self.relate('connect','rotation','start-head');self.relate('connect','rotation','end-head')

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
