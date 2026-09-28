"""Upright bill carrying a dollar sign. VRECT_L centerline extremes (8,4)-(40,44). Lucide receipt informs the two rounded S bowls; credit-card informs tangent quarter-circle corners. Omit the two text rules to preserve a legible currency symbol and clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import rounded_rect, circle, dollar

SOURCE_ICON_ID = '5662c539-f168-56d1-b6ea-bf9f49c2826e'
SOURCE_PATH = 'pictographic-primitives/payments/accounting bill_5662c539-f168-56d1-b6ea-bf9f49c2826e.svg'
AUTHOR = 'gpt-6'

class BillWithDollarSign(Solo48):
    icon_id = 'bill-with-dollar-sign'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'payments'
    categories = ('primitives', 'payments')
    aliases = ()
    keywords = ('bill', 'invoice', 'dollar', 'document', 'accounting', 'payment', 'money', 'receipt')

    def build(self):
        # Document owns a centered dollar, with paired bowl dimensions.
        rounded_rect(self, 'paper', 8, 4, 40, 44, 4)
        dollar(self, 24, 24)
