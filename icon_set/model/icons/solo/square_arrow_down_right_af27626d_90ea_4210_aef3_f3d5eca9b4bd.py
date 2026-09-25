from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'af27626d-90ea-4210-aef3-f3d5eca9b4bd'
SOURCE_PATH = 'icon_set/work/todo-references/square arrow down right_af27626d-90ea-4210-aef3-f3d5eca9b4bd.svg'
AUTHOR = 'gpt-6'
# Plan: Vertical downward arrow in a rounded square; supplied artwork is not diagonal.
# References: square-arrow-right: consistent rounded frame and joined arrow shaft/head.
# Reduction: No defining parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'square-arrow-down-right'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('square', 'arrow', 'down', 'right')

    def build(self):
        self.box('frame',6,6,42,42,4)
        self.add_line('shaft',(24,15),(24,33))
        self.add_polyline('head',(16,25),(24,33),(32,25))
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
