"""Diagram arrow dash left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30d15cef-d6d9-5f0c-854a-890cd1e3c75e'
SOURCE_PATH = 'icons-json/arrows/diagram arrow dash left_30d15cef-d6d9-5f0c-854a-890cd1e3c75e.json'
AUTHOR = 'json_to_solo'

class DiagramArrowDashLeft(Solo48):
    icon_id = 'diagram-arrow-dash-left'
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
        self.add_arc('e4', (43, 24), (44, 24), radius_x=51, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c1', 'c2')
