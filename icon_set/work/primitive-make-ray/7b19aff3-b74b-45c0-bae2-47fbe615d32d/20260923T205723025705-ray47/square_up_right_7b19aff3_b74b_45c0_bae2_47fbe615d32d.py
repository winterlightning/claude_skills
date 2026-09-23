from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7b19aff3-b74b-45c0-bae2-47fbe615d32d'
SOURCE_PATH = 'icon_set/work/todo-references/square up right_7b19aff3-b74b-45c0-bae2-47fbe615d32d.svg'
AUTHOR = 'gpt-6'
# Plan: Upward arrow in a rounded square; source direction is vertical.
# References: square-arrow-up: shared central axis and equal arrowhead wings.
# Reduction: No parts omitted; tiny shaft/head discontinuity in source is joined coherently.

class AuthoredIcon(Solo48):
    icon_id = 'square-up-right'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('square', 'up', 'right')

    def build(self):
        self.box("frame",6,6,42,42,4)
        self.add_line('shaft',(24,33),(24,15));self.add_polyline('head',(16,23),(24,15),(32,23));self.relate('connect','shaft','head')

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
