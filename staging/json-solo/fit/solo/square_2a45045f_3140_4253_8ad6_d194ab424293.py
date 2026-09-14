"""Square (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
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
        self.add_line('sym-e1', (40, 42), (41, 42))
        self.add_line('sym-e2', (41, 42), (42, 40))
        self.add_line('sym-e5', (42, 40), (42, 24))
        self.add_line('sym-e6', (42, 24), (42, 8))
        self.add_line('sym-e9', (42, 8), (41, 6))
        self.add_line('sym-e10', (41, 6), (40, 6))
        self.add_line('sym-e11', (40, 6), (24, 6))
        self.add_line('sym-e12', (24, 6), (8, 6))
        self.add_line('sym-e13', (8, 6), (7, 6))
        self.add_line('sym-e14', (7, 6), (6, 8))
        self.add_line('sym-e17', (6, 8), (6, 24))
        self.add_line('sym-e18', (6, 24), (6, 40))
        self.add_line('sym-e21', (6, 40), (7, 42))
        self.add_arc('sym-e22', (7, 42), (8, 42), radius_x=1)
        self.add_line('sym-e23', (8, 42), (24, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e5', 'sym-e6', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e17', 'sym-e18', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
