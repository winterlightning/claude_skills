"""Rand (money), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4458e707-6b88-4e46-8b5b-6a58a4c07dc7'
SOURCE_PATH = 'icons-json/money/rand_4458e707-6b88-4e46-8b5b-6a58a4c07dc7.json'
AUTHOR = 'json_to_solo'

class RandMoney(Solo48):
    icon_id = 'rand-money'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('rand', 'money')

    def build(self):
        self.add_line('e0', (25, 25), (8, 25))
        self.add_line('e1', (8, 44), (8, 26))
        self.add_line('e2', (40, 44), (25, 25))
        self.add_line('e3', (26, 4), (8, 4))
        self.add_line('e4', (8, 4), (8, 26))
        self.add_bezier('e5', (25, 25), ((26.674, 24.827), (28.714, 24.682), (30.326, 24.309)), ((35.889, 23), (39.975, 19.473), (39.975, 15.045)), ((39.975, 14.827), (40, 14.6), (40, 14.373)), ((40, 14.227), (40, 14.073), (39.988, 13.927)), ((39.988, 13.364), (39.766, 12.745), (39.606, 12.191)), ((38.462, 8.245), (34.351, 5.318), (29.095, 4.382)), ((28.258, 4.236), (26.862, 4), (26, 4)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e5', 'e3', 'e4')
        self.relate('connect', 'c0', 'c2')
