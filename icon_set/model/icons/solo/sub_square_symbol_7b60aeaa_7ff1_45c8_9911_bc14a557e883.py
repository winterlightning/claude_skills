"""Sub square (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7b60aeaa-7ff1-45c8-9911-bc14a557e883'
SOURCE_PATH = 'icons-json/symbol/sub square_7b60aeaa-7ff1-45c8-9911-bc14a557e883.json'
AUTHOR = 'gpt-6'

class SubSquareSymbol(Solo48):
    icon_id = 'sub-square-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('sub', 'square', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 6), (40, 6))
        self.add_arc('sym-e2', (40, 6), (42, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e4', (42, 8), (42, 40))
        self.add_arc('sym-e7', (42, 40), (40, 42), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('sym-e8', (40, 42), (39, 42), radius_x=40, radius_y=40, large_arc=False, sweep=False)
        self.add_line('sym-e9', (39, 42), (9, 42))
        self.add_arc('sym-e11', (9, 42), (8, 42), radius_x=22, radius_y=22, large_arc=False, sweep=False)
        self.add_arc('sym-e12', (8, 42), (6, 40), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e14', (6, 40), (6, 8))
        self.add_arc('sym-e17', (6, 8), (8, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e18', (8, 6), (24, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e4', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e17', 'sym-e18', closed=True)
