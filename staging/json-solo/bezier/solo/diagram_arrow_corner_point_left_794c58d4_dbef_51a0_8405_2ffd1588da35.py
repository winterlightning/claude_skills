"""Diagram arrow corner point left (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e4', (40, 14), ((40.213, 14), (39.946, 14.116), (40.167, 14.149)), ((41.026, 14.288), (41.992, 15.205), (41.992, 16.121)), ((42, 16.178), (42, 16.235), (42, 16.293)), ((42, 16.407), (42, 16.885), (42, 17)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e4', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
