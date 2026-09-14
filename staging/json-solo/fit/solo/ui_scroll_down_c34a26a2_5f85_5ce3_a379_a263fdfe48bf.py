"""Ui scroll down (websites), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c34a26a2-5f85-5ce3-a379-a263fdfe48bf'
SOURCE_PATH = 'icons-json/websites/ui scroll down_c34a26a2-5f85-5ce3-a379-a263fdfe48bf.json'
AUTHOR = 'json_to_solo'

class UiScrollDownWebsites(Solo48):
    icon_id = 'ui-scroll-down-websites'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'websites'
    aliases = ()
    keywords = ('ui', 'scroll', 'down', 'websites')

    def build(self):
        self.add_line('e0', (24, 4), (24, 38))
        self.add_line('e1', (24, 38), (13, 28))
        self.add_line('e2', (35, 28), (24, 38))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
