"""An invoice with a dollar sign rises from an open envelope. VRECT_L preserves the upright letter above the envelope. Lucide mail-open informs mirrored envelope folds; receipt informs the dollar. Drop text lines and redundant front seams.
Centerline bounds: (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import rounded_rect
from ._payments_batch02 import small_dollar
SOURCE_ICON_ID='57201c70-c002-40bb-8fad-0abd9f9ca4db'
SOURCE_PATH='pictographic-primitives/payments/invoice mail_57201c70-c002-40bb-8fad-0abd9f9ca4db.svg'
AUTHOR='gpt-6'

class InvoiceInOpenEnvelope(Solo48):
    icon_id='invoice-in-open-envelope'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'payments'
    categories = ('primitives', 'payments')
    aliases=()
    keywords=('invoice', 'mail', 'envelope', 'bill', 'dollar', 'letter', 'payment', 'billing')
    def build(self):
        # Paper rises above the envelope. The envelope owns mirrored folds.
        self.add_polyline('paper',(12,24),(12,4),(36,4),(36,24))
        self.add_line('back-left',(8,28),(12,24))
        self.add_line('back-right',(36,24),(40,28))
        self.relate('connect','paper','back-left')
        self.relate('connect','paper','back-right')
        self.add_line('envelope-left',(8,28),(8,40))
        self.add_arc('envelope-bl',(8,40),(12,44),radius_x=4,sweep=False)
        self.add_line('envelope-bottom',(12,44),(36,44))
        self.add_arc('envelope-br',(36,44),(40,40),radius_x=4,sweep=False)
        self.add_line('envelope-right',(40,40),(40,28))
        self.add_contour('envelope','envelope-left','envelope-bl','envelope-bottom','envelope-br','envelope-right')
        self.add_polyline('front-fold',(8,28),(24,38),(40,28))
        self.relate('connect','envelope','front-fold')
        self.relate('connect','envelope','back-left')
        self.relate('connect','envelope','back-right')
        self.relate('connect','front-fold','back-left')
        self.relate('connect','front-fold','back-right')
        small_dollar(self,24,20)
