"""Magnetic building toy node (internet), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '85c569db-4bac-5b00-820c-70809dc82800'
SOURCE_PATH = 'icons-json/internet/magnetic building toy node_85c569db-4bac-5b00-820c-70809dc82800.json'
AUTHOR = 'json_to_solo'

class MagneticBuildingToyNodeInternet(Solo48):
    icon_id = 'magnetic-building-toy-node-internet'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'internet'
    aliases = ()
    keywords = ('magnetic', 'building', 'toy', 'node', 'internet')

    def build(self):
        self.add_line('e0', (35, 35), (31, 29))
        self.add_line('e1', (29, 17), (35, 13))
        self.add_line('e2', (17, 19), (13, 13))
        self.add_line('e3', (19, 31), (13, 35))
        self.add_arc('e4-top', (34, 38), (42, 38), radius_x=4)
        self.add_arc('e4-bottom', (42, 38), (34, 38), radius_x=4)
        self.add_arc('e5-top', (16, 24), (32, 24), radius_x=8)
        self.add_arc('e5-bottom', (32, 24), (16, 24), radius_x=8)
        self.add_line('e6-1', (35, 13), (34, 9))
        self.add_arc('e6-2', (34, 9), (38, 6), radius_x=5)
        self.add_arc('e6-3', (38, 6), (42, 10), radius_x=4)
        self.add_arc('e6-4', (42, 10), (39, 14), radius_x=5)
        self.add_arc('e6-5', (39, 14), (35, 13), radius_x=4)
        self.add_arc('e7-1', (13, 13), (10, 6), radius_x=5, sweep=False)
        self.add_arc('e7-2', (10, 6), (6, 10), radius_x=4, sweep=False)
        self.add_arc('e7-3', (6, 10), (9, 14), radius_x=5, sweep=False)
        self.add_arc('e7-4', (9, 14), (13, 13), radius_x=4, sweep=False)
        self.add_arc('e8-1', (13, 35), (10, 42), radius_x=5)
        self.add_arc('e8-2', (10, 42), (6, 38), radius_x=4)
        self.add_arc('e8-3', (6, 38), (9, 34), radius_x=5)
        self.add_arc('e8-4', (9, 34), (13, 35), radius_x=4)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e7-1', 'e7-2', 'e7-3', 'e7-4', closed=True)
        self.add_contour('c4', 'e3', 'e8-1', 'e8-2', 'e8-3', 'e8-4')
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c0', 'e5')
        self.relate('connect', 'c1', 'e5')
        self.relate('connect', 'c2', 'e5')
        self.relate('connect', 'c4', 'e5')
