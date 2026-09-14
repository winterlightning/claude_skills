"""Navigation arrows left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4069ed45-da1b-585a-8cd7-896cccee9989'
SOURCE_PATH = 'icons-json/interface-essential/navigation arrows left_4069ed45-da1b-585a-8cd7-896cccee9989.json'
AUTHOR = 'json_to_solo'

class NavigationArrowsLeft4069ed45(Solo48):
    icon_id = 'navigation-arrows-left-4069ed45'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'arrows', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (32, 29), (44, 40))
        self.add_line('e1', (44, 40), (44, 8))
        self.add_line('e2', (44, 8), (27, 24))
        self.add_line('e3', (27, 24), (32, 29))
        self.add_line('e4', (32, 29), (32, 40))
        self.add_line('e5', (32, 40), (16, 24))
        self.add_line('e6', (16, 24), (32, 8))
        self.add_line('e7', (32, 8), (32, 19))
        self.add_line('e8', (21, 18), (21, 8))
        self.add_line('e9', (21, 8), (4, 24))
        self.add_line('e10', (4, 24), (21, 40))
        self.add_line('e11', (21, 40), (21, 30))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7')
        self.add_contour('c1', 'e8', 'e9', 'e10', 'e11')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
