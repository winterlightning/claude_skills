"""Smile face (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '89fbe59a-21d5-4c1c-b815-db67a6781259'
SOURCE_PATH = 'icons-json/symbol/smile face_89fbe59a-21d5-4c1c-b815-db67a6781259.json'
AUTHOR = 'json_to_solo'

class SmileFace(Solo48):
    icon_id = 'smile-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('smile', 'face', 'symbol')

    def build(self):
        self.add_line('e0', (17, 21), (17, 19))
        self.add_line('e1', (31, 19), (31, 21))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e3', (17, 31), (31, 32), radius_x=10, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e3')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
