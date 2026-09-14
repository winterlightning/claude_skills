"""Database (servers), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7226fb36-c110-4033-9d0b-3e66cfa5b027'
SOURCE_PATH = 'icons-json/servers/database_7226fb36-c110-4033-9d0b-3e66cfa5b027.json'
AUTHOR = 'json_to_solo'

class Database7226fb36(Solo48):
    icon_id = 'database-7226fb36'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'servers'
    aliases = ()
    keywords = ('database', 'servers')

    def build(self):
        self.add_arc('sym-e1', (24, 23), (32, 22), radius_x=32, sweep=False)
        self.add_arc('sym-e2', (32, 22), (40, 19), radius_x=34, sweep=False)
        self.add_line('sym-e3', (40, 19), (40, 29))
        self.add_line('sym-e4', (40, 29), (33, 33))
        self.add_line('sym-e5', (33, 33), (24, 34))
        self.add_line('sym-e8', (24, 34), (15, 33))
        self.add_arc('sym-e9', (15, 33), (8, 29), radius_x=43)
        self.add_line('sym-e10', (8, 29), (8, 37))
        self.add_line('sym-e12', (8, 37), (8, 38))
        self.add_line('sym-e13', (8, 38), (11, 41))
        self.add_arc('sym-e14', (11, 41), (23, 44), radius_x=26, sweep=False)
        self.add_arc('sym-e15', (23, 44), (24, 44), radius_x=43)
        self.add_line('sym-e16', (24, 44), (25, 44))
        self.add_arc('sym-e17', (25, 44), (37, 41), radius_x=26, sweep=False)
        self.add_line('sym-e18', (37, 41), (40, 38))
        self.add_line('sym-e19', (40, 38), (40, 37))
        self.add_line('sym-e21', (40, 37), (40, 29))
        self.add_line('sym-e22', (40, 19), (40, 9))
        self.add_line('sym-e23', (40, 9), (38, 8))
        self.add_arc('sym-e24', (38, 8), (25, 4), radius_x=24, sweep=False)
        self.add_line('sym-e25', (25, 4), (24, 4))
        self.add_arc('sym-e28', (24, 4), (23, 4), radius_x=70)
        self.add_arc('sym-e29', (23, 4), (10, 8), radius_x=24, sweep=False)
        self.add_line('sym-e30', (10, 8), (8, 9))
        self.add_line('sym-e31', (8, 9), (8, 19))
        self.add_arc('sym-e32', (8, 19), (16, 22), radius_x=34, sweep=False)
        self.add_line('sym-e33', (16, 22), (24, 23))
        self.add_line('sym-e35', (8, 29), (8, 19))
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e21')
        self.add_contour('sym-c1', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33')
        self.add_contour('sym-c2', 'sym-e35')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
