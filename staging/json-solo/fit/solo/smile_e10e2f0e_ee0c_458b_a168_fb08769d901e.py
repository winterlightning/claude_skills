"""Smile (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e10e2f0e-ee0c-458b-a168-fb08769d901e'
SOURCE_PATH = 'icons-json/smileys/smile_e10e2f0e-ee0c-458b-a168-fb08769d901e.json'
AUTHOR = 'json_to_solo'

class Smile(Solo48):
    icon_id = 'smile'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('smile', 'smileys')

    def build(self):
        self.add_line('e0', (14, 20), (15, 19))
        self.add_arc('e1-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e1-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e2-1', (15, 19), (18, 17), radius_x=3)
        self.add_arc('e2-2', (18, 17), (20, 20), radius_x=3)
        self.add_arc('e3', (28, 19), (34, 19), radius_x=3)
        self.add_arc('e4', (14, 29), (34, 29), radius_x=12, sweep=False)
        self.add_contour('c0', 'e0', 'e2-1', 'e2-2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
