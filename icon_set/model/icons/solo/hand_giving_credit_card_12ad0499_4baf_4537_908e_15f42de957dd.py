"""A hand offers a landscape credit card to the right. HRECT_L centerline extremes (4,8)-(44,40). Lucide credit-card informs a single stripe and rounded corners; hand-coins informs an open hand silhouette. Omit the small face dash and layered finger creases. Intentional asymmetry conveys giving."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import rounded_rect, circle, dollar

SOURCE_ICON_ID = '12ad0499-4baf-4537-908e-15f42de957dd'
SOURCE_PATH = 'pictographic-primitives/payments/credit card give_12ad0499-4baf-4537-908e-15f42de957dd.svg'
AUTHOR = 'gpt-6'

class HandGivingCreditCard(Solo48):
    icon_id = 'hand-giving-credit-card'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'payments'
    aliases = ()
    keywords = ('credit-card', 'hand', 'give', 'payment', 'card', 'offer', 'pay', 'purchase')

    def build(self):
        # Card and hand share the thumb and lower card attachment points.
        self.add_line('card-left', (14, 16), (14, 12))
        self.add_arc('card-tl', (14, 12), (18, 8), radius_x=4)
        self.add_line('card-top', (18, 8), (40, 8))
        self.add_arc('card-tr', (40, 8), (44, 12), radius_x=4)
        self.add_line('card-right-1', (44, 12), (44, 16))
        self.add_line('card-right-2', (44, 16), (44, 28))
        self.add_arc('card-br', (44, 28), (40, 32), radius_x=4)
        self.add_line('card-bottom-right', (40, 32), (36, 32))
        self.add_line('card-bottom-left', (36, 32), (18, 32))
        self.add_arc('card-bl', (18, 32), (14, 28), radius_x=4)
        self.add_line('card-left-lower', (14, 28), (14, 24))
        self.add_contour('card', 'card-left','card-tl','card-top','card-tr','card-right-1','card-right-2','card-br','card-bottom-right','card-bottom-left','card-bl','card-left-lower')
        self.add_line('thumb-top-1', (4, 24), (12, 16))
        self.add_line('thumb-top-2', (12, 16), (14, 16))
        self.add_line('thumb-top-3', (14, 16), (24, 16))
        self.add_arc('thumb-tip', (24, 16), (24, 24), radius_x=4)
        self.add_line('thumb-bottom', (24, 24), (14, 24))
        self.add_contour('thumb', 'thumb-top-1','thumb-top-2','thumb-top-3','thumb-tip','thumb-bottom')
        self.add_line('stripe', (24, 16), (44, 16))
        self.relate('connect','card','stripe')
        self.relate('connect','thumb','stripe')
        self.relate('connect','card','thumb')
        self.add_line('palm-1', (4, 36), (12, 40))
        self.add_line('palm-2', (12, 40), (28, 40))
        self.add_arc('fingers', (28, 40), (36, 32), radius_x=8, sweep=False)
        self.add_contour('hand-base', 'palm-1','palm-2','fingers')
        self.relate('connect','card','hand-base')
