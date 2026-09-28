"""Diamond shape (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bf86e9b1-2710-45c2-8393-0cae02c8611c'
SOURCE_PATH = 'pictographic-primitives/design/diamond shape_bf86e9b1-2710-45c2-8393-0cae02c8611c.svg'
AUTHOR = 'gpt-6'

class DiamondShapeBf86e9b1(Solo48):
    icon_id = 'diamond-shape-bf86e9b1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('diamond', 'shape', 'design')

    def build(self):
        self.add_line('sym-e1', (24, 6), (6, 24))
        self.add_line('sym-e6', (6, 24), (24, 42))
        self.add_line('sym-e11', (24, 42), (42, 24))
        self.add_line('sym-e16', (42, 24), (24, 6))
        self.add_contour('sym-c0', 'sym-e1', 'sym-e6', 'sym-e11', 'sym-e16', closed=True)
