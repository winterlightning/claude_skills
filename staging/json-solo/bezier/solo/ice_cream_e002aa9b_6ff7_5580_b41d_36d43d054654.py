"""Ice cream (food), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e002aa9b-6ff7-5580-b41d-36d43d054654'
SOURCE_PATH = 'icons-json/food/ice cream_e002aa9b-6ff7-5580-b41d-36d43d054654.json'
AUTHOR = 'json_to_solo'

class IceCreamFood(Solo48):
    icon_id = 'ice-cream-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('ice', 'cream', 'food')

    def build(self):
        self.add_bezier('sym-e0', (14, 25), ((14.468, 24.955), (15.508, 25.1), (16, 25)))
        self.add_bezier('sym-e1', (16, 25), ((16.517, 24.891), (17.458, 23.827), (18, 24)))
        self.add_bezier('sym-e2', (18, 24), ((20.006, 24.636), (21.785, 25.018), (24, 25)))
        self.add_bezier('sym-e3', (24, 25), ((24.045, 25), (23.955, 25), (24, 25)))
        self.add_bezier('sym-e4', (24, 25), ((24.045, 25), (23.955, 25), (24, 25)))
        self.add_bezier('sym-e5', (24, 25), ((26.215, 25.018), (27.994, 24.636), (30, 24)))
        self.add_bezier('sym-e6', (30, 24), ((30.542, 23.827), (31.483, 24.891), (32, 25)))
        self.add_bezier('sym-e7', (32, 25), ((32.492, 25.1), (33.532, 24.955), (34, 25)))
        self.add_bezier('sym-e8', (34, 25), ((32.708, 27.891), (31.243, 31.091), (30, 34)))
        self.add_bezier('sym-e9', (30, 34), ((29.151, 35.991), (27.935, 38.036), (27, 40)))
        self.add_bezier('sym-e10', (27, 40), ((26.618, 40.773), (26.48, 42.464), (26, 43)))
        self.add_bezier('sym-e11', (26, 43), ((25.601, 43.425), (24.674, 44), (24, 44)))
        self.add_bezier('sym-e12', (24, 44), ((23.326, 44), (22.399, 43.425), (22, 43)))
        self.add_bezier('sym-e13', (22, 43), ((21.52, 42.464), (21.382, 40.773), (21, 40)))
        self.add_bezier('sym-e14', (21, 40), ((20.065, 38.036), (18.849, 35.991), (18, 34)))
        self.add_bezier('sym-e15', (18, 34), ((16.757, 31.091), (15.292, 27.891), (14, 25)))
        self.add_bezier('sym-e16', (14, 25), ((13.212, 24.891), (12.738, 24.255), (12, 24)))
        self.add_bezier('sym-e17', (12, 24), ((10.055, 23.345), (8, 21.655), (8, 20)))
        self.add_bezier('sym-e18', (8, 20), ((8, 19.882), (8.012, 20.118), (8, 20)))
        self.add_bezier('sym-e19', (8, 20), ((8.012, 19.882), (8, 20.127), (8, 20)))
        self.add_bezier('sym-e20', (8, 20), ((8, 19.1), (8.286, 17.7), (9, 17)))
        self.add_bezier('sym-e21', (9, 17), ((9.16, 16.845), (9.926, 17.173), (10, 17)))
        self.add_bezier('sym-e22', (10, 17), ((10.16, 16.627), (10.025, 15.4), (10, 15)))
        self.add_bezier('sym-e23', (10, 15), ((9.938, 13.918), (9.68, 13.055), (10, 12)))
        self.add_bezier('sym-e24', (10, 12), ((11.305, 7.791), (17.043, 4), (23, 4)))
        self.add_bezier('sym-e25', (23, 4), ((23.222, 4), (23.791, 4), (24, 4)))
        self.add_bezier('sym-e26', (24, 4), ((24.097, 4), (23.901, 4), (24, 4)))
        self.add_bezier('sym-e27', (24, 4), ((24.099, 4), (23.903, 4), (24, 4)))
        self.add_bezier('sym-e28', (24, 4), ((24.209, 4), (24.778, 4), (25, 4)))
        self.add_bezier('sym-e29', (25, 4), ((30.957, 4), (36.695, 7.791), (38, 12)))
        self.add_bezier('sym-e30', (38, 12), ((38.32, 13.055), (38.062, 13.918), (38, 15)))
        self.add_bezier('sym-e31', (38, 15), ((37.975, 15.4), (37.84, 16.627), (38, 17)))
        self.add_bezier('sym-e32', (38, 17), ((38.074, 17.173), (38.84, 16.845), (39, 17)))
        self.add_bezier('sym-e33', (39, 17), ((39.714, 17.7), (40, 19.1), (40, 20)))
        self.add_bezier('sym-e34', (40, 20), ((40, 20.127), (39.988, 19.882), (40, 20)))
        self.add_bezier('sym-e35', (40, 20), ((39.988, 20.118), (40, 19.882), (40, 20)))
        self.add_bezier('sym-e36', (40, 20), ((40, 21.655), (37.945, 23.345), (36, 24)))
        self.add_bezier('sym-e37', (36, 24), ((35.262, 24.255), (34.788, 24.891), (34, 25)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36', 'sym-e37')
