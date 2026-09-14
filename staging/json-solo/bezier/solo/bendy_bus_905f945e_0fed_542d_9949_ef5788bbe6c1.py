"""Bendy bus (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e11', (44, 25), ((42.755, 24.988), (41.227, 25.403), (40.018, 24.837)), ((37.991, 23.889), (36.264, 22), (34, 22)))
        self.add_bezier('e12', (9, 35), ((6.745, 35.037), (4.009, 35.766), (4.009, 31.582)), ((4.009, 31.102), (4, 30.48), (4, 30)))
        self.add_bezier('e13', (4, 12), ((4, 11.902), (4, 11.495), (4, 11.397)), ((4, 9.895), (5.227, 8.012), (6.382, 8.012)), ((6.664, 8.012), (6.945, 8), (7.227, 8)), ((7.364, 8), (7.864, 8), (8, 8)))
        self.add_bezier('e14', (39, 8), ((39.082, 8), (39.618, 8.012), (39.691, 8.012)), ((41.882, 8.012), (42.691, 10.465), (43, 13)))
        self.add_bezier('e15', (44, 20), ((44, 20.468), (43.982, 21.243), (43.982, 21.711)), ((43.982, 21.871), (43.982, 22.018), (43.982, 22.166)), ((43.982, 22.412), (44, 22.658), (44, 22.905)), ((44, 23.68), (43.991, 24.455), (44, 25.231)), ((44, 26.092), (43.973, 26.966), (43.982, 27.828)), ((43.982, 29.982), (44, 33.034), (42.618, 34.474)), ((42.264, 34.843), (41.418, 34.84), (41, 35)))
        self.add_bezier('e16', (32, 35), ((32.3, 34.175), (32.7, 33.825), (33, 33)))
        self.add_contour('c0', 'e11')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e12', 'e2', 'e13', 'e3', 'e14', 'e4', 'e15', 'e5')
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
