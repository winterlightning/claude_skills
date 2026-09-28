"""Colon (money), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd33e2391-0e74-47bd-bbe9-206ebce84000'
SOURCE_PATH = 'pictographic-primitives/money/colon_d33e2391-0e74-47bd-bbe9-206ebce84000.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Colon(Solo48):
    icon_id = 'colon'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    categories = ('primitives', 'money')
    aliases = ()
    keywords = ('colon', 'money')

    def build(self):
        # Plan: remove subpixel cubic detours while preserving real contour nodes.
        # Reference: supplied subject and its existing stroke graph.
        self.add_bezier('e0', (31, 25), ((33.507, 26.482), (35.333, 27.891), (36.24, 30.136)), ((38.173, 35), (34.44, 41.418), (27.387, 43.345)), ((26.2, 43.673), (24.893, 43.982), (23.587, 43.982)), ((23.387, 43.982), (23.173, 44), (22.973, 44)), ((22.822, 44), (22.678, 43.991), (22.533, 43.991)), ((19.84, 43.991), (17.333, 42.782), (15, 42)))
        self.add_bezier('e1', (33, 5), ((32.573, 5), (32.427, 5), (32, 5)))
        self.add_bezier('e2', (15, 42), ((19.4, 35.827), (25.027, 30.564), (30.667, 24.909)), ((33.853, 21.718), (39.987, 16.055), (39.987, 12.155)), ((39.987, 12.02), (40, 11.877), (40, 11.743)), ((40, 11.664), (39.987, 11.582), (39.987, 11.5)), ((39.987, 8.609), (37.067, 6.082), (33.333, 4.909)), ((32.893, 4.773), (32.813, 5), (32, 5)))
        self.add_bezier('e3', (15, 42), ((11.453, 40.245), (8.027, 37.991), (8.027, 34.809)), ((8.027, 34.691), (8, 34.564), (8, 34.445)), ((8, 34.173), (8.013, 33.905), (8.013, 33.645)), ((8.013, 29.545), (11.92, 25.355), (15, 22)))
        self.add_bezier('e4', (32, 5), ((27.04, 11.136), (20.72, 16.2), (15, 22)))
        self.add_bezier('e5', (32, 5), ((30.2, 4.627), (28.133, 4.009), (26.227, 4.009)), ((26.069, 4.009), (25.912, 4), (25.754, 4)), ((25.547, 4), (25.333, 4.009), (25.12, 4.009)), ((23.227, 4.009), (21.107, 4.482), (19.413, 5.027)), ((12.053, 7.382), (8.947, 13.136), (11.48, 18.291)), ((12.187, 19.718), (13.773, 20.755), (15, 22)))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', closed=False)
        self.add_contour('c3', 'e3', closed=False)
        self.add_contour('c4', 'e4', closed=False)
        self.add_contour('c5', 'e5', closed=False)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
