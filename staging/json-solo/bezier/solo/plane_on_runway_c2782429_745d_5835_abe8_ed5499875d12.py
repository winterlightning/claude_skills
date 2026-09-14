"""Plane on runway (travel), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2782429-745d-5835-abe8-ed5499875d12'
SOURCE_PATH = 'icons-json/travel/plane on runway_c2782429-745d-5835-abe8-ed5499875d12.json'
AUTHOR = 'json_to_solo'

class PlaneOnRunwayTravel(Solo48):
    icon_id = 'plane-on-runway-travel'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    aliases = ()
    keywords = ('plane', 'on', 'runway', 'travel')

    def build(self):
        self.add_line('e0', (5, 40), (44, 40))
        self.add_line('e1', (37, 8), (26, 14))
        self.add_line('e2', (26, 14), (15, 8))
        self.add_line('e3', (15, 8), (11, 10))
        self.add_line('e4', (11, 10), (19, 18))
        self.add_line('e5', (19, 18), (12, 21))
        self.add_line('e6', (12, 21), (6, 18))
        self.add_line('e7', (6, 18), (4, 19))
        self.add_line('e8', (4, 19), (9, 26))
        self.add_line('e9', (17, 28), (39, 16))
        self.add_bezier('e10', (9, 26), ((11.136, 29.29), (13.773, 29.7), (17, 28)))
        self.add_bezier('e11', (39, 16), ((40.9, 15), (44, 13.88), (44, 11.14)), ((44, 10.21), (41.136, 8.01), (40.391, 8.01)), ((40.309, 8.01), (40.227, 8), (40.155, 8)), ((39.009, 8), (38.145, 8), (37, 8)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e10', 'e9', 'e11', closed=True)
