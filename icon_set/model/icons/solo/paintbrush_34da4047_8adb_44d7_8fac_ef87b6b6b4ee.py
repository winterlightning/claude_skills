"""Paintbrush (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '34da4047-8adb-44d7-8fac-ef87b6b6b4ee'
SOURCE_PATH = 'icons-json/symbol/paintbrush_34da4047-8adb-44d7-8fac-ef87b6b6b4ee.json'
AUTHOR = 'json_to_solo'

class PaintbrushSymbol(Solo48):
    icon_id = 'paintbrush-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('paintbrush', 'symbol')

    def build(self):
        self.add_line('e0', (11, 33), (10, 37))
        self.add_line('e1', (19, 29), (20, 31))
        self.add_line('e2', (20, 22), (39, 6))
        self.add_line('e3', (42, 9), (27, 30))
        self.add_bezier('e4', (19, 29), ((18.125, 28.656), (17.373, 28.189), (16.424, 28.181)), ((13.863, 28.14), (11.491, 30.554), (11, 33)))
        self.add_bezier('e5', (10, 37), ((9.73, 38.334), (8.675, 39.488), (7.62, 40.225)), ((7.362, 40.41), (6, 41.198), (6, 41.277)), ((6, 41.278), (6, 41.279), (6, 41.28)), ((6.311, 41.37), (6.622, 41.46), (6.933, 41.542)), ((7.98, 41.845), (9.158, 41.992), (10.255, 41.992)), ((10.351, 41.992), (10.44, 42), (10.536, 42)), ((10.538, 42), (10.539, 42), (10.541, 42)), ((10.835, 42), (11.122, 41.992), (11.416, 41.992)), ((15.974, 41.992), (21.194, 38.555), (20.785, 33.499)), ((20.695, 32.444), (20.401, 31.974), (20, 31)))
        self.add_bezier('e6', (19, 29), ((18.108, 26.873), (17.725, 24.843), (19.001, 22.74)), ((19.255, 22.331), (19.624, 22.311), (20, 22)))
        self.add_bezier('e7', (39, 6), ((39.213, 6), (39.145, 6.008), (39.357, 6.008)), ((39.578, 6.008), (39.815, 6), (40.045, 6)), ((40.315, 6), (40.585, 6), (40.846, 6)), ((41.264, 6), (42, 6.785), (42, 7.186)), ((42, 7.538), (41.984, 7.882), (41.984, 8.225)), ((41.984, 8.365), (41.992, 8.504), (41.992, 8.643)), ((41.992, 8.716), (42, 8.782), (42, 8.855)), ((42, 8.995), (42, 8.861), (42, 9)))
        self.add_bezier('e8', (27, 30), ((26.673, 30.458), (26.365, 30.537), (25.882, 30.807)), ((23.853, 31.928), (21.98, 31.916), (20, 31)))
        self.add_contour('c0', 'e4', 'e0', 'e5')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e6', 'e2', 'e7', 'e3', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
