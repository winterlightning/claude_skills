"""Navigation down circle (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18069a19-0b23-40e6-a387-d8413a5d55b4'
SOURCE_PATH = 'icons-json/interface-essential/navigation down circle_18069a19-0b23-40e6-a387-d8413a5d55b4.json'
AUTHOR = 'json_to_solo'

class NavigationDownCircleInterfaceEssential(Solo48):
    icon_id = 'navigation-down-circle-interface-essential'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'down', 'circle', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 12), (24, 34))
        self.add_line('e1', (16, 26), (24, 34))
        self.add_line('e2', (32, 26), (24, 34))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
