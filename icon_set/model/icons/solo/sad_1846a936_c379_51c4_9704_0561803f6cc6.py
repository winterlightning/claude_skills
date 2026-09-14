"""Sad (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1846a936-c379-51c4-9704-0561803f6cc6'
SOURCE_PATH = 'icons-json/smileys/sad_1846a936-c379-51c4-9704-0561803f6cc6.json'
AUTHOR = 'json_to_solo'

class Sad(Solo48):
    icon_id = 'sad'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('sad', 'smileys')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1', (15, 32), (33, 32), radius_x=11)
        self.add_arc('e2', (12, 22), (19, 19), radius_x=7, sweep=False)
        self.add_arc('e3', (29, 19), (35, 22), radius_x=7, sweep=False)
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
