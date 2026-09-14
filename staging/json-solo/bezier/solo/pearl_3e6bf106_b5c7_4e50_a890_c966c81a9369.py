"""Pearl (products), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e6bf106-b5c7-4e50-a890-c966c81a9369'
SOURCE_PATH = 'icons-json/products/pearl_3e6bf106-b5c7-4e50-a890-c966c81a9369.json'
AUTHOR = 'json_to_solo'

class PearlProducts(Solo48):
    icon_id = 'pearl-products'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'products'
    aliases = ()
    keywords = ('pearl', 'products')

    def build(self):
        self.add_arc('sym-e0', (19, 25), (29, 25), radius_x=5)
        self.add_arc('sym-e1', (29, 25), (19, 25), radius_x=5)
        self.add_bezier('sym-e2', (24, 44), ((23.767, 44), (23.231, 44), (23, 44)))
        self.add_bezier('sym-e3', (23, 44), ((18.385, 44), (14.276, 42.6), (11, 39)))
        self.add_bezier('sym-e4', (11, 39), ((10.486, 38.445), (8, 35.718), (8, 35)))
        self.add_bezier('sym-e5', (8, 35), ((8, 34.509), (8, 33.491), (8, 33)))
        self.add_bezier('sym-e6', (8, 33), ((9.002, 33.527), (9.931, 34.636), (11, 35)))
        self.add_bezier('sym-e7', (11, 35), ((12.954, 35.664), (14.971, 35.782), (17, 36)))
        self.add_bezier('sym-e8', (17, 36), ((19.317, 36.252), (21.698, 36), (24, 36)))
        self.add_bezier('sym-e9', (24, 36), ((26.302, 36), (28.683, 36.252), (31, 36)))
        self.add_bezier('sym-e10', (31, 36), ((33.029, 35.782), (35.046, 35.664), (37, 35)))
        self.add_bezier('sym-e11', (37, 35), ((38.069, 34.636), (38.998, 33.527), (40, 33)))
        self.add_bezier('sym-e12', (40, 33), ((40, 33.491), (40, 34.509), (40, 35)))
        self.add_bezier('sym-e13', (40, 35), ((40, 35.718), (37.514, 38.445), (37, 39)))
        self.add_bezier('sym-e14', (37, 39), ((33.724, 42.6), (29.615, 44), (25, 44)))
        self.add_bezier('sym-e15', (25, 44), ((24.769, 44), (24.233, 44), (24, 44)))
        self.add_line('sym-e16', (8, 33), (8, 31))
        self.add_bezier('sym-e17', (8, 31), ((8.051, 30.855), (8, 31.145), (8, 31)))
        self.add_bezier('sym-e18', (8, 31), ((8.741, 29.645), (12.552, 28.264), (14, 28)))
        self.add_line('sym-e19', (14, 28), (19, 27))
        self.add_line('sym-e20', (19, 27), (12, 22))
        self.add_bezier('sym-e21', (12, 22), ((10.274, 20.836), (8, 18.355), (8, 16)))
        self.add_bezier('sym-e22', (8, 16), ((8, 15.927), (8, 15.064), (8, 15)))
        self.add_bezier('sym-e23', (8, 15), ((8, 14.927), (8, 15.064), (8, 15)))
        self.add_bezier('sym-e24', (8, 15), ((8, 14.155), (8.688, 13.755), (9, 13)))
        self.add_bezier('sym-e25', (9, 13), ((10.027, 10.445), (11.398, 7.782), (14, 7)))
        self.add_bezier('sym-e26', (14, 7), ((14.707, 6.791), (15.276, 6.936), (16, 7)))
        self.add_bezier('sym-e27', (16, 7), ((16.312, 7.027), (16.806, 7.064), (17, 7)))
        self.add_bezier('sym-e28', (17, 7), ((17.017, 6.991), (18.789, 6.155), (19, 6)))
        self.add_bezier('sym-e29', (19, 6), ((20.255, 5.045), (21.451, 4), (23, 4)))
        self.add_bezier('sym-e30', (23, 4), ((23.067, 4), (23.933, 4), (24, 4)))
        self.add_bezier('sym-e31', (24, 4), ((24.142, 4), (23.86, 4), (24, 4)))
        self.add_bezier('sym-e32', (24, 4), ((24.14, 4), (23.858, 4), (24, 4)))
        self.add_bezier('sym-e33', (24, 4), ((24.067, 4), (24.933, 4), (25, 4)))
        self.add_bezier('sym-e34', (25, 4), ((26.549, 4), (27.745, 5.045), (29, 6)))
        self.add_bezier('sym-e35', (29, 6), ((29.211, 6.155), (30.983, 6.991), (31, 7)))
        self.add_bezier('sym-e36', (31, 7), ((31.194, 7.064), (31.688, 7.027), (32, 7)))
        self.add_bezier('sym-e37', (32, 7), ((32.724, 6.936), (33.293, 6.791), (34, 7)))
        self.add_bezier('sym-e38', (34, 7), ((36.602, 7.782), (37.973, 10.445), (39, 13)))
        self.add_bezier('sym-e39', (39, 13), ((39.312, 13.755), (40, 14.155), (40, 15)))
        self.add_bezier('sym-e40', (40, 15), ((40, 15.064), (40, 14.927), (40, 15)))
        self.add_bezier('sym-e41', (40, 15), ((40, 15.064), (40, 15.927), (40, 16)))
        self.add_bezier('sym-e42', (40, 16), ((40, 18.355), (37.726, 20.836), (36, 22)))
        self.add_line('sym-e43', (36, 22), (29, 27))
        self.add_line('sym-e44', (29, 27), (34, 28))
        self.add_bezier('sym-e45', (34, 28), ((35.448, 28.264), (39.259, 29.645), (40, 31)))
        self.add_bezier('sym-e46', (40, 31), ((40, 31.145), (39.949, 30.855), (40, 31)))
        self.add_line('sym-e47', (40, 31), (40, 33))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
        self.add_contour('sym-c2', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36', 'sym-e37', 'sym-e38', 'sym-e39', 'sym-e40', 'sym-e41', 'sym-e42', 'sym-e43', 'sym-e44', 'sym-e45', 'sym-e46', 'sym-e47')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
