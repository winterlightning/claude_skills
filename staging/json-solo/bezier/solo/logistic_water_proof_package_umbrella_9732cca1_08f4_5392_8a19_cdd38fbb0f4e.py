"""Logistic water proof package umbrella (shipping), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9732cca1-08f4-5392-8a19-cdd38fbb0f4e'
SOURCE_PATH = 'icons-json/shipping/logistic water proof package umbrella_9732cca1-08f4-5392-8a19-cdd38fbb0f4e.json'
AUTHOR = 'json_to_solo'

class LogisticWaterProofPackageUmbrellaShipping(Solo48):
    icon_id = 'logistic-water-proof-package-umbrella-shipping'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('logistic', 'water', 'proof', 'package', 'umbrella', 'shipping')

    def build(self):
        self.add_line('e0', (24, 32), (13, 29))
        self.add_line('e1', (13, 29), (24, 25))
        self.add_line('e2', (24, 32), (24, 44))
        self.add_line('e3', (24, 32), (35, 29))
        self.add_line('e4', (35, 29), (24, 25))
        self.add_line('e5', (24, 44), (13, 39))
        self.add_line('e6', (13, 39), (13, 29))
        self.add_line('e7', (24, 44), (35, 39))
        self.add_line('e8', (35, 39), (35, 29))
        self.add_line('e9', (24, 25), (24, 17))
        self.add_line('e10', (24, 4), (24, 6))
        self.add_bezier('e11', (40, 19), ((39.69, 17.755), (39.41, 15.964), (38.84, 14.764)), ((36.33, 9.555), (30.29, 5.755), (24, 5.818)), ((17.81, 5.882), (11.85, 9.482), (9.21, 14.555)), ((8.96, 15.036), (8.6, 15.6), (8.48, 16.127)), ((8.322, 16.87), (8, 17.604), (8, 18.346)), ((8, 18.358), (8.002, 18.37), (8, 18.382)), ((8.82, 17.936), (9.65, 17.482), (10.47, 17.036)), ((11.33, 16.582), (12.39, 16.364), (13.38, 16.336)), ((14.68, 16.309), (16.01, 16.564), (17.08, 17.291)), ((17.39, 17.5), (18.77, 18.782), (18.9, 18.8)), ((18.93, 18.8), (20.16, 17.818), (20.38, 17.691)), ((21.49, 17.018), (22.69, 16.809), (24, 16.727)), ((25.32, 16.645), (26.55, 16.982), (27.62, 17.691)), ((28.14, 18.018), (29.21, 18.836), (29.21, 18.836)), ((30.34, 18.173), (30.86, 17.264), (32.09, 16.782)), ((34.16, 15.973), (36.22, 16.364), (38.13, 17.282)), ((38.33, 17.382), (39.63, 17.991), (39.67, 18.082)), ((39.78, 18.536), (39.89, 18.545), (40, 19)))
        self.add_contour('c0', 'e11')
        self.add_contour('c1', 'e0', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4')
        self.add_contour('c4', 'e5', 'e6')
        self.add_contour('c5', 'e7', 'e8')
        self.add_contour('c6', 'e9')
        self.add_contour('c7', 'e10')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c6', 'c0')
        self.relate('connect', 'c7', 'c0')
