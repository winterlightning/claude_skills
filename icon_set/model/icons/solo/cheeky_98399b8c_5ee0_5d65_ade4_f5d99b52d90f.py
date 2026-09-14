"""Cheeky (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '98399b8c-5ee0-5d65-ade4-f5d99b52d90f'
SOURCE_PATH = 'icons-json/smileys/cheeky_98399b8c-5ee0-5d65-ade4-f5d99b52d90f.json'
AUTHOR = 'json_to_solo'

class Cheeky(Solo48):
    icon_id = 'cheeky'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('cheeky', 'smileys')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1', (13, 21), (19, 21), radius_x=3)
        self.add_arc('e2', (28, 21), (35, 19), radius_x=4)
        self.add_arc('e3-1', (15, 29), (27, 35), radius_x=9, sweep=False)
        self.add_arc('e3-2', (27, 35), (33, 29), radius_x=9, sweep=False)
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3-1', 'e3-2')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
