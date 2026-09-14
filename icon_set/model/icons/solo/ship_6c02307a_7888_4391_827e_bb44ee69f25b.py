"""Ship (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6c02307a-7888-4391-827e-bb44ee69f25b'
SOURCE_PATH = 'icons-json/transportation/ship_6c02307a-7888-4391-827e-bb44ee69f25b.json'
AUTHOR = 'json_to_solo'

class Ship(Solo48):
    icon_id = 'ship'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('ship', 'transportation')

    def build(self):
        self.add_line('e0', (39, 28), (9, 28))
        self.add_line('e1', (29, 39), (32, 37))
        self.add_line('e2', (13, 37), (9, 40))
        self.add_line('e3', (19, 28), (27, 27))
        self.add_bezier('e4', (33, 37), ((34.418, 35.678), (35.955, 33.928), (37.027, 32.337)), ((37.927, 31.006), (38.082, 29.305), (39, 28)))
        self.add_bezier('e5', (9, 28), ((9.545, 31.865), (10.236, 34.069), (13, 37)))
        self.add_bezier('e6', (13, 37), ((14.536, 36.714), (16.264, 36.893), (17.818, 37.255)), ((20.6, 37.92), (22.673, 40), (25.673, 40)), ((26.618, 40), (28.236, 39.531), (29, 39)))
        self.add_bezier('e7', (9, 40), ((7.482, 40), (5.518, 40), (4, 40)))
        self.add_bezier('e8', (32, 37), ((33.836, 37.118), (35.891, 36.8), (37.573, 37.549)), ((39.491, 38.392), (41.345, 39.992), (43.573, 39.992)), ((43.627, 39.992), (43.673, 40), (43.727, 40)), ((43.818, 40), (43.909, 40), (44, 40)))
        self.add_bezier('e9', (27, 27), ((29.464, 26.427), (32.236, 24.135), (34.255, 22.703)), ((34.927, 22.232), (35.573, 21.735), (36.182, 21.204)), ((36.245, 21.162), (36.3, 21.12), (36.364, 21.078)), ((34.245, 14.484), (29.636, 9.937), (22.227, 8.539)), ((21.118, 8.332), (19.647, 8), (18.717, 8)), ((18.702, 8), (18.687, 8), (18.673, 8)), ((18.691, 8.067), (18.709, 8.135), (18.727, 8.211)), ((18.773, 8.413), (18.827, 8.623), (18.873, 8.834)), ((18.991, 9.339), (19.109, 9.836), (19.218, 10.341)), ((19.573, 11.882), (19.9, 13.432), (20.182, 14.989)), ((20.573, 17.069), (20.845, 19.259), (20.664, 21.381)), ((20.464, 23.672), (19.436, 25.735), (19, 28)))
        self.add_contour('c0', 'e4', 'e0', 'e5')
        self.add_contour('c1', 'e6', 'e1')
        self.add_contour('c2', 'e2', 'e7')
        self.add_contour('c3', 'e8')
        self.add_contour('c4', 'e3', 'e9', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c4', 'c0')
