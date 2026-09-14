"""Pets allow (wayfinding), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb4d6c32-3a9f-5788-8ea2-e36095e0f764'
SOURCE_PATH = 'icons-json/wayfinding/pets allow_eb4d6c32-3a9f-5788-8ea2-e36095e0f764.json'
AUTHOR = 'json_to_solo'

class PetsAllowWayfinding(Solo48):
    icon_id = 'pets-allow-wayfinding'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('pets', 'allow', 'wayfinding')

    def build(self):
        self.add_line('e0', (26, 12), (24, 21))
        self.add_line('e1', (22, 22), (10, 22))
        self.add_line('e2', (5, 22), (7, 24))
        self.add_line('e3', (7, 24), (7, 40))
        self.add_line('e4', (7, 40), (11, 40))
        self.add_line('e5', (11, 40), (14, 32))
        self.add_line('e6', (14, 32), (28, 32))
        self.add_line('e7', (28, 32), (30, 40))
        self.add_line('e8', (30, 40), (35, 40))
        self.add_line('e9', (35, 40), (35, 22))
        self.add_line('e10', (35, 22), (39, 22))
        self.add_line('e11', (44, 16), (32, 12))
        self.add_line('e12', (32, 12), (32, 8))
        self.add_bezier('e13', (32, 8), ((31.891, 8), (31.955, 8.008), (31.845, 8.008)), ((29.291, 8.008), (26.518, 9.6), (26, 12)))
        self.add_bezier('e14', (24, 21), ((23.791, 21.968), (22.864, 21.613), (22, 22)))
        self.add_bezier('e15', (10, 22), ((8.364, 22), (6.809, 20.749), (5.773, 19.688)), ((5.382, 19.284), (5.009, 18.863), (4.627, 18.451)), ((4.473, 18.291), (4.373, 18.189), (4.218, 18.029)), ((4.145, 17.954), (4.073, 17.878), (4, 17.811)), ((4, 17.839), (4, 17.868), (4, 17.897)), ((4, 19.688), (4.275, 20.475), (5, 22)))
        self.add_bezier('e16', (39, 22), ((39.409, 22), (40.309, 22.131), (40.673, 21.987)), ((43.109, 21.027), (43.991, 18.349), (43.991, 16.076)), ((43.991, 15.907), (44, 16.168), (44, 16)))
        self.add_contour('c0', 'e13', 'e0', 'e14', 'e1', 'e15', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e16', 'e11', 'e12', closed=True)
