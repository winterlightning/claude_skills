"""Curve up 1 large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ce5aba91-3eaf-468d-840f-73f4b6f97bf5'
SOURCE_PATH = 'icons-json/arrows/curve up 1 large head_ce5aba91-3eaf-468d-840f-73f4b6f97bf5.json'
AUTHOR = 'json_to_solo'

class CurveUp1LargeHeadArrows(Solo48):
    icon_id = 'curve-up-1-large-head-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curve', 'up', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (37, 6), (42, 12))
        self.add_line('e1', (6, 42), (17, 42))
        self.add_line('e2', (22, 36), (22, 20))
        self.add_line('e3', (30, 12), (42, 12))
        self.add_line('e4', (36, 17), (42, 12))
        self.add_arc('e5', (17, 42), (22, 36), radius_x=7, sweep=False)
        self.add_arc('e6', (22, 20), (30, 12), radius_x=9)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2', 'e6', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
