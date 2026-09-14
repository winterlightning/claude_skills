"""Diagram arrow dash corner point bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '616df8be-e4ab-5a77-b44c-bbf0e82e3e54'
SOURCE_PATH = 'icons-json/arrows/diagram arrow dash corner point bottom_616df8be-e4ab-5a77-b44c-bbf0e82e3e54.json'
AUTHOR = 'json_to_solo'

class DiagramArrowDashCornerPointBottomArrows(Solo48):
    icon_id = 'diagram-arrow-dash-corner-point-bottom-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('diagram', 'arrow', 'dash', 'corner', 'point', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (6, 27), (21, 42))
        self.add_line('e1', (35, 27), (21, 42))
        self.add_line('e2', (21, 42), (21, 6))
        self.add_line('e3', (21, 6), (42, 6))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3')
