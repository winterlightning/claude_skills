"""Navigation menu horizontal (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5094fde9-e2bf-5105-b3e2-9fe5c51241c7'
SOURCE_PATH = 'icons-json/interface-essential/navigation menu horizontal_5094fde9-e2bf-5105-b3e2-9fe5c51241c7.json'
AUTHOR = 'json_to_solo'

class NavigationMenuHorizontal(Solo48):
    icon_id = 'navigation-menu-horizontal'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'menu', 'horizontal', 'interface-essential')

    def build(self):
        self.add_arc('sym-e0', (22, 23), (26, 23), radius_x=2)
        self.add_arc('sym-e1', (26, 23), (22, 23), radius_x=2)
        self.add_arc('sym-e2', (13, 23), (17, 23), radius_x=2)
        self.add_arc('sym-e3', (17, 23), (13, 23), radius_x=2)
        self.add_arc('sym-e4', (35, 23), (31, 23), radius_x=2, sweep=False)
        self.add_arc('sym-e5', (31, 23), (35, 23), radius_x=2, sweep=False)
        self.add_line('sym-e6', (24, 42), (10, 42))
        self.add_arc('sym-e8-1', (10, 42), (7, 41), radius_x=5)
        self.add_line('sym-e8-2', (7, 41), (6, 39))
        self.add_line('sym-e9', (6, 39), (6, 10))
        self.add_line('sym-e11-1', (6, 10), (7, 7))
        self.add_line('sym-e11-2', (7, 7), (9, 6))
        self.add_line('sym-e12', (9, 6), (24, 6))
        self.add_line('sym-e13', (24, 6), (39, 6))
        self.add_line('sym-e14-1', (39, 6), (41, 7))
        self.add_line('sym-e14-2', (41, 7), (42, 10))
        self.add_line('sym-e16', (42, 10), (42, 39))
        self.add_line('sym-e17-1', (42, 39), (41, 41))
        self.add_arc('sym-e17-2', (41, 41), (38, 42), radius_x=5)
        self.add_line('sym-e19', (38, 42), (24, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', closed=True)
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', closed=True)
        self.add_contour('sym-c3', 'sym-e6', 'sym-e8-1', 'sym-e8-2', 'sym-e9', 'sym-e11-1', 'sym-e11-2', 'sym-e12', 'sym-e13', 'sym-e14-1', 'sym-e14-2', 'sym-e16', 'sym-e17-1', 'sym-e17-2', 'sym-e19', closed=True)
