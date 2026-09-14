"""Skull (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b01deac-dd2c-4265-92f5-d17735f0c07e'
SOURCE_PATH = 'icons-json/interface-essential/skull_7b01deac-dd2c-4265-92f5-d17735f0c07e.json'
AUTHOR = 'json_to_solo'

class Skull7b01deac(Solo48):
    icon_id = 'skull-7b01deac'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('skull', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 44), (24, 39))
        self.add_bezier('e1', (14, 44), ((14, 42.127), (14.24, 38.618), (13.676, 36.964)), ((13.229, 35.636), (11.596, 34.136), (10.813, 32.836)), ((9.112, 30.009), (8.017, 26.464), (8.017, 23.064)), ((8.017, 22.894), (8, 22.715), (8, 22.544)), ((8, 22.542), (8, 22.539), (8, 22.536)), ((8, 22.191), (8.017, 21.836), (8.017, 21.491)), ((8.017, 12.691), (15.133, 4.009), (23.469, 4.009)), ((23.503, 4.009), (23.544, 4), (23.577, 4)), ((23.578, 4), (23.578, 4), (23.579, 4)), ((23.924, 4), (24.261, 4.009), (24.606, 4.009)), ((32.994, 4.009), (39.992, 13.091), (39.992, 21.818)), ((39.992, 21.908), (40, 21.988), (40, 22.078)), ((40, 22.079), (40, 22.08), (40, 22.082)), ((40, 22.391), (39.992, 22.691), (39.992, 23)), ((39.992, 26.345), (38.939, 29.927), (37.246, 32.709)), ((36.825, 33.4), (36.379, 34.073), (35.882, 34.709)), ((35.377, 35.355), (34.728, 35.927), (34.417, 36.718)), ((33.777, 38.345), (34, 42.118), (34, 44)))
        self.add_dot('e2', (16, 21))
        self.add_dot('e3', (32, 21))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e0')
