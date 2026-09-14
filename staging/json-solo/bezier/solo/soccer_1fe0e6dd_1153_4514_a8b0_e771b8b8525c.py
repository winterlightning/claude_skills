"""Soccer (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1fe0e6dd-1153-4514-a8b0-e771b8b8525c'
SOURCE_PATH = 'icons-json/symbol/soccer_1fe0e6dd-1153-4514-a8b0-e771b8b8525c.json'
AUTHOR = 'json_to_solo'

class SoccerSymbol(Solo48):
    icon_id = 'soccer-symbol'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('soccer', 'symbol')

    def build(self):
        self.add_line('e0', (32, 28), (42, 32))
        self.add_line('e1', (32, 28), (24, 34))
        self.add_line('e2', (32, 28), (29, 18))
        self.add_line('e3', (24, 44), (24, 34))
        self.add_line('e4', (16, 28), (24, 34))
        self.add_line('e5', (16, 28), (6, 32))
        self.add_line('e6', (16, 28), (19, 18))
        self.add_line('e7', (10, 10), (19, 18))
        self.add_line('e8', (19, 18), (29, 18))
        self.add_line('e9', (29, 18), (38, 10))
        self.add_arc('e10-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e10-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
        self.add_contour('c8', 'e8')
        self.add_contour('c9', 'e9')
        self.add_contour('e10', 'e10-top', 'e10-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c8')
        self.relate('connect', 'c2', 'c9')
        self.relate('connect', 'c8', 'c9')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c0', 'e10')
        self.relate('connect', 'c3', 'e10')
        self.relate('connect', 'c5', 'e10')
        self.relate('connect', 'c7', 'e10')
        self.relate('connect', 'c9', 'e10')
