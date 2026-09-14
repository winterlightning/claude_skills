"""Diagram arrow corner point top (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5d9319c6-31dc-547e-a038-75ea80d950a0'
SOURCE_PATH = 'icons-json/arrows/diagram arrow corner point top_5d9319c6-31dc-547e-a038-75ea80d950a0.json'
AUTHOR = 'json_to_solo'

class DiagramArrowCornerPointTop(Solo48):
    icon_id = 'diagram-arrow-corner-point-top'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('diagram', 'arrow', 'corner', 'point', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (42, 15), (34, 6))
        self.add_line('e1', (34, 6), (25, 15))
        self.add_line('e2', (34, 6), (34, 40))
        self.add_line('e3', (31, 42), (6, 42))
        self.add_line('e4-1', (34, 40), (32, 42))
        self.add_arc('e4-2', (32, 42), (31, 42), radius_x=32, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e4-1', 'e4-2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
