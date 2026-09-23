from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9ebf76c2-ab68-40f7-a75f-c12173488a0a'
SOURCE_PATH = 'icon_set/work/todo-references/square this way up_9ebf76c2-ab68-40f7-a75f-c12173488a0a.svg'
AUTHOR = 'gpt-6'
# Plan: Rounded square with two upward arrows above a shared horizontal baseline.
# References: square-arrow-up: joined shaft/head; arrows share size and baseline.
# Reduction: No parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'square-this-way-up'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('square', 'this', 'way', 'up')

    def build(self):
        self.box("frame",6,6,42,42,4)
        for n,x in [('left',18),('right',30)]:
            self.add_line(n+'-shaft',(x,16),(x,27))
            self.add_polyline(n+'-head',(x-4,20),(x,16),(x+4,20));self.relate('connect',n+'-shaft',n+'-head')
        self.add_line('baseline',(15,35),(33,35))

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
