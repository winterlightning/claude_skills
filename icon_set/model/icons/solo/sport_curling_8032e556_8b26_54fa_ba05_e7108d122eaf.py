from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8032e556-8b26-54fa-ba05-e7108d122eaf'
SOURCE_PATH = 'icon_set/work/todo-references/sport curling_8032e556-8b26-54fa-ba05-e7108d122eaf.svg'
AUTHOR = 'gpt-6'
# Plan: Curling stone, diagonal broom and small curling stone marker.
# References: No useful exact local Lucide match; coherent stone dome, handle and diagonal broom.
# Reduction: Omitted small stone side seam; retained handle, broom head and round marker.

class AuthoredIcon(Solo48):
    icon_id = 'sport-curling'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('sport', 'curling')

    def build(self):
        self.add_arc('stone-top',(6,28),(26,28),radius_x=10,radius_y=6)
        self.add_line('stone-mid',(6,28),(26,28));self.relate('connect','stone-top','stone-mid')
        self.add_bezier('stone-side',(6,28),((6,35),(8,36),(10,36)))
        self.relate('connect','stone-side','stone-top');self.relate('connect','stone-side','stone-mid')
        self.add_polyline('handle',(13,22),(13,17),(21,17));self.relate('connect','handle','stone-top')
        self.add_line('broom-shaft',(42,6),(23,40))
        self.add_bezier('broom-head',(23,40),((21,44),(13,42),(13,38)),((13,32),(19,34),(27,35)))
        self.relate('connect','broom-shaft','broom-head')
        self.circle('marker',36,39,3)

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
