"""Shipment (delivery), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a2c341f-4bcd-442f-bcb0-58b566bc0857'
SOURCE_PATH = 'icons-json/delivery/shipment_8a2c341f-4bcd-442f-bcb0-58b566bc0857.json'
AUTHOR = 'json_to_solo'

class Shipment8a2c341f(Solo48):
    icon_id = 'shipment-8a2c341f'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'delivery'
    aliases = ()
    keywords = ('shipment', 'delivery')

    def build(self):
        self.add_line('e0', (30, 35), (29, 35))
        self.add_line('e1', (9, 35), (6, 35))
        self.add_line('e2', (4, 33), (4, 10))
        self.add_line('e3', (6, 8), (27, 8))
        self.add_line('e4', (29, 10), (29, 13))
        self.add_line('e5', (39, 35), (42, 35))
        self.add_line('e6', (44, 33), (44, 24))
        self.add_line('e7', (44, 23), (39, 14))
        self.add_line('e8', (37, 13), (29, 13))
        self.add_line('e9', (19, 35), (29, 35))
        self.add_line('e10', (29, 35), (29, 13))
        self.add_arc('e11-top', (30, 35), (40, 35), radius_x=5)
        self.add_arc('e11-bottom', (40, 35), (30, 35), radius_x=5)
        self.add_bezier('e12', (9, 34), ((9.991, 29.97), (14.564, 28.64), (17.227, 31.86)), ((17.982, 32.77), (18.727, 33.84), (19, 35)))
        self.add_bezier('e13', (9, 35), ((8.973, 37.9), (10.936, 39.99), (13.682, 39.99)), ((13.834, 39.99), (13.995, 40), (14.147, 40)), ((14.15, 40), (14.152, 40), (14.155, 40)), ((14.255, 40), (14.355, 39.98), (14.464, 39.98)), ((16.182, 39.98), (17.736, 38.67), (18.3, 36.9)), ((18.482, 36.31), (18.945, 35.6), (19, 35)))
        self.add_bezier('e14', (6, 35), ((4.8, 34.37), (4.536, 34.3), (4, 33)))
        self.add_bezier('e15', (4, 10), ((4.3, 9.28), (4.545, 8.59), (5.245, 8.18)), ((5.436, 8.07), (5.818, 8.1), (6, 8)))
        self.add_bezier('e16', (27, 8), ((28.227, 8.56), (28.5, 8.69), (29, 10)))
        self.add_bezier('e17', (42, 35), ((43.2, 34.46), (43.527, 34.28), (44, 33)))
        self.add_bezier('e18', (44, 24), ((44, 23.67), (44, 23.33), (44, 23)))
        self.add_bezier('e19', (39, 14), ((38.609, 13.35), (37.609, 13.2), (37, 13)))
        self.add_contour('c0', 'e12')
        self.add_contour('c1', 'e13')
        self.add_contour('c2', 'e0')
        self.add_contour('c3', 'e1', 'e14', 'e2', 'e15', 'e3', 'e16', 'e4')
        self.add_contour('c4', 'e5', 'e17', 'e6', 'e18', 'e7', 'e19', 'e8')
        self.add_contour('c5', 'e9')
        self.add_contour('c6', 'e10')
        self.add_contour('e11', 'e11-top', 'e11-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c2', 'e11')
        self.relate('connect', 'c4', 'e11')
