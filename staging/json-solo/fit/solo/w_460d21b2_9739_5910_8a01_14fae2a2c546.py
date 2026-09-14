"""W (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '460d21b2-9739-5910-8a01-14fae2a2c546'
SOURCE_PATH = 'icons-json/typeface/W_460d21b2-9739-5910-8a01-14fae2a2c546.json'
AUTHOR = 'json_to_solo'

class W460d21b2(Solo48):
    icon_id = 'w-460d21b2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('w', 'typeface')

    def build(self):
        self.add_line('sym-e0', (42, 6), (35, 39))
        self.add_arc('sym-e1', (35, 39), (33, 42), radius_x=3)
        self.add_arc('sym-e4', (33, 42), (31, 37), radius_x=6)
        self.add_line('sym-e5', (31, 37), (26, 14))
        self.add_line('sym-e6', (26, 14), (25, 14))
        self.add_arc('sym-e7', (25, 14), (24, 13), radius_x=1, sweep=False)
        self.add_arc('sym-e8', (24, 13), (23, 14), radius_x=1, sweep=False)
        self.add_line('sym-e9', (23, 14), (22, 14))
        self.add_line('sym-e10', (22, 14), (17, 37))
        self.add_arc('sym-e11', (17, 37), (15, 42), radius_x=5)
        self.add_arc('sym-e14', (15, 42), (13, 39), radius_x=4)
        self.add_line('sym-e15', (13, 39), (6, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e14', 'sym-e15')
