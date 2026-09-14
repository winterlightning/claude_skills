"""Tape (office), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5cea5442-b0ab-4306-aab1-4574e1814623'
SOURCE_PATH = 'icons-json/office/tape_5cea5442-b0ab-4306-aab1-4574e1814623.json'
AUTHOR = 'json_to_solo'

class TapeOffice(Solo48):
    icon_id = 'tape-office'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('tape', 'office')

    def build(self):
        self.add_line('e0', (17, 16), (11, 21))
        self.add_line('e1', (11, 21), (4, 29))
        self.add_line('e2', (5, 30), (16, 30))
        self.add_arc('e3-top', (24, 24), (34, 24), radius_x=5, radius_y=6)
        self.add_arc('e3-bottom', (34, 24), (24, 24), radius_x=5, radius_y=6)
        self.add_arc('e4-top', (14, 24), (44, 24), radius_x=15, radius_y=16)
        self.add_arc('e4-bottom', (44, 24), (14, 24), radius_x=15, radius_y=16)
        self.add_arc('e5', (4, 29), (5, 30), radius_x=1, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e5', 'e2')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c0', 'e4')
