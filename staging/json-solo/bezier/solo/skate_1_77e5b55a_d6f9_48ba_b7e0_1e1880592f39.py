"""Skate 1 (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77e5b55a-d6f9-48ba-b7e0-1e1880592f39'
SOURCE_PATH = 'icons-json/symbol/skate 1_77e5b55a-d6f9-48ba-b7e0-1e1880592f39.json'
AUTHOR = 'json_to_solo'

class Skate1Symbol(Solo48):
    icon_id = 'skate-1-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('skate', 'symbol')

    def build(self):
        self.add_line('e0', (35, 23), (29, 21))
        self.add_line('e1', (25, 15), (25, 6))
        self.add_line('e2', (25, 6), (8, 6))
        self.add_line('e3', (8, 6), (8, 19))
        self.add_line('e4', (9, 32), (42, 32))
        self.add_bezier('e5', (42, 32), ((42, 31.419), (41.984, 31.012), (41.984, 30.431)), ((41.984, 26.626), (38.191, 24.195), (35, 23)))
        self.add_bezier('e6', (29, 21), ((26.464, 20.051), (25, 17.725), (25, 15)))
        self.add_bezier('e7', (8, 19), ((8, 19.565), (7.391, 20.302), (7.252, 20.842)), ((6.843, 22.364), (6.016, 24.581), (6.016, 26.16)), ((6.008, 26.217), (6.008, 26.275), (6, 26.34)), ((6, 26.342), (6, 26.343), (6, 26.345)), ((6, 26.45), (6.008, 26.563), (6.008, 26.667)), ((6.008, 28.484), (6.775, 32), (9, 32)))
        self.add_dot('e8', (25, 42))
        self.add_dot('e9', (10, 42))
        self.add_dot('e10', (40, 42))
        self.add_contour('c0', 'e5', 'e0', 'e6', 'e1', 'e2', 'e3', 'e7', 'e4', closed=True)
