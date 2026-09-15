'email-logo: distinct review variant.\n\nConstruction: Envelope logo with a central circular seal; equal diagonal folds terminate at opposite seal extrema.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nConstruction reference: mail from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'aef6da05-b81c-4b53-95f9-6548945f3eb6'
SOURCE_PATH = 'pictographic-primitives/logos/email logo_aef6da05-b81c-4b53-95f9-6548945f3eb6.svg'
AUTHOR = 'gpt-6'


class EmailLogoVariant2(Solo48):
    icon_id = 'email-logo-v2'
    variant_of = 'email-logo'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('email', 'logo', 'logos')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'envelope',4,8,44,40,4)
        ellipse(self,'seal',24,25,3)
        line(self,'left-fold',(4,12),(21,25))
        line(self,'right-fold',(27,25),(44,12))
        contacts(self)
