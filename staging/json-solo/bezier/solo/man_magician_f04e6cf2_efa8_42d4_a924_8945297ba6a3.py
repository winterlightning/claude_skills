"""Man magician (avatars), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f04e6cf2-efa8-42d4-a924-8945297ba6a3'
SOURCE_PATH = 'icons-json/avatars/man magician_f04e6cf2-efa8-42d4-a924-8945297ba6a3.json'
AUTHOR = 'json_to_solo'

class ManMagicianAvatars(Solo48):
    icon_id = 'man-magician-avatars'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('man', 'magician', 'avatars')

    def build(self):
        self.add_line('sym-e0', (12, 18), (36, 18))
        self.add_line('sym-e1', (4, 24), (12, 25))
        self.add_line('sym-e2', (12, 25), (11, 9))
        self.add_bezier('sym-e3', (11, 9), ((14.582, 8.503), (18.382, 8), (22, 8)))
        self.add_bezier('sym-e4', (22, 8), ((22.409, 8), (22.591, 8), (23, 8)))
        self.add_bezier('sym-e5', (23, 8), ((23.221, 8), (23.779, 8), (24, 8)))
        self.add_bezier('sym-e6', (24, 8), ((24.221, 8), (24.779, 8), (25, 8)))
        self.add_bezier('sym-e7', (25, 8), ((25.409, 8), (25.591, 8), (26, 8)))
        self.add_bezier('sym-e8', (26, 8), ((29.618, 8), (33.418, 8.503), (37, 9)))
        self.add_line('sym-e9', (37, 9), (36, 25))
        self.add_line('sym-e10', (36, 25), (44, 24))
        self.add_bezier('sym-e11', (24, 25), ((20.054, 25), (15.915, 25.329), (12, 25)))
        self.add_line('sym-e12', (12, 25), (13, 31))
        self.add_bezier('sym-e13', (13, 31), ((13.191, 32.238), (13.464, 33.846), (14, 35)))
        self.add_bezier('sym-e14', (14, 35), ((15.509, 38.267), (19.182, 40), (23, 40)))
        self.add_bezier('sym-e15', (23, 40), ((23.082, 40), (22.918, 40), (23, 40)))
        self.add_bezier('sym-e16', (23, 40), ((23.172, 40), (23.827, 40), (24, 40)))
        self.add_bezier('sym-e17', (24, 40), ((24.173, 40), (24.828, 40), (25, 40)))
        self.add_bezier('sym-e18', (25, 40), ((25.082, 40), (24.918, 40), (25, 40)))
        self.add_bezier('sym-e19', (25, 40), ((28.818, 40), (32.491, 38.267), (34, 35)))
        self.add_bezier('sym-e20', (34, 35), ((34.536, 33.846), (34.809, 32.238), (35, 31)))
        self.add_line('sym-e21', (35, 31), (36, 25))
        self.add_bezier('sym-e22', (36, 25), ((32.085, 25.329), (27.946, 25), (24, 25)))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c2', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', closed=True)
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
