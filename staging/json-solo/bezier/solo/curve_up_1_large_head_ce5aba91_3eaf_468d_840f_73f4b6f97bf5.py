"""Curve up 1 large head (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e5', (17, 42), ((17.352, 42), (17.34, 41.828), (17.659, 41.697)), ((19.737, 40.879), (21.014, 38.817), (21.415, 36.69)), ((21.431, 36.592), (22, 36.057), (22, 36)))
        self.add_bezier('e6', (22, 20), ((22, 19.697), (21.75, 19.091), (21.832, 18.764)), ((22.56, 15.769), (24.892, 13.2), (27.796, 12.185)), ((28.369, 11.981), (29.395, 12), (30, 12)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2', 'e6', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
