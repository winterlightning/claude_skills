"""Seat settings (wayfinding), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '07eded86-d9a7-4839-86f2-fdaf9ec4dd8c'
SOURCE_PATH = 'icons-json/wayfinding/seat settings_07eded86-d9a7-4839-86f2-fdaf9ec4dd8c.json'
AUTHOR = 'json_to_solo'

class SeatSettings(Solo48):
    icon_id = 'seat-settings'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('seat', 'settings', 'wayfinding')

    def build(self):
        self.add_line('e0', (42, 23), (35, 16))
        self.add_line('e1', (32, 22), (35, 16))
        self.add_line('e2', (35, 16), (40, 13))
        self.add_line('e3', (40, 13), (29, 8))
        self.add_line('e4', (27, 8), (32, 22))
        self.add_line('e5', (17, 34), (17, 26))
        self.add_line('e6', (17, 16), (15, 8))
        self.add_line('e7', (13, 6), (8, 6))
        self.add_line('e8', (11, 42), (35, 42))
        self.add_bezier('e9', (29, 8), ((28.452, 8), (27.548, 8), (27, 8)))
        self.add_bezier('e10', (17, 26), ((17.319, 23.104), (17.638, 18.864), (17, 16)))
        self.add_bezier('e11', (15, 8), ((14.787, 7.043), (14.092, 6.63), (13.241, 6.172)), ((13.004, 6.049), (13.237, 6.082), (13, 6)))
        self.add_bezier('e12', (8, 6), ((7.836, 6.082), (7.293, 6.057), (7.129, 6.155)), ((6.589, 6.475), (6.008, 7.154), (6.008, 7.808)), ((6.008, 7.873), (6, 7.937), (6, 8.001)), ((6, 8.002), (6, 8.004), (6, 8.005)), ((6, 8.07), (6.008, 8.135), (6.008, 8.201)), ((6.008, 9.003), (6.18, 9.813), (6.237, 10.606)), ((6.401, 12.676), (6.573, 14.755), (6.695, 16.825)), ((7.047, 22.748), (7.391, 28.664), (7.595, 34.595)), ((7.669, 36.854), (7.448, 40.069), (9.526, 41.46)), ((9.919, 41.73), (10.509, 42), (11, 42)))
        self.add_bezier('e13', (35, 42), ((36.636, 42), (37.868, 40.372), (38.367, 39.095)), ((39.333, 36.592), (40.625, 33.753), (37.361, 32.223)), ((35.839, 31.503), (33.025, 32.002), (31.331, 32.108)), ((29.122, 32.247), (26.896, 32.378), (24.704, 32.673)), ((22.012, 33.041), (19.7, 33.681), (17, 34)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e9', 'e4', closed=True)
        self.add_contour('c2', 'e5', 'e10', 'e6', 'e11', 'e7', 'e12', 'e8', 'e13', closed=True)
        self.relate('connect', 'c0', 'c1')
