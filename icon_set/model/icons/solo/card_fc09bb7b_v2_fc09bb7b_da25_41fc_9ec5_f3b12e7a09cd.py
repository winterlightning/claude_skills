'card-fc09bb7b: distinct review variant.\n\nConstruction: Payment card with a lower stripe and two upper identification dots; rounded corners remain consistent.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nConstruction reference: credit-card from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'fc09bb7b-da25-41fc-9ec5-f3b12e7a09cd'
SOURCE_PATH = 'pictographic-primitives/business/card_fc09bb7b-da25-41fc-9ec5-f3b12e7a09cd.svg'
AUTHOR = 'gpt-6'


class CardFc09bb7bVariant2(Solo48):
    icon_id = 'card-fc09bb7b-v2'
    variant_of = 'card-fc09bb7b'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('card', 'business')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'card',4,8,44,40,4,ys=(28,))
        line(self,'stripe',(4,28),(44,28))
        self.add_dot('id-left',(14,18));self.add_dot('id-right',(24,18))
        contacts(self)
