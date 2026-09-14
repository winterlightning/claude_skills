"""Exotic shorthair (pets), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd474f15d-d178-4b58-a27b-c0ae5030abcd'
SOURCE_PATH = 'icons-json/pets/exotic shorthair_d474f15d-d178-4b58-a27b-c0ae5030abcd.json'
AUTHOR = 'json_to_solo'

class ExoticShorthairPets(Solo48):
    icon_id = 'exotic-shorthair-pets'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('exotic', 'shorthair', 'pets')

    def build(self):
        self.add_line('e0', (4, 40), (4, 28))
        self.add_line('e1', (19, 14), (19, 10))
        self.add_line('e2', (29, 14), (29, 10))
        self.add_line('e3', (44, 40), (44, 28))
        self.add_line('e4', (12, 10), (16, 11))
        self.add_bezier('e5', (12, 26), ((9.355, 27.802), (7.264, 27.975), (4, 28)))
        self.add_bezier('e6', (35, 26), ((37.764, 27.895), (40.627, 27.924), (44, 28)))
        self.add_bezier('e7', (4, 28), ((4, 26.375), (4.018, 24.96), (4.018, 23.343)), ((4.018, 21.482), (4.545, 19.537), (5.436, 17.878)), ((5.618, 17.533), (7, 15.764), (7.009, 15.714)), ((7.027, 15.638), (6.227, 14.063), (6.127, 13.794)), ((5.664, 12.497), (5.518, 11.133), (5.6, 9.777)), ((5.609, 9.592), (5.818, 8), (6.027, 8)), ((7.727, 8), (9.055, 8.758), (10.582, 9.305)), ((11.109, 9.491), (11.464, 9.874), (12, 10)))
        self.add_bezier('e8', (16, 11), ((17.209, 10.52), (17.7, 10.202), (19, 10)))
        self.add_bezier('e9', (44, 28), ((44, 27.672), (43.982, 27.554), (43.982, 27.217)), ((43.982, 24.514), (44, 21.634), (43.027, 19.065)), ((42.727, 18.324), (42.345, 17.592), (41.864, 16.935)), ((41.618, 16.598), (41.064, 16.126), (40.918, 15.756)), ((40.864, 15.621), (41.136, 15.242), (41.2, 15.116)), ((41.6, 14.307), (41.918, 13.457), (42.091, 12.581)), ((42.345, 11.242), (42.364, 9.92), (42.091, 8.589)), ((42.055, 8.429), (42.109, 8.168), (41.964, 8.076)), ((41.718, 8.051), (41.482, 8.034), (41.236, 8.008)), ((41.192, 8.008), (41.138, 8), (41.093, 8)), ((41.092, 8), (41.092, 8), (41.091, 8)), ((40.955, 8), (40.818, 8.017), (40.682, 8.017)), ((38.873, 8.017), (36.473, 8.918), (34.9, 9.718)), ((34.6, 9.878), (32.9, 10.939), (32.782, 10.964)), ((32.564, 11.015), (31.873, 10.602), (31.664, 10.518)), ((30.664, 10.122), (30.064, 10.227), (29, 10)))
        self.add_bezier('e10', (19, 10), ((22.064, 9.579), (25.936, 9.562), (29, 10)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e3')
        self.add_contour('c6', 'e7', 'e4', 'e8')
        self.add_contour('c7', 'e9')
        self.add_contour('c8', 'e10')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c2', 'c8')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c3', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c5', 'c7')
