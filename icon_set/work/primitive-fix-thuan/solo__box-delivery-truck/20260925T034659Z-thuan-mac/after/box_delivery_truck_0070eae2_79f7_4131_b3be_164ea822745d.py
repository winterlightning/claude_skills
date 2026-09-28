from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0070eae2-79f7-4131-b3be-164ea822745d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__box-delivery-truck/20260925T034659Z-thuan-mac/reference/carrier_0070eae2-79f7-4131-b3be-164ea822745d.svg'
AUTHOR = 'gpt-6'
# Plan: Delivery truck with tall rectangular cargo box, distinct cab and two large wheels; replace flattened cab silhouette.
# Construction reference: Lucide truck cargo/cab hierarchy and wheel alignment.
# Envelope: HRECT_L; bounds are defined by its outer contour/extreme tips.
class AuthoredIcon(Solo48):
    icon_id = 'box-delivery-truck'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('box', 'delivery', 'truck')
    def build(self):
        self.add_polyline('cargo',(4,26),(4,8),(28,8),(28,26))
        self.add_polyline('cab',(28,16),(36,16),(44,26),(44,26))
        self.relate('connect','cargo','cab')
        self.add_line('chassis',(4,26),(44,26))
        self.relate('connect','cargo','chassis')
        self.relate('connect','cab','chassis')
        for x in (12,36): self.circle(f'wheel-{x}',x,37,3)

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
