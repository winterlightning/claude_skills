"""Liras (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '986af714-6fb8-449a-ad31-d5271f278137'
SOURCE_PATH = 'icons-json/money/liras_986af714-6fb8-449a-ad31-d5271f278137.json'
AUTHOR = 'json_to_solo'

class LirasMoney(Solo48):
    icon_id = 'liras-money'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('liras', 'money')

    def build(self):
        self.add_line('e0', (17, 12), (17, 36))
        self.add_line('e1', (10, 44), (8, 44))
        self.add_line('e2', (9, 19), (30, 19))
        self.add_line('e3', (40, 44), (10, 44))
        self.add_line('e4', (9, 33), (30, 33))
        self.add_arc('e5-1', (39, 11), (34, 5), radius_x=8, sweep=False)
        self.add_line('e5-2', (34, 5), (28, 4))
        self.add_line('e5-3', (28, 4), (22, 5))
        self.add_line('e5-4', (22, 5), (19, 7))
        self.add_arc('e5-5', (19, 7), (17, 12), radius_x=10, sweep=False)
        self.add_arc('e6', (17, 36), (10, 44), radius_x=12)
        self.add_contour('c0', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e0', 'e6', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c2', 'c0')
