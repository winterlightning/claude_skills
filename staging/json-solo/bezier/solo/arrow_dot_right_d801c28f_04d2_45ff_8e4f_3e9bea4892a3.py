"""Arrow dot right (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd801c28f-04d2-45ff-8e4f-3e9bea4892a3'
SOURCE_PATH = 'icons-json/arrows/arrow dot right_d801c28f-04d2-45ff-8e4f-3e9bea4892a3.json'
AUTHOR = 'json_to_solo'

class ArrowDotRightArrows(Solo48):
    icon_id = 'arrow-dot-right-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'dot', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (32, 24), (44, 24))
        self.add_line('e1', (44, 24), (37, 40))
        self.add_line('e2', (44, 24), (37, 8))
        self.add_line('e3', (24, 24), (19, 24))
        self.add_line('e4', (10, 24), (4, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
