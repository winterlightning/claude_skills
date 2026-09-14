"""Navigation right circle 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e6140da1-12a6-42b8-8c1e-0d011b328cb6'
SOURCE_PATH = 'icons-json/interface-essential/navigation right circle 1_e6140da1-12a6-42b8-8c1e-0d011b328cb6.json'
AUTHOR = 'json_to_solo'

class NavigationRightCircle1InterfaceEssential(Solo48):
    icon_id = 'navigation-right-circle-1-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'right', 'circle', 'interface-essential')

    def build(self):
        self.add_line('e0', (38, 8), (44, 15))
        self.add_line('e1', (4, 40), (4, 24))
        self.add_line('e2', (12, 15), (44, 15))
        self.add_line('e3', (38, 22), (44, 15))
        self.add_arc('e4', (4, 24), (12, 15), radius_x=10)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e4', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
