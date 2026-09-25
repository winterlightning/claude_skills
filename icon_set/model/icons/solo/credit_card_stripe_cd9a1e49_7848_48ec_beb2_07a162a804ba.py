"""Rounded payment card with stripe and lower-right detail. Lucide credit-card informs tangent corner arcs and a stripe joined to split side walls.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='cd9a1e49-7848-48ec-beb2-07a162a804ba'
SOURCE_PATH='pictographic-primitives/symbol/state credit_cd9a1e49-7848-48ec-beb2-07a162a804ba.svg'
AUTHOR='gpt-6'

class CreditCardStripe(Solo48):
    icon_id='credit-card-stripe'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    aliases=()
    keywords=('credit-card', 'card', 'payment', 'bank', 'debit', 'finance', 'purchase', 'money')

    def oval(self,n,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(n+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(n+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,points,closed=False):
        self.add_polyline(n,*points,closed=closed)

    def build(self):

        self.add_line('top',(10,8),(38,8))
        self.add_arc('tr',(38,8),(44,14),radius_x=6)
        self.add_line('ru',(44,14),(44,19));self.add_line('rl',(44,19),(44,34))
        self.add_arc('br',(44,34),(38,40),radius_x=6)
        self.add_line('bottom',(38,40),(10,40))
        self.add_arc('bl',(10,40),(4,34),radius_x=6)
        self.add_line('ll',(4,34),(4,19));self.add_line('lu',(4,19),(4,14))
        self.add_arc('tl',(4,14),(10,8),radius_x=6)
        self.add_contour('card','top','tr','ru','rl','br','bottom','bl','ll','lu','tl',closed=True)
        self.add_line('stripe',(4,19),(44,19));self.relate('connect','stripe','card')
        self.add_line('detail',(28,30),(34,30))
