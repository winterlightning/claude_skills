"""A with lines (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e0363621-7f83-4768-b93a-69d3b06ec1c9'
SOURCE_PATH = 'icons-json/symbol/a with lines_e0363621-7f83-4768-b93a-69d3b06ec1c9.json'
AUTHOR = 'json_to_solo'

class AWithLinesSymbol(Solo48):
    icon_id = 'a-with-lines-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('a', 'with', 'lines', 'symbol')

    def build(self):
        self.add_line('e0', (42, 26), (35, 6))
        self.add_line('e1', (35, 6), (27, 26))
        self.add_line('e2', (40, 21), (30, 21))
        self.add_line('e3', (6, 34), (42, 34))
        self.add_line('e4', (6, 42), (27, 42))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
