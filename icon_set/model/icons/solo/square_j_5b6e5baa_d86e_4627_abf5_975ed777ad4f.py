from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5b6e5baa-d86e-4627-abf5-975ed777ad4f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__square-j/20260925T034659Z-thuan-mac/reference/square j_5b6e5baa-d86e-4627-abf5-975ed777ad4f.svg'
AUTHOR = 'gpt-6'
# Plan: Conventional capital J with top bar and rounded lower hook; remove misleading right arrow.
# Construction reference: Lucide square-arrow-right rounded enclosure and joined arrow construction.
# Envelope: SQUARE; bounds are defined by its outer contour/extreme tips.
class AuthoredIcon(Solo48):
    icon_id = 'square-j'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('square', 'j')
    def build(self):
        self.box('frame',6,6,42,42)
        self.add_line('top',(17,15),(31,15))
        self.add_line('stem',(27,15),(27,27))
        self.add_arc('hook',(27,27),(17,27),radius_x=5)
        self.add_contour('letter','stem','hook')
        self.relate('connect','top','letter')

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
