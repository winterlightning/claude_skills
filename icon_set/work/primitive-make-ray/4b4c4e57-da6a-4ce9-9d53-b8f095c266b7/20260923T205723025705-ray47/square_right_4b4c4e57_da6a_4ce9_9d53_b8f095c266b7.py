from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4b4c4e57-da6a-4ce9-9d53-b8f095c266b7'
SOURCE_PATH = 'icon_set/work/todo-references/square right_4b4c4e57-da6a-4ce9-9d53-b8f095c266b7.svg'
AUTHOR = 'gpt-6'
# Plan: Rightward arrow inside a square enclosure with two chamfered right corners.
# References: square-arrow-up: joined arrow construction; source owns asymmetric tag-like enclosure.
# Reduction: No parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'square-right'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('square', 'right')

    def build(self):
        self.add_polyline('frame',(6,6),(30,6),(42,18),(42,30),(30,42),(6,42),closed=True)
        self.add_line('shaft',(15,24),(32,24));self.add_polyline('head',(25,17),(32,24),(25,31));self.relate('connect','shaft','head')

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
