"""Navigation arrows up (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '428c508c-c9f9-43d1-90d2-74e0ffbb6354'
SOURCE_PATH = 'icons-json/interface-essential/navigation arrows up_428c508c-c9f9-43d1-90d2-74e0ffbb6354.json'
AUTHOR = 'json_to_solo'

class NavigationArrowsUpInterfaceEssential(Solo48):
    icon_id = 'navigation-arrows-up-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'arrows', 'up', 'interface-essential')

    def build(self):
        self.add_line('e0', (8, 19), (24, 4))
        self.add_line('e1', (24, 44), (24, 4))
        self.add_line('e2', (40, 19), (27, 7))
        self.add_line('e3', (27, 7), (24, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
