"""Skull (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bf02abda-c65a-4ff2-af41-3fdc5c490cc7'
SOURCE_PATH = 'icons-json/interface-essential/skull_bf02abda-c65a-4ff2-af41-3fdc5c490cc7.json'
AUTHOR = 'json_to_solo'

class Skull(Solo48):
    icon_id = 'skull'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('skull', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 38), (24, 44))
        self.add_line('e1', (12, 34), (15, 37))
        self.add_line('e2', (15, 37), (15, 40))
        self.add_line('e3', (18, 44), (30, 44))
        self.add_line('e4', (33, 40), (33, 37))
        self.add_bezier('e5', (33, 37), ((33.893, 35.973), (35.192, 34.8), (36.059, 33.745)), ((38.476, 30.8), (39.983, 26.664), (39.983, 22.709)), ((39.992, 22.618), (39.992, 22.518), (40, 22.427)), ((40, 22.424), (40, 22.42), (40, 22.417)), ((40, 22.203), (39.992, 21.997), (39.992, 21.782)), ((39.992, 12.9), (33.263, 4.009), (24.674, 4.009)), ((24.466, 4.009), (24.267, 4), (24.068, 4)), ((24.065, 4), (24.062, 4), (24.059, 4)), ((23.857, 4), (23.663, 4.018), (23.469, 4.018)), ((22.088, 4.018), (20.665, 4.364), (19.352, 4.8)), ((12.699, 7.018), (8.017, 13.955), (8.017, 21.5)), ((8.009, 21.625), (8, 21.759), (8, 21.894)), ((8, 21.896), (8, 21.898), (8, 21.9)), ((8.008, 22.045), (8.008, 22.191), (8.017, 22.336)), ((8.017, 26.145), (9.482, 31.282), (12, 34)))
        self.add_bezier('e6', (15, 40), ((15, 41.473), (16.48, 43.118), (17.491, 43.8)), ((17.684, 43.936), (17.789, 43.9), (18, 44)))
        self.add_bezier('e7', (30, 44), ((30.067, 44), (30.029, 44), (30.097, 44)), ((31.933, 44), (32.512, 41.555), (33, 40)))
        self.add_dot('e8', (32, 20))
        self.add_dot('e9', (16, 20))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e5', 'e1', 'e2', 'e6', 'e3', 'e7', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
