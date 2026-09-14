"""Diagram arrow dash right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c6608cc-a1a4-50b5-b6c3-fe2569ed4c3b'
SOURCE_PATH = 'icons-json/arrows/diagram arrow dash right_2c6608cc-a1a4-50b5-b6c3-fe2569ed4c3b.json'
AUTHOR = 'json_to_solo'

class DiagramArrowDashRight(Solo48):
    icon_id = 'diagram-arrow-dash-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('diagram', 'arrow', 'dash', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (16, 24), (9, 24))
        self.add_line('e1', (33, 40), (44, 24))
        self.add_line('e2', (33, 8), (44, 24))
        self.add_line('e3', (44, 24), (20, 24))
        self.add_arc('e4', (5, 24), (4, 24), radius_x=12, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c1', 'c2')
