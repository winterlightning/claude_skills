"""Dating lips (romance), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8077f630-37ed-409c-b63e-a8b7f1a3579d'
SOURCE_PATH = 'icons-json/romance/dating lips_8077f630-37ed-409c-b63e-a8b7f1a3579d.json'
AUTHOR = 'json_to_solo'

class DatingLipsRomance(Solo48):
    icon_id = 'dating-lips-romance'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    aliases = ()
    keywords = ('dating', 'lips', 'romance')

    def build(self):
        self.add_line('sym-e0', (4, 23), (19, 23))
        self.add_bezier('sym-e1', (19, 23), ((19.273, 23), (18.736, 22.898), (19, 23)))
        self.add_line('sym-e2', (19, 23), (23, 24))
        self.add_bezier('sym-e3', (23, 24), ((23.261, 24.101), (23.68, 24), (24, 24)))
        self.add_bezier('sym-e4', (24, 24), ((24.003, 24), (23.997, 24), (24, 24)))
        self.add_bezier('sym-e5', (24, 24), ((24.32, 24), (24.739, 24.101), (25, 24)))
        self.add_line('sym-e6', (25, 24), (29, 23))
        self.add_bezier('sym-e7', (29, 23), ((29.264, 22.898), (28.727, 23), (29, 23)))
        self.add_line('sym-e8', (29, 23), (44, 23))
        self.add_line('sym-e9', (44, 23), (40, 30))
        self.add_bezier('sym-e10', (40, 30), ((39.327, 31.353), (38.9, 32.098), (38, 33)))
        self.add_bezier('sym-e11', (38, 33), ((34.1, 36.898), (29.673, 40), (25, 40)))
        self.add_bezier('sym-e12', (25, 40), ((24.927, 40), (24.073, 40), (24, 40)))
        self.add_bezier('sym-e13', (24, 40), ((23.893, 40), (24.107, 40), (24, 40)))
        self.add_bezier('sym-e14', (24, 40), ((23.946, 40), (24.054, 40), (24, 40)))
        self.add_bezier('sym-e15', (24, 40), ((23.946, 40), (24.054, 40), (24, 40)))
        self.add_bezier('sym-e16', (24, 40), ((23.893, 40), (24.107, 40), (24, 40)))
        self.add_bezier('sym-e17', (24, 40), ((23.927, 40), (23.073, 40), (23, 40)))
        self.add_bezier('sym-e18', (23, 40), ((18.327, 40), (13.9, 36.898), (10, 33)))
        self.add_bezier('sym-e19', (10, 33), ((9.1, 32.098), (8.673, 31.353), (8, 30)))
        self.add_line('sym-e20', (8, 30), (4, 23))
        self.add_line('sym-e21', (4, 23), (9, 15))
        self.add_bezier('sym-e22', (9, 15), ((10.936, 11.902), (15.182, 8), (18, 8)))
        self.add_bezier('sym-e23', (18, 8), ((18.109, 8), (17.891, 8), (18, 8)))
        self.add_bezier('sym-e24', (18, 8), ((19.209, 8), (21, 8.938), (22, 10)))
        self.add_bezier('sym-e25', (22, 10), ((22.754, 10.795), (23.045, 11.961), (24, 12)))
        self.add_bezier('sym-e26', (24, 12), ((24.955, 11.961), (25.246, 10.795), (26, 10)))
        self.add_bezier('sym-e27', (26, 10), ((27, 8.938), (28.791, 8), (30, 8)))
        self.add_bezier('sym-e28', (30, 8), ((30.109, 8), (29.891, 8), (30, 8)))
        self.add_bezier('sym-e29', (30, 8), ((32.818, 8), (37.064, 11.902), (39, 15)))
        self.add_line('sym-e30', (39, 15), (44, 23))
        self.add_bezier('sym-e31', (24, 24), ((23.997, 24), (24.003, 24), (24, 24)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30')
        self.add_contour('sym-c1', 'sym-e31', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
