"""Heart check (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4bbd96be-f6bf-4a56-b592-6fde129cb45c'
SOURCE_PATH = 'icons-json/state/heart check_4bbd96be-f6bf-4a56-b592-6fde129cb45c.json'
AUTHOR = 'json_to_solo'

class HeartCheck(Solo48):
    icon_id = 'heart-check'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('heart', 'check', 'state')

    def build(self):
        self.add_line('e0', (34, 18), (23, 28))
        self.add_line('e1', (23, 28), (17, 22))
        self.add_line('e2', (24, 40), (8, 25))
        self.add_line('e3', (41, 24), (24, 40))
        self.add_arc('e4-1', (8, 25), (4, 17), radius_x=10)
        self.add_arc('e4-2', (4, 17), (14, 8), radius_x=11)
        self.add_arc('e4-3', (14, 8), (24, 13), radius_x=14)
        self.add_arc('e4-4', (24, 13), (25, 12), radius_x=14, sweep=False)
        self.add_arc('e4-5', (25, 12), (33, 8), radius_x=13)
        self.add_line('e4-6', (33, 8), (38, 9))
        self.add_arc('e4-7', (38, 9), (42, 12), radius_x=10)
        self.add_line('e4-8', (42, 12), (44, 18))
        self.add_arc('e4-9', (44, 18), (41, 24), radius_x=8)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7', 'e4-8', 'e4-9', 'e3', closed=True)
