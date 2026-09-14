"""Helmet (protection), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b6d3305-8956-4ad4-a029-b8f48909ae94'
SOURCE_PATH = 'icons-json/protection/helmet_6b6d3305-8956-4ad4-a029-b8f48909ae94.json'
AUTHOR = 'json_to_solo'

class Helmet(Solo48):
    icon_id = 'helmet'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('helmet', 'protection')

    def build(self):
        self.add_line('e0', (29, 29), (29, 13))
        self.add_line('e1', (19, 29), (19, 10))
        self.add_line('e2', (29, 10), (29, 13))
        self.add_line('e3', (6, 29), (43, 29))
        self.add_line('e4', (44, 31), (44, 37))
        self.add_line('e5', (42, 40), (6, 40))
        self.add_arc('e6', (40, 29), (29, 13), radius_x=16, sweep=False)
        self.add_line('e7-1', (19, 10), (23, 8))
        self.add_line('e7-2', (23, 8), (26, 8))
        self.add_line('e7-3', (26, 8), (29, 10))
        self.add_arc('e8', (8, 29), (19, 13), radius_x=17)
        self.add_arc('e9', (43, 29), (44, 31), radius_x=4)
        self.add_line('e10', (44, 37), (42, 40))
        self.add_arc('e11-1', (6, 40), (4, 38), radius_x=2)
        self.add_arc('e11-2', (4, 38), (4, 37), radius_x=1, sweep=False)
        self.add_line('e11-3', (4, 37), (4, 31))
        self.add_arc('e11-4', (4, 31), (6, 29), radius_x=2)
        self.add_contour('c0', 'e6')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1', 'e7-1', 'e7-2', 'e7-3', 'e2')
        self.add_contour('c3', 'e8')
        self.add_contour('c4', 'e3', 'e9', 'e4', 'e10', 'e5', 'e11-1', 'e11-2', 'e11-3', 'e11-4', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c2')
