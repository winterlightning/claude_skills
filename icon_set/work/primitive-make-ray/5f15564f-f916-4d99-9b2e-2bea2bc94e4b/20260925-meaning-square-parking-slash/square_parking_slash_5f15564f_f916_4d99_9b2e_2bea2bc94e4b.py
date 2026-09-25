from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5f15564f-f916-4d99-9b2e-2bea2bc94e4b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__square-parking-slash/20260925T034659Z-thuan-mac/reference/square parking slash_5f15564f-f916-4d99-9b2e-2bea2bc94e4b.svg'
AUTHOR = 'gpt-6'
# Plan: No parking symbol: capital P crossed by a complete diagonal prohibition slash, replacing R-like mark.
# Construction reference: Lucide square-arrow-right rounded enclosure and joined arrow construction.
# Envelope: SQUARE; bounds are defined by its outer contour/extreme tips.
class AuthoredIcon(Solo48):
    icon_id = 'square-parking-slash'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('square', 'parking', 'slash')
    def build(self):
        self.box('frame',6,6,42,42)
        self.add_line('stem',(16,15),(16,33))
        self.add_line('top',(16,15),(25,15))
        self.add_arc('bowl',(25,15),(25,27),radius_x=6)
        self.add_line('mid',(25,27),(16,27))
        self.add_contour('bowl-shape','top','bowl','mid')
        self.relate('connect','stem','bowl-shape')
        self.add_line('slash',(16,15),(34,33))
        self.relate('connect','slash','stem')
        self.relate('connect','slash','bowl-shape')

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
