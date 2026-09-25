from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fbc92d89-8107-55c0-bb86-46259baa871b'
SOURCE_PATH = 'icon_set/work/todo-references/shelf tv_fbc92d89-8107-55c0-bb86-46259baa871b.svg'
AUTHOR = 'gpt-6'
# Plan: Television on a trapezoidal stand above a low shelf with two short legs.
# Construction references: tv: rounded screen with clean straight sides; paired stand and shelf legs share x-axis symmetry.
# Reduction: No defining parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'shelf-tv-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "furnitures"
    aliases = ()
    keywords = ('shelf', 'tv')

    def build(self):
        self.box('screen',10,6,38,22,2)
        self.add_line('stand-left',(19,22),(15,30));self.add_line('stand-right',(29,22),(33,30))
        self.add_polyline("shelf",(6,30),(42,30),(42,38),(6,38),closed=True)
        for n in ('stand-left','stand-right'):
            self.relate('connect',n,'screen');self.relate('connect',n,'shelf')
        for n,x in [('left',10),('right',38)]:
            self.add_line(n+'-leg',(x,38),(x,42));self.relate('connect',n+'-leg','shelf')

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

    def shield(self):
        self.add_bezier('crown-left',(8,12),((15,12),(21,7),(24,4)))
        self.add_bezier('crown-right',(24,4),((27,7),(33,12),(40,12)))
        self.add_line('wall-right',(40,12),(40,23))
        self.add_bezier('base-right',(40,23),((40,33),(33,40),(24,44)))
        self.add_bezier('base-left',(24,44),((15,40),(8,33),(8,23)))
        self.add_line('wall-left',(8,23),(8,12))
        self.add_contour('shield','crown-left','crown-right','wall-right','base-right','base-left','wall-left',closed=True)
