"""state-mail: approved original model.

Construction: Square mail state badge: centered V fold with a vertical lower seam; compact proportions distinguish it from the wide envelopes.
Keyshape: SQUARE; exact SOLO48 envelope.
Construction reference: mail from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = 'f42c1e62-6183-4903-b7ff-5d9817c49685'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__state-mail/20260927T094403Z-thuan-mac-1/reference/state mail_f42c1e62-6183-4903-b7ff-5d9817c49685.svg'
AUTHOR = "gpt-6"

class StateMail(Solo48):
    icon_id = 'state-mail'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('state', 'mail', 'symbol')
    keyshape = Keyshape.HRECT_L

    def build(self):
        # Wide rounded envelope with its single centered V flap.
        from icon_set.model.icons.solo._symmetry_curves import box, poly, contacts
        box(self, 'envelope', 4, 8, 44, 40, 4, xs=(24,))
        poly(self, 'flap', (4, 12), (24, 28), (44, 12))
        contacts(self)
