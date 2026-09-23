from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '545b491e-d8c6-4538-a8f0-b05b3ee99855'
SOURCE_PATH = 'icon_set/work/todo-references/row insert_545b491e-d8c6-4538-a8f0-b05b3ee99855.svg'
AUTHOR = 'gpt-6'
# Plan: Two empty row bars with a rightward insertion chevron on the left.
# Reference: square-dashed/rounded rectangle construction: repeated equal corner radii.
# Reduction: No defining parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'row-insert'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('row', 'insert')

    def build(self):
        for n,y in [('upper',6),('lower',30)]: self.box(n,20,y,42,y+12,3)
        self.add_polyline('insert',(6,18),(12,24),(6,30))

    def circle(self, n, x, y, r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self, n, l, t, r, b, q=3):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)
