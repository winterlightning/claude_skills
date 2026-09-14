"""Nagras sign (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd29473b3-fd58-4d03-b71d-c51e5c3ecb6c'
SOURCE_PATH = 'icons-json/symbol/nagras sign_d29473b3-fd58-4d03-b71d-c51e5c3ecb6c.json'
AUTHOR = 'json_to_solo'

class NagrasSignSymbol(Solo48):
    icon_id = 'nagras-sign-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('nagras', 'sign', 'symbol')

    def build(self):
        self.add_line('e0', (25, 24), (6, 24))
        self.add_line('e1', (36, 41), (36, 24))
        self.add_line('e2', (36, 24), (42, 24))
        self.add_line('e3', (12, 42), (12, 6))
        self.add_line('e4', (12, 6), (16, 12))
        self.add_line('e5', (16, 12), (24, 24))
        self.add_line('e6', (24, 24), (36, 24))
        self.add_line('e7', (36, 24), (36, 6))
        self.add_bezier('e8', (36, 41), ((31.713, 35.584), (28.641, 29.85), (25, 24)))
        self.add_contour('c0', 'e8', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3', 'e4', 'e5', 'e6', 'e7')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c2', 'c0')
