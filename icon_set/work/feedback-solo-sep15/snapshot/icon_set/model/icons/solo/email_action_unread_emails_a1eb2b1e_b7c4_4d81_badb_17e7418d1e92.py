"""Email action unread (emails), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a1eb2b1e-b7c4-4d81-badb-17e7418d1e92'
SOURCE_PATH = 'pictographic-primitives/emails/email action unread_a1eb2b1e-b7c4-4d81-badb-17e7418d1e92.svg'
AUTHOR = 'gpt-6'

class EmailActionUnreadEmails(Solo48):
    icon_id = 'email-action-unread-emails'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ()
    keywords = ('email', 'action', 'unread', 'emails')

    def build(self):
        self.add_line('sym-e0', (4, 9), (9, 13))
        self.add_line('sym-e1', (9, 13), (24, 27))
        self.add_line('sym-e2', (24, 27), (39, 13))
        self.add_line('sym-e3', (39, 13), (44, 9))
        self.add_line('sym-e4', (44, 9), (44, 36))
        self.add_arc('sym-e6', (44, 36), (44, 37), radius_x=37, radius_y=37, large_arc=False, sweep=False)
        self.add_line('sym-e7', (44, 37), (41, 40))
        self.add_arc('sym-e8', (41, 40), (40, 40), radius_x=41, radius_y=41, large_arc=False, sweep=False)
        self.add_line('sym-e9', (40, 40), (8, 40))
        self.add_arc('sym-e11', (8, 40), (7, 40), radius_x=20, radius_y=20, large_arc=False, sweep=False)
        self.add_line('sym-e12', (7, 40), (4, 37))
        self.add_line('sym-e13', (4, 37), (4, 8))
        self.add_line('sym-e17', (4, 8), (44, 8))
        self.add_line('sym-e21', (44, 8), (44, 9))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e17', 'sym-e21', closed=False)
