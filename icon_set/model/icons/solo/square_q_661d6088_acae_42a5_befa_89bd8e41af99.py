from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '661d6088-acae-42a5-befa-89bd8e41af99'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__square-q/20260925T034659Z-thuan-mac/reference/square q_661d6088-acae-42a5-befa-89bd8e41af99.svg'
AUTHOR = 'gpt-6'
# Plan: Open Q bowl and clear diagonal tail; distinguish Q from magnifier.
# Construction reference: Lucide square-arrow-right rounded enclosure and joined arrow construction.
# Envelope: SQUARE; bounds are defined by its outer contour/extreme tips.
class AuthoredIcon(Solo48):
    icon_id = 'square-q'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('square', 'q')
    def build(self):
        self.box('frame',6,6,42,42)
        self.add_line('top',(21,15),(27,15))
        self.add_arc('tr',(27,15),(32,20),radius_x=5)
        self.add_line('right',(32,20),(32,26))
        self.add_arc('br',(32,26),(27,31),radius_x=5)
        self.add_line('bottom',(27,31),(21,31))
        self.add_arc('bl',(21,31),(16,26),radius_x=5)
        self.add_line('left',(16,26),(16,20))
        self.add_arc('tl',(16,20),(21,15),radius_x=5)
        self.add_contour('bowl','top','tr','right','br','bottom','bl','left','tl',closed=True)
        self.add_line('tail',(25,25),(33,33))
        self.relate('connect','tail','bowl')

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
