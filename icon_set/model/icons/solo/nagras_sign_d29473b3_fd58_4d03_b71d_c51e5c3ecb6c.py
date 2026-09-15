"""Nagras sign (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd29473b3-fd58-4d03-b71d-c51e5c3ecb6c'
SOURCE_PATH = 'icons-json/symbol/nagras sign_d29473b3-fd58-4d03-b71d-c51e5c3ecb6c.json'
AUTHOR = 'gpt-6'

class NagrasSign(Solo48):
    icon_id = 'nagras-sign'
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
        self.add_line('e4', (12, 6), (24, 24))
        self.add_line('e6', (24, 24), (36, 24))
        self.add_line('e7', (36, 24), (36, 6))
        self.add_line('e8', (36, 41), (25, 24))
        self.add_contour('c0', 'e8', 'e0', closed=False)
        self.add_contour('c1', 'e1', 'e2', closed=False)
        self.add_contour('c2', 'e3', 'e4', 'e6', 'e7', closed=False)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c2', 'c0')
