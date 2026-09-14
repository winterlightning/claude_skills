"""Outdoors barn bench (outdoors), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1fd48bb2-3ac8-46c0-a63f-a618a4f6efc3'
SOURCE_PATH = 'icons-json/outdoors/outdoors barn bench_1fd48bb2-3ac8-46c0-a63f-a618a4f6efc3.json'
AUTHOR = 'json_to_solo'

class OutdoorsBarnBenchOutdoors(Solo48):
    icon_id = 'outdoors-barn-bench-outdoors'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('outdoors', 'barn', 'bench')

    def build(self):
        self.add_line('e0', (42, 6), (6, 21))
        self.add_line('e1', (9, 20), (9, 41))
        self.add_line('e2', (10, 42), (42, 42))
        self.add_line('e3', (35, 25), (21, 25))
        self.add_line('e4', (31, 25), (35, 39))
        self.add_line('e5', (39, 32), (17, 32))
        self.add_line('e6', (25, 25), (20, 39))
        self.add_arc('e7', (9, 41), (10, 42), radius_x=41, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c2')
        self.relate('connect', 'c5', 'c2')
