from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4b4c4e57-da6a-4ce9-9d53-b8f095c266b7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__square-right/20260925T034659Z-thuan-mac/reference/square right_4b4c4e57-da6a-4ce9-9d53-b8f095c266b7.svg'
AUTHOR = 'gpt-6'
# Plan: Right-pointing arrow inside a true square, replacing tag-like frame.
# Construction reference: Lucide square-arrow-right rounded enclosure and joined arrow construction.
# Envelope: SQUARE; bounds are defined by its outer contour/extreme tips.
class AuthoredIcon(Solo48):
    icon_id = 'square-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('square', 'right')
    def build(self):
        self.box('frame',6,6,42,42)
        self.add_line('shaft',(15,24),(33,24))
        self.add_polyline('head',(24,15),(33,24),(24,33))
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
