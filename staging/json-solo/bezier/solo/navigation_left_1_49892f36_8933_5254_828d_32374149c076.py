"""Navigation left 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '49892f36-8933-5254-828d-32374149c076'
SOURCE_PATH = 'icons-json/interface-essential/navigation left 1_49892f36-8933-5254-828d-32374149c076.json'
AUTHOR = 'json_to_solo'

class NavigationLeft1InterfaceEssential(Solo48):
    icon_id = 'navigation-left-1-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (20, 8), (4, 24))
        self.add_line('e1', (4, 24), (20, 40))
        self.add_line('e2', (14, 24), (44, 24))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
