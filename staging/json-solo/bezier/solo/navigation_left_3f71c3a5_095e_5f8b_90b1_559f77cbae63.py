"""Navigation left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f71c3a5-095e-5f8b-90b1-559f77cbae63'
SOURCE_PATH = 'icons-json/interface-essential/navigation left_3f71c3a5-095e-5f8b-90b1-559f77cbae63.json'
AUTHOR = 'json_to_solo'

class NavigationLeft(Solo48):
    icon_id = 'navigation-left'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (40, 4), (8, 24))
        self.add_line('e1', (8, 24), (40, 44))
        self.add_contour('c0', 'e0', 'e1')
