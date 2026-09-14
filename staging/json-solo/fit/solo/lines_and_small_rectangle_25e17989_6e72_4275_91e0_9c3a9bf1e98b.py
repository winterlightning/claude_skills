"""Lines and small rectangle (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25e17989-6e72-4275-91e0-9c3a9bf1e98b'
SOURCE_PATH = 'icons-json/symbol/lines and small rectangle_25e17989-6e72-4275-91e0-9c3a9bf1e98b.json'
AUTHOR = 'json_to_solo'

class LinesAndSmallRectangleSymbol(Solo48):
    icon_id = 'lines-and-small-rectangle-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('lines', 'and', 'small', 'rectangle', 'symbol')

    def build(self):
        self.add_line('e0', (31, 13), (42, 13))
        self.add_line('e1', (31, 35), (42, 35))
        self.add_line('e2', (20, 6), (6, 6))
        self.add_line('e3', (6, 6), (6, 18))
        self.add_line('e4', (6, 18), (20, 18))
        self.add_line('e5', (20, 18), (20, 6))
        self.add_line('e6', (20, 30), (6, 30))
        self.add_line('e7', (6, 30), (6, 42))
        self.add_line('e8', (6, 42), (20, 42))
        self.add_line('e9', (20, 42), (20, 30))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4', 'e5', closed=True)
        self.add_contour('c3', 'e6', 'e7', 'e8', 'e9', closed=True)
