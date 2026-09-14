"""Landscape card gripped at its right end by an upward hand. SQUARE balances card and hand. Lucide credit-card and hand-coins inform rounded enclosure, stripe and open grasp. Drop the face dash; preserve the directional hand.
Centerline bounds: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import rounded_rect
from ._payments_batch02 import small_dollar
SOURCE_ICON_ID='b8b0be96-48c9-4d4f-9c4a-c278eedc3dbe'
SOURCE_PATH='pictographic-primitives/payments/credit card scan_b8b0be96-48c9-4d4f-9c4a-c278eedc3dbe.svg'
AUTHOR='gpt-6'

class HandHoldingCard(Solo48):
    icon_id='hand-holding-card'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/payments'
    aliases=()
    keywords=('credit-card', 'card', 'hand', 'holding', 'scan', 'payment', 'pay', 'purchase')
    def build(self):
        # Rounded card at upper left; one broad index-finger hook on the right.
        self.add_line('card-top',(24,6),(10,6))
        self.add_arc('card-tl',(10,6),(6,10),radius_x=4,sweep=False)
        self.add_line('card-left-upper',(6,10),(6,14))
        self.add_line('card-left-lower',(6,14),(6,24))
        self.add_arc('card-bl',(6,24),(10,28),radius_x=4,sweep=False)
        self.add_line('card-bottom',(10,28),(18,28))
        self.add_contour('card','card-top','card-tl','card-left-upper','card-left-lower','card-bl','card-bottom')
        self.add_line('stripe',(6,14),(20,14))
        self.relate('connect','card','stripe')
        self.add_line('finger-tip-top',(32,6),(38,6))
        self.add_arc('finger-tip',(32,6),(32,14),radius_x=4,sweep=False)
        self.add_line('finger-inner',(32,14),(34,14))
        self.add_arc('finger-curl',(34,14),(34,30),radius_x=8)
        self.add_line('finger-return',(34,30),(26,24))
        self.add_arc('thumb-tip-upper',(26,24),(18,28),radius_x=5,sweep=False)
        self.add_arc('thumb-tip-lower',(18,28),(20,32),radius_x=5,sweep=False)
        self.add_line('thumb-lower',(20,32),(28,42))
        self.add_contour('grip','finger-tip','finger-inner','finger-curl','finger-return','thumb-tip-upper','thumb-tip-lower','thumb-lower')
        self.add_line('hand-outside',(42,18),(42,42))
        self.add_arc('knuckle',(38,6),(42,18),radius_x=4,radius_y=12)
        self.add_contour('back','finger-tip-top','knuckle','hand-outside')
        self.relate('connect','grip','back')
        self.relate('connect','card','grip')
