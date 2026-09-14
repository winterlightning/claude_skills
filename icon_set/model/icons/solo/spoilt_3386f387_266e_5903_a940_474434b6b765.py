"""Spoilt (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3386f387-266e-5903-a940-474434b6b765'
SOURCE_PATH = 'icons-json/smileys/spoilt_3386f387-266e-5903-a940-474434b6b765.json'
AUTHOR = 'json_to_solo'

class Spoilt(Solo48):
    icon_id = 'spoilt'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('spoilt', 'smileys')

    def build(self):
        self.add_line('e0', (5, 29), (4, 24))
        self.add_arc('e1-1', (8, 12), (38, 10), radius_x=20)
        self.add_arc('e1-2', (38, 10), (37, 39), radius_x=20)
        self.add_arc('e1-3', (37, 39), (5, 29), radius_x=20)
        self.add_arc('e2-1', (4, 24), (8, 13), radius_x=20)
        self.add_arc('e2-2', (8, 13), (10, 10), radius_x=11)
        self.add_arc('e3', (29, 19), (36, 21), radius_x=8, sweep=False)
        self.add_arc('e4', (12, 21), (19, 19), radius_x=8, sweep=False)
        self.add_arc('e5', (17, 25), (17, 26), radius_x=27, sweep=False)
        self.add_arc('e6', (30, 25), (30, 26), radius_x=1)
        self.add_arc('e7', (18, 35), (30, 35), radius_x=8)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e0', 'e2-1', 'e2-2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e7')
