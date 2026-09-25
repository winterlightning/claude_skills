"""Horse head (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9fa5c4e8-5509-4115-889b-fb3874cf4d30'
SOURCE_PATH = 'pictographic-primitives/symbol/horse head_9fa5c4e8-5509-4115-889b-fb3874cf4d30.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class HorseHeadSymbol(Solo48):
    icon_id = 'horse-head-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('horse', 'head', 'symbol')

    def build(self):
        self.add_line('e0', (26, 4), (22, 8))
        self.add_line('e1', (8, 44), (32, 44))
        self.add_line('e2', (39, 23), (40, 19))
        self.add_bezier('e3', (22, 8), ((21.29, 8.645), (19.62, 8.755), (18.74, 9.155)), ((16.88, 9.982), (15.12, 11.318), (13.86, 12.809)), ((8.56, 19.073), (8.02, 31.527), (8.02, 39.209)), ((8.02, 39.555), (8, 39.9), (8, 40.255)), ((8, 41.5), (8, 42.745), (8, 44)))
        self.add_bezier('e4', (32, 44), ((30.05, 38.382), (26.69, 33.2), (25.16, 27.445)), ((24.82, 26.155), (24.53, 24.845), (24.29, 23.536)), ((24.22, 23.127), (24.03, 22.155), (24.05, 22.145)), ((24.07, 22.136), (26.11, 23.182), (26.93, 23.418)), ((28.5, 23.873), (30.13, 24.091), (31.69, 24.555)), ((32.89, 24.918), (33.97, 25.909), (35.26, 26.018)), ((37.17, 26.182), (38.65, 24.582), (39, 23)))
        self.add_bezier('e5', (40, 19), ((38.32, 17.682), (36.39, 16.236), (34.51, 15.155)), ((32.61, 14.064), (30.76, 12.864), (29.09, 11.5)), ((28.37, 10.909), (27.46, 10.218), (27.04, 9.409)), ((26.24, 7.882), (26.18, 5.509), (26, 4)))
        self.add_contour('c0', 'e0', 'e3', 'e1', 'e4', 'e2', 'e5', closed=True)
