"""Circle half (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '031da5e5-a8c4-45af-9b74-e8c1dae95201'
SOURCE_PATH = 'pictographic-primitives/symbol/circle half_031da5e5-a8c4-45af-9b74-e8c1dae95201.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class CircleHalfSymbol(Solo48):
    icon_id = 'circle-half-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('circle', 'half', 'symbol')

    def build(self):
        self.add_line('e0', (40, 44), (40, 4))
        self.add_bezier('e1', (40, 4), ((39.651, 4), (39.302, 4.009), (38.953, 4.009)), ((22.531, 4.009), (8.015, 12.864), (8.015, 23.2)), ((8.015, 23.54), (8, 23.88), (8, 24.22)), ((8, 24.226), (8, 24.231), (8, 24.236)), ((8, 28.373), (10.327, 32.555), (14.211, 35.882)), ((19.505, 40.427), (28.858, 43.982), (38.138, 43.982)), ((38.502, 43.982), (38.865, 44), (39.229, 44)), ((39.476, 44), (39.738, 44), (40, 44)))
        self.add_contour('c0', 'e1', 'e0', closed=True)
