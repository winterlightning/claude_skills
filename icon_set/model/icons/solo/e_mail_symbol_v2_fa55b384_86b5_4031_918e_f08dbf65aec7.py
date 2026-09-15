'e-mail-symbol: distinct review variant.\n\nConstruction: Envelope symbol with a deep, continuous elliptical flap rather than diagonal fold rails.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nConstruction reference: mail from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'fa55b384-86b5-4031-918e-f08dbf65aec7'
SOURCE_PATH = 'pictographic-primitives/symbol/e mail_fa55b384-86b5-4031-918e-f08dbf65aec7.svg'
AUTHOR = 'gpt-6'


class EMailSymbolVariant2(Solo48):
    icon_id = 'e-mail-symbol-v2'
    variant_of = 'e-mail-symbol'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('e', 'mail', 'symbol')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'envelope',4,8,44,40,4,ys=(16,))
        path(self,'flap',(4,16),('A',20,16,False,(24,32)),('A',20,16,False,(44,16)))
        contacts(self)
