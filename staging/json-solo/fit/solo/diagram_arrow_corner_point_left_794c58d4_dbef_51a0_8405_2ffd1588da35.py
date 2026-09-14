"""Diagram arrow corner point left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '794c58d4-dbef-51a0-8405-2ffd1588da35'
SOURCE_PATH = 'icons-json/arrows/diagram arrow corner point left_794c58d4-dbef-51a0-8405-2ffd1588da35.json'
AUTHOR = 'json_to_solo'

class DiagramArrowCornerPointLeftArrows(Solo48):
    icon_id = 'diagram-arrow-corner-point-left-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('diagram', 'arrow', 'corner', 'point', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (15, 6), (6, 14))
        self.add_line('e1', (6, 14), (15, 23))
        self.add_line('e2', (6, 14), (40, 14))
        self.add_line('e3', (42, 17), (42, 42))
        self.add_line('e4-1', (40, 14), (42, 16))
        self.add_arc('e4-2', (42, 16), (42, 17), radius_x=24, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e4-1', 'e4-2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
