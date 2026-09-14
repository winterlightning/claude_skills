"""Br (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '59fae115-395e-4744-9e31-b1a906596371'
SOURCE_PATH = 'icons-json/symbol/br (text u)_59fae115-395e-4744-9e31-b1a906596371.json'
AUTHOR = 'json_to_solo'

class BrTextUSymbol(Solo48):
    icon_id = 'br-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('br', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (15, 4), (8, 4))
        self.add_line('e1', (8, 4), (8, 27))
        self.add_line('e2', (8, 27), (14, 27))
        self.add_line('e3', (16, 15), (8, 15))
        self.add_line('e4', (32, 13), (32, 27))
        self.add_line('e5', (8, 44), (40, 44))
        self.add_bezier('e6', (14, 27), ((15.32, 27), (16.77, 26.8), (18.06, 26.482)), ((21.21, 25.709), (22.87, 22.973), (22.41, 20.091)), ((22.09, 18.145), (20.8, 16.618), (18.89, 15.745)), ((18.31, 15.482), (17.66, 15.327), (17.05, 15.173)), ((16.82, 15.118), (16.64, 15.073), (16.41, 15.027)), ((16.28, 14.982), (16.14, 14.945), (16, 14.909)), ((16.45, 14.736), (16.95, 14.682), (17.41, 14.5)), ((18.53, 14.082), (19.69, 13.209), (20.3, 12.245)), ((22.83, 8.282), (19.97, 4), (15, 4)))
        self.add_bezier('e7', (40, 13), ((40, 13), (39.99, 13.082), (39.99, 13.082)), ((39.99, 13.018), (39.7, 12.836), (39.65, 12.8)), ((38.64, 12.036), (37.29, 11.682), (36, 12.009)), ((33.62, 12.618), (32.62, 15.045), (32, 17)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e6', closed=True)
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e7')
        self.add_contour('c4', 'e5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c2')
