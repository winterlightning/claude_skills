"""Boat (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '64779290-47a6-5d1a-8219-16cccfc7da32'
SOURCE_PATH = 'icons-json/transportation/boat_64779290-47a6-5d1a-8219-16cccfc7da32.json'
AUTHOR = 'json_to_solo'

class Boat64779290(Solo48):
    icon_id = 'boat-64779290'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('boat', 'transportation')

    def build(self):
        self.add_line('e0', (14, 8), (25, 8))
        self.add_line('e1', (28, 10), (33, 21))
        self.add_line('e2', (18, 8), (13, 22))
        self.add_line('e3', (35, 21), (7, 24))
        self.add_line('e4', (6, 26), (4, 38))
        self.add_line('e5', (4, 40), (32, 40))
        self.add_line('e6', (44, 21), (35, 21))
        self.add_line('e7', (25, 8), (28, 10))
        self.add_arc('e8', (7, 24), (6, 26), radius_x=21, sweep=False)
        self.add_line('e9', (4, 38), (4, 40))
        self.add_arc('e10', (32, 40), (44, 21), radius_x=27, sweep=False)
        self.add_contour('c0', 'e0', 'e7', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e8', 'e4', 'e9', 'e5', 'e10', 'e6', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c2')
