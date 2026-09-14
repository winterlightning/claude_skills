"""Navigation right circle 2 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1d6c618c-6f46-4174-85da-537df6f1d70f'
SOURCE_PATH = 'icons-json/interface-essential/navigation right circle 2_1d6c618c-6f46-4174-85da-537df6f1d70f.json'
AUTHOR = 'json_to_solo'

class NavigationRightCircle2InterfaceEssential(Solo48):
    icon_id = 'navigation-right-circle-2-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'right', 'circle', 'interface-essential')

    def build(self):
        self.add_line('e0', (34, 8), (44, 24))
        self.add_line('e1', (4, 24), (44, 24))
        self.add_line('e2', (34, 40), (44, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
