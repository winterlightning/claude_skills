"""Blessed (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4669a42f-119e-5431-9305-4e31305f43c1'
SOURCE_PATH = 'icons-json/smileys/blessed_4669a42f-119e-5431-9305-4e31305f43c1.json'
AUTHOR = 'json_to_solo'

class Blessed(Solo48):
    icon_id = 'blessed'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('blessed', 'smileys')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1-1', (12, 22), (15, 19), radius_x=5)
        self.add_arc('e1-2', (15, 19), (20, 21), radius_x=3)
        self.add_arc('e2-1', (28, 22), (31, 19), radius_x=4)
        self.add_arc('e2-2', (31, 19), (36, 22), radius_x=5)
        self.add_arc('e3', (15, 29), (34, 29), radius_x=10, sweep=False)
        self.add_contour('c0', 'e1-1', 'e1-2')
        self.add_contour('c1', 'e2-1', 'e2-2')
        self.add_contour('c2', 'e3')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
