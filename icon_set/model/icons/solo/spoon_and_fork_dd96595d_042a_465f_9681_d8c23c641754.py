from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dd96595d-042a-465f-9681-d8c23c641754'
SOURCE_PATH = 'icon_set/work/todo-references/spoon and fork_dd96595d-042a-465f-9681-d8c23c641754.svg'
AUTHOR = 'gpt-6'
# Plan: Round plate with a three-tined fork inside and a short diagonal utensil handle outside.
# References: utensils: equal tines and a rounded fork bowl; supplied image has no separate spoon bowl.
# Reduction: No defining parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'spoon-and-fork'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('spoon', 'and', 'fork')

    def build(self):
        self.circle('plate',24,24,18)
        self.add_line('tine-left',(16,19),(16,24));self.add_arc('bowl',(16,24),(32,24),radius_x=8,sweep=False)
        self.add_line('tine-right',(32,24),(32,19));self.add_contour('fork','tine-left','bowl','tine-right')
        self.add_line('center-tine',(24,19),(24,32));self.add_line('handle',(24,32),(24,33))
        self.relate('connect','center-tine','fork');self.relate('connect','handle','fork');self.relate('connect','center-tine','handle')
        self.add_line('outer-handle',(37,37),(42,42));self.relate('connect','outer-handle','plate')

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
