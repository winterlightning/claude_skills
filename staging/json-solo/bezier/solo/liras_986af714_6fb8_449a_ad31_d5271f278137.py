"""Liras (money), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '986af714-6fb8-449a-ad31-d5271f278137'
SOURCE_PATH = 'icons-json/money/liras_986af714-6fb8-449a-ad31-d5271f278137.json'
AUTHOR = 'json_to_solo'

class LirasMoney(Solo48):
    icon_id = 'liras-money'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('liras', 'money')

    def build(self):
        self.add_line('e0', (17, 12), (17, 36))
        self.add_line('e1', (10, 44), (8, 44))
        self.add_line('e2', (9, 19), (30, 19))
        self.add_line('e3', (40, 44), (10, 44))
        self.add_line('e4', (9, 33), (30, 33))
        self.add_bezier('e5', (39, 11), ((38.029, 6.545), (34.016, 4.009), (28.629, 4.009)), ((28.545, 4.009), (28.461, 4), (28.377, 4)), ((28.376, 4), (28.375, 4), (28.373, 4)), ((28.096, 4), (27.829, 4.009), (27.552, 4.009)), ((22.773, 4.009), (18.155, 6.455), (16.992, 10.509)), ((16.896, 10.818), (17, 11.773), (17, 12)))
        self.add_bezier('e6', (17, 36), ((17, 36.109), (16.224, 36.873), (16.171, 37.091)), ((15.221, 40.327), (12.923, 41.882), (10, 44)))
        self.add_contour('c0', 'e5', 'e0', 'e6', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c2', 'c0')
