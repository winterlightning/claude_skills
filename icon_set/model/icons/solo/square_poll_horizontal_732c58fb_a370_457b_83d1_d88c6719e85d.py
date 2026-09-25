from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '732c58fb-a370-457b-83d1-d88c6719e85d'
SOURCE_PATH = 'icon_set/work/todo-references/square poll horizontal_732c58fb-a370-457b-83d1-d88c6719e85d.svg'
AUTHOR = 'gpt-6'
# Plan: Rounded square with three horizontal poll rows, the bottom row shorter.
# References: Simple repeated horizontal strokes inside a canonical rounded square.
# Reduction: No parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'square-poll-horizontal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('square', 'poll', 'horizontal')

    def build(self):
        self.box("frame",6,6,42,42,4)
        for i,length in enumerate((18,18,10)):
            y=16+8*i;self.add_line('row-'+str(i),(15,y),(15+length,y))

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
