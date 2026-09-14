"""Sushi (food), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b9289ab5-a821-4c9d-9497-b44e31767d04'
SOURCE_PATH = 'icons-json/food/sushi_b9289ab5-a821-4c9d-9497-b44e31767d04.json'
AUTHOR = 'json_to_solo'

class Sushi(Solo48):
    icon_id = 'sushi'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('sushi', 'food')

    def build(self):
        self.add_line('e0', (34, 40), (14, 40))
        self.add_line('e1', (40, 30), (42, 30))
        self.add_line('e2', (12, 25), (19, 9))
        self.add_line('e3', (34, 24), (39, 14))
        self.add_line('e4', (24, 22), (30, 9))
        self.add_arc('e5', (40, 30), (34, 24), radius_x=17, sweep=False)
        self.add_arc('e6', (40, 30), (34, 40), radius_x=8)
        self.add_arc('e7', (14, 40), (8, 30), radius_x=8)
        self.add_line('e8-1', (42, 30), (44, 27))
        self.add_arc('e8-2', (44, 27), (39, 14), radius_x=20, sweep=False)
        self.add_line('e9', (8, 30), (12, 25))
        self.add_line('e10-1', (8, 30), (5, 30))
        self.add_line('e10-2', (5, 30), (4, 27))
        self.add_arc('e10-3', (4, 27), (19, 9), radius_x=19)
        self.add_arc('e11', (12, 25), (24, 22), radius_x=21)
        self.add_arc('e12', (34, 24), (24, 22), radius_x=24, sweep=False)
        self.add_arc('e13', (30, 9), (39, 14), radius_x=20)
        self.add_line('e14-1', (30, 9), (26, 8))
        self.add_line('e14-2', (26, 8), (19, 9))
        self.add_contour('c0', 'e5')
        self.add_contour('c1', 'e6', 'e0', 'e7')
        self.add_contour('c2', 'e1', 'e8-1', 'e8-2')
        self.add_contour('c3', 'e9')
        self.add_contour('c4', 'e10-1', 'e10-2', 'e10-3')
        self.add_contour('c5', 'e11')
        self.add_contour('c6', 'e2')
        self.add_contour('c7', 'e3')
        self.add_contour('c8', 'e12')
        self.add_contour('c9', 'e4')
        self.add_contour('c10', 'e13')
        self.add_contour('c11', 'e14-1', 'e14-2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c0', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c10', 'c2')
        self.relate('connect', 'c10', 'c7')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c11', 'c4')
        self.relate('connect', 'c11', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c8')
        self.relate('connect', 'c5', 'c9')
        self.relate('connect', 'c8', 'c9')
        self.relate('connect', 'c10', 'c11')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c11', 'c9')
