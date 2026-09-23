from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '888e184a-239b-4644-8a3e-4dd840b12966'
SOURCE_PATH = 'icon_set/work/todo-references/row selected point_888e184a-239b-4644-8a3e-4dd840b12966.svg'
AUTHOR = 'gpt-6'
# Plan: Selected row crossing a vertical table fragment, with a right arrow pointing into its left edge.
# Reference: Rounded rectangle and arrow construction; no exact local Lucide subject match.
# Reduction: Reduced open table fragment to upper and lower L-shaped corners.

class AuthoredIcon(Solo48):
    icon_id = 'row-selected-point'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('row', 'selected', 'point')

    def build(self):
        self.add_polyline('upper',(24,12),(24,6),(42,6))
        self.add_polyline('lower',(24,36),(24,42),(42,42))
        self.box('row',18,20,42,28,2)
        self.add_line('divider',(29,20),(29,28));self.relate('connect','divider','row')
        self.add_line('shaft',(6,24),(10,24))
        self.add_polyline('arrow',(6,20),(10,24),(6,28));self.relate('connect','shaft','arrow')

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
