"""Navigation menu horizontal (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5094fde9-e2bf-5105-b3e2-9fe5c51241c7'
SOURCE_PATH = 'icons-json/interface-essential/navigation menu horizontal_5094fde9-e2bf-5105-b3e2-9fe5c51241c7.json'
AUTHOR = 'json_to_solo'

class NavigationMenuHorizontalInterfaceEssential(Solo48):
    icon_id = 'navigation-menu-horizontal-interface-essential'
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
        self.add_bezier('sym-e7', (10, 42), ((9.869, 42), (10.131, 42), (10, 42)))
        self.add_bezier('sym-e8', (10, 42), ((8.29, 42), (6, 40.874), (6, 39)))
        self.add_line('sym-e9', (6, 39), (6, 10))
        self.add_bezier('sym-e10', (6, 10), ((6, 9.853), (6, 10.147), (6, 10)))
        self.add_bezier('sym-e11', (6, 10), ((6, 8.38), (7.257, 6), (9, 6)))
        self.add_line('sym-e12', (9, 6), (24, 6))
        self.add_line('sym-e13', (24, 6), (39, 6))
        self.add_bezier('sym-e14', (39, 6), ((40.743, 6), (42, 8.38), (42, 10)))
        self.add_bezier('sym-e15', (42, 10), ((42, 10.147), (42, 9.853), (42, 10)))
        self.add_line('sym-e16', (42, 10), (42, 39))
        self.add_bezier('sym-e17', (42, 39), ((42, 40.874), (39.71, 42), (38, 42)))
        self.add_bezier('sym-e18', (38, 42), ((37.869, 42), (38.131, 42), (38, 42)))
        self.add_line('sym-e19', (38, 42), (24, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', closed=True)
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', closed=True)
        self.add_contour('sym-c3', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
