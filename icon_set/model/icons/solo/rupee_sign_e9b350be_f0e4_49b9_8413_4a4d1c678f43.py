from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e9b350be-f0e4-49b9-8413-4a4d1c678f43'
SOURCE_PATH = 'icon_set/work/todo-references/rupee sign_e9b350be-f0e4-49b9-8413-4a4d1c678f43.svg'
AUTHOR = 'gpt-6'
# Plan: Indian rupee sign with two horizontal rules, rounded bowl and diagonal leg.
# Reference: indian-rupee: two bars crossing a single rounded bowl plus diagonal leg.
# Reduction: No defining parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'rupee-sign'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('rupee', 'sign')

    def build(self):
        self.add_line('top',(10,4),(38,4))
        self.add_arc('bowl-top',(18,4),(30,16),radius_x=12)
        self.add_arc('bowl-bottom',(30,16),(18,28),radius_x=12)
        self.add_line('return',(18,28),(10,28))
        self.add_line('leg',(10,28),(30,44))
        self.add_contour('bowl-leg','bowl-top','bowl-bottom','return','leg')
        self.add_line('bar-left',(10,16),(30,16));self.add_line('bar-right',(30,16),(38,16))
        self.relate('connect','top','bowl-leg');self.relate('connect','bar-left','bowl-leg');self.relate('connect','bar-right','bowl-leg');self.relate('connect','bar-left','bar-right')

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
