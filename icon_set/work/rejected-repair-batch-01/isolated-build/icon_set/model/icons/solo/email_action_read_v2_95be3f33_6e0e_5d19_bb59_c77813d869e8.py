'email-action-read: independent smooth-curve repair.\n\nConstruction: Rounded envelope with a single gently curved flap; mirrored cubic controls preserve the central fold. Removed cramped redundant lower diagonals.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/mail.svg and atomic-debug/mail.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '95be3f33-6e0e-5d19-bb59-c77813d869e8'
SOURCE_PATH = 'pictographic-primitives/emails/email action read_95be3f33-6e0e-5d19-bb59-c77813d869e8.svg'
AUTHOR = 'gpt-6'


class EmailActionReadVariant2(Solo48):
    icon_id = 'email-action-read-v2'
    variant_of = 'email-action-read'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ()
    keywords = ('email', 'action', 'read', 'emails')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'envelope',4,8,44,40,4,ys=(16,))
        path(self,'flap',(4,16),('L',(20,27)),('C',(22,28.375),(26,28.375),(28,27)),('L',(44,16)))
        contacts(self)
