"""Sad face 1 (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c6daa8db-ea16-41b2-8d86-2c6d7cd97c5a'
SOURCE_PATH = 'icons-json/symbol/sad face 1_c6daa8db-ea16-41b2-8d86-2c6d7cd97c5a.json'
AUTHOR = 'json_to_solo'

class SadFace1Symbol(Solo48):
    icon_id = 'sad-face-1-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('sad', 'face', 'symbol')

    def build(self):
        self.add_line('e0', (13, 16), (13, 8))
        self.add_line('e1', (34, 16), (34, 8))
        self.add_arc('e2', (4, 40), (44, 40), radius_x=22)
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1')
