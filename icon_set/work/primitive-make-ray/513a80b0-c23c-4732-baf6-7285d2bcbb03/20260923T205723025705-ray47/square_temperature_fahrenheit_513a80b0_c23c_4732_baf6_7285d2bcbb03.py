from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '513a80b0-c23c-4732-baf6-7285d2bcbb03'
SOURCE_PATH = 'icon_set/work/todo-references/square temperature fahrenheit_513a80b0-c23c-4732-baf6-7285d2bcbb03.svg'
AUTHOR = 'gpt-6'
# Plan: Rounded square enclosing a degree mark and the letter F.
# References: No exact local Lucide typography match; F is hand-authored with shared stem intersections.
# Reduction: Tiny source degree mark retained as a dot; no defining parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'square-temperature-fahrenheit'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('square', 'temperature', 'fahrenheit')

    def build(self):
        self.box("frame",6,6,42,42,4)
        self.add_dot('degree',(16,17))
        self.add_polyline('f',(26,33),(26,16),(33,16))
        self.add_line('f-bar',(26,25),(32,25));self.relate('connect','f','f-bar')

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
