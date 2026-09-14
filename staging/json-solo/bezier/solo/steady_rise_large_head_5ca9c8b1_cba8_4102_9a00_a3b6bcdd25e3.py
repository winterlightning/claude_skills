"""Steady rise large head (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ca9c8b1-cba8-4102-9a00-a3b6bcdd25e3'
SOURCE_PATH = 'icons-json/arrows/steady rise large head_5ca9c8b1-cba8-4102-9a00-a3b6bcdd25e3.json'
AUTHOR = 'json_to_solo'

class SteadyRiseLargeHeadArrows(Solo48):
    icon_id = 'steady-rise-large-head-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('steady', 'rise', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (36, 8), (44, 8))
        self.add_line('e1', (4, 40), (10, 40))
        self.add_line('e2', (16, 34), (16, 29))
        self.add_line('e3', (20, 24), (28, 24))
        self.add_line('e4', (31, 23), (44, 8))
        self.add_line('e5', (44, 17), (44, 8))
        self.add_bezier('e6', (10, 40), ((12.773, 40), (16, 37.04), (16, 34)))
        self.add_bezier('e7', (16, 29), ((16, 26.64), (17.845, 24), (20, 24)))
        self.add_bezier('e8', (28, 24), ((28.8, 24), (30.409, 23.7), (31, 23)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e6', 'e2', 'e7', 'e3', 'e8', 'e4')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
