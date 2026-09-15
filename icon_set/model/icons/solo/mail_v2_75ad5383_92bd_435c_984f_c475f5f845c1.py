'mail: distinct review variant.\n\nConstruction: Sealed mail viewed from the back, with four folds meeting at one shared central junction.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nConstruction reference: mail from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '75ad5383-92bd-435c-984f-c475f5f845c1'
SOURCE_PATH = 'pictographic-primitives/symbol/mail_75ad5383-92bd-435c-984f-c475f5f845c1.svg'
AUTHOR = 'gpt-6'


class MailVariant2(Solo48):
    icon_id = 'mail-v2'
    variant_of = 'mail'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('mail', 'symbol')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'envelope',4,8,44,40,4)
        poly(self,'top-fold',(4,12),(24,24),(44,12))
        poly(self,'bottom-fold',(4,36),(24,24),(44,36))
        contacts(self)
