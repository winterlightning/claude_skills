"""Square with lines with pen (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '87a60b78-ba59-46b6-98bc-5b60564657b5'
SOURCE_PATH = 'icons-json/symbol/square with lines with pen_87a60b78-ba59-46b6-98bc-5b60564657b5.json'
AUTHOR = 'json_to_solo'

class SquareWithLinesWithPenSymbol(Solo48):
    icon_id = 'square-with-lines-with-pen-symbol'
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
        self.add_bezier('e5', (22, 32), ((20.617, 33.383), (19.606, 34.947), (18.224, 36.33)), ((17.438, 37.115), (16.653, 38.089), (15.704, 38.695)), ((14.926, 39.194), (13.814, 39.406), (12.955, 39.701)), ((10.647, 40.495), (8.324, 41.264), (6, 42)))
        self.add_bezier('e6', (7, 38), ((7.205, 36.969), (7.424, 35.937), (7.743, 34.939)), ((8.119, 33.777), (8.075, 31.9), (9, 31)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2', 'e6', 'e3', 'e4', closed=True)
