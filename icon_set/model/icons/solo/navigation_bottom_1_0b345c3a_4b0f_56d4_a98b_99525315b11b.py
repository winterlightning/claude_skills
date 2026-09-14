"""Navigation bottom 1 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0b345c3a-4b0f-56d4-a98b-99525315b11b'
SOURCE_PATH = 'icons-json/arrows/navigation bottom 1_0b345c3a-4b0f-56d4-a98b-99525315b11b.json'
AUTHOR = 'json_to_solo'

class NavigationBottom1(Solo48):
    icon_id = 'navigation-bottom-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('navigation', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (8, 28), (24, 44))
        self.add_line('e1', (24, 44), (40, 28))
        self.add_line('e2', (24, 34), (24, 4))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
