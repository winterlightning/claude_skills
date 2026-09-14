"""Diagram arrow dash corner point left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '340d3436-de41-5d1f-8da4-62faf581c08e'
SOURCE_PATH = 'icons-json/arrows/diagram arrow dash corner point left_340d3436-de41-5d1f-8da4-62faf581c08e.json'
AUTHOR = 'json_to_solo'

class DiagramArrowDashCornerPointLeft(Solo48):
    icon_id = 'diagram-arrow-dash-corner-point-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('diagram', 'arrow', 'dash', 'corner', 'point', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (21, 6), (6, 21))
        self.add_line('e1', (21, 35), (6, 21))
        self.add_line('e2', (6, 21), (42, 21))
        self.add_line('e3', (42, 21), (42, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3')
