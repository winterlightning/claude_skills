"""Warp squeeze (design), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'efb3c5db-a644-505f-b7f3-a21fccc2fb30'
SOURCE_PATH = 'icons-json/design/warp squeeze_efb3c5db-a644-505f-b7f3-a21fccc2fb30.json'
AUTHOR = 'json_to_solo'

class WarpSqueezeDesign(Solo48):
    icon_id = 'warp-squeeze-design'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'squeeze', 'design')

    def build(self):
        self.add_bezier('sym-e0', (24, 44), ((23.91, 44), (24.088, 44), (24, 44)))
        self.add_bezier('sym-e1', (24, 44), ((19.638, 44), (14.579, 42.773), (11, 40)))
        self.add_bezier('sym-e2', (11, 40), ((10.276, 39.436), (9.716, 38.582), (9, 38)))
        self.add_bezier('sym-e3', (9, 38), ((8.891, 37.918), (8, 38.127), (8, 38)))
        self.add_bezier('sym-e4', (8, 38), ((8, 37.991), (9.596, 36.291), (10, 36)))
        self.add_bezier('sym-e5', (10, 36), ((11.676, 34.8), (12.931, 33.855), (14, 32)))
        self.add_bezier('sym-e6', (14, 32), ((17.528, 25.9), (15.817, 17.891), (11, 13)))
        self.add_bezier('sym-e7', (11, 13), ((9.989, 11.973), (9.162, 10.791), (8, 10)))
        self.add_bezier('sym-e8', (8, 10), ((8.143, 9.864), (8, 10.118), (8, 10)))
        self.add_bezier('sym-e9', (8, 10), ((9.036, 9.2), (9.897, 8.691), (11, 8)))
        self.add_bezier('sym-e10', (11, 8), ((14.402, 5.873), (19.042, 4), (23, 4)))
        self.add_bezier('sym-e11', (23, 4), ((23.261, 4), (23.739, 4), (24, 4)))
        self.add_bezier('sym-e12', (24, 4), ((24.056, 4), (23.944, 4), (24, 4)))
        self.add_bezier('sym-e13', (24, 4), ((24.056, 4), (23.944, 4), (24, 4)))
        self.add_bezier('sym-e14', (24, 4), ((24.261, 4), (24.739, 4), (25, 4)))
        self.add_bezier('sym-e15', (25, 4), ((28.958, 4), (33.598, 5.873), (37, 8)))
        self.add_bezier('sym-e16', (37, 8), ((38.103, 8.691), (38.964, 9.2), (40, 10)))
        self.add_bezier('sym-e17', (40, 10), ((40, 10.118), (39.857, 9.864), (40, 10)))
        self.add_bezier('sym-e18', (40, 10), ((38.838, 10.791), (38.011, 11.973), (37, 13)))
        self.add_bezier('sym-e19', (37, 13), ((32.183, 17.891), (30.472, 25.9), (34, 32)))
        self.add_bezier('sym-e20', (34, 32), ((35.069, 33.855), (36.324, 34.8), (38, 36)))
        self.add_bezier('sym-e21', (38, 36), ((38.404, 36.291), (40, 37.991), (40, 38)))
        self.add_bezier('sym-e22', (40, 38), ((40, 38.127), (39.109, 37.918), (39, 38)))
        self.add_bezier('sym-e23', (39, 38), ((38.284, 38.582), (37.724, 39.436), (37, 40)))
        self.add_bezier('sym-e24', (37, 40), ((33.421, 42.773), (28.362, 44), (24, 44)))
        self.add_bezier('sym-e25', (24, 44), ((23.912, 44), (24.09, 44), (24, 44)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
