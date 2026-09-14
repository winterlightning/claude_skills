"""Diagram arrow corner point top (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5d9319c6-31dc-547e-a038-75ea80d950a0'
SOURCE_PATH = 'icons-json/arrows/diagram arrow corner point top_5d9319c6-31dc-547e-a038-75ea80d950a0.json'
AUTHOR = 'json_to_solo'

class DiagramArrowCornerPointTopArrows(Solo48):
    icon_id = 'diagram-arrow-corner-point-top-arrows'
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
        self.add_bezier('e4', (34, 40), ((34, 40.213), (33.884, 39.946), (33.851, 40.167)), ((33.712, 41.026), (32.795, 41.992), (31.879, 41.992)), ((31.822, 42), (31.765, 42), (31.707, 42)), ((31.593, 42), (31.115, 42), (31, 42)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e4', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
