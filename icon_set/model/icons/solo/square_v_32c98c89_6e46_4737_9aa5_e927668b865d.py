from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '32c98c89-6e46-4737-9aa5-e927668b865d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__square-v/20260925T034659Z-thuan-mac/reference/square v_32c98c89-6e46-4737-9aa5-e927668b865d.svg'
AUTHOR = 'gpt-6'
# Plan: Symmetric capital V, replacing asymmetric check mark.
# Construction reference: Lucide square-arrow-right rounded enclosure and joined arrow construction.
# Envelope: SQUARE; bounds are defined by its outer contour/extreme tips.
class AuthoredIcon(Solo48):
    icon_id = 'square-v'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('square', 'v')
    def build(self):
        self.box('frame',6,6,42,42)
        axis=24
        self.add_polyline('letter',(axis-9,15),(axis,33),(axis+9,15))

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
