"""Email action reply (emails), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e6', (44, 40), ((43.509, 39.35), (44, 39.93), (43.709, 39.3)), ((43.545, 39.2), (43.391, 39.09), (43.227, 38.98)), ((42.818, 38.63), (42.482, 38.04), (42.136, 37.6)), ((41.264, 36.49), (40.382, 35.3), (39.355, 34.35)), ((34.055, 29.44), (26.755, 27.93), (20, 28)))
        self.add_bezier('e7', (27, 17), ((28.127, 17), (29.064, 17.44), (30.136, 17.76)), ((36.636, 19.71), (40.991, 25.03), (42.6, 32.11)), ((42.745, 32.73), (42.9, 33.37), (43, 34)))
        self.add_contour('c0', 'e6', 'e0', 'e1', 'e2', 'e3', 'e4', 'e7', 'e5', closed=True)
