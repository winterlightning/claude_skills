from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd0a09db7-a22e-4745-bc46-9d0121135f54'
SOURCE_PATH = 'icon_set/work/todo-references/square ampersand_d0a09db7-a22e-4745-bc46-9d0121135f54.svg'
AUTHOR = 'gpt-6'
# Plan: Rounded square enclosing a hand-drawn ampersand with crossed lower loop.
# References: No exact local Lucide ampersand match; smooth handwritten loops and canonical rounded frame.
# Reduction: No defining parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'square-ampersand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('square', 'ampersand')

    def build(self):
        self.box('frame',6,6,42,42,4)
        self.add_bezier('ampersand',(31,33),((27,29),(17,20),(18,17)),((19,14),(29,15),(28,18)),((27,22),(16,23),(15,28)),((14,33),(28,35),(32,25)))

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,l,t,r,b,q=3):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)
