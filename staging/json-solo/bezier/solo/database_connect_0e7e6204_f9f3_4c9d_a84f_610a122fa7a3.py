"""Database connect (programing), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e7e6204-f9f3-4c9d-a84f-610a122fa7a3'
SOURCE_PATH = 'icons-json/programing/database connect_0e7e6204-f9f3-4c9d-a84f-610a122fa7a3.json'
AUTHOR = 'json_to_solo'

class DatabaseConnectPrograming(Solo48):
    icon_id = 'database-connect-programing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('database', 'connect', 'programing')

    def build(self):
        self.add_line('e0', (32, 32), (24, 24))
        self.add_line('e1', (17, 31), (24, 24))
        self.add_line('e2', (32, 16), (24, 24))
        self.add_line('e3', (16, 16), (24, 24))
        self.add_arc('e4-top', (30, 36), (42, 36), radius_x=6)
        self.add_arc('e4-bottom', (42, 36), (30, 36), radius_x=6)
        self.add_arc('e5-top', (6, 36), (18, 36), radius_x=6)
        self.add_arc('e5-bottom', (18, 36), (6, 36), radius_x=6)
        self.add_arc('e6-top', (30, 12), (42, 12), radius_x=6)
        self.add_arc('e6-bottom', (42, 12), (30, 12), radius_x=6)
        self.add_arc('e7-top', (6, 12), (18, 12), radius_x=6)
        self.add_arc('e7-bottom', (18, 12), (6, 12), radius_x=6)
        self.add_bezier('e8', (16, 32), ((16.27, 31.73), (16.73, 31.27), (17, 31)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e8', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c1', 'e5')
        self.relate('connect', 'c2', 'e6')
        self.relate('connect', 'c3', 'e7')
