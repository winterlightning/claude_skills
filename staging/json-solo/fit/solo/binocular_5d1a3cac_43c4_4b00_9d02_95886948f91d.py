"""Binocular (outdoors), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5d1a3cac-43c4-4b00-9d02-95886948f91d'
SOURCE_PATH = 'icons-json/outdoors/binocular_5d1a3cac-43c4-4b00-9d02-95886948f91d.json'
AUTHOR = 'json_to_solo'

class BinocularOutdoors(Solo48):
    icon_id = 'binocular-outdoors'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('binocular', 'outdoors')

    def build(self):
        self.add_line('e0', (31, 18), (28, 17))
        self.add_line('e1', (17, 18), (20, 17))
        self.add_line('e2', (26, 32), (24, 32))
        self.add_line('e3', (42, 27), (35, 10))
        self.add_line('e4', (28, 10), (28, 17))
        self.add_line('e5', (28, 17), (24, 17))
        self.add_line('e6', (24, 17), (24, 32))
        self.add_line('e7', (24, 32), (21, 32))
        self.add_line('e8', (20, 17), (20, 10))
        self.add_line('e9', (13, 9), (7, 26))
        self.add_arc('e10-top', (26, 32), (44, 32), radius_x=9, radius_y=8)
        self.add_arc('e10-bottom', (44, 32), (26, 32), radius_x=9, radius_y=8)
        self.add_line('e11-1', (35, 10), (34, 9))
        self.add_arc('e11-2', (34, 9), (30, 8), radius_x=14, sweep=False)
        self.add_arc('e11-3', (30, 8), (28, 10), radius_x=2, sweep=False)
        self.add_arc('e12', (7, 26), (21, 32), radius_x=9)
        self.add_line('e13', (24, 17), (20, 17))
        self.add_arc('e14-1', (20, 10), (18, 8), radius_x=2, sweep=False)
        self.add_line('e14-2', (18, 8), (13, 9))
        self.add_arc('e15-1', (7, 26), (4, 32), radius_x=9, sweep=False)
        self.add_arc('e15-2', (4, 32), (7, 38), radius_x=8, sweep=False)
        self.add_line('e15-3', (7, 38), (13, 40))
        self.add_arc('e15-4', (13, 40), (21, 32), radius_x=8, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e11-1', 'e11-2', 'e11-3', 'e4')
        self.add_contour('c4', 'e12')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e13')
        self.add_contour('c8', 'e7')
        self.add_contour('c9', 'e8', 'e14-1', 'e14-2', 'e9', 'e15-1', 'e15-2', 'e15-3', 'e15-4')
        self.add_contour('e10', 'e10-top', 'e10-bottom', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c1', 'c7')
        self.relate('connect', 'c1', 'c9')
        self.relate('connect', 'c7', 'c9')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c2', 'c8')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c4', 'c9')
        self.relate('connect', 'c8', 'c9')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c2', 'e10')
        self.relate('connect', 'c3', 'e10')
        self.relate('connect', 'c4', 'c9')
