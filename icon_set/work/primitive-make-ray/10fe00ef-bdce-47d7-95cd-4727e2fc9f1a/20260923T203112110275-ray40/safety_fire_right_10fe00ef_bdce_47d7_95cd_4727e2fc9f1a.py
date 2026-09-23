from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '10fe00ef-bdce-47d7-95cd-4727e2fc9f1a'
SOURCE_PATH = 'icon_set/work/todo-references/safety fire right_10fe00ef-bdce-47d7-95cd-4727e2fc9f1a.svg'
AUTHOR = 'gpt-6'
# Plan: Right-pointing evacuation arrow with three flowing flame trails underneath.
# Reference: rotate-cw: joined arrowhead principles; no useful local flame-trail match.
# Reduction: Reduced bottom flame outline to one smooth tongue; three trails retained.

class AuthoredIcon(Solo48):
    icon_id = 'safety-fire-right'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('safety', 'fire', 'right')

    def build(self):
        self.add_polyline('arrow',(6,16),(34,16),(26,8),(28,6),(42,20),(28,34),(26,32),(34,24),(25,24))
        self.add_bezier('trail-top',(6,25),((12,27),(18,26),(25,24)));self.relate('connect','arrow','trail-top')
        self.add_bezier('trail-mid',(6,34),((12,27),(19,36),(26,29)))
        self.add_bezier('trail-bottom',(6,42),((10,33),(17,41),(22,36)),((20,43),(12,42),(6,42)))

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
