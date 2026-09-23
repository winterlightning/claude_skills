from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0a3eaab8-811e-4846-b3b3-d0a35a3068ff'
SOURCE_PATH = 'icon_set/work/todo-references/sort down_0a3eaab8-811e-4846-b3b3-d0a35a3068ff.svg'
AUTHOR = 'gpt-6'
# Plan: Downward arrow over three equally spaced horizontal sort rows.
# References: arrow-down: equal arrow wings and shared shaft endpoint.
# Reduction: No defining parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'sort-down'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('sort', 'down')

    def build(self):
        self.add_line('shaft',(24,6),(24,18))
        self.add_polyline('head',*((16,10),(24,18),(32,10)))
        self.relate('connect','shaft','head')
        for i in range(3):
            y=26+8*i;self.add_line('row-'+str(i),(6,y),(42,y))

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
