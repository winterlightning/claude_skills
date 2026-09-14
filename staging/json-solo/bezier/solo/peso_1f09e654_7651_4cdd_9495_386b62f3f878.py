"""Peso (money), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f09e654-7651-4cdd-9495-386b62f3f878'
SOURCE_PATH = 'icons-json/money/peso_1f09e654-7651-4cdd-9495-386b62f3f878.json'
AUTHOR = 'json_to_solo'

class Peso1f09e654(Solo48):
    icon_id = 'peso-1f09e654'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('peso', 'money')

    def build(self):
        self.add_line('e0', (8, 22), (14, 22))
        self.add_line('e1', (14, 22), (14, 44))
        self.add_line('e2', (14, 22), (32, 22))
        self.add_line('e3', (30, 4), (14, 4))
        self.add_line('e4', (14, 4), (14, 22))
        self.add_bezier('e5', (32, 22), ((36.194, 22), (39.992, 18.518), (39.992, 14.036)), ((39.992, 13.866), (40, 13.687), (40, 13.517)), ((40, 13.514), (40, 13.512), (40, 13.509)), ((40, 8.891), (36.051, 5.591), (32.303, 4.464)), ((31.545, 4.236), (30.792, 4), (30, 4)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e5', 'e3', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
