"""Judo athlete man (avatars), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc792bf4-601d-4b62-be0e-ae9f2cb6db06'
SOURCE_PATH = 'icons-json/avatars/judo athlete man_bc792bf4-601d-4b62-be0e-ae9f2cb6db06.json'
AUTHOR = 'json_to_solo'

class JudoAthleteMan(Solo48):
    icon_id = 'judo-athlete-man'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('judo', 'athlete', 'man', 'avatars')

    def build(self):
        self.add_line('e0', (40, 20), (32, 20))
        self.add_bezier('e1', (32, 20), ((28.8, 20), (24.674, 18.755), (21.827, 17.218)), ((21.044, 16.8), (18.055, 14.6), (18.013, 14.6)), ((17.676, 14.973), (17.331, 15.336), (16.994, 15.709)), ((16.463, 16.282), (15.907, 16.827), (15.301, 17.309)), ((13.137, 19.018), (10.535, 19.218), (8, 20)))
        self.add_bezier('e2', (40, 20), ((40, 22.027), (39.992, 24.427), (39.992, 26.455)), ((39.992, 27.8), (39.68, 29.173), (39.377, 30.464)), ((37.642, 37.882), (31.512, 43.991), (24.211, 43.991)), ((24.086, 43.991), (23.954, 44), (23.829, 44)), ((23.827, 44), (23.825, 44), (23.823, 44)), ((23.562, 44), (23.301, 43.991), (23.04, 43.991)), ((14.88, 43.991), (8.017, 34.955), (8.017, 26.473)), ((8.017, 26.055), (8, 25.627), (8, 25.209)), ((8, 23.591), (8, 21.618), (8, 20)))
        self.add_bezier('e3', (40, 20), ((39.789, 18.291), (39.562, 17.055), (38.989, 15.436)), ((36.825, 9.227), (30.947, 4.009), (24.632, 4.009)), ((24.574, 4.009), (24.507, 4), (24.449, 4)), ((24.448, 4), (24.447, 4), (24.446, 4)), ((24.185, 4), (23.924, 4.009), (23.663, 4.009)), ((17.592, 4.009), (12.227, 7.955), (9.558, 13.8)), ((9.162, 14.673), (8, 17.873), (8, 18.736)), ((8, 19.273), (8, 19.455), (8, 20)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
