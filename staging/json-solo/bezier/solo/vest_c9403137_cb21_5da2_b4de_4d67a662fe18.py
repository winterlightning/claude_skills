"""Vest (clothes), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9403137-cb21-5da2-b4de-4d67a662fe18'
SOURCE_PATH = 'icons-json/clothes/vest_c9403137-cb21-5da2-b4de-4d67a662fe18.json'
AUTHOR = 'json_to_solo'

class VestC9403137(Solo48):
    icon_id = 'vest-c9403137'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('vest', 'clothes')

    def build(self):
        self.add_line('e0', (17, 4), (12, 5))
        self.add_line('e1', (12, 5), (12, 9))
        self.add_line('e2', (8, 20), (8, 38))
        self.add_line('e3', (18, 44), (26, 44))
        self.add_line('e4', (28, 44), (35, 43))
        self.add_line('e5', (40, 39), (40, 20))
        self.add_line('e6', (36, 13), (36, 5))
        self.add_line('e7', (36, 5), (31, 4))
        self.add_line('e8', (24, 12), (24, 44))
        self.add_bezier('e9', (12, 9), ((12, 13.682), (12.126, 17.327), (8, 20)))
        self.add_bezier('e10', (8, 38), ((8, 38.455), (8.017, 38.545), (8.017, 39.009)), ((8.017, 43.409), (11.512, 43.436), (14.56, 43.664)), ((15.335, 43.718), (16.118, 43.764), (16.884, 43.836)), ((17.078, 43.855), (17.322, 44), (17.499, 44)), ((17.701, 44), (17.806, 44), (18, 44)))
        self.add_bezier('e11', (26, 44), ((26.842, 44), (27.158, 44), (28, 44)))
        self.add_bezier('e12', (35, 43), ((36.954, 42.736), (39.992, 42.645), (39.992, 39.673)), ((39.992, 39.6), (40, 39.073), (40, 39)))
        self.add_bezier('e13', (40, 20), ((39.924, 19.9), (39.84, 20.164), (39.764, 20.064)), ((39.453, 19.8), (39.023, 19.682), (38.695, 19.427)), ((37.221, 18.282), (36.514, 16.818), (36.118, 14.927)), ((36, 14.355), (36, 13.591), (36, 13)))
        self.add_bezier('e14', (31, 4), ((30.823, 7.645), (29.954, 9.618), (26.745, 11.345)), ((25.996, 11.745), (24.842, 12.218), (24, 12.182)), ((23.629, 12.164), (23.2, 11.991), (22.838, 11.9)), ((20.387, 11.245), (18.114, 9.455), (17.507, 6.691)), ((17.314, 5.827), (17.059, 4.882), (17, 4)))
        self.add_contour('c0', 'e0', 'e1', 'e9', 'e2', 'e10', 'e3', 'e11', 'e4', 'e12', 'e5', 'e13', 'e6', 'e7', 'e14', closed=True)
        self.add_contour('c1', 'e8')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
