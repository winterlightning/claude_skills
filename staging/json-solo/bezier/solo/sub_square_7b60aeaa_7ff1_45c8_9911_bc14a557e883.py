"""Sub square (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b60aeaa-7ff1-45c8-9911-bc14a557e883'
SOURCE_PATH = 'icons-json/symbol/sub square_7b60aeaa-7ff1-45c8-9911-bc14a557e883.json'
AUTHOR = 'json_to_solo'

class SubSquare7b60aeaa(Solo48):
    icon_id = 'sub-square-7b60aeaa'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('sub', 'square', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 6), (39, 6))
        self.add_bezier('sym-e1', (39, 6), ((39.319, 6), (39.681, 6), (40, 6)))
        self.add_bezier('sym-e2', (40, 6), ((41.055, 6), (42, 6.912), (42, 8)))
        self.add_bezier('sym-e3', (42, 8), ((42, 8.074), (42, 7.926), (42, 8)))
        self.add_line('sym-e4', (42, 8), (42, 24))
        self.add_line('sym-e5', (42, 24), (42, 40))
        self.add_bezier('sym-e6', (42, 40), ((42, 40.074), (42, 39.926), (42, 40)))
        self.add_bezier('sym-e7', (42, 40), ((42, 41.088), (41.055, 42), (40, 42)))
        self.add_bezier('sym-e8', (40, 42), ((39.681, 42), (39.319, 42), (39, 42)))
        self.add_line('sym-e9', (39, 42), (24, 42))
        self.add_line('sym-e10', (24, 42), (9, 42))
        self.add_bezier('sym-e11', (9, 42), ((8.681, 42), (8.319, 42), (8, 42)))
        self.add_bezier('sym-e12', (8, 42), ((6.945, 42), (6, 41.088), (6, 40)))
        self.add_bezier('sym-e13', (6, 40), ((6, 39.926), (6, 40.074), (6, 40)))
        self.add_line('sym-e14', (6, 40), (6, 24))
        self.add_line('sym-e15', (6, 24), (6, 8))
        self.add_bezier('sym-e16', (6, 8), ((6, 7.926), (6, 8.074), (6, 8)))
        self.add_bezier('sym-e17', (6, 8), ((6, 6.912), (6.945, 6), (8, 6)))
        self.add_bezier('sym-e18', (8, 6), ((8.319, 6), (8.681, 6), (9, 6)))
        self.add_line('sym-e19', (9, 6), (24, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
