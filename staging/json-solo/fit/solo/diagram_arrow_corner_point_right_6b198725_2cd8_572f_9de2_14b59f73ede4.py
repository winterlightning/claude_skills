"""Diagram arrow corner point right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b198725-2cd8-572f-9de2-14b59f73ede4'
SOURCE_PATH = 'icons-json/arrows/diagram arrow corner point right_6b198725-2cd8-572f-9de2-14b59f73ede4.json'
AUTHOR = 'json_to_solo'

class DiagramArrowCornerPointRightArrows(Solo48):
    icon_id = 'diagram-arrow-corner-point-right-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('diagram', 'arrow', 'corner', 'point', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (33, 42), (42, 34))
        self.add_line('e1', (42, 34), (33, 25))
        self.add_line('e2', (42, 34), (8, 34))
        self.add_line('e3', (6, 31), (6, 6))
        self.add_line('e4-1', (8, 34), (6, 32))
        self.add_line('e4-2', (6, 32), (6, 31))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e4-1', 'e4-2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
