"""Diagram arrow dash corner point right (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'faba3467-1140-5371-82fa-2877034d02a7'
SOURCE_PATH = 'icons-json/arrows/diagram arrow dash corner point right_faba3467-1140-5371-82fa-2877034d02a7.json'
AUTHOR = 'json_to_solo'

class DiagramArrowDashCornerPointRightArrows(Solo48):
    icon_id = 'diagram-arrow-dash-corner-point-right-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('diagram', 'arrow', 'dash', 'corner', 'point', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (27, 42), (42, 27))
        self.add_line('e1', (27, 13), (42, 27))
        self.add_line('e2', (42, 27), (6, 27))
        self.add_line('e3', (6, 27), (6, 6))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3')
