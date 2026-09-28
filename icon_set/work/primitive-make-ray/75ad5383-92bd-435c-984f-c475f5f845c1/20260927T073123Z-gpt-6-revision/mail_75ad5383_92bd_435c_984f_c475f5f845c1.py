"""mail: approved original model.

Construction: Sealed mail viewed from the back, with four folds meeting at one shared central junction.
Keyshape: HRECT_L; exact SOLO48 envelope.
Construction reference: mail from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = '75ad5383-92bd-435c-984f-c475f5f845c1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mail/20260927T072903Z-thuan-mac-1/reference/mail_75ad5383-92bd-435c-984f-c475f5f845c1.svg'
AUTHOR = "gpt-6"

class Mail(Solo48):
    icon_id = 'mail'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('mail', 'symbol')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self, 'envelope', 4, 8, 44, 40, 4)
        poly(self, 'top-fold', (4, 14), (24, 27), (44, 14))
        contacts(self)
