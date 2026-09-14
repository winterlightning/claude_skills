"""Ca (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c402655-e593-48d7-b819-f0043a385dd2'
SOURCE_PATH = 'icons-json/symbol/ca (text u)_8c402655-e593-48d7-b819-f0043a385dd2.json'
AUTHOR = 'json_to_solo'

class CaTextUSymbol(Solo48):
    icon_id = 'ca-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('ca', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 9), (8, 21))
        self.add_line('e1', (40, 27), (40, 23))
        self.add_line('e2', (8, 44), (40, 44))
        self.add_bezier('e3', (19, 8), ((17.973, 5.991), (16.168, 4.009), (13.912, 4.009)), ((13.777, 4.009), (13.642, 4), (13.507, 4)), ((13.506, 4), (13.505, 4), (13.504, 4)), ((13.438, 4), (13.372, 4), (13.305, 4.009)), ((10.813, 4.009), (8.008, 6.391), (8.008, 9.236)), ((8.008, 9.309), (8, 8.927), (8, 9)))
        self.add_bezier('e4', (8, 21), ((8, 24.691), (11.933, 27.2), (14.947, 26.518)), ((16.8, 26.091), (18.099, 24.736), (19, 23)))
        self.add_bezier('e5', (40, 23), ((40, 23), (40, 23.1), (39.992, 23.1)), ((39.992, 23.291), (39.638, 23.673), (39.537, 23.809)), ((38.434, 25.327), (36.808, 26.473), (34.973, 26.509)), ((30.998, 26.582), (27.983, 24.464), (27.916, 19.809)), ((27.865, 16.173), (30.24, 12.745), (33.634, 12.155)), ((35.983, 11.755), (39.992, 13.809), (39.992, 16.755)), ((39.992, 16.836), (40, 16.918), (40, 16.991)), ((40, 19.027), (40, 20.964), (40, 23)))
        self.add_contour('c0', 'e3', 'e0', 'e4')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e5', closed=True)
