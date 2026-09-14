"""Baht (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd48f163d-0715-5aa1-ab17-7c224344ee83'
SOURCE_PATH = 'icons-json/money/baht_d48f163d-0715-5aa1-ab17-7c224344ee83.json'
AUTHOR = 'json_to_solo'

class Baht(Solo48):
    icon_id = 'baht'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('baht', 'money')

    def build(self):
        self.add_line('e0', (29, 39), (8, 39))
        self.add_line('e1', (8, 39), (8, 9))
        self.add_line('e2', (8, 9), (28, 9))
        self.add_line('e3', (30, 24), (8, 24))
        self.add_line('e4', (23, 44), (23, 4))
        self.add_arc('e5-1', (28, 9), (38, 14), radius_x=12)
        self.add_arc('e5-2', (38, 14), (30, 24), radius_x=8)
        self.add_arc('e5-3', (30, 24), (40, 32), radius_x=10)
        self.add_arc('e5-4', (40, 32), (29, 39), radius_x=9)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e5-1', 'e5-2', 'e5-3', 'e5-4', closed=True)
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
