"""Armchair (furnitures), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '049cac05-52fa-5b8f-9a6e-d5ee4caeceb0'
SOURCE_PATH = 'icons-json/furnitures/armchair_049cac05-52fa-5b8f-9a6e-d5ee4caeceb0.json'
AUTHOR = 'json_to_solo'

class ArmchairFurnitures(Solo48):
    icon_id = 'armchair-furnitures'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('armchair', 'furnitures')

    def build(self):
        self.add_line('e0', (35, 39), (13, 39))
        self.add_line('e1', (14, 42), (14, 39))
        self.add_line('e2', (34, 42), (34, 39))
        self.add_bezier('e3', (38, 33), ((36.601, 31.445), (35.029, 30.333), (33, 29.727)), ((27.085, 27.968), (20.924, 28.017), (15, 29.727)), ((13.085, 30.284), (12.17, 31.421), (11, 33)))
        self.add_bezier('e4', (38, 33), ((38.327, 35.839), (38.813, 39), (35, 39)))
        self.add_bezier('e5', (13, 39), ((9.204, 39), (10.476, 35.536), (11, 33)))
        self.add_bezier('e6', (38, 33), ((40.291, 32.313), (42, 31.126), (42, 28.451)), ((42, 28.449), (42, 28.447), (42, 28.445)), ((42, 28.316), (41.992, 28.195), (41.984, 28.066)), ((41.984, 25.726), (40.257, 23.763), (38.015, 23.272)), ((37.426, 23.141), (36.638, 23.008), (36, 23)))
        self.add_bezier('e7', (36, 23), ((36.425, 20.873), (37.41, 18.682), (37.083, 16.489)), ((36.183, 10.304), (30.341, 6.008), (24.262, 6.008)), ((24.189, 6.008), (24.109, 6), (24.036, 6)), ((24.035, 6), (24.034, 6), (24.033, 6)), ((23.967, 6), (23.902, 6.008), (23.836, 6.008)), ((18.559, 6.008), (13.053, 9.387), (11.4, 14.542)), ((10.484, 17.397), (11.427, 20.161), (12, 23)))
        self.add_bezier('e8', (36, 23), ((32.875, 23.974), (31.904, 26.915), (33, 30)))
        self.add_bezier('e9', (15, 30), ((15.155, 27.014), (15.254, 24.172), (11.727, 23.182)), ((11.498, 23.116), (11.122, 23.19), (10.876, 23.198)), ((9.019, 23.28), (7.767, 24.311), (6.769, 25.808)), ((6.409, 26.348), (6.008, 27.076), (6.008, 27.739)), ((6, 27.804), (6, 27.868), (6, 27.932)), ((6, 27.933), (6, 27.934), (6, 27.935)), ((6, 28.001), (6, 28.058), (6.008, 28.124)), ((6.008, 28.77), (6.286, 29.359), (6.605, 29.899)), ((7.636, 31.666), (9.11, 32.329), (11, 33)))
        self.add_contour('c0', 'e3')
        self.add_contour('c1', 'e4', 'e0', 'e5')
        self.add_contour('c2', 'e6')
        self.add_contour('c3', 'e7')
        self.add_contour('c4', 'e8')
        self.add_contour('c5', 'e9')
        self.add_contour('c6', 'e1')
        self.add_contour('c7', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c0')
        self.relate('connect', 'c5', 'c0')
        self.relate('connect', 'c6', 'c1')
        self.relate('connect', 'c7', 'c1')
