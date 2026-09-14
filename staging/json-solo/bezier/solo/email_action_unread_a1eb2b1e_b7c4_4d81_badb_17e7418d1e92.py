"""Email action unread (emails), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a1eb2b1e-b7c4-4d81-badb-17e7418d1e92'
SOURCE_PATH = 'icons-json/emails/email action unread_a1eb2b1e-b7c4-4d81-badb-17e7418d1e92.json'
AUTHOR = 'json_to_solo'

class EmailActionUnreadA1eb2b1e(Solo48):
    icon_id = 'email-action-unread-a1eb2b1e'
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
        self.add_line('sym-e4', (44, 9), (44, 12))
        self.add_line('sym-e5', (44, 12), (44, 36))
        self.add_bezier('sym-e6', (44, 36), ((44, 36.18), (44, 36.82), (44, 37)))
        self.add_bezier('sym-e7', (44, 37), ((44, 38.17), (42.045, 40), (41, 40)))
        self.add_bezier('sym-e8', (41, 40), ((40.836, 40), (40.164, 40), (40, 40)))
        self.add_line('sym-e9', (40, 40), (24, 40))
        self.add_line('sym-e10', (24, 40), (8, 40))
        self.add_bezier('sym-e11', (8, 40), ((7.836, 40), (7.164, 40), (7, 40)))
        self.add_bezier('sym-e12', (7, 40), ((5.955, 40), (4, 38.17), (4, 37)))
        self.add_bezier('sym-e13', (4, 37), ((4, 36.82), (4, 36.18), (4, 36)))
        self.add_line('sym-e14', (4, 36), (4, 12))
        self.add_line('sym-e15', (4, 12), (4, 9))
        self.add_line('sym-e16', (4, 9), (4, 8))
        self.add_line('sym-e17', (4, 8), (8, 8))
        self.add_line('sym-e18', (8, 8), (24, 8))
        self.add_line('sym-e19', (24, 8), (40, 8))
        self.add_line('sym-e20', (40, 8), (44, 8))
        self.add_line('sym-e21', (44, 8), (44, 9))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21')
