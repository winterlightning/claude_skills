"""Email action reply (emails), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '941eddd0-ce09-5acc-8292-b980e062b376'
SOURCE_PATH = 'icons-json/emails/email action reply_941eddd0-ce09-5acc-8292-b980e062b376.json'
AUTHOR = 'json_to_solo'

class EmailActionReplyEmails(Solo48):
    icon_id = 'email-action-reply-emails'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ()
    keywords = ('email', 'action', 'reply', 'emails')

    def build(self):
        self.add_line('e0', (20, 28), (20, 38))
        self.add_line('e1', (20, 38), (4, 23))
        self.add_line('e2', (4, 23), (20, 8))
        self.add_line('e3', (20, 8), (20, 17))
        self.add_line('e4', (20, 17), (27, 17))
        self.add_line('e5', (43, 34), (44, 40))
        self.add_arc('e6', (44, 40), (20, 28), radius_x=26, sweep=False)
        self.add_arc('e7', (27, 17), (43, 34), radius_x=19)
        self.add_contour('c0', 'e6', 'e0', 'e1', 'e2', 'e3', 'e4', 'e7', 'e5', closed=True)
