"""Vectors anchor square (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '765d4600-b424-48ac-a39f-4041183aa21d'
SOURCE_PATH = 'pictographic-primitives/design/vectors anchor square_765d4600-b424-48ac-a39f-4041183aa21d.svg'
AUTHOR = 'gpt-6'

class VectorsAnchorSquare(Solo48):
    icon_id = 'vectors-anchor-square'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('vectors', 'anchor', 'square', 'design')

    def build(self):
        self.add_line('sym-e0', (40, 42), (8, 42))
        self.add_arc('sym-e2', (8, 42), (6, 40), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e3', (6, 40), (6, 8))
        self.add_line('sym-e5', (6, 8), (8, 6))
        self.add_line('sym-e6', (8, 6), (40, 6))
        self.add_line('sym-e8', (40, 6), (42, 8))
        self.add_line('sym-e9', (42, 8), (42, 40))
        self.add_line('sym-e11', (42, 40), (40, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e11', closed=True)
