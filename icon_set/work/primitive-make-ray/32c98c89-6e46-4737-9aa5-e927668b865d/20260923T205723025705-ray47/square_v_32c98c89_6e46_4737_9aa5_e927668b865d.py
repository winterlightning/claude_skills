from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '32c98c89-6e46-4737-9aa5-e927668b865d'
SOURCE_PATH = 'icon_set/work/todo-references/square v_32c98c89-6e46-4737-9aa5-e927668b865d.svg'
AUTHOR = 'gpt-6'
# Plan: Rounded square with a check mark, matching the supplied square-v artwork.
# References: Joined two-segment check with deliberate asymmetry.
# Reduction: No parts omitted; source is a check rather than a letter V.

class AuthoredIcon(Solo48):
    icon_id = 'square-v'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('square', 'v')

    def build(self):
        self.box("frame",6,6,42,42,4)
        self.add_polyline('check',(15,24),(22,31),(33,17))

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
