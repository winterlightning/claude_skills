"""Bendy bus (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '905f945e-0fed-542d-9949-ef5788bbe6c1'
SOURCE_PATH = 'icons-json/transportation/bendy bus_905f945e-0fed-542d-9949-ef5788bbe6c1.json'
AUTHOR = 'json_to_solo'

class BendyBusTransportation(Solo48):
    icon_id = 'bendy-bus-transportation'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('bendy', 'bus', 'transportation')

    def build(self):
        self.add_line('e0', (34, 22), (34, 8))
        self.add_line('e1', (34, 22), (4, 22))
        self.add_line('e2', (4, 30), (4, 12))
        self.add_line('e3', (8, 8), (39, 8))
        self.add_line('e4', (43, 13), (44, 20))
        self.add_line('e5', (41, 35), (39, 35))
        self.add_line('e6', (16, 35), (32, 35))
        self.add_line('e7', (23, 8), (23, 22))
        self.add_line('e8', (13, 8), (13, 22))
        self.add_arc('e9-top', (8, 35), (16, 35), radius_x=4, radius_y=5)
        self.add_arc('e9-bottom', (16, 35), (8, 35), radius_x=4, radius_y=5)
        self.add_arc('e10-top', (32, 35), (40, 35), radius_x=4, radius_y=5)
        self.add_arc('e10-bottom', (40, 35), (32, 35), radius_x=4, radius_y=5)
        self.add_arc('e11-1', (44, 25), (41, 25), radius_x=15)
        self.add_line('e11-2', (41, 25), (34, 22))
        self.add_arc('e12-1', (9, 35), (6, 35), radius_x=12, sweep=False)
        self.add_arc('e12-2', (6, 35), (4, 33), radius_x=2)
        self.add_line('e12-3', (4, 33), (4, 30))
        self.add_arc('e13-1', (4, 12), (5, 9), radius_x=5)
        self.add_arc('e13-2', (5, 9), (7, 8), radius_x=3)
        self.add_arc('e13-3', (7, 8), (8, 8), radius_x=8, sweep=False)
        self.add_line('e14-1', (39, 8), (42, 9))
        self.add_arc('e14-2', (42, 9), (43, 13), radius_x=9)
        self.add_line('e15-1', (44, 20), (43, 34))
        self.add_arc('e15-2', (43, 34), (41, 35), radius_x=2)
        self.add_line('e16', (32, 35), (33, 33))
        self.add_contour('c0', 'e11-1', 'e11-2')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e12-1', 'e12-2', 'e12-3', 'e2', 'e13-1', 'e13-2', 'e13-3', 'e3', 'e14-1', 'e14-2', 'e4', 'e15-1', 'e15-2', 'e5')
        self.add_contour('c4', 'e6', 'e16')
        self.add_contour('c5', 'e7')
        self.add_contour('c6', 'e8')
        self.add_contour('e10', 'e10-top', 'e10-bottom', closed=True)
        self.add_contour('e9', 'e9-top', 'e9-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'e9')
        self.relate('connect', 'c3', 'e10')
        self.relate('connect', 'c4', 'e9')
        self.relate('connect', 'c4', 'e10')
        self.relate('connect', 'c4', 'e10')
        self.relate('connect', 'c5', 'c3')
        self.relate('connect', 'c5', 'c2')
        self.relate('connect', 'c6', 'c3')
        self.relate('connect', 'c6', 'c2')
