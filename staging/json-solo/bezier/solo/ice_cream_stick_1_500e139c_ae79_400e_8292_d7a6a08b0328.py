"""Ice cream stick 1 (food), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '500e139c-ae79-400e-8292-d7a6a08b0328'
SOURCE_PATH = 'icons-json/food/ice cream stick 1_500e139c-ae79-400e-8292-d7a6a08b0328.json'
AUTHOR = 'json_to_solo'

class IceCreamStick1Food(Solo48):
    icon_id = 'ice-cream-stick-1-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('ice', 'cream', 'stick', 'food')

    def build(self):
        self.add_line('e0', (24, 44), (24, 33))
        self.add_line('e1', (8, 15), (40, 15))
        self.add_line('e2', (8, 15), (8, 31))
        self.add_line('e3', (10, 33), (24, 33))
        self.add_line('e4', (40, 15), (40, 31))
        self.add_line('e5', (38, 33), (24, 33))
        self.add_bezier('e6', (8, 31), ((8.123, 31.191), (8.086, 31.664), (8.222, 31.855)), ((8.763, 32.564), (9.089, 32.673), (10, 33)))
        self.add_bezier('e7', (8, 15), ((8, 14.709), (8.025, 14.327), (8.025, 14.036)), ((8.025, 13.355), (8.357, 12.609), (8.603, 11.964)), ((10.351, 7.573), (16.788, 4.009), (23.003, 4.009)), ((23.185, 4.009), (23.367, 4), (23.548, 4)), ((23.551, 4), (23.554, 4), (23.557, 4)), ((24.025, 4), (24.48, 4.009), (24.948, 4.009)), ((31.397, 4.009), (37.711, 7.745), (39.446, 12.264)), ((39.655, 12.8), (39.975, 13.491), (39.975, 14.055)), ((39.988, 14.118), (39.988, 14.182), (40, 14.255)), ((40, 14.473), (40, 14.782), (40, 15)))
        self.add_bezier('e8', (40, 31), ((39.188, 32.218), (39.686, 32.373), (38, 33)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e6', 'e3')
        self.add_contour('c3', 'e7')
        self.add_contour('c4', 'e4', 'e8', 'e5')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
