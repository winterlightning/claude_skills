"""Database (diagrams), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('sym-e0', (40, 25), (38, 27), radius_x=14, sweep=False)
        self.add_arc('sym-e1', (38, 27), (32, 29), radius_x=18, sweep=False)
        self.add_line('sym-e2', (32, 29), (24, 30))
        self.add_line('sym-e3', (24, 30), (16, 29))
        self.add_arc('sym-e4', (16, 29), (10, 27), radius_x=18, sweep=False)
        self.add_arc('sym-e5', (10, 27), (8, 25), radius_x=14, sweep=False)
        self.add_line('sym-e6', (8, 25), (8, 11))
        self.add_line('sym-e7', (8, 11), (8, 9))
        self.add_line('sym-e8', (8, 9), (9, 8))
        self.add_arc('sym-e9-1', (9, 8), (15, 5), radius_x=13)
        self.add_line('sym-e9-2', (15, 5), (23, 4))
        self.add_arc('sym-e11', (23, 4), (24, 4), radius_x=70, sweep=False)
        self.add_line('sym-e12', (24, 4), (25, 4))
        self.add_line('sym-e14-1', (25, 4), (33, 5))
        self.add_arc('sym-e14-2', (33, 5), (39, 8), radius_x=13)
        self.add_line('sym-e15', (39, 8), (40, 9))
        self.add_line('sym-e16', (40, 9), (40, 11))
        self.add_line('sym-e17', (40, 11), (40, 25))
        self.add_line('sym-e18', (40, 25), (40, 38))
        self.add_arc('sym-e20', (40, 38), (36, 42), radius_x=8)
        self.add_line('sym-e21', (36, 42), (25, 44))
        self.add_arc('sym-e23', (25, 44), (24, 44), radius_x=29, sweep=False)
        self.add_line('sym-e24', (24, 44), (23, 44))
        self.add_line('sym-e26', (23, 44), (12, 42))
        self.add_arc('sym-e27', (12, 42), (8, 38), radius_x=8)
        self.add_line('sym-e29', (8, 38), (8, 25))
        self.add_arc('sym-e30', (40, 11), (37, 14), radius_x=22, sweep=False)
        self.add_arc('sym-e31', (37, 14), (24, 16), radius_x=28)
        self.add_arc('sym-e32', (24, 16), (11, 14), radius_x=28)
        self.add_arc('sym-e33', (11, 14), (8, 11), radius_x=22)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9-1', 'sym-e9-2', 'sym-e11', 'sym-e12', 'sym-e14-1', 'sym-e14-2', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e20', 'sym-e21', 'sym-e23', 'sym-e24', 'sym-e26', 'sym-e27', 'sym-e29')
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
