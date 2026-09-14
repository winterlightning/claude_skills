"""Arrow double top (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd71931e-46f1-5390-a409-62af27b325ee'
SOURCE_PATH = 'icons-json/arrows/arrow double top_fd71931e-46f1-5390-a409-62af27b325ee.json'
AUTHOR = 'json_to_solo'

class ArrowDoubleTopArrows(Solo48):
    icon_id = 'arrow-double-top-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'double', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (39, 19), (24, 4))
        self.add_line('e1', (24, 4), (8, 20))
        self.add_line('e2', (40, 44), (24, 28))
        self.add_line('e3', (24, 28), (8, 44))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
