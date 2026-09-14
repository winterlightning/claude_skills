"""Headphones (audio), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2d504cf2-ccfb-4d8e-aadb-8ee57a7202fa'
SOURCE_PATH = 'icons-json/audio/headphones_2d504cf2-ccfb-4d8e-aadb-8ee57a7202fa.json'
AUTHOR = 'json_to_solo'

class Headphones2d504cf2(Solo48):
    icon_id = 'headphones-2d504cf2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('headphones', 'audio')

    def build(self):
        self.add_line('e0', (42, 29), (40, 28))
        self.add_line('e1', (40, 28), (35, 28))
        self.add_line('e2', (34, 29), (34, 40))
        self.add_line('e3', (35, 42), (40, 42))
        self.add_line('e4', (42, 40), (42, 29))
        self.add_line('e5', (42, 28), (42, 22))
        self.add_line('e6', (6, 22), (6, 28))
        self.add_line('e7', (6, 31), (6, 40))
        self.add_line('e8', (8, 42), (13, 42))
        self.add_line('e9', (14, 40), (14, 29))
        self.add_line('e10', (13, 28), (8, 28))
        self.add_bezier('e11', (40, 28), ((39.73, 28), (40.27, 28), (40, 28)))
        self.add_bezier('e12', (35, 28), ((33.928, 28.123), (34.728, 28.255), (34, 29)))
        self.add_bezier('e13', (34, 40), ((34.458, 41.006), (34.026, 41.534), (35, 42)))
        self.add_bezier('e14', (40, 42), ((40.925, 41.697), (41.992, 40.977), (41.992, 39.758)), ((41.992, 39.725), (42, 39.685), (42, 39.652)), ((42, 39.619), (42, 40.033), (42, 40)))
        self.add_bezier('e15', (42, 29), ((42, 28.73), (42, 28.27), (42, 28)))
        self.add_bezier('e16', (42, 22), ((42, 20.707), (41.517, 18.772), (41.084, 17.561)), ((38.703, 10.958), (31.756, 6.008), (24.704, 6.008)), ((24.615, 6.008), (24.519, 6), (24.43, 6)), ((24.428, 6), (24.427, 6), (24.425, 6)), ((23.984, 6), (23.534, 6.008), (23.092, 6.008)), ((15.843, 6.008), (8.97, 11.277), (6.704, 18.052)), ((6.344, 19.124), (6, 20.871), (6, 22)))
        self.add_bezier('e17', (6, 28), ((6, 28.27), (6, 28.73), (6, 29)))
        self.add_bezier('e18', (6, 40), ((6, 40.041), (6.008, 39.627), (6.008, 39.668)), ((6.008, 40.773), (7.235, 41.984), (8.348, 41.984)), ((8.381, 41.992), (7.967, 41.992), (8, 42)))
        self.add_bezier('e19', (13, 42), ((13.99, 41.534), (13.55, 41.023), (14, 40)))
        self.add_bezier('e20', (14, 29), ((13.313, 28.272), (13.941, 28.115), (13, 28)))
        self.add_bezier('e21', (8, 28), ((7.575, 28), (7.268, 28.189), (6.892, 28.402)), ((6.589, 28.574), (6.295, 28.737), (6, 28.909)), ((6, 29.457), (6, 30.452), (6, 31)))
        self.add_contour('c0', 'e0', 'e11', 'e1', 'e12', 'e2', 'e13', 'e3', 'e14', 'e4', closed=True)
        self.add_contour('c1', 'e15', 'e5', 'e16', 'e6', 'e17')
        self.add_contour('c2', 'e7', 'e18', 'e8', 'e19', 'e9', 'e20', 'e10', 'e21', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c2')
