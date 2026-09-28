"""A hand touches a freestanding payment kiosk. VRECT_L balances monitor, stand and fingertip. Lucide monitor informs the screen/neck/base, and hand-coins the hand. Retain the dollar; remove the tile grid to avoid changing the payment subject into a general touchscreen.
Centerline bounds: (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import rounded_rect
from ._payments_batch02 import small_dollar
SOURCE_ICON_ID='3ef6b67e-c42b-4c1d-bcda-1a6c0146046d'
SOURCE_PATH='pictographic-primitives/payments/self payment touch_3ef6b67e-c42b-4c1d-bcda-1a6c0146046d.svg'
AUTHOR='gpt-6'

class HandTouchingPaymentKiosk(Solo48):
    icon_id='hand-touching-payment-kiosk'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'payments'
    categories = ('primitives', 'payments')
    aliases=()
    keywords=('self-service', 'kiosk', 'touch', 'payment', 'screen', 'hand', 'checkout', 'dollar')
    def build(self):
        # Tall monitor leaves a 32-unit band for the price and a separate foot.
        self.add_line('screen-top',(12,4),(36,4))
        self.add_arc('screen-tr',(36,4),(40,8),radius_x=4)
        self.add_line('screen-right',(40,8),(40,15))
        self.add_contour('screen-upper','screen-top','screen-tr','screen-right')
        self.add_arc('screen-tl',(8,8),(12,4),radius_x=4)
        self.add_line('screen-left',(8,32),(8,8))
        self.add_arc('screen-bl',(12,36),(8,32),radius_x=4)
        self.add_line('screen-bottom',(22,36),(18,36))
        self.add_line('screen-bottom-left',(18,36),(12,36))
        self.add_contour('screen-lower','screen-bottom','screen-bottom-left','screen-bl','screen-left','screen-tl')
        self.relate('connect','screen-upper','screen-lower')
        self.add_line('neck',(18,36),(14,44))
        self.add_polyline('base',(8,44),(14,44),(22,44))
        self.relate('connect','screen-lower','neck')
        self.relate('connect','neck','base')
        self.add_line('finger-left',(32,40),(32,28))
        self.add_arc('finger-tip',(32,28),(40,28),radius_x=4)
        self.add_line('hand-right',(40,28),(40,44))
        self.add_contour('hand','finger-left','finger-tip','hand-right')
        small_dollar(self,20,20)
