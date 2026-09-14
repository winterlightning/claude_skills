"""Tracker smartwatch (health), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c47953f-1034-5ce5-9f6c-89467580488b'
SOURCE_PATH = 'icons-json/health/tracker smartwatch_2c47953f-1034-5ce5-9f6c-89467580488b.json'
AUTHOR = 'json_to_solo'

class TrackerSmartwatchHealth(Solo48):
    icon_id = 'tracker-smartwatch-health'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('tracker', 'smartwatch', 'health')

    def build(self):
        self.add_line('e0', (34, 35), (34, 41))
        self.add_line('e1', (29, 44), (19, 44))
        self.add_line('e2', (15, 40), (15, 35))
        self.add_line('e3', (40, 24), (33, 24))
        self.add_line('e4', (33, 24), (28, 29))
        self.add_line('e5', (28, 29), (22, 20))
        self.add_line('e6', (22, 20), (18, 25))
        self.add_line('e7', (18, 25), (8, 25))
        self.add_line('e8', (34, 13), (34, 7))
        self.add_line('e9', (29, 4), (19, 4))
        self.add_line('e10', (15, 7), (15, 13))
        self.add_line('e11', (40, 32), (40, 17))
        self.add_line('e12', (33, 13), (13, 13))
        self.add_line('e13', (8, 18), (8, 31))
        self.add_line('e14', (15, 35), (35, 35))
        self.add_bezier('e15', (34, 41), ((34, 42.727), (31.006, 44), (29, 44)))
        self.add_bezier('e16', (19, 44), ((18.803, 43.991), (18.695, 43.991), (18.498, 43.982)), ((16.8, 43.982), (15.508, 42.736), (15.298, 41.6)), ((15.225, 41.164), (15, 40.418), (15, 40)))
        self.add_bezier('e17', (34, 7), ((34, 5.2), (31.08, 4), (29, 4)))
        self.add_bezier('e18', (19, 4), ((18.877, 4), (18.843, 4.009), (18.72, 4.009)), ((16.849, 4.009), (15, 5.673), (15, 7)))
        self.add_bezier('e19', (40, 17), ((40, 16.9), (40, 16.527), (40, 16.436)), ((40, 13.518), (36.997, 13.082), (33.846, 13.091)), ((31.249, 13.1), (35.855, 13), (33, 13)))
        self.add_bezier('e20', (13, 13), ((10.058, 13), (8.025, 13.845), (8.025, 16.218)), ((8.025, 16.691), (8, 17.527), (8, 18)))
        self.add_bezier('e21', (8, 31), ((8, 31.091), (8.012, 31.464), (8.012, 31.555)), ((8.012, 33.045), (9.575, 34.173), (11.348, 34.691)), ((12.517, 35.036), (13.782, 35), (15, 35)))
        self.add_bezier('e22', (35, 35), ((36.969, 35), (38.757, 33.973), (39.754, 32.755)), ((39.914, 32.573), (39.865, 32.191), (40, 32)))
        self.add_contour('c0', 'e0', 'e15', 'e1', 'e16', 'e2')
        self.add_contour('c1', 'e3', 'e4', 'e5', 'e6', 'e7')
        self.add_contour('c2', 'e8', 'e17', 'e9', 'e18', 'e10')
        self.add_contour('c3', 'e11', 'e19', 'e12', 'e20', 'e13', 'e21', 'e14', 'e22', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c3')
