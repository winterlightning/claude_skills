"""Google maps logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa153f72-36bd-4f55-b299-fbbd01a43d85'
SOURCE_PATH = 'pictographic-primitives/logos/google maps logo_fa153f72-36bd-4f55-b299-fbbd01a43d85.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class GoogleMapsLogo(Solo48):
    icon_id = 'google-maps-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('google', 'maps', 'logo', 'logos')

    def build(self):
        # Plan: remove subpixel cubic detours while preserving real contour nodes.
        # Reference: supplied subject and its existing stroke graph.
        self.add_line('e0', (17, 35), (29, 23))
        self.add_line('e1', (17, 35), (11, 28))
        self.add_line('e2', (17, 35), (22, 43))
        self.add_line('e3', (26, 14), (11, 28))
        self.add_line('e4', (26, 14), (34, 7))
        self.add_bezier('e5', (29, 23), ((29.59, 22.418), (29.99, 21.7), (30.2, 20.945)), ((31.06, 17.809), (28.33, 15.836), (26, 14)))
        self.add_bezier('e6', (22, 43), ((22.5, 43.318), (23.16, 43.982), (23.82, 43.982)), ((23.899, 43.991), (23.968, 44), (24.046, 44)), ((26.09, 44), (27, 41.6), (27.81, 40.282)), ((28.29, 39.518), (28.78, 38.764), (29.28, 38.009)), ((33.23, 31.955), (39.99, 27.4), (39.99, 19.773)), ((39.99, 19.701), (40, 19.63), (40, 19.558)), ((40, 19.273), (39.99, 18.991), (39.99, 18.709)), ((39.99, 15.5), (38.67, 11.955), (36.64, 9.345)), ((35.88, 8.373), (34.95, 7.836), (34, 7)))
        self.add_bezier('e7', (11, 28), ((10.78, 27.636), (10.56, 26.909), (10.34, 26.545)), ((9.08, 24.482), (8.01, 22.318), (8.01, 19.909)), ((8.01, 19.802), (8, 19.703), (8, 19.605)), ((8, 19.227), (8.02, 18.855), (8.02, 18.482)), ((8.02, 10.791), (15.38, 4.009), (23.81, 4.009)), ((24.036, 4.009), (24.253, 4), (24.479, 4)), ((24.75, 4), (25.01, 4.018), (25.28, 4.018)), ((28.5, 4.018), (31.35, 5.455), (34, 7)))
        self.add_contour('c0', 'e0', 'e5', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', 'e6', closed=False)
        self.add_contour('c3', 'e3', closed=False)
        self.add_contour('c4', 'e4', closed=False)
        self.add_contour('c5', 'e7', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
