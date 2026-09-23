from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0cb36b98-e0c5-4184-a2a5-b1149dd0db98'
SOURCE_PATH = 'icon_set/work/todo-references/square arrow down left_0cb36b98-e0c5-4184-a2a5-b1149dd0db98.svg'
AUTHOR = 'gpt-6'
# Plan: Diagonal arrow points down-right inside a rounded square, matching the supplied artwork rather than its down-left filename.
# References: square-arrow-right: consistent rounded frame and joined arrow shaft/head.
# Reduction: No defining parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'square-arrow-down-left'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('square', 'arrow', 'down', 'left')

    def build(self):
        self.box('frame',6,6,42,42,4)
        self.add_line('shaft',(15,15),(33,33))
        self.add_polyline('head',(23,33),(33,33),(33,23))
        self.relate('connect','shaft','head')

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
