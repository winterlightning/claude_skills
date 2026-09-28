"""Fresh SOLO48 revision of invoice-in-open-envelope from the claimed reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
from icon_set.model.icons.solo._payments_batch02 import small_dollar

SOURCE_ICON_ID = '57201c70-c002-40bb-8fad-0abd9f9ca4db'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__invoice-in-open-envelope/20260927T071330Z-thuan-mac-1/reference/invoice mail_57201c70-c002-40bb-8fad-0abd9f9ca4db.svg'
AUTHOR = "gpt-6"

class InvoiceInOpenEnvelope(Solo48):
    icon_id='invoice-in-open-envelope'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'payments'
    categories = ('primitives', 'payments')
    aliases=()
    keywords=('invoice', 'mail', 'envelope', 'bill', 'dollar', 'letter', 'payment', 'billing')
    def build(self) -> None:

        poly(self,'paper',(8,28),(8,4),(40,4),(40,28))
        line(self,'invoice-line',(16,12),(18,12))
        small_dollar(self,28,24)
        poly(self,'envelope',(8,28),(8,40),(12,44),(36,44),(40,40),(40,28))
        poly(self,'fold',(8,28),(24,38),(40,28))
        contacts(self)
