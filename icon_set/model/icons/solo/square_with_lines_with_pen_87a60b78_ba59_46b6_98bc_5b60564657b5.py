"""Square with lines with pen (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '87a60b78-ba59-46b6-98bc-5b60564657b5'
SOURCE_PATH = 'icons-json/symbol/square with lines with pen_87a60b78-ba59-46b6-98bc-5b60564657b5.json'
AUTHOR = 'json_to_solo'

class SquareWithLinesWithPen(Solo48):
    icon_id = 'square-with-lines-with-pen'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('square', 'with', 'lines', 'pen', 'symbol')

    def build(self):
        self.add_line('e0', (6, 42), (37, 42))
        self.add_line('e1', (42, 13), (22, 32))
        self.add_line('e2', (6, 42), (7, 38))
        self.add_line('e3', (9, 31), (35, 6))
        self.add_line('e4', (35, 6), (42, 13))
        self.add_arc('e5', (22, 32), (6, 42), radius_x=21)
        self.add_arc('e6', (7, 38), (9, 31), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2', 'e6', 'e3', 'e4', closed=True)
