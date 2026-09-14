"""Diagram arrow corner point bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ddce33b4-ce1b-5aa5-ab58-508f35fa586c'
SOURCE_PATH = 'icons-json/arrows/diagram arrow corner point bottom_ddce33b4-ce1b-5aa5-ab58-508f35fa586c.json'
AUTHOR = 'json_to_solo'

class DiagramArrowCornerPointBottomArrows(Solo48):
    icon_id = 'diagram-arrow-corner-point-bottom-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('diagram', 'arrow', 'corner', 'point', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (6, 33), (14, 42))
        self.add_line('e1', (14, 42), (23, 33))
        self.add_line('e2', (14, 42), (14, 8))
        self.add_line('e3', (17, 6), (42, 6))
        self.add_bezier('e4', (14, 8), ((14, 7.787), (14.116, 8.054), (14.149, 7.833)), ((14.288, 6.974), (15.205, 6.008), (16.121, 6.008)), ((16.178, 6), (16.235, 6), (16.293, 6)), ((16.407, 6), (16.885, 6), (17, 6)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e4', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
