"""Wink (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8dd8865b-3604-51e7-a9f8-21d3178f09a9'
SOURCE_PATH = 'icons-json/smileys/wink_8dd8865b-3604-51e7-a9f8-21d3178f09a9.json'
AUTHOR = 'json_to_solo'

class WinkSmileys(Solo48):
    icon_id = 'wink-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('wink', 'smileys')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1', (16, 20), (19, 20), radius_x=2, large_arc=True)
        self.add_arc('e2', (28, 19), (35, 19), radius_x=5)
        self.add_arc('e3', (15, 29), (34, 29), radius_x=11, sweep=False)
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
