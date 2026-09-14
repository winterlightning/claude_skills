"""Arrows retweet (_uncategorized_04), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e2917c28-d316-437f-b17b-a46efe1736c1'
SOURCE_PATH = 'icons-json/_uncategorized_04/arrows retweet_e2917c28-d316-437f-b17b-a46efe1736c1.json'
AUTHOR = 'json_to_solo'

class ArrowsRetweet(Solo48):
    icon_id = 'arrows-retweet'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_04'
    aliases = ()
    keywords = ('arrows', 'retweet', '_uncategorized_04')

    def build(self):
        self.add_line('e0', (35, 6), (42, 13))
        self.add_line('e1', (6, 25), (6, 16))
        self.add_line('e2', (9, 13), (42, 13))
        self.add_line('e3', (35, 18), (42, 13))
        self.add_line('e4', (42, 23), (42, 33))
        self.add_line('e5', (38, 36), (6, 36))
        self.add_line('e6', (13, 30), (6, 36))
        self.add_line('e7', (13, 42), (6, 36))
        self.add_arc('e8', (6, 16), (9, 13), radius_x=4)
        self.add_arc('e9', (42, 33), (38, 36), radius_x=5)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e8', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e9', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
