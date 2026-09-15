"""Spinach (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ee2140a-910a-408f-a46b-adcaa33ec5b6'
SOURCE_PATH = 'pictographic-primitives/symbol/spinach_4ee2140a-910a-408f-a46b-adcaa33ec5b6.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Spinach(Solo48):
    icon_id = 'spinach'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('spinach', 'symbol')

    def build(self):
        self.add_line('e0', (26, 18), (12, 44))
        self.add_line('e1', (12, 33), (15, 37))
        self.add_bezier('e2', (15, 37), ((17.929, 37.118), (21.378, 36.982), (24.283, 36.5)), ((34.572, 34.782), (39.975, 28.009), (39.975, 20.555)), ((39.975, 20.268), (40, 19.982), (40, 19.687)), ((40, 19.682), (40, 19.677), (40, 19.673)), ((40, 19.227), (39.975, 18.782), (39.975, 18.336)), ((39.975, 14.918), (38.055, 10.218), (36.135, 7.118)), ((35.52, 6.118), (34.868, 5.136), (34.154, 4.182)), ((34.105, 4.118), (34.068, 4.064), (34.018, 4)), ((34.005, 4), (33.991, 4), (33.975, 4)), ((32.984, 4), (26.811, 6.253), (25.563, 6.755)), ((18.228, 9.691), (11.532, 13.936), (8.997, 20.009)), ((8.48, 21.264), (8.025, 22.6), (8.025, 23.918)), ((8.012, 24.027), (8.012, 24.136), (8, 24.245)), ((8, 24.248), (8, 24.25), (8, 24.253)), ((8, 24.405), (8.025, 24.557), (8.025, 24.718)), ((8.025, 27.264), (9.92, 30.945), (12, 33)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', closed=True)
        self.relate('connect', 'c1', 'c0')
