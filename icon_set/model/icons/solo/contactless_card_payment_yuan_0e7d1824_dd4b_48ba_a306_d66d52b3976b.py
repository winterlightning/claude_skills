"""A hand holds a yuan-marked card with contactless waves.
SQUARE centerline extremes (6,6)-(42,42). Shared card, thumb and signal definitions retain equality across the four
currency variants. The upper-right card corner is open to reserve the signal.
Lucide credit-card, hand-coins and nfc inform the construction. An upright card keeps
the currency clear of the lower-right thumb. Omit the rear finger crease,
second signal arc and redundant currency bars. Preserve the directional grasp.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import contactless_candidate

SOURCE_ICON_ID = '0e7d1824-dd4b-48ba-a306-d66d52b3976b'
SOURCE_PATH = 'pictographic-primitives/payments/contactless payment yuan_0e7d1824-dd4b-48ba-a306-d66d52b3976b.svg'
AUTHOR = 'gpt-6'

class ContactlessCardPaymentYuan(Solo48):
    icon_id = 'contactless-card-payment-yuan'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/payments'
    aliases = ()
    keywords = ('contactless','payment','card','hand','nfc','yuan')

    def build(self):
        contactless_candidate(self, 'yuan', 'upright')
