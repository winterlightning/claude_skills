"""Steady and fall large head (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7c78b2f2-0d07-40e5-88ac-1010b7292e8f'
SOURCE_PATH = 'icons-json/arrows/steady and fall large head_7c78b2f2-0d07-40e5-88ac-1010b7292e8f.json'
AUTHOR = 'json_to_solo'

class SteadyAndFallLargeHeadArrows(Solo48):
    icon_id = 'steady-and-fall-large-head-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('steady', 'and', 'fall', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (6, 6), (6, 18))
        self.add_line('e1', (11, 23), (21, 23))
        self.add_line('e2', (16, 37), (21, 42))
        self.add_line('e3', (26, 37), (21, 42))
        self.add_line('e4', (36, 30), (42, 23))
        self.add_line('e5', (36, 17), (40, 22))
        self.add_line('e6', (40, 22), (42, 23))
        self.add_line('e7', (21, 23), (21, 42))
        self.add_line('e8', (21, 23), (42, 23))
        self.add_bezier('e9', (6, 18), ((6, 20.185), (8.807, 23), (11, 23)))
        self.add_contour('c0', 'e0', 'e9', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5', 'e6')
        self.add_contour('c5', 'e7')
        self.add_contour('c6', 'e8')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
