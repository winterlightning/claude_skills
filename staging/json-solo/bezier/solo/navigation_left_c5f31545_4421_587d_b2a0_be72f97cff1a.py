"""Navigation left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5f31545-4421-587d-b2a0-be72f97cff1a'
SOURCE_PATH = 'icons-json/interface-essential/navigation left_c5f31545-4421-587d-b2a0-be72f97cff1a.json'
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
        self.add_line('e0', (4, 24), (16, 8))
        self.add_line('e1', (4, 24), (16, 40))
        self.add_line('e2', (4, 24), (44, 24))
        self.add_line('e3', (44, 34), (44, 14))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c2', 'c3')
