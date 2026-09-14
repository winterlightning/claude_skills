"""Two opposed hands exchange a bitcoin. SQUARE fits coin and diagonal hands. Lucide bitcoin informs the two equal B bowls; hand-coins informs the grasp. Retain the B and short currency terminals; remove finger creases and a redundant parallel stem.
Centerline bounds: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import rounded_rect
from ._payments_batch02 import small_dollar
SOURCE_ICON_ID='ef9be51e-2927-4177-9d02-48b17a96d654'
SOURCE_PATH='pictographic-primitives/payments/crypto trade_ef9be51e-2927-4177-9d02-48b17a96d654.svg'
AUTHOR='gpt-6'

class HandsExchangingBitcoin(Solo48):
    icon_id='hands-exchanging-bitcoin'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/payments'
    aliases=()
    keywords=('crypto', 'bitcoin', 'trade', 'exchange', 'coin', 'hands', 'currency', 'blockchain')
    def build(self):
        # Coin owns a B made of equal bowls and two short currency terminals.
        self.add_arc('coin-top-right',(24,6),(42,24),radius_x=18)
        self.add_arc('coin-bottom-left',(24,42),(6,24),radius_x=18)
        # One tangent finger definition, repeated by a half-turn about (24,24).
        for prefix, flipped, coin_side in [('upper',False,'coin-bottom-left'),('lower',True,'coin-top-right')]:
            def point(x,y):
                return (48-x,48-y) if flipped else (x,y)
            self.add_line(prefix+'-wrist',point(6,6),point(10,9))
            self.add_arc(prefix+'-finger',point(10,9),point(10,17),radius_x=5)
            self.add_line(prefix+'-thumb',point(10,17),point(6,20))
            self.add_line(prefix+'-palm',point(6,20),point(6,24))
            self.add_contour('hand-'+prefix,prefix+'-wrist',prefix+'-finger',prefix+'-thumb',prefix+'-palm')
            self.add_line('hand-'+prefix+'-bridge',point(18,6),point(24,6))
            self.relate('connect','hand-'+prefix,coin_side)
            self.relate('connect','hand-'+prefix+'-bridge','coin-top-right' if not flipped else 'coin-bottom-left')
        for name,y in [('b-upper',16),('b-lower',24)]:
            self.add_arc(name,(20,y),(20,y+8),radius_x=8,radius_y=4)
        self.add_line('b-back-lower',(20,32),(20,24))
        self.add_line('b-back-upper',(20,24),(20,16))
        self.add_contour('bitcoin','b-upper','b-lower','b-back-lower','b-back-upper',closed=True)
        self.add_line('b-top',(20,15),(20,16))
        self.add_line('b-bottom',(20,32),(20,33))
        self.relate('connect','bitcoin','b-top')
        self.relate('connect','bitcoin','b-bottom')
