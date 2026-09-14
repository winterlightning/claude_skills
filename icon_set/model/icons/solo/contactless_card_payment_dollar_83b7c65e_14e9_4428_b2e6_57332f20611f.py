"""A hand holds a dollar-marked card with contactless waves.
SQUARE centerline extremes (6,6)-(42,42). Shared card, thumb and signal definitions retain equality across the four
currency variants. The upper-right card corner is open to reserve the signal.
Lucide credit-card, hand-coins and nfc inform the construction. An upright card keeps
the currency clear of the lower-right thumb. Omit the rear finger crease,
second signal arc and redundant currency bars. Preserve the directional grasp.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import contactless_candidate

SOURCE_ICON_ID = '83b7c65e-14e9-4428-b2e6-57332f20611f'
SOURCE_PATH = 'pictographic-primitives/payments/contactless payment_83b7c65e-14e9-4428-b2e6-57332f20611f.svg'
AUTHOR = 'gpt-6'

class ContactlessCardPaymentDollar(Solo48):
    icon_id = 'contactless-card-payment-dollar'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/payments'
    aliases = ()
    keywords = ('contactless','payment','card','hand','nfc','dollar')

    def build(self):
        contactless_candidate(self, 'dollar', 'upright')
