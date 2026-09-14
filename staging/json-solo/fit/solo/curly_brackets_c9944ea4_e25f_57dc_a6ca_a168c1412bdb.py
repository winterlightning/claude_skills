"""Curly brackets (programing), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9944ea4-e25f-57dc-a6ca-a168c1412bdb'
SOURCE_PATH = 'icons-json/programing/curly brackets_c9944ea4-e25f-57dc-a6ca-a168c1412bdb.json'
AUTHOR = 'json_to_solo'

class CurlyBracketsC9944ea4(Solo48):
    icon_id = 'curly-brackets-c9944ea4'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('curly', 'brackets', 'programing')

    def build(self):
        self.add_line('e0', (40, 27), (40, 36))
        self.add_line('e1', (9, 21), (9, 11))
        self.add_line('e2', (9, 29), (9, 36))
        self.add_line('e3-1', (35, 8), (40, 10))
        self.add_line('e3-2', (40, 10), (41, 22))
        self.add_arc('e3-3', (41, 22), (44, 24), radius_x=5, sweep=False)
        self.add_line('e4', (44, 24), (40, 27))
        self.add_arc('e5-1', (40, 36), (37, 40), radius_x=4)
        self.add_line('e5-2', (37, 40), (35, 40))
        self.add_line('e6', (6, 24), (9, 21))
        self.add_arc('e7-1', (9, 11), (12, 8), radius_x=7)
        self.add_arc('e7-2', (12, 8), (14, 8), radius_x=12, sweep=False)
        self.add_arc('e8', (4, 24), (9, 29), radius_x=4)
        self.add_arc('e9-1', (9, 36), (12, 40), radius_x=4, sweep=False)
        self.add_line('e9-2', (12, 40), (14, 40))
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3')
        self.add_contour('c1', 'e4', 'e0', 'e5-1', 'e5-2')
        self.add_contour('c2', 'e6', 'e1', 'e7-1', 'e7-2')
        self.add_contour('c3', 'e8', 'e2', 'e9-1', 'e9-2')
        self.relate('connect', 'c2', 'c3')
