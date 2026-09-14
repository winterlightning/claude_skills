"""Diagram arrow dash corner point top (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '41c932c6-e845-57da-9e0d-8598b55e272d'
SOURCE_PATH = 'icons-json/arrows/diagram arrow dash corner point top_41c932c6-e845-57da-9e0d-8598b55e272d.json'
AUTHOR = 'json_to_solo'

class DiagramArrowDashCornerPointTop(Solo48):
    icon_id = 'diagram-arrow-dash-corner-point-top'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('diagram', 'arrow', 'dash', 'corner', 'point', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (42, 21), (27, 6))
        self.add_line('e1', (13, 21), (27, 6))
        self.add_line('e2', (27, 6), (27, 42))
        self.add_line('e3', (27, 42), (6, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3')
