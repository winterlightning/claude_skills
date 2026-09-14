"""Charging (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'adb38709-2d40-4069-b4f6-36531140d2ed'
SOURCE_PATH = 'icons-json/symbol/charging_adb38709-2d40-4069-b4f6-36531140d2ed.json'
AUTHOR = 'json_to_solo'

class ChargingSymbol(Solo48):
    icon_id = 'charging-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('charging', 'symbol')

    def build(self):
        self.add_line('e0', (8, 27), (8, 40))
        self.add_line('e1', (12, 44), (36, 44))
        self.add_line('e2', (40, 40), (40, 27))
        self.add_line('e3', (8, 27), (40, 27))
        self.add_line('e4', (8, 27), (8, 13))
        self.add_line('e5', (18, 9), (18, 4))
        self.add_line('e6', (18, 4), (30, 4))
        self.add_line('e7', (30, 4), (30, 9))
        self.add_line('e8', (40, 12), (40, 27))
        self.add_bezier('e9', (8, 40), ((8.13, 40.373), (8, 40.6), (8.11, 40.973)), ((8.64, 42.191), (9.96, 43.318), (11.24, 43.864)), ((12.11, 44), (11.22, 43.709), (12, 44)))
        self.add_bezier('e10', (36, 44), ((37.23, 43.582), (35.59, 44), (36.91, 43.873)), ((38.36, 43.336), (40, 41.527), (40, 40)))
        self.add_bezier('e11', (8, 13), ((8, 12.818), (8, 12.718), (8, 12.536)), ((8, 12.009), (8.37, 11.327), (8.7, 10.918)), ((10.73, 8.418), (15.14, 8.836), (18, 9)))
        self.add_bezier('e12', (30, 9), ((32.64, 8.845), (35.6, 8.655), (38.08, 9.764)), ((38.38, 9.9), (40, 10.745), (40, 10.818)), ((40, 11.273), (40, 11.545), (40, 12)))
        self.add_contour('c0', 'e0', 'e9', 'e1', 'e10', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e11', 'e5', 'e6', 'e7', 'e12', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
