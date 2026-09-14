"""Binocular (outdoors), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e11', (35, 10), ((34.682, 9.663), (34.291, 8.893), (33.845, 8.682)), ((33.264, 8.396), (30.618, 8.008), (29.927, 8.008)), ((29.865, 8.008), (29.811, 8), (29.757, 8)), ((29.756, 8), (29.755, 8), (29.755, 8)), ((29.7, 8), (29.655, 8.008), (29.609, 8.008)), ((28.5, 8.008), (28.355, 9.208), (28, 10)))
        self.add_bezier('e12', (7, 26), ((8.8, 25.318), (10.373, 24.177), (12.382, 24.244)), ((17.5, 24.421), (20.745, 27.301), (21, 32)))
        self.add_bezier('e13', (24, 17), ((22.791, 17), (21.2, 16.722), (20, 17)))
        self.add_bezier('e14', (20, 10), ((19.5, 9.04), (19.373, 8.017), (18.073, 8.017)), ((17.927, 8.017), (17.782, 8), (17.636, 8)), ((17.464, 8), (17.291, 8.017), (17.118, 8.017)), ((16.745, 8.017), (16.364, 8.017), (15.982, 8.017)), ((15.682, 8.017), (15.373, 8), (15.064, 8)), ((14.955, 8), (14.845, 8.017), (14.736, 8.017)), ((13.982, 8.017), (13.509, 8.571), (13, 9)))
        self.add_bezier('e15', (7, 26), ((5.664, 27.676), (4.009, 29.221), (4.009, 31.402)), ((4.009, 31.584), (4, 31.767), (4, 31.949)), ((4, 31.952), (4, 31.955), (4, 31.958)), ((4, 32.076), (4.009, 32.202), (4.009, 32.32)), ((4.009, 36.312), (8.055, 39.992), (12.327, 39.992)), ((12.39, 39.992), (12.453, 40), (12.515, 40)), ((12.516, 40), (12.517, 40), (12.518, 40)), ((12.645, 40), (12.782, 39.992), (12.909, 39.992)), ((16.045, 39.992), (19.391, 38.029), (20.6, 35.335)), ((21.027, 34.375), (20.882, 33.019), (21, 32)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e11', 'e4')
        self.add_contour('c4', 'e12')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e13')
        self.add_contour('c8', 'e7')
        self.add_contour('c9', 'e8', 'e14', 'e9', 'e15')
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
