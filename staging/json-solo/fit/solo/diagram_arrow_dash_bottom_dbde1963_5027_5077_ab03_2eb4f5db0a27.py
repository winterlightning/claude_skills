"""Diagram arrow dash bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dbde1963-5027-5077-ab03-2eb4f5db0a27'
SOURCE_PATH = 'icons-json/arrows/diagram arrow dash bottom_dbde1963-5027-5077-ab03-2eb4f5db0a27.json'
AUTHOR = 'json_to_solo'

class DiagramArrowDashBottomArrows(Solo48):
    icon_id = 'diagram-arrow-dash-bottom-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('diagram', 'arrow', 'dash', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (24, 16), (24, 9))
        self.add_line('e1', (8, 33), (24, 44))
        self.add_line('e2', (40, 33), (24, 44))
        self.add_line('e3', (24, 44), (24, 20))
        self.add_arc('e4', (24, 5), (24, 4), radius_x=12, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c1', 'c2')
