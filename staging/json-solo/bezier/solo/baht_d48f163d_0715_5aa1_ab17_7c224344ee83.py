"""Baht (money), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd48f163d-0715-5aa1-ab17-7c224344ee83'
SOURCE_PATH = 'icons-json/money/baht_d48f163d-0715-5aa1-ab17-7c224344ee83.json'
AUTHOR = 'json_to_solo'

class BahtMoney(Solo48):
    icon_id = 'baht-money'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('baht', 'money')

    def build(self):
        self.add_line('e0', (29, 39), (8, 39))
        self.add_line('e1', (8, 39), (8, 9))
        self.add_line('e2', (8, 9), (28, 9))
        self.add_line('e3', (30, 24), (8, 24))
        self.add_line('e4', (23, 44), (23, 4))
        self.add_bezier('e5', (28, 9), ((36.369, 9), (40, 15.264), (36.628, 20.509)), ((35.618, 21.582), (34.191, 22.391), (32.665, 23.027)), ((31.951, 23.318), (30.154, 23.973), (30.154, 24)), ((30.154, 24), (30.806, 24.191), (31.089, 24.273)), ((32.308, 24.636), (33.526, 24.991), (34.683, 25.436)), ((37.206, 26.4), (39.988, 28.945), (39.988, 31.136)), ((39.988, 31.271), (40, 31.405), (40, 31.539)), ((40, 31.541), (40, 31.543), (40, 31.545)), ((40, 31.745), (39.975, 31.955), (39.975, 32.155)), ((39.975, 32.945), (39.643, 33.7), (39.249, 34.436)), ((37.588, 37.536), (33.48, 39), (29, 39)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e5', closed=True)
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
