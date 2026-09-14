"""A hand holds a pound-marked card with contactless waves.
SQUARE centerline extremes (6,6)-(42,42). Shared card, thumb and signal definitions retain equality across the four
currency variants. The upper-right card corner is open to reserve the signal.
Lucide credit-card, hand-coins and nfc inform the construction. An upright card keeps
the currency clear of the lower-right thumb. Omit the rear finger crease,
second signal arc and redundant currency bars. Preserve the directional grasp.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import draw_contactless

SOURCE_ICON_ID = '57128c06-400e-4952-ab1f-47b45784e8e3'
SOURCE_PATH = 'pictographic-primitives/payments/contactless payment pound_57128c06-400e-4952-ab1f-47b45784e8e3.svg'
AUTHOR = 'gpt-6'

class ContactlessCardPaymentPound(Solo48):
    icon_id = 'contactless-card-payment-pound'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/payments'
    aliases = ()
    keywords = ('contactless','payment','card','hand','nfc','pound')

    def build(self):
        draw_contactless(self, 'pound')
