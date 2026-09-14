"""Blushing (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '488475b1-7c72-5f21-ba4a-76116df6b100'
SOURCE_PATH = 'icons-json/smileys/blushing_488475b1-7c72-5f21-ba4a-76116df6b100.json'
AUTHOR = 'json_to_solo'

class Blushing(Solo48):
    icon_id = 'blushing'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('blushing', 'smileys')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1-1', (13, 20), (17, 17), radius_x=4)
        self.add_arc('e1-2', (17, 17), (20, 20), radius_x=3)
        self.add_arc('e2-1', (28, 21), (30, 18), radius_x=3)
        self.add_arc('e2-2', (30, 18), (35, 20), radius_x=4)
        self.add_arc('e3', (15, 29), (33, 29), radius_x=10, sweep=False)
        self.add_contour('c0', 'e1-1', 'e1-2')
        self.add_contour('c1', 'e2-1', 'e2-2')
        self.add_contour('c2', 'e3')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
