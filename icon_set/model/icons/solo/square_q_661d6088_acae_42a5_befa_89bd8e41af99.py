from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '661d6088-acae-42a5-befa-89bd8e41af99'
SOURCE_PATH = 'icon_set/work/todo-references/square q_661d6088-acae-42a5-befa-89bd8e41af99.svg'
AUTHOR = 'gpt-6'
# Plan: Rounded square containing a circular Q with a diagonal tail.
# References: No exact local Lucide letter match; circular bowl and attached diagonal tail.
# Reduction: No parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'square-q'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('square', 'q')

    def build(self):
        self.box("frame",6,6,42,42,4)
        self.circle('q-bowl',24,24,9)
        self.add_line('q-tail',(30,30),(33,33));self.relate('connect','q-bowl','q-tail')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,l,t,r,b,q=4):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)
