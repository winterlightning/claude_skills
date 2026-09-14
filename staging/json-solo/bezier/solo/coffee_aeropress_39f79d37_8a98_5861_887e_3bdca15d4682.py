"""Coffee aeropress (drinks), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39f79d37-8a98-5861-887e-3bdca15d4682'
SOURCE_PATH = 'icons-json/drinks/coffee aeropress_39f79d37-8a98-5861-887e-3bdca15d4682.json'
AUTHOR = 'json_to_solo'

class CoffeeAeropressDrinks(Solo48):
    icon_id = 'coffee-aeropress-drinks'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('coffee', 'aeropress', 'drinks')

    def build(self):
        self.add_line('sym-e0', (35, 32), (13, 32))
        self.add_bezier('sym-e1', (13, 32), ((13.005, 31.721), (13, 32.048), (13, 32)))
        self.add_bezier('sym-e2', (13, 32), ((13, 31.904), (13, 31.521), (13, 31)))
        self.add_line('sym-e3', (13, 31), (13, 23))
        self.add_line('sym-e4', (13, 23), (14, 23))
        self.add_line('sym-e5', (14, 23), (34, 23))
        self.add_line('sym-e6', (34, 23), (35, 23))
        self.add_line('sym-e7', (35, 23), (40, 23))
        self.add_line('sym-e8', (13, 23), (8, 23))
        self.add_line('sym-e9', (10, 4), (14, 4))
        self.add_line('sym-e10', (14, 4), (34, 4))
        self.add_line('sym-e11', (34, 4), (38, 4))
        self.add_line('sym-e12', (35, 23), (35, 31))
        self.add_bezier('sym-e13', (35, 31), ((35, 31.521), (35, 31.904), (35, 32)))
        self.add_bezier('sym-e14', (35, 32), ((35, 32.048), (34.995, 31.721), (35, 32)))
        self.add_bezier('sym-e15', (35, 32), ((35.032, 33.836), (36.528, 35.391), (38, 37)))
        self.add_bezier('sym-e16', (38, 37), ((38.656, 37.745), (40, 39.127), (40, 40)))
        self.add_bezier('sym-e17', (40, 40), ((40, 40.055), (40, 39.945), (40, 40)))
        self.add_bezier('sym-e18', (40, 40), ((40, 40.055), (40, 39.945), (40, 40)))
        self.add_bezier('sym-e19', (40, 40), ((40, 41.973), (36.688, 43.436), (34, 44)))
        self.add_line('sym-e20', (34, 44), (24, 44))
        self.add_line('sym-e21', (24, 44), (14, 44))
        self.add_bezier('sym-e22', (14, 44), ((11.312, 43.436), (8, 41.973), (8, 40)))
        self.add_bezier('sym-e23', (8, 40), ((8, 39.945), (8, 40.055), (8, 40)))
        self.add_bezier('sym-e24', (8, 40), ((8, 39.945), (8, 40.055), (8, 40)))
        self.add_bezier('sym-e25', (8, 40), ((8, 39.127), (9.344, 37.745), (10, 37)))
        self.add_bezier('sym-e26', (10, 37), ((11.472, 35.391), (12.968, 33.836), (13, 32)))
        self.add_line('sym-e27', (34, 23), (34, 4))
        self.add_line('sym-e28', (14, 23), (14, 4))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c1', 'sym-e8')
        self.add_contour('sym-c2', 'sym-e9', 'sym-e10', 'sym-e11')
        self.add_contour('sym-c3', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26')
        self.add_contour('sym-c4', 'sym-e27')
        self.add_contour('sym-c5', 'sym-e28')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c5')
        self.relate('connect', 'sym-c2', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c2', 'sym-c5')
        self.relate('connect', 'sym-c2', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
