"""Arrow thin top (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e2d0f3f2-7989-4553-a926-724f4995f1c2'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow thin top_e2d0f3f2-7989-4553-a926-724f4995f1c2.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class ArrowThinTopSymbol(Solo48):
    icon_id = 'arrow-thin-top-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'thin', 'top', 'symbol')

    def build(self):
        # Plan: exact reflection of both arrowhead arms about the shaft.
        # Reference: the existing directional symbol and shared dimensions.
        self.add_line('e0', (40, 23), (24, 4))
        self.add_line('e1', (8, 23), (24, 4))
        self.add_line('e2', (24, 44), (24, 4))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
