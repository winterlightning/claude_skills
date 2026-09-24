from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e9b350be-f0e4-49b9-8413-4a4d1c678f43'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_33/rupee sign_e9b350be-f0e4-49b9-8413-4a4d1c678f43.svg'
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
        # The bowl departs the top rule vertically at its right endpoint, avoiding a grazing wedge.
        self.add_polyline('top',(10,4),(38,4),(38,12))
        self.add_arc('bowl',(38,12),(24,26),radius_x=14)
        self.add_polyline('return-leg',(24,26),(10,26),(30,44))
        self.add_line('bar',(10,12),(38,12))
        self.relate('connect','top','bowl')
        self.relate('connect','top','bar')
        self.relate('connect','bowl','bar')
        self.relate('connect','bowl','return-leg')

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
