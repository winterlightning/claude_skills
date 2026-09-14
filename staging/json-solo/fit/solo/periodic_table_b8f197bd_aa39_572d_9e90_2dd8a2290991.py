"""Periodic table (science), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8f197bd-aa39-572d-9e90-2dd8a2290991'
SOURCE_PATH = 'icons-json/science/periodic table_b8f197bd-aa39-572d-9e90-2dd8a2290991.json'
AUTHOR = 'json_to_solo'

class PeriodicTableScience(Solo48):
    icon_id = 'periodic-table-science'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('periodic', 'table', 'science')

    def build(self):
        self.add_line('e0', (44, 29), (4, 29))
        self.add_line('e1', (15, 40), (15, 19))
        self.add_line('e2', (15, 19), (4, 19))
        self.add_line('e3', (44, 19), (31, 19))
        self.add_line('e4', (31, 40), (31, 12))
        self.add_line('e5', (33, 10), (43, 10))
        self.add_line('e6', (44, 11), (44, 37))
        self.add_line('e7', (40, 40), (7, 40))
        self.add_line('e8', (4, 36), (4, 12))
        self.add_line('e9', (12, 12), (12, 19))
        self.add_arc('e10', (31, 12), (33, 10), radius_x=3)
        self.add_arc('e11', (43, 10), (44, 11), radius_x=2)
        self.add_arc('e12-1', (44, 37), (41, 40), radius_x=3)
        self.add_arc('e12-2', (41, 40), (40, 40), radius_x=41, sweep=False)
        self.add_arc('e13-1', (7, 40), (5, 39), radius_x=3)
        self.add_arc('e13-2', (5, 39), (4, 36), radius_x=5)
        self.add_line('e14-1', (4, 12), (5, 9))
        self.add_line('e14-2', (5, 9), (7, 8))
        self.add_line('e14-3', (7, 8), (11, 9))
        self.add_arc('e14-4', (11, 9), (12, 12), radius_x=4)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e10', 'e5', 'e11', 'e6', 'e12-1', 'e12-2', 'e7', 'e13-1', 'e13-2', 'e8', 'e14-1', 'e14-2', 'e14-3', 'e14-4', 'e9')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'c1')
