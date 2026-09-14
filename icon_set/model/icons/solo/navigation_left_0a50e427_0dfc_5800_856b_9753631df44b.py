"""Navigation left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a50e427-0dfc-5800-856b-9753631df44b'
SOURCE_PATH = 'icons-json/interface-essential/navigation left_0a50e427-0dfc-5800-856b-9753631df44b.json'
AUTHOR = 'json_to_solo'

class NavigationLeftInterfaceEssential(Solo48):
    icon_id = 'navigation-left-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (27, 16), (19, 24))
        self.add_line('e1', (19, 24), (44, 24))
        self.add_line('e2', (44, 24), (44, 8))
        self.add_line('e3', (44, 8), (20, 8))
        self.add_line('e4', (19, 40), (44, 40))
        self.add_line('e5', (27, 32), (19, 24))
        self.add_arc('e6-1', (20, 8), (4, 24), radius_x=17, sweep=False)
        self.add_arc('e6-2', (4, 24), (19, 40), radius_x=17, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e6-1', 'e6-2', 'e4')
        self.add_contour('c1', 'e5')
