'email-action-read: distinct review variant.\n\nConstruction: Read mail shown as an open envelope: raised triangular back flap and low front pocket.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nConstruction reference: mail from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '95be3f33-6e0e-5d19-bb59-c77813d869e8'
SOURCE_PATH = 'pictographic-primitives/emails/email action read_95be3f33-6e0e-5d19-bb59-c77813d869e8.svg'
AUTHOR = 'gpt-6'


class EmailActionReadVariant2(Solo48):
    icon_id = 'email-action-read-v2'
    variant_of = 'email-action-read'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ()
    keywords = ('email', 'action', 'read', 'emails')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'back',(4,24),('L',(21,9)),('C',(23,7.666666667),(25,7.666666667),(27,9)),('L',(44,24)))
        path(self,'pocket',(4,24),('L',(20,31)),('C',(22,31.875),(26,31.875),(28,31)),('L',(44,24)),('L',(44,36)),('A',4,4,True,(40,40)),('L',(8,40)),('A',4,4,True,(4,36)),('L',(4,24)),closed=True)
        contacts(self)
