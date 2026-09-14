"""Smirk (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b2da279-812c-5533-9f31-a920f7b8d2ab'
SOURCE_PATH = 'icons-json/smileys/smirk_9b2da279-812c-5533-9f31-a920f7b8d2ab.json'
AUTHOR = 'json_to_solo'

class SmirkSmileys(Solo48):
    icon_id = 'smirk-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('smirk', 'smileys')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e1', (21, 35), ((25.873, 35.864), (30.118, 34.145), (33, 30)))
        self.add_bezier('e2', (14, 18), ((16.645, 17.391), (17.982, 17.264), (20, 19)))
        self.add_bezier('e3', (28, 20), ((30.355, 18.845), (32.427, 18.564), (35, 19)))
        self.add_bezier('e4', (18, 27), ((18, 27.3), (18, 27.7), (18, 28)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
