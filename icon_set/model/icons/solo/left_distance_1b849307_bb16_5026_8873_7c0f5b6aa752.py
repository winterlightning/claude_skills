"""Left distance (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b849307-bb16-5026-8873-7c0f5b6aa752'
SOURCE_PATH = 'icons-json/design/left distance_1b849307-bb16-5026-8873-7c0f5b6aa752.json'
AUTHOR = 'json_to_solo'

class LeftDistance(Solo48):
    icon_id = 'left-distance'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('left', 'distance', 'design')

    def build(self):
        self.add_line('e0', (4, 8), (4, 40))
        self.add_line('e1', (26, 24), (12, 24))
        self.add_line('e2', (12, 24), (18, 19))
        self.add_line('e3', (12, 24), (18, 29))
        self.add_line('e4', (27, 16), (41, 16))
        self.add_line('e5', (44, 18), (44, 31))
        self.add_line('e6', (43, 32), (27, 32))
        self.add_line('e7', (26, 31), (26, 20))
        self.add_arc('e8', (26, 20), (27, 16), radius_x=3)
        self.add_arc('e9', (41, 16), (44, 18), radius_x=3)
        self.add_arc('e10', (44, 31), (43, 32), radius_x=1)
        self.add_arc('e11', (27, 32), (26, 31), radius_x=1)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e8', 'e4', 'e9', 'e5', 'e10', 'e6', 'e11', 'e7', closed=True)
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
