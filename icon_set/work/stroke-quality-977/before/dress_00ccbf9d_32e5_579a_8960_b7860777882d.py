"""Dress (clothes), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00ccbf9d-32e5-579a-8960-b7860777882d'
SOURCE_PATH = 'pictographic-primitives/clothes/dress_00ccbf9d-32e5-579a-8960-b7860777882d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Dress(Solo48):
    icon_id = 'dress-00ccbf9d'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('dress', 'clothes')

    def build(self):
        self.add_line('e0', (32, 8), (33, 12))
        self.add_line('e1', (17, 19), (15, 13))
        self.add_line('e2', (15, 11), (16, 8))
        self.add_line('e3', (16, 8), (16, 4))
        self.add_line('e4', (32, 8), (24, 13))
        self.add_line('e5', (24, 13), (16, 8))
        self.add_line('e6', (32, 8), (32, 4))
        self.add_bezier('e7', (33, 12), ((32.77, 13.8), (32.16, 15.691), (31.56, 17.418)), ((31.3, 18.173), (30.69, 19.173), (30.9, 19.982)), ((31.06, 20.6), (31.51, 21.218), (31.81, 21.782)), ((32.49, 23.055), (33.16, 24.327), (33.82, 25.609)), ((35.6, 29.082), (37.2, 32.655), (38.5, 36.3)), ((38.766, 37.043), (40, 39.864), (40, 40.646)), ((40, 40.659), (40, 40.67), (40, 40.682)), ((39.92, 40.709), (39.85, 40.745), (39.77, 40.773)), ((38.81, 41.173), (37.84, 41.545), (36.86, 41.891)), ((33.27, 43.136), (29.28, 43.991), (25.42, 43.991)), ((25.292, 43.991), (25.164, 44), (25.046, 44)), ((25.044, 44), (25.042, 44), (25.04, 44)), ((24.62, 44), (24.2, 43.991), (23.78, 43.991)), ((19.62, 43.991), (15.37, 43.282), (11.45, 42)), ((10.37, 41.645), (9.3, 41.255), (8.24, 40.845)), ((8.16, 40.818), (8.08, 40.782), (8, 40.755)), ((8, 40.754), (8, 40.754), (8, 40.753)), ((8, 40.726), (8.01, 40.7), (8.02, 40.673)), ((8.02, 40.173), (8.34, 39.555), (8.49, 39.082)), ((9.04, 37.409), (9.62, 35.727), (10.3, 34.1)), ((12.37, 29.155), (14.74, 23.873), (17, 19)))
        self.add_bezier('e8', (15, 13), ((14.84, 12.491), (14.86, 11.5), (15, 11)))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8', 'e2', 'e3')
        self.add_contour('c1', 'e4', 'e5')
        self.add_contour('c2', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
