"""Man construction (avatars), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e34e75b6-7322-4658-bc40-c90c4e98051e'
SOURCE_PATH = 'icons-json/avatars/man construction_e34e75b6-7322-4658-bc40-c90c4e98051e.json'
AUTHOR = 'json_to_solo'

class ManConstructionAvatars(Solo48):
    icon_id = 'man-construction-avatars'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('man', 'construction', 'avatars')

    def build(self):
        self.add_line('sym-e0', (26, 23), (22, 23))
        self.add_line('sym-e1', (22, 23), (17, 9))
        self.add_bezier('sym-e2', (17, 9), ((15.74, 9.957), (15.113, 10.863), (14, 12)))
        self.add_bezier('sym-e3', (14, 12), ((10.842, 15.232), (9.622, 18.713), (9, 23)))
        self.add_line('sym-e4', (9, 23), (6, 23))
        self.add_line('sym-e5', (42, 23), (39, 23))
        self.add_bezier('sym-e6', (39, 23), ((38.378, 18.713), (37.158, 15.232), (34, 12)))
        self.add_bezier('sym-e7', (34, 12), ((32.887, 10.863), (32.26, 9.957), (31, 9)))
        self.add_line('sym-e8', (31, 9), (26, 23))
        self.add_line('sym-e9', (26, 23), (39, 23))
        self.add_line('sym-e10', (39, 23), (39, 28))
        self.add_bezier('sym-e11', (39, 28), ((39, 29.178), (38.344, 30.887), (38, 32)))
        self.add_bezier('sym-e12', (38, 32), ((36.151, 37.907), (30.308, 42), (24, 42)))
        self.add_bezier('sym-e13', (24, 42), ((23.91, 42), (24.09, 42), (24, 42)))
        self.add_bezier('sym-e14', (24, 42), ((23.954, 42), (24.047, 42), (24, 42)))
        self.add_bezier('sym-e15', (24, 42), ((23.953, 42), (24.046, 42), (24, 42)))
        self.add_bezier('sym-e16', (24, 42), ((23.91, 42), (24.09, 42), (24, 42)))
        self.add_bezier('sym-e17', (24, 42), ((17.692, 42), (11.849, 37.907), (10, 32)))
        self.add_bezier('sym-e18', (10, 32), ((9.656, 30.887), (9, 29.178), (9, 28)))
        self.add_line('sym-e19', (9, 28), (9, 23))
        self.add_line('sym-e20', (9, 23), (22, 23))
        self.add_bezier('sym-e21', (31, 9), ((31.033, 8.894), (31.049, 8.082), (31, 8)))
        self.add_bezier('sym-e22', (31, 8), ((30.82, 7.697), (29.327, 7.106), (29, 7)))
        self.add_bezier('sym-e23', (29, 7), ((27.928, 6.665), (26.096, 6), (25, 6)))
        self.add_bezier('sym-e24', (25, 6), ((24.91, 6), (24.098, 6), (24, 6)))
        self.add_bezier('sym-e25', (24, 6), ((23.91, 6), (24.09, 6), (24, 6)))
        self.add_bezier('sym-e26', (24, 6), ((23.943, 6), (24.057, 6), (24, 6)))
        self.add_bezier('sym-e27', (24, 6), ((23.943, 6), (24.057, 6), (24, 6)))
        self.add_bezier('sym-e28', (24, 6), ((23.91, 6), (24.09, 6), (24, 6)))
        self.add_bezier('sym-e29', (24, 6), ((23.902, 6), (23.09, 6), (23, 6)))
        self.add_bezier('sym-e30', (23, 6), ((21.904, 6), (20.072, 6.665), (19, 7)))
        self.add_bezier('sym-e31', (19, 7), ((18.673, 7.106), (17.18, 7.697), (17, 8)))
        self.add_bezier('sym-e32', (17, 8), ((16.951, 8.082), (16.967, 8.894), (17, 9)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c1', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20')
        self.add_contour('sym-c2', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
