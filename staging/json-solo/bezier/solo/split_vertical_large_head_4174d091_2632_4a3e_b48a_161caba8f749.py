"""Split vertical large head (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4174d091-2632-4a3e-b48a-161caba8f749'
SOURCE_PATH = 'icons-json/arrows/split vertical large head_4174d091-2632-4a3e-b48a-161caba8f749.json'
AUTHOR = 'json_to_solo'

class SplitVerticalLargeHeadArrows(Solo48):
    icon_id = 'split-vertical-large-head-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('split', 'vertical', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (24, 8), (24, 25))
        self.add_line('e1', (8, 12), (4, 16))
        self.add_line('e2', (9, 20), (4, 16))
        self.add_line('e3', (24, 40), (24, 23))
        self.add_line('e4', (40, 20), (44, 16))
        self.add_line('e5', (40, 11), (44, 16))
        self.add_line('e6', (24, 25), (21, 20))
        self.add_line('e7', (13, 16), (4, 16))
        self.add_line('e8', (24, 25), (28, 20))
        self.add_line('e9', (36, 16), (44, 16))
        self.add_bezier('e10', (21, 20), ((19.855, 17.878), (16.1, 15.966), (13.627, 15.697)), ((13.473, 15.68), (13.127, 16), (13, 16)))
        self.add_bezier('e11', (28, 20), ((29.745, 17.575), (32.827, 16), (36, 16)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6', 'e10', 'e7')
        self.add_contour('c7', 'e8', 'e11', 'e9')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c6', 'c3')
        self.relate('connect', 'c7', 'c3')
        self.relate('connect', 'c3', 'c0')
