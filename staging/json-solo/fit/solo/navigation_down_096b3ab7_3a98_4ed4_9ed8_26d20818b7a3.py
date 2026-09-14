"""Navigation down (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '096b3ab7-3a98-4ed4-9ed8-26d20818b7a3'
SOURCE_PATH = 'icons-json/interface-essential/navigation down_096b3ab7-3a98-4ed4-9ed8-26d20818b7a3.json'
AUTHOR = 'json_to_solo'

class NavigationDownInterfaceEssential(Solo48):
    icon_id = 'navigation-down-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'down', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 4), (24, 44))
        self.add_line('e1', (8, 33), (24, 44))
        self.add_line('e2', (40, 33), (24, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
