"""Square (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a45045f-3140-4253-8ad6-d194ab424293'
SOURCE_PATH = 'icons-json/symbol/square_2a45045f-3140-4253-8ad6-d194ab424293.json'
AUTHOR = 'json_to_solo'

class Square(Solo48):
    icon_id = 'square'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('square', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 42), (40, 42))
        self.add_bezier('sym-e1', (40, 42), ((40.147, 41.918), (40.853, 42), (41, 42)))
        self.add_bezier('sym-e2', (41, 42), ((41.597, 41.615), (42, 40.72), (42, 40)))
        self.add_bezier('sym-e3', (42, 40), ((42, 39.951), (42, 40.057), (42, 40)))
        self.add_bezier('sym-e4', (42, 40), ((42, 39.959), (42, 40.041), (42, 40)))
        self.add_line('sym-e5', (42, 40), (42, 24))
        self.add_line('sym-e6', (42, 24), (42, 8))
        self.add_bezier('sym-e7', (42, 8), ((42, 7.959), (42, 8.041), (42, 8)))
        self.add_bezier('sym-e8', (42, 8), ((42, 7.943), (42, 8.049), (42, 8)))
        self.add_bezier('sym-e9', (42, 8), ((42, 7.28), (41.597, 6.385), (41, 6)))
        self.add_bezier('sym-e10', (41, 6), ((40.853, 6), (40.147, 6.082), (40, 6)))
        self.add_line('sym-e11', (40, 6), (24, 6))
        self.add_line('sym-e12', (24, 6), (8, 6))
        self.add_bezier('sym-e13', (8, 6), ((7.853, 6.082), (7.147, 6), (7, 6)))
        self.add_bezier('sym-e14', (7, 6), ((6.403, 6.385), (6, 7.28), (6, 8)))
        self.add_bezier('sym-e15', (6, 8), ((6, 8.049), (6, 7.943), (6, 8)))
        self.add_bezier('sym-e16', (6, 8), ((6, 8.041), (6, 7.959), (6, 8)))
        self.add_line('sym-e17', (6, 8), (6, 24))
        self.add_line('sym-e18', (6, 24), (6, 40))
        self.add_bezier('sym-e19', (6, 40), ((6, 40.041), (6, 39.959), (6, 40)))
        self.add_bezier('sym-e20', (6, 40), ((6, 40.057), (6, 39.951), (6, 40)))
        self.add_bezier('sym-e21', (6, 40), ((6, 40.72), (6.403, 41.615), (7, 42)))
        self.add_bezier('sym-e22', (7, 42), ((7.147, 42), (7.853, 41.918), (8, 42)))
        self.add_line('sym-e23', (8, 42), (24, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
