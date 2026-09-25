from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24b42876-a6e9-460a-9c01-a039af2dee79'
SOURCE_PATH = 'icon_set/work/todo-references/rounded rectanguler 1_24b42876-a6e9-460a-9c01-a039af2dee79.svg'
AUTHOR = 'gpt-6'
# Plan: Closed quadrilateral with two diagonally opposed quarter-circle corners; both radii share one parameter.
# Reference: No exact Lucide match; elementary tangent quarter-circle construction.
# Reduction: No parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'rounded-rectanguler-1'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    aliases = ()
    keywords = ('rounded', 'rectanguler', '1')

    def build(self):
        l,t,r,b,q = (6,6,42,42,14)
        self.add_line('top',(l+q,t),(r,t))
        self.add_line('right',(r,t),(r,b-q))
        self.add_arc('round-bottom-right',(r,b-q),(r-q,b),radius_x=q)
        self.add_line('bottom',(r-q,b),(l,b))
        self.add_line('left',(l,b),(l,t+q))
        self.add_arc('round-top-left',(l,t+q),(l+q,t),radius_x=q)
        self.add_contour('outline','top','right','round-bottom-right','bottom','left','round-top-left',closed=True)

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
