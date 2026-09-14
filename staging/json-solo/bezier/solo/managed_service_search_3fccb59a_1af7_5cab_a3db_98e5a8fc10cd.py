"""Managed service search (programing), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3fccb59a-1af7-5cab-a3db-98e5a8fc10cd'
SOURCE_PATH = 'icons-json/programing/managed service search_3fccb59a-1af7-5cab-a3db-98e5a8fc10cd.json'
AUTHOR = 'json_to_solo'

class ManagedServiceSearch3fccb59a(Solo48):
    icon_id = 'managed-service-search-3fccb59a'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('managed', 'service', 'search', 'programing')

    def build(self):
        self.add_line('e0', (43, 23), (35, 23))
        self.add_line('e1', (34, 22), (33, 21))
        self.add_line('e2', (33, 21), (29, 31))
        self.add_line('e3', (29, 31), (24, 14))
        self.add_line('e4', (24, 14), (19, 28))
        self.add_line('e5', (19, 28), (17, 23))
        self.add_line('e6', (17, 23), (4, 23))
        self.add_line('e7', (44, 40), (36, 33))
        self.add_arc('e8-top', (11, 22), (41, 22), radius_x=15, radius_y=14)
        self.add_arc('e8-bottom', (41, 22), (11, 22), radius_x=15, radius_y=14)
        self.add_bezier('e9', (35, 23), ((34.673, 22.722), (34.309, 22.295), (34, 22)))
        self.add_contour('c0', 'e0', 'e9', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6')
        self.add_contour('c1', 'e7')
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.relate('connect', 'c1', 'e8')
