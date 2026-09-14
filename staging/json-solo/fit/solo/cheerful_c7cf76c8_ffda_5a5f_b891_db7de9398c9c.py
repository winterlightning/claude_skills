"""Cheerful (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c7cf76c8-ffda-5a5f-b891-db7de9398c9c'
SOURCE_PATH = 'icons-json/smileys/cheerful_c7cf76c8-ffda-5a5f-b891-db7de9398c9c.json'
AUTHOR = 'json_to_solo'

class CheerfulSmileys(Solo48):
    icon_id = 'cheerful-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('cheerful', 'smileys')

    def build(self):
        self.add_line('e0', (14, 27), (19, 28))
        self.add_arc('e1-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e1-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e2-1', (34, 27), (24, 36), radius_x=11)
        self.add_arc('e2-2', (24, 36), (14, 27), radius_x=11)
        self.add_arc('e3-1', (19, 28), (34, 27), radius_x=57, sweep=False)
        self.add_line('e3-2', (34, 27), (33, 29))
        self.add_arc('e4-1', (13, 19), (17, 16), radius_x=4)
        self.add_arc('e4-2', (17, 16), (20, 19), radius_x=3)
        self.add_arc('e5-1', (28, 19), (31, 15), radius_x=3)
        self.add_arc('e5-2', (31, 15), (35, 19), radius_x=4)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e0', 'e3-1', 'e3-2')
        self.add_contour('c1', 'e4-1', 'e4-2')
        self.add_contour('c2', 'e5-1', 'e5-2')
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
