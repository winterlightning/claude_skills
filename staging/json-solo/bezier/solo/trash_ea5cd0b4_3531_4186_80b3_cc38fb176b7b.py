"""Trash (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ea5cd0b4-3531-4186-80b3-cc38fb176b7b'
SOURCE_PATH = 'icons-json/symbol/trash_ea5cd0b4-3531-4186-80b3-cc38fb176b7b.json'
AUTHOR = 'json_to_solo'

class Trash(Solo48):
    icon_id = 'trash'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('trash', 'symbol')

    def build(self):
        self.add_line('sym-e0', (42, 13), (38, 13))
        self.add_line('sym-e1', (38, 13), (24, 13))
        self.add_line('sym-e2', (24, 13), (10, 13))
        self.add_line('sym-e3', (10, 13), (6, 13))
        self.add_line('sym-e4', (24, 6), (24, 13))
        self.add_line('sym-e5', (38, 13), (38, 38))
        self.add_bezier('sym-e6', (38, 38), ((38, 39.915), (37.185, 42), (35, 42)))
        self.add_bezier('sym-e7', (35, 42), ((34.673, 42), (34.327, 42), (34, 42)))
        self.add_bezier('sym-e8', (34, 42), ((33.542, 42), (32.458, 42), (32, 42)))
        self.add_line('sym-e9', (32, 42), (24, 42))
        self.add_line('sym-e10', (24, 42), (16, 42))
        self.add_bezier('sym-e11', (16, 42), ((15.542, 42), (14.458, 42), (14, 42)))
        self.add_bezier('sym-e12', (14, 42), ((13.673, 42), (13.327, 42), (13, 42)))
        self.add_bezier('sym-e13', (13, 42), ((10.815, 42), (10, 39.915), (10, 38)))
        self.add_line('sym-e14', (10, 38), (10, 13))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c1', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
