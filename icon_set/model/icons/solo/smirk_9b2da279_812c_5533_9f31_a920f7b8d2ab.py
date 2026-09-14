"""Smirk (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b2da279-812c-5533-9f31-a920f7b8d2ab'
SOURCE_PATH = 'icons-json/smileys/smirk_9b2da279-812c-5533-9f31-a920f7b8d2ab.json'
AUTHOR = 'json_to_solo'

class Smirk(Solo48):
    icon_id = 'smirk'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('smirk', 'smileys')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1', (21, 35), (33, 30), radius_x=10, sweep=False)
        self.add_arc('e2', (14, 18), (20, 19), radius_x=6)
        self.add_arc('e3', (28, 20), (35, 19), radius_x=11)
        self.add_arc('e4', (18, 27), (18, 28), radius_x=29, sweep=False)
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
