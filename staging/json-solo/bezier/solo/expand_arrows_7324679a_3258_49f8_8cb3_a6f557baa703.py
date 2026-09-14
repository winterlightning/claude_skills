"""Expand arrows (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7324679a-3258-49f8-8cb3-a6f557baa703'
SOURCE_PATH = 'icons-json/symbol/expand arrows_7324679a-3258-49f8-8cb3-a6f557baa703.json'
AUTHOR = 'json_to_solo'

class ExpandArrowsSymbol(Solo48):
    icon_id = 'expand-arrows-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('expand', 'arrows', 'symbol')

    def build(self):
        self.add_line('e0', (14, 6), (6, 6))
        self.add_line('e1', (6, 6), (6, 14))
        self.add_line('e2', (18, 18), (6, 6))
        self.add_line('e3', (34, 6), (42, 6))
        self.add_line('e4', (42, 6), (30, 18))
        self.add_line('e5', (42, 6), (42, 14))
        self.add_line('e6', (18, 30), (6, 42))
        self.add_line('e7', (6, 33), (6, 42))
        self.add_line('e8', (6, 42), (14, 42))
        self.add_line('e9', (30, 30), (42, 42))
        self.add_line('e10', (34, 42), (42, 42))
        self.add_line('e11', (42, 42), (42, 33))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6')
        self.add_contour('c6', 'e7', 'e8')
        self.add_contour('c7', 'e9')
        self.add_contour('c8', 'e10', 'e11')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c5', 'c6')
