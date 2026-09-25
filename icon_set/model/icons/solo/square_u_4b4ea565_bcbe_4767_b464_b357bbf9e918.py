from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4b4ea565-bcbe-4767-b464-b357bbf9e918'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__square-u/20260925T034659Z-thuan-mac/reference/square u_4b4ea565-bcbe-4767-b464-b357bbf9e918.svg'
AUTHOR = 'gpt-6'
# Plan: Conventional capital U with equal uprights and semicircular bottom; remove right arrow.
# Construction reference: Lucide square-arrow-right rounded enclosure and joined arrow construction.
# Envelope: SQUARE; bounds are defined by its outer contour/extreme tips.
class AuthoredIcon(Solo48):
    icon_id = 'square-u'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('square', 'u')
    def build(self):
        self.box('frame',6,6,42,42)
        self.add_line('left',(16,15),(16,25))
        self.add_arc('bottom',(16,25),(32,25),radius_x=8,sweep=False)
        self.add_line('right',(32,25),(32,15))
        self.add_contour('letter','left','bottom','right')

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
