from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5d1e690d-7cb8-4583-96b6-60ab81cb1101'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__angle-down/20260925T034659Z-thuan-mac/reference/angle down_5d1e690d-7cb8-4583-96b6-60ab81cb1101.svg'
AUTHOR = 'gpt-6'
# Plan: Conventional downward chevron; equal mirrored arms replace diagonal arrow.
# Construction reference: Lucide chevron-down mirrored continuous stroke.
# Envelope: HRECT_M; bounds are defined by its outer contour/extreme tips.
class AuthoredIcon(Solo48):
    icon_id = 'angle-down'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('angle', 'down')
    def build(self):
        axis=24
        self.add_polyline('chevron',(axis-20,10),(axis,38),(axis+20,10))

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
