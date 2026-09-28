from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '05bd420f-ccd3-45f2-a021-10901b4a7362'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tog/20260925T034659Z-thuan-mac/reference/tog_05bd420f-ccd3-45f2-a021-10901b4a7362.svg'
AUTHOR = 'gpt-6'
# Plan: Tag with clearly visible punched hole and clipped shoulder; interpret ambiguous Tog from its tag reference.
# Construction reference: Lucide tag clipped shoulder and punched hole.
# Envelope: SQUARE; bounds are defined by its outer contour/extreme tips.
class AuthoredIcon(Solo48):
    icon_id = 'tog'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('tog',)
    def build(self):
        self.add_polyline('outline',(6,6),(26,6),(42,22),(22,42),(6,26),closed=True)
        self.circle('hole',17,17,3)

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
