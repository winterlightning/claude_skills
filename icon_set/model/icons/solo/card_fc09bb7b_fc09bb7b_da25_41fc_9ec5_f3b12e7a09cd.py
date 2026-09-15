'card-fc09bb7b: independent smooth-curve repair.\n\nConstruction: Card with four equal quarter-circle corners and a horizontal band.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/credit-card.svg and atomic-debug/credit-card.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'fc09bb7b-da25-41fc-9ec5-f3b12e7a09cd'
SOURCE_PATH = 'pictographic-primitives/business/card_fc09bb7b-da25-41fc-9ec5-f3b12e7a09cd.svg'
AUTHOR = 'gpt-6'


class CardFc09bb7b(Solo48):
    icon_id = 'card-fc09bb7b'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('card', 'business')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'card',4,8,44,40,4,ys=(20,))
        line(self,'stripe',(4,20),(44,20))
        contacts(self)
