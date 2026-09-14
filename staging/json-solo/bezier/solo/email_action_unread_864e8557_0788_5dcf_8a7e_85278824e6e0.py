"""Email action unread (emails), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '864e8557-0788-5dcf-8a7e-85278824e6e0'
SOURCE_PATH = 'icons-json/emails/email action unread_864e8557-0788-5dcf-8a7e-85278824e6e0.json'
AUTHOR = 'json_to_solo'

class EmailActionUnread864e8557(Solo48):
    icon_id = 'email-action-unread-864e8557'
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
        self.add_bezier('e6', (44, 12), ((43.5, 10.07), (42.145, 8), (40, 8)))
        self.add_bezier('e7', (8, 8), ((7.855, 8), (7.355, 8.01), (7.209, 8.01)), ((5.355, 8.01), (4.491, 9.26), (4, 11)))
        self.add_bezier('e8', (9, 40), ((8.936, 40), (8.409, 40), (8.345, 40)), ((5.727, 40), (4.018, 37.7), (4.018, 34.98)), ((4.018, 34.77), (4, 34.56), (4, 34.35)), ((4, 34.23), (4, 34.12), (4, 34)))
        self.add_bezier('e9', (21, 25), ((22.882, 26.42), (24.809, 27.77), (27, 26)))
        self.add_bezier('e10', (44, 35), ((44, 35.08), (44, 35.16), (44, 35.24)), ((44, 37.48), (41.709, 39.98), (39.673, 39.98)), ((39.445, 39.98), (39.218, 40), (38.991, 40)), ((38.845, 40), (39.145, 40), (39, 40)))
        self.add_contour('c0', 'e6', 'e0', 'e7')
        self.add_contour('c1', 'e8', 'e1', 'e2', 'e9', 'e3', 'e4', 'e10', 'e5', closed=True)
