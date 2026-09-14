"""Split vertical (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0426ebd5-cfe4-416c-bda2-27405f3e8a75'
SOURCE_PATH = 'icons-json/arrows/split vertical_0426ebd5-cfe4-416c-bda2-27405f3e8a75.json'
AUTHOR = 'json_to_solo'

class SplitVerticalArrows(Solo48):
    icon_id = 'split-vertical-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('split', 'vertical', 'arrows')

    def build(self):
        self.add_line('e0', (10, 6), (6, 10))
        self.add_line('e1', (10, 14), (6, 10))
        self.add_line('e2', (24, 42), (24, 22))
        self.add_line('e3', (33, 10), (42, 10))
        self.add_line('e4', (38, 14), (42, 10))
        self.add_line('e5', (38, 6), (42, 10))
        self.add_line('e6', (6, 10), (14, 10))
        self.add_bezier('e7', (24, 22), ((24, 21.91), (24, 21.619), (24, 21.545)), ((23.992, 21.275), (24, 21.27), (24, 21)))
        self.add_bezier('e8', (24, 22), ((25.096, 17.811), (25.865, 13.315), (30.014, 11.032)), ((30.848, 10.574), (32.035, 10), (33, 10)))
        self.add_bezier('e9', (14, 10), ((15.072, 10), (16.489, 10.459), (17.438, 10.942)), ((21.766, 13.11), (22.855, 17.696), (24, 22)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e7')
        self.add_contour('c4', 'e8', 'e3')
        self.add_contour('c5', 'e4')
        self.add_contour('c6', 'e5')
        self.add_contour('c7', 'e6', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c1', 'c7')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c7', 'c3')
        self.relate('connect', 'c7', 'c4')
