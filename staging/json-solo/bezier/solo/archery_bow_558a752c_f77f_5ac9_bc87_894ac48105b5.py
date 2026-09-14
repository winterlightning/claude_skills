"""Archery bow (sports), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e8', (28, 20), ((27.026, 18.552), (26.34, 16.955), (25.489, 15.442)), ((23.975, 12.709), (21.513, 10.426), (18.69, 9.093)), ((17.111, 8.348), (15.335, 7.923), (13.593, 7.874)), ((12.267, 7.833), (10.811, 8.013), (9.51, 7.694)), ((8.675, 7.489), (7.514, 7.031), (6.875, 6.466)), ((6.785, 6.368), (6.695, 6.27), (6.605, 6.172)), ((6.303, 6), (6.319, 6.172), (6, 6)))
        self.add_bezier('e9', (33, 23), ((35.283, 24.522), (37.075, 26.733), (38.179, 29.245)), ((38.351, 29.637), (38.943, 30.583), (39, 31)))
        self.add_bezier('e10', (40, 36), ((40.311, 38.193), (40.454, 40.372), (42, 42)))
        self.add_contour('c0', 'e8', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3', 'e9', 'e4', 'e10')
        self.add_contour('c3', 'e5', 'e6')
        self.add_contour('c4', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
