"""A hand holds a euro-marked card with contactless waves.
SQUARE centerline extremes (6,6)-(42,42). Shared card, thumb and signal definitions retain equality across the four
currency variants. The upper-right card corner is open to reserve the signal.
Lucide credit-card, hand-coins and nfc inform the construction. An upright card keeps
the currency clear of the lower-right thumb. Omit the rear finger crease,
second signal arc and redundant currency bars. Preserve the directional grasp.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import draw_contactless

SOURCE_ICON_ID = 'ca0a4566-389d-4992-b347-18d26c406419'
SOURCE_PATH = 'pictographic-primitives/payments/contactless payment euro_ca0a4566-389d-4992-b347-18d26c406419.svg'
AUTHOR = 'gpt-6'

class ContactlessCardPaymentEuro(Solo48):
    icon_id = 'contactless-card-payment-euro'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'payments'
    aliases = ()
    keywords = ('contactless','payment','card','hand','nfc','euro')

    def build(self):
        draw_contactless(self, 'euro')
