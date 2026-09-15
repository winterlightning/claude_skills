'email-action-unread-emails: distinct review variant.\n\nConstruction: Unread emails shown as two overlapping envelopes with an exposed rear top and right edge; actual shared junctions.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nConstruction reference: mail from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'a1eb2b1e-b7c4-4d81-badb-17e7418d1e92'
SOURCE_PATH = 'pictographic-primitives/emails/email action unread_a1eb2b1e-b7c4-4d81-badb-17e7418d1e92.svg'
AUTHOR = 'gpt-6'


class EmailActionUnreadEmailsVariant2(Solo48):
    icon_id = 'email-action-unread-emails-v2'
    variant_of = 'email-action-unread-emails'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ()
    keywords = ('email', 'action', 'unread', 'emails')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'front',4,18,36,40,4,ys=(22,30),xs=(12,))
        poly(self,'flap',(4,22),(20,32),(36,22))
        path(self,'back',(12,18),('L',(12,12)),('A',4,4,True,(16,8)),('L',(40,8)),('A',4,4,True,(44,12)),('L',(44,26)),('A',4,4,True,(40,30)),('L',(36,30)))
        contacts(self)
