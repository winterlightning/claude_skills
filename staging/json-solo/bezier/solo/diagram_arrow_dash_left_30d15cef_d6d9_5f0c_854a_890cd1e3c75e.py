"""Diagram arrow dash left (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30d15cef-d6d9-5f0c-854a-890cd1e3c75e'
SOURCE_PATH = 'icons-json/arrows/diagram arrow dash left_30d15cef-d6d9-5f0c-854a-890cd1e3c75e.json'
AUTHOR = 'json_to_solo'

class DiagramArrowDashLeftArrows(Solo48):
    icon_id = 'diagram-arrow-dash-left-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('diagram', 'arrow', 'dash', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (32, 24), (39, 24))
        self.add_line('e1', (15, 8), (4, 24))
        self.add_line('e2', (15, 40), (4, 24))
        self.add_line('e3', (4, 24), (28, 24))
        self.add_bezier('e4', (43, 24), ((43.3, 24), (43.7, 24), (44, 24)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c1', 'c2')
