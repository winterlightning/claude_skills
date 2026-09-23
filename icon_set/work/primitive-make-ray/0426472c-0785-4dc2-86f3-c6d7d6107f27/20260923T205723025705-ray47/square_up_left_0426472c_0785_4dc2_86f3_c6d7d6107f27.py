from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0426472c-0785-4dc2-86f3-c6d7d6107f27'
SOURCE_PATH = 'icon_set/work/todo-references/square up left_0426472c-0785-4dc2-86f3-c6d7d6107f27.svg'
AUTHOR = 'gpt-6'
# Plan: Bent upward arrow: horizontal approach from left turns upward inside a rounded square.
# References: square-arrow-up: equal head wings; rounded elbow on the shaft.
# Reduction: No parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'square-up-left'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('square', 'up', 'left')

    def build(self):
        self.box("frame",6,6,42,42,4)
        self.add_line('shaft-bottom',(15,33),(21,33))
        self.add_arc('elbow',(21,33),(24,30),radius_x=3,sweep=False)
        self.add_line('shaft-top',(24,30),(24,15));self.add_contour('shaft','shaft-bottom','elbow','shaft-top')
        self.add_polyline('head',(18,21),(24,15),(30,21));self.relate('connect','shaft','head')

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
