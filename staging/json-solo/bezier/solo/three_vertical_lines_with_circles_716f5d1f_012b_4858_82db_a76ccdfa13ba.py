"""Three vertical lines with circles (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '716f5d1f-012b-4858-82db-a76ccdfa13ba'
SOURCE_PATH = 'icons-json/symbol/three vertical lines with circles_716f5d1f-012b-4858-82db-a76ccdfa13ba.json'
AUTHOR = 'json_to_solo'

class ThreeVerticalLinesWithCirclesSymbol(Solo48):
    icon_id = 'three-vertical-lines-with-circles-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('three', 'vertical', 'lines', 'with', 'circles', 'symbol')

    def build(self):
        self.add_line('e0', (10, 27), (10, 39))
        self.add_line('e1', (24, 42), (24, 16))
        self.add_line('e2', (38, 27), (38, 39))
        self.add_arc('e3-top', (6, 23), (14, 23), radius_x=4)
        self.add_arc('e3-bottom', (14, 23), (6, 23), radius_x=4)
        self.add_arc('e4-top', (19, 11), (29, 11), radius_x=5)
        self.add_arc('e4-bottom', (29, 11), (19, 11), radius_x=5)
        self.add_arc('e5-top', (34, 23), (42, 23), radius_x=4)
        self.add_arc('e5-bottom', (42, 23), (34, 23), radius_x=4)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c2', 'e5')
