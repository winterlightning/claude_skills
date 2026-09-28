from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7b19aff3-b74b-45c0-bae2-47fbe615d32d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__square-up-right/20260925T034659Z-thuan-mac/reference/square up right_7b19aff3-b74b-45c0-bae2-47fbe615d32d.svg'
AUTHOR = 'gpt-6'
# Plan: Arrow points diagonally upper-right, with equal orthogonal arrowhead arms.
# Construction reference: Lucide square-arrow-right rounded enclosure and joined arrow construction.
# Envelope: SQUARE; bounds are defined by its outer contour/extreme tips.
class AuthoredIcon(Solo48):
    icon_id = 'square-up-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('square', 'up', 'right')
    def build(self):
        self.box('frame',6,6,42,42)
        self.add_line('shaft',(15,33),(33,15))
        self.add_polyline('head',(19,15),(33,15),(33,29))
        self.relate('connect','shaft','head')

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
