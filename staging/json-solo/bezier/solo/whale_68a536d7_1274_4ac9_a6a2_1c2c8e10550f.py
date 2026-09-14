"""Whale (animals), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '68a536d7-1274-4ac9-a6a2-1c2c8e10550f'
SOURCE_PATH = 'icons-json/animals/whale_68a536d7-1274-4ac9-a6a2-1c2c8e10550f.json'
AUTHOR = 'json_to_solo'

class Whale(Solo48):
    icon_id = 'whale'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('whale', 'animals')

    def build(self):
        self.add_line('e0', (22, 7), (24, 11))
        self.add_line('e1', (24, 11), (24, 14))
        self.add_line('e2', (24, 11), (25, 9))
        self.add_bezier('e3', (15, 9), ((15.076, 8.482), (14.829, 7.536), (15.023, 7.045)), ((15.537, 5.755), (16.935, 4.009), (18.383, 4.009)), ((18.441, 4.009), (18.499, 4), (18.557, 4)), ((18.558, 4), (18.559, 4), (18.56, 4)), ((18.653, 4), (18.737, 4.009), (18.821, 4.009)), ((20.286, 4.009), (21.225, 5.864), (22, 7)))
        self.add_bezier('e4', (24, 10), ((24, 10.3), (24, 10.709), (24, 11)))
        self.add_bezier('e5', (25, 9), ((25.547, 7.227), (26.787, 4.009), (28.8, 4.009)), ((28.842, 4.009), (28.876, 4), (28.918, 4)), ((29.053, 4), (29.179, 4.009), (29.314, 4.009)), ((30.88, 4.009), (32.396, 5.627), (32.96, 7.082)), ((33.145, 7.555), (32.924, 8.5), (33, 9)))
        self.add_bezier('e6', (27, 44), ((27.48, 43.045), (28.421, 42.055), (28.8, 41.018)), ((29.718, 38.491), (29.916, 35.682), (30, 33)))
        self.add_bezier('e7', (27, 44), ((24.752, 44), (23.248, 44), (21, 44)))
        self.add_bezier('e8', (27, 44), ((27.497, 44), (28.354, 44), (28.851, 44)), ((28.943, 44), (29.011, 43.882), (29.112, 43.864)), ((29.811, 43.718), (30.501, 43.573), (31.175, 43.345)), ((34.695, 42.173), (37.987, 40.055), (39.36, 36.164)), ((39.697, 35.2), (39.983, 34.109), (39.983, 33.073)), ((39.983, 32.836), (40, 32.6), (40, 32.355)), ((40, 31.691), (40, 30.664), (40, 30)))
        self.add_bezier('e9', (30, 33), ((26.067, 33.645), (21.933, 33.618), (18, 33)))
        self.add_bezier('e10', (30, 33), ((33.461, 32.464), (36.8, 31.573), (40, 30)))
        self.add_bezier('e11', (21, 44), ((20.52, 43.073), (19.646, 42.191), (19.276, 41.209)), ((18.299, 38.645), (18.168, 35.727), (18, 33)))
        self.add_bezier('e12', (21, 44), ((20.512, 44), (19.663, 44), (19.175, 44)), ((18.745, 44), (17.465, 43.582), (16.968, 43.436)), ((13.246, 42.291), (9.928, 40.027), (8.581, 35.927)), ((8.269, 34.973), (8.017, 33.864), (8.017, 32.845)), ((8.017, 32.527), (8, 32.218), (8, 31.9)), ((8, 31.391), (8, 30.509), (8, 30)))
        self.add_bezier('e13', (18, 33), ((14.522, 32.445), (11.208, 31.6), (8, 30)))
        self.add_bezier('e14', (24, 14), ((30.964, 14.1), (36.488, 18.082), (38.939, 25.273)), ((39.36, 26.518), (39.587, 27.764), (39.857, 29.045)), ((39.891, 29.227), (40, 29.445), (40, 29.627)), ((40, 29.873), (40, 29.755), (40, 30)))
        self.add_bezier('e15', (24, 14), ((16.968, 14.091), (11.891, 17.745), (9.196, 24.827)), ((8.792, 25.909), (8.008, 28.518), (8.008, 29.727)), ((8.008, 29.782), (8, 29.827), (8, 29.882)), ((8, 30.045), (8, 29.836), (8, 30)))
        self.add_contour('c0', 'e3', 'e0')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e7')
        self.add_contour('c6', 'e8')
        self.add_contour('c7', 'e9')
        self.add_contour('c8', 'e10')
        self.add_contour('c9', 'e11')
        self.add_contour('c10', 'e12')
        self.add_contour('c11', 'e13')
        self.add_contour('c12', 'e14')
        self.add_contour('c13', 'e15')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c12', 'c13')
        self.relate('connect', 'c12', 'c2')
        self.relate('connect', 'c13', 'c2')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c10', 'c5')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c5', 'c9')
        self.relate('connect', 'c12', 'c6')
        self.relate('connect', 'c12', 'c8')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c11', 'c7')
        self.relate('connect', 'c11', 'c9')
        self.relate('connect', 'c7', 'c9')
        self.relate('connect', 'c10', 'c11')
        self.relate('connect', 'c10', 'c13')
        self.relate('connect', 'c11', 'c13')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c3')
