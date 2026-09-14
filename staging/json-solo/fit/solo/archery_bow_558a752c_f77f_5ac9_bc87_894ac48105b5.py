"""Archery bow (sports), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '558a752c-f77f-5ac9-bc87-894ac48105b5'
SOURCE_PATH = 'icons-json/sports/archery bow_558a752c-f77f-5ac9-bc87-894ac48105b5.json'
AUTHOR = 'json_to_solo'

class ArcheryBowSports(Solo48):
    icon_id = 'archery-bow-sports'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('archery', 'bow', 'sports')

    def build(self):
        self.add_line('e0', (6, 6), (6, 42))
        self.add_line('e1', (28, 20), (37, 11))
        self.add_line('e2', (37, 11), (31, 13))
        self.add_line('e3', (28, 20), (33, 23))
        self.add_line('e4', (39, 31), (40, 36))
        self.add_line('e5', (42, 42), (6, 42))
        self.add_line('e6', (6, 42), (28, 20))
        self.add_line('e7', (36, 17), (37, 11))
        self.add_arc('e8-1', (28, 20), (23, 12), radius_x=33, sweep=False)
        self.add_arc('e8-2', (23, 12), (15, 8), radius_x=15, sweep=False)
        self.add_arc('e8-3', (15, 8), (6, 6), radius_x=10)
        self.add_arc('e9', (33, 23), (39, 31), radius_x=14)
        self.add_arc('e10', (40, 36), (42, 42), radius_x=9, sweep=False)
        self.add_contour('c0', 'e8-1', 'e8-2', 'e8-3', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3', 'e9', 'e4', 'e10')
        self.add_contour('c3', 'e5', 'e6')
        self.add_contour('c4', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
