"""Shield (protection), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ee28756e-a560-4166-b776-2aebcbfcabaa'
SOURCE_PATH = 'pictographic-primitives/protection/shield_ee28756e-a560-4166-b776-2aebcbfcabaa.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ShieldEe28756e(Solo48):
    icon_id = 'shield-ee28756e'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('shield', 'protection')

    def build(self):
        self.add_line('e0', (38, 7), (32, 5))
        self.add_line('e1', (16, 6), (10, 8))
        self.add_line('e2', (8, 9), (8, 25))
        self.add_line('e3', (40, 26), (40, 8))
        self.add_line('e4', (40, 8), (38, 7))
        self.add_bezier('e5', (32, 5), ((30.358, 4.555), (27.545, 4.018), (25.861, 4.018)), ((25.67, 4.018), (25.488, 4), (25.297, 4)), ((25.294, 4), (25.291, 4), (25.288, 4)), ((25.145, 4), (24.994, 4.018), (24.851, 4.018)), ((23.865, 4.018), (22.855, 4.255), (21.886, 4.436)), ((19.781, 4.827), (18.055, 5.364), (16, 6)))
        self.add_bezier('e6', (10, 8), ((9.512, 8.155), (8.531, 7.664), (8.168, 8.173)), ((8.118, 8.3), (8.059, 8.873), (8, 9)))
        self.add_bezier('e7', (8, 25), ((8, 25.036), (8.008, 24.991), (8.008, 25.027)), ((8.008, 26.336), (8.396, 27.727), (8.733, 28.973)), ((10.299, 34.745), (14.072, 38.427), (18.669, 41.482)), ((19.966, 42.345), (22.257, 43.991), (23.806, 43.991)), ((23.839, 43.991), (23.873, 44), (23.906, 44)), ((23.906, 44), (23.907, 44), (23.907, 44)), ((24.025, 44), (24.143, 43.991), (24.261, 43.991)), ((25.785, 43.991), (28.093, 42.336), (29.44, 41.518)), ((33.878, 38.836), (37.76, 34.655), (39.352, 29.345)), ((39.663, 28.291), (39.983, 27.073), (39.983, 25.955)), ((39.992, 25.909), (39.992, 26.045), (40, 26)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7', 'e3', 'e4', closed=True)
