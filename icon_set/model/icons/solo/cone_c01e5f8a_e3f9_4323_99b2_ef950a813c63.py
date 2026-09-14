"""Cone (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c01e5f8a-e3f9-4323-99b2-ef950a813c63'
SOURCE_PATH = 'icons-json/symbol/cone_c01e5f8a-e3f9-4323-99b2-ef950a813c63.json'
AUTHOR = 'json_to_solo'

class Cone(Solo48):
    icon_id = 'cone'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('cone', 'symbol')

    def build(self):
        self.add_line('e0', (24, 4), (40, 39))
        self.add_line('e1', (8, 39), (24, 4))
        self.add_arc('e2-1', (40, 39), (33, 43), radius_x=16)
        self.add_line('e2-2', (33, 43), (23, 44))
        self.add_arc('e2-3', (23, 44), (13, 42), radius_x=27)
        self.add_line('e2-4', (13, 42), (8, 39))
        self.add_contour('c0', 'e0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e1', closed=True)
