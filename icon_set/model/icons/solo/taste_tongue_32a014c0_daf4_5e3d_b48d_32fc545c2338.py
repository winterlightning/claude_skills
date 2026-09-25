"""Taste tongue (health), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '32a014c0-daf4-5e3d-b48d-32fc545c2338'
SOURCE_PATH = 'pictographic-primitives/health/taste tongue_32a014c0-daf4-5e3d-b48d-32fc545c2338.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class TasteTongue(Solo48):
    icon_id = 'taste-tongue'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('taste', 'tongue', 'health')

    def build(self):
        # Plan: remove subpixel cubic detours while preserving real contour nodes.
        # Reference: supplied subject and its existing stroke graph.
        self.add_line('e0', (40, 14), (36, 10))
        self.add_line('e1', (24, 19), (24, 31))
        self.add_line('e2', (4, 16), (6, 15))
        self.add_bezier('e3', (37, 18), ((32.436, 16.425), (28.336, 16.954), (24, 19)))
        self.add_bezier('e4', (37, 18), ((37.545, 20.257), (37.355, 22.585), (37.345, 24.893)), ((37.318, 31.149), (35.827, 36.968), (28.7, 39.267)), ((27.527, 39.646), (26.245, 39.992), (24.991, 39.992)), ((24.812, 39.992), (24.633, 40), (24.454, 40)), ((24.127, 40), (23.818, 39.983), (23.5, 39.983)), ((22.273, 39.983), (21.036, 39.705), (19.864, 39.394)), ((18.1, 38.939), (16.364, 38.038), (15.018, 36.901)), ((11.236, 33.726), (10.627, 29.549), (10.609, 25.027)), ((10.6, 22.712), (10.409, 20.257), (11, 18)))
        self.add_bezier('e5', (37, 18), ((38.982, 17.789), (40.555, 17.482), (42.373, 16.699)), ((42.827, 16.505), (44, 15.975), (44, 15.958)), ((44, 15.88), (43.217, 15.561), (43.136, 15.52)), ((42.173, 15.065), (40.773, 14.716), (40, 14)))
        self.add_bezier('e6', (36, 10), ((34.773, 8.863), (32.727, 8.008), (31.027, 8.008)), ((30.83, 8.008), (30.642, 8), (30.446, 8)), ((30.245, 8), (30.045, 8.008), (29.855, 8.008)), ((27.509, 8.008), (25.636, 9.552), (24, 11)))
        self.add_bezier('e7', (24, 19), ((21.145, 17.568), (16.2, 16.387), (13.027, 17.474)), ((12.445, 17.684), (11.582, 17.789), (11, 18)))
        self.add_bezier('e8', (11, 18), ((7.955, 17.545), (6.764, 17.457), (4, 16)))
        self.add_bezier('e9', (6, 15), ((7.245, 14.107), (8.236, 12.884), (9.373, 11.874)), ((11.636, 9.853), (13.591, 8.008), (17, 8.008)), ((17.145, 8.008), (17.291, 8), (17.436, 8)), ((17.655, 8), (17.873, 8.017), (18.091, 8.017)), ((20.382, 8.017), (22.382, 9.611), (24, 11)))
        self.add_contour('c0', 'e3', closed=False)
        self.add_contour('c1', 'e4', closed=False)
        self.add_contour('c2', 'e5', 'e0', 'e6', closed=False)
        self.add_contour('c3', 'e7', closed=False)
        self.add_contour('c4', 'e1', closed=False)
        self.add_contour('c5', 'e8', 'e2', 'e9', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c3', 'c5')
