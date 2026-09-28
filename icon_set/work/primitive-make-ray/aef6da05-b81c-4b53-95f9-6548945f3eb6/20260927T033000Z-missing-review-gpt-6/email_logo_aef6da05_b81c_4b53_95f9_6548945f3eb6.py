"""email-logo: approved original model.

Construction: Envelope logo with a central circular seal; equal diagonal folds terminate at opposite seal extrema.
Keyshape: HRECT_L; exact SOLO48 envelope.
Construction reference: mail from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = 'aef6da05-b81c-4b53-95f9-6548945f3eb6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__email-logo/20260927T032256Z-thuan-mac-1/reference/email logo_aef6da05-b81c-4b53-95f9-6548945f3eb6.svg'
AUTHOR = "gpt-6"

class EmailLogo(Solo48):
    icon_id = 'email-logo'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('email', 'logo', 'logos')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self, 'envelope', 4, 8, 44, 40, 4)
        line(self, 'left-fold', (4, 12), (24, 26))
        line(self, 'right-fold', (24, 26), (44, 12))
        self.relate('connect', 'left-fold', 'right-fold')
        self.relate('connect', 'left-fold', 'envelope')
        self.relate('connect', 'right-fold', 'envelope')
