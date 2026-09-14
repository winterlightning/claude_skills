"""Diagram arrow dash top (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2fd0a7e-0c70-5cb1-84f4-8e9a1adf8669'
SOURCE_PATH = 'icons-json/arrows/diagram arrow dash top_a2fd0a7e-0c70-5cb1-84f4-8e9a1adf8669.json'
AUTHOR = 'json_to_solo'

class DiagramArrowDashTop(Solo48):
    icon_id = 'diagram-arrow-dash-top'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('diagram', 'arrow', 'dash', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (24, 32), (24, 39))
        self.add_line('e1', (40, 15), (24, 4))
        self.add_line('e2', (8, 15), (24, 4))
        self.add_line('e3', (24, 4), (24, 28))
        self.add_arc('e4', (24, 43), (24, 44), radius_x=52, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c1', 'c2')
