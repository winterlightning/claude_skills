"""Navigation next (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c508d891-3f07-4433-8411-1ec63acc9088'
SOURCE_PATH = 'icons-json/interface-essential/navigation next_c508d891-3f07-4433-8411-1ec63acc9088.json'
AUTHOR = 'json_to_solo'

class NavigationNextInterfaceEssential(Solo48):
    icon_id = 'navigation-next-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'next', 'interface-essential')

    def build(self):
        self.add_line('e0', (37, 8), (42, 14))
        self.add_line('e1', (42, 14), (44, 16))
        self.add_line('e2', (26, 16), (44, 16))
        self.add_line('e3', (37, 25), (44, 16))
        self.add_line('e4', (25, 8), (5, 8))
        self.add_line('e5', (4, 10), (4, 38))
        self.add_line('e6', (6, 40), (25, 40))
        self.add_line('e7', (28, 38), (28, 26))
        self.add_arc('e8', (18, 31), (26, 16), radius_x=11)
        self.add_arc('e9', (5, 8), (4, 10), radius_x=3, sweep=False)
        self.add_arc('e10', (4, 38), (6, 40), radius_x=2, sweep=False)
        self.add_line('e11', (25, 40), (28, 38))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e8', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e9', 'e5', 'e10', 'e6', 'e11', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
