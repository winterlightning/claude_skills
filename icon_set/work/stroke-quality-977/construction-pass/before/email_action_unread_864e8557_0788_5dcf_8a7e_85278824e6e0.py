"""Email action unread (emails), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '864e8557-0788-5dcf-8a7e-85278824e6e0'
SOURCE_PATH = 'pictographic-primitives/emails/email action unread_864e8557-0788-5dcf-8a7e-85278824e6e0.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class EmailActionUnread(Solo48):
    icon_id = 'email-action-unread'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ()
    keywords = ('email', 'action', 'unread', 'emails')

    def build(self):
        self.add_line('e0', (40, 8), (8, 8))
        self.add_line('e1', (4, 34), (4, 12))
        self.add_line('e2', (4, 12), (21, 25))
        self.add_line('e3', (27, 26), (44, 12))
        self.add_line('e4', (44, 12), (44, 35))
        self.add_line('e5', (39, 40), (9, 40))
        self.add_arc('e6', (44, 12), (40, 8), radius_x=4, sweep=False)
        self.add_line('e7-1', (8, 8), (5, 9))
        self.add_arc('e7-2', (5, 9), (4, 11), radius_x=5, sweep=False)
        self.add_arc('e8-1', (9, 40), (5, 38), radius_x=5)
        self.add_line('e8-2', (5, 38), (4, 34))
        self.add_arc('e9', (21, 25), (27, 26), radius_x=4, sweep=False)
        self.add_arc('e10', (44, 35), (39, 40), radius_x=5)
        self.add_contour('c0', 'e6', 'e0', 'e7-1', 'e7-2')
        self.add_contour('c1', 'e8-1', 'e8-2', 'e1', 'e2', 'e9', 'e3', 'e4', 'e10', 'e5', closed=True)
