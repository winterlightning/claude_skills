"""Wine glass (drinks), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f90eeb6e-787b-5f51-8bb0-0f4ffe811c20'
SOURCE_PATH = 'icons-json/drinks/wine glass_f90eeb6e-787b-5f51-8bb0-0f4ffe811c20.json'
AUTHOR = 'json_to_solo'

class WineGlassDrinks(Solo48):
    icon_id = 'wine-glass-drinks'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('wine', 'glass', 'drinks')

    def build(self):
        self.add_line('e0', (13, 44), (22, 44))
        self.add_line('e1', (24, 44), (24, 29))
        self.add_line('e2', (10, 4), (36, 4))
        self.add_line('e3', (8, 15), (10, 4))
        self.add_bezier('e4', (22, 44), ((22.825, 44), (23.175, 44), (24, 44)), ((24.825, 44), (25.649, 43.982), (26.474, 43.982)), ((29.206, 43.982), (31.926, 43.982), (34.658, 43.982)), ((34.794, 43.991), (34.865, 43.991), (35, 44)))
        self.add_bezier('e5', (36, 4), ((36.111, 4.145), (36.615, 4.236), (36.726, 4.391)), ((37.526, 5.627), (37.785, 7.1), (38.191, 8.427)), ((38.954, 10.955), (39.975, 13.664), (39.975, 16.264)), ((39.975, 16.482), (40, 16.691), (40, 16.909)), ((40, 16.912), (40, 16.916), (40, 16.919)), ((40, 17.134), (39.988, 17.349), (39.988, 17.564)), ((39.988, 18.336), (39.618, 19.2), (39.372, 19.945)), ((37.612, 25.236), (31.2, 28.491), (24, 28.545)), ((17.797, 28.6), (11.815, 26.018), (9.169, 21.827)), ((8.665, 21.045), (8.012, 20), (8.012, 19.109)), ((8.012, 19.045), (8, 18.973), (8, 18.909)), ((8, 17.573), (8, 16.336), (8, 15)))
        self.add_contour('c0', 'e0', 'e4')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e5', 'e3', closed=True)
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c2')
