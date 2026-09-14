"""Navigation left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '02b66f96-8efb-5dcf-8a1d-9350c9ca831d'
SOURCE_PATH = 'icons-json/interface-essential/navigation left_02b66f96-8efb-5dcf-8a1d-9350c9ca831d.json'
AUTHOR = 'json_to_solo'

class NavigationLeft(Solo48):
    icon_id = 'navigation-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (19, 8), (4, 24))
        self.add_line('e1', (4, 24), (19, 40))
        self.add_line('e2', (15, 24), (44, 24))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
