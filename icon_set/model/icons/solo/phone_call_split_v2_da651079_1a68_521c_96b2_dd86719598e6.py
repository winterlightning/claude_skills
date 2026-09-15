'phone-call-split: distinct review variant.\n\nConstruction: Split-call routing arrow with a crisp central Y junction and straight diagonal branches; keep arrow corners purposeful.\nKeyshape: SQUARE; exact SOLO48 envelope.\nConstruction reference: split from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'da651079-1a68-521c-96b2-dd86719598e6'
SOURCE_PATH = 'pictographic-primitives/phones/phone call split_da651079-1a68-521c-96b2-dd86719598e6.svg'
AUTHOR = 'gpt-6'


class PhoneCallSplitVariant2(Solo48):
    icon_id = 'phone-call-split-v2'
    variant_of = 'phone-call-split'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    aliases = ()
    keywords = ('phone', 'call', 'split', 'phones')
    keyshape = Keyshape.SQUARE

    def build(self):
        line(self,'stem',(24,42),(24,24))
        poly(self,'branches',(6,6),(24,24),(42,6))
        poly(self,'left-head',(6,18),(6,6),(18,6))
        poly(self,'right-head',(30,6),(42,6),(42,18))
        contacts(self)
