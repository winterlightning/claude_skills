"""Ball with lines (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '02c70f52-9dee-4f13-8c03-a5f8a38f8a84'
SOURCE_PATH = 'icons-json/symbol/ball with lines_02c70f52-9dee-4f13-8c03-a5f8a38f8a84.json'
AUTHOR = 'json_to_solo'

class BallWithLines(Solo48):
    icon_id = 'ball-with-lines'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('ball', 'with', 'lines', 'symbol')

    def build(self):
        self.add_line('e0', (29, 32), (19, 32))
        self.add_line('e1', (29, 32), (35, 40))
        self.add_line('e2', (29, 32), (33, 21))
        self.add_line('e3', (19, 32), (13, 40))
        self.add_line('e4', (19, 32), (15, 21))
        self.add_line('e5', (33, 21), (43, 19))
        self.add_line('e6', (33, 21), (24, 14))
        self.add_line('e7', (24, 14), (15, 21))
        self.add_line('e8', (15, 21), (5, 19))
        self.add_line('e9', (24, 14), (24, 4))
        self.add_arc('e10-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e10-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6', 'e7')
        self.add_contour('c7', 'e8')
        self.add_contour('c8', 'e9')
        self.add_contour('e10', 'e10-top', 'e10-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c1', 'e10')
        self.relate('connect', 'c3', 'e10')
        self.relate('connect', 'c5', 'e10')
        self.relate('connect', 'c7', 'e10')
        self.relate('connect', 'c8', 'e10')
