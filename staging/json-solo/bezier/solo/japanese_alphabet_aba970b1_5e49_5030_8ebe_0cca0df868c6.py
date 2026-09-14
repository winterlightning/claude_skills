"""Japanese alphabet (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aba970b1-5e49-5030-8ebe-0cca0df868c6'
SOURCE_PATH = 'icons-json/interface-essential/japanese alphabet_aba970b1-5e49-5030-8ebe-0cca0df868c6.json'
AUTHOR = 'json_to_solo'

class JapaneseAlphabetInterfaceEssential(Solo48):
    icon_id = 'japanese-alphabet-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('japanese', 'alphabet', 'interface-essential')

    def build(self):
        self.add_line('e0', (19, 21), (19, 6))
        self.add_line('e1', (35, 41), (31, 42))
        self.add_line('e2', (7, 11), (40, 11))
        self.add_line('e3', (22, 41), (20, 37))
        self.add_bezier('e4', (33, 17), ((29.891, 25.075), (26.945, 31.675), (19.909, 37.091)), ((18.518, 38.163), (16.988, 39.194), (15.376, 39.905)), ((12.136, 41.313), (7.947, 41.517), (6.434, 37.672)), ((6.139, 36.919), (6, 36.027), (6, 35.225)), ((6, 35.225), (6, 35.224), (6, 35.223)), ((6, 35.167), (6.008, 35.118), (6.008, 35.062)), ((6.008, 29.506), (10.786, 24.376), (15.515, 22.045)), ((16.653, 21.48), (17.797, 21.376), (19, 21)))
        self.add_bezier('e5', (20, 37), ((19.763, 35.175), (19.246, 33.45), (19.091, 31.601)), ((18.911, 29.441), (19.05, 27.224), (19.066, 25.064)), ((19.075, 24.475), (18.985, 20.94), (19.091, 20.727)), ((19.173, 20.711), (19.255, 20.686), (19.328, 20.67)), ((19.835, 20.547), (20.343, 20.433), (20.858, 20.326)), ((22.65, 19.942), (24.483, 19.844), (26.315, 19.811)), ((31.773, 19.705), (38.498, 21.194), (41.059, 26.602)), ((41.648, 27.829), (42, 29.228), (42, 30.603)), ((42, 30.605), (42, 30.607), (42, 30.608)), ((42, 30.729), (41.992, 30.85), (41.992, 30.979)), ((41.992, 34.505), (39.987, 37.492), (37.369, 39.668)), ((36.616, 40.29), (35.974, 40.804), (35, 41)))
        self.add_contour('c0', 'e4', 'e0')
        self.add_contour('c1', 'e5', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c1', 'c0')
