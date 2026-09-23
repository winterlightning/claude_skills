from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '776da6f9-d7d4-597a-a158-44ea69d4fbb8'
SOURCE_PATH = 'icon_set/work/todo-references/saving money flower_776da6f9-d7d4-597a-a158-44ea69d4fbb8.svg'
AUTHOR = 'gpt-6'
# Plan: Money flower: dollar coin atop stem with paired leaves.
# Reference: sprout: paired leaf contours and shared stem; circular coin and handwritten dollar.
# Reduction: No defining parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'saving-money-flower'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('saving', 'money', 'flower')

    def build(self):
        self.circle('coin',24,14,10)
        self.add_bezier('dollar',(27,10),((19,7),(19,15),(24,14)),((30,13),(30,21),(21,18)))
        self.add_line('dollar-stem',(24,7),(24,21));self.relate('connect','dollar','dollar-stem')
        self.add_line('stem',(24,24),(24,44));self.relate('connect','coin','stem')
        for n,s in [('left',-1),('right',1)]:
            def p(x,y):return (24+s*x,y)
            self.add_bezier(n,p(16,28),(p(6,27),p(4,34),p(8,36)),(p(14,38),p(16,33),p(16,28)))
            self.add_line(n+'-branch',p(8,36),(24,44));self.relate('connect',n,n+'-branch');self.relate('connect','stem',n+'-branch')

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
