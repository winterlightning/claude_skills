"""Sub square (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a804d8c-0118-4464-a055-b981357df848'
SOURCE_PATH = 'icons-json/symbol/sub square_4a804d8c-0118-4464-a055-b981357df848.json'
AUTHOR = 'json_to_solo'

class SubSquare4a804d8c(Solo48):
    icon_id = 'sub-square-4a804d8c'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('sub', 'square', 'symbol')

    def build(self):
        self.add_line('e0', (6, 6), (17, 6))
        self.add_line('e1', (6, 6), (6, 17))
        self.add_line('e2', (6, 6), (18, 18))
        self.add_line('e3', (32, 6), (42, 6))
        self.add_line('e4', (30, 18), (42, 6))
        self.add_line('e5', (42, 6), (42, 17))
        self.add_line('e6', (30, 30), (42, 42))
        self.add_line('e7', (42, 42), (42, 31))
        self.add_line('e8', (31, 42), (42, 42))
        self.add_line('e9', (18, 30), (6, 42))
        self.add_line('e10', (6, 42), (6, 31))
        self.add_line('e11', (6, 42), (16, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e5')
        self.add_contour('c5', 'e6', 'e7')
        self.add_contour('c6', 'e8')
        self.add_contour('c7', 'e9', 'e10')
        self.add_contour('c8', 'e11')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
