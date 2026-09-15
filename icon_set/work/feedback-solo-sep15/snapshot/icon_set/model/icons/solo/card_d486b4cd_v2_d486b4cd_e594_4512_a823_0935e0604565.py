'card-d486b4cd: independent smooth-curve repair.\n\nConstruction: Card with four equal quarter-circle corners and a horizontal band.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/credit-card.svg and atomic-debug/credit-card.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'd486b4cd-e594-4512-a823-0935e0604565'
SOURCE_PATH = 'pictographic-primitives/business/card_d486b4cd-e594-4512-a823-0935e0604565.svg'
AUTHOR = 'gpt-6'


class CardD486b4cdVariant2(Solo48):
    icon_id = 'card-d486b4cd-v2'
    variant_of = 'card-d486b4cd'
    variant_label = 'Smooth curves and symmetry'
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
