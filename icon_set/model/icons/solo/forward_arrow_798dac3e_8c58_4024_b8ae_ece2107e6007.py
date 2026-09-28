"""Forward arrow (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '798dac3e-8c58-4024-b8ae-ece2107e6007'
SOURCE_PATH = 'pictographic-primitives/symbol/forward arrow_798dac3e-8c58-4024-b8ae-ece2107e6007.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ForwardArrow(Solo48):
    icon_id = 'forward-arrow'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('forward', 'arrow', 'symbol')

    def build(self):
        self.add_line('e0', (30, 4), (40, 15))
        self.add_line('e1', (8, 44), (8, 35))
        self.add_line('e2', (25, 15), (40, 15))
        self.add_line('e3', (30, 27), (40, 15))
        self.add_bezier('e4', (8, 35), ((8, 34.809), (8, 34.536), (8, 34.345)), ((8, 33.527), (8.202, 32.582), (8.328, 31.773)), ((9.356, 24.845), (13.507, 19.009), (19.512, 16.264)), ((21.12, 15.527), (23.24, 15), (25, 15)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e4', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
