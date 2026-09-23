from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '454d4a71-e0ab-4aca-9a55-2498b1b5a3c7'
SOURCE_PATH = 'icon_set/work/todo-references/square plus_454d4a71-e0ab-4aca-9a55-2498b1b5a3c7.svg'
AUTHOR = 'gpt-6'
# Plan: Rounded square with a centered plus sign.
# References: square-plus: shared central junction and equal arms.
# Reduction: No parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'square-plus'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('square', 'plus')

    def build(self):
        self.box("frame",6,6,42,42,4)
        self.add_line('vertical',(24,15),(24,33))
        self.add_line('horizontal',(15,24),(33,24));self.relate('connect','vertical','horizontal')

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
