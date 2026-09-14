"""Car side (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '695aca30-f091-42f4-b8c1-dabb9d4a8a44'
SOURCE_PATH = 'icons-json/symbol/car side_695aca30-f091-42f4-b8c1-dabb9d4a8a44.json'
AUTHOR = 'json_to_solo'

class CarSideSymbol(Solo48):
    icon_id = 'car-side-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('car', 'side', 'symbol')

    def build(self):
        self.add_line('e0', (39, 34), (42, 34))
        self.add_line('e1', (28, 34), (19, 34))
        self.add_line('e2', (10, 19), (15, 10))
        self.add_line('e3', (18, 8), (29, 8))
        self.add_line('e4', (30, 9), (37, 19))
        self.add_line('e5', (10, 19), (37, 19))
        self.add_arc('e6-top', (28, 34), (38, 34), radius_x=5, radius_y=6)
        self.add_arc('e6-bottom', (38, 34), (28, 34), radius_x=5, radius_y=6)
        self.add_arc('e7-top', (8, 34), (18, 34), radius_x=5, radius_y=6)
        self.add_arc('e7-bottom', (18, 34), (8, 34), radius_x=5, radius_y=6)
        self.add_arc('e8-1', (42, 34), (44, 32), radius_x=2, sweep=False)
        self.add_line('e8-2', (44, 32), (43, 23))
        self.add_arc('e8-3', (43, 23), (37, 19), radius_x=7, sweep=False)
        self.add_line('e9-1', (8, 34), (5, 34))
        self.add_line('e9-2', (5, 34), (4, 30))
        self.add_line('e9-3', (4, 30), (4, 25))
        self.add_arc('e9-4', (4, 25), (10, 19), radius_x=6)
        self.add_arc('e10', (15, 10), (18, 8), radius_x=4)
        self.add_line('e11', (29, 8), (30, 9))
        self.add_contour('c0', 'e0', 'e8-1', 'e8-2', 'e8-3')
        self.add_contour('c1', 'e9-1', 'e9-2', 'e9-3', 'e9-4')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2', 'e10', 'e3', 'e11', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c0', 'e6')
        self.relate('connect', 'c1', 'e7')
        self.relate('connect', 'c2', 'e6')
        self.relate('connect', 'c2', 'e7')
