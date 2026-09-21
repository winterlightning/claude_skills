"""Ho (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e5643e3-1aed-4c98-8075-d06df0b03f59'
SOURCE_PATH = 'icons-json/symbol/ho (text u)_3e5643e3-1aed-4c98-8075-d06df0b03f59.json'
AUTHOR = 'json_to_solo'

class HoTextU(Solo48):
    icon_id = 'ho-text-u'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('ho', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (8, 27))
        self.add_line('e1', (21, 15), (8, 15))
        self.add_line('e2', (21, 27), (21, 4))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_bezier('e4', (32, 12), ((31.242, 12.455), (31.04, 13.091), (30.56, 13.9)), ((28.749, 16.909), (29.078, 23.455), (31.916, 25.582)), ((32.749, 26.2), (33.76, 26.455), (34.762, 26.455)), ((38.24, 26.455), (39.983, 23.182), (39.983, 19.755)), ((39.983, 19.6), (40, 19.445), (40, 19.291)), ((40, 19.073), (39.983, 18.864), (39.983, 18.645)), ((39.983, 14.073), (36.219, 10.682), (32, 12)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', closed=True)
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c0')
