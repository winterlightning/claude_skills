"""Database (diagrams), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b3ea511d-2f05-474a-944e-587c5423980b'
SOURCE_PATH = 'icons-json/diagrams/database_b3ea511d-2f05-474a-944e-587c5423980b.json'
AUTHOR = 'json_to_solo'

class DatabaseB3ea511d(Solo48):
    icon_id = 'database-b3ea511d'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    aliases = ()
    keywords = ('database', 'diagrams')

    def build(self):
        self.add_bezier('sym-e0', (40, 25), ((39.225, 25.7), (38.901, 26.482), (38, 27)))
        self.add_bezier('sym-e1', (38, 27), ((36.274, 28), (33.912, 28.6), (32, 29)))
        self.add_bezier('sym-e2', (32, 29), ((29.348, 29.558), (26.671, 30), (24, 30)))
        self.add_bezier('sym-e3', (24, 30), ((21.329, 30), (18.652, 29.558), (16, 29)))
        self.add_bezier('sym-e4', (16, 29), ((14.088, 28.6), (11.726, 28), (10, 27)))
        self.add_bezier('sym-e5', (10, 27), ((9.099, 26.482), (8.775, 25.7), (8, 25)))
        self.add_line('sym-e6', (8, 25), (8, 11))
        self.add_line('sym-e7', (8, 11), (8, 9))
        self.add_bezier('sym-e8', (8, 9), ((8.236, 8.509), (8.621, 8.418), (9, 8)))
        self.add_bezier('sym-e9', (9, 8), ((11.846, 4.936), (19.034, 4), (23, 4)))
        self.add_bezier('sym-e10', (23, 4), ((23.211, 4), (22.789, 4), (23, 4)))
        self.add_bezier('sym-e11', (23, 4), ((23.243, 4), (23.755, 4), (24, 4)))
        self.add_bezier('sym-e12', (24, 4), ((24.245, 4), (24.757, 4), (25, 4)))
        self.add_bezier('sym-e13', (25, 4), ((25.211, 4), (24.789, 4), (25, 4)))
        self.add_bezier('sym-e14', (25, 4), ((28.966, 4), (36.154, 4.936), (39, 8)))
        self.add_bezier('sym-e15', (39, 8), ((39.379, 8.418), (39.764, 8.509), (40, 9)))
        self.add_line('sym-e16', (40, 9), (40, 11))
        self.add_line('sym-e17', (40, 11), (40, 25))
        self.add_line('sym-e18', (40, 25), (40, 38))
        self.add_bezier('sym-e19', (40, 38), ((39.933, 38.218), (40, 37.791), (40, 38)))
        self.add_bezier('sym-e20', (40, 38), ((39.259, 39.627), (37.457, 41.255), (36, 42)))
        self.add_bezier('sym-e21', (36, 42), ((32.589, 43.727), (28.747, 44), (25, 44)))
        self.add_bezier('sym-e22', (25, 44), ((24.941, 44), (25.059, 44), (25, 44)))
        self.add_bezier('sym-e23', (25, 44), ((24.815, 44), (24.185, 44), (24, 44)))
        self.add_bezier('sym-e24', (24, 44), ((23.815, 44), (23.185, 44), (23, 44)))
        self.add_bezier('sym-e25', (23, 44), ((22.941, 44), (23.059, 44), (23, 44)))
        self.add_bezier('sym-e26', (23, 44), ((19.253, 44), (15.411, 43.727), (12, 42)))
        self.add_bezier('sym-e27', (12, 42), ((10.543, 41.255), (8.741, 39.627), (8, 38)))
        self.add_bezier('sym-e28', (8, 38), ((8, 37.791), (8.067, 38.218), (8, 38)))
        self.add_line('sym-e29', (8, 38), (8, 25))
        self.add_bezier('sym-e30', (40, 11), ((38.914, 11.827), (38.196, 13.382), (37, 14)))
        self.add_bezier('sym-e31', (37, 14), ((33.432, 15.834), (28.386, 16), (24, 16)))
        self.add_bezier('sym-e32', (24, 16), ((19.614, 16), (14.568, 15.834), (11, 14)))
        self.add_bezier('sym-e33', (11, 14), ((9.804, 13.382), (9.086, 11.827), (8, 11)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29')
        self.add_contour('sym-c1', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
