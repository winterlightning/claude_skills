"""Navigation arrows down 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8db0a809-08d9-4893-84fd-28f93e9891b3'
SOURCE_PATH = 'icons-json/interface-essential/navigation arrows down 1_8db0a809-08d9-4893-84fd-28f93e9891b3.json'
AUTHOR = 'json_to_solo'

class NavigationArrowsDown1InterfaceEssential(Solo48):
    icon_id = 'navigation-arrows-down-1-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'arrows', 'down', 'interface-essential')

    def build(self):
        self.add_line('e0', (17, 27), (22, 32))
        self.add_line('e1', (25, 32), (30, 27))
        self.add_line('e2', (17, 27), (8, 17))
        self.add_line('e3', (9, 16), (17, 16))
        self.add_line('e4', (17, 27), (9, 27))
        self.add_line('e5', (8, 29), (22, 44))
        self.add_line('e6', (25, 44), (38, 29))
        self.add_line('e7', (38, 29), (40, 27))
        self.add_line('e8', (40, 27), (36, 27))
        self.add_line('e9', (36, 27), (30, 27))
        self.add_line('e10', (30, 27), (39, 17))
        self.add_line('e11', (38, 16), (30, 16))
        self.add_line('e12', (17, 16), (22, 21))
        self.add_line('e13', (25, 21), (30, 16))
        self.add_line('e14', (17, 16), (8, 6))
        self.add_line('e15', (9, 4), (38, 4))
        self.add_line('e16', (39, 6), (30, 16))
        self.add_arc('e17', (22, 32), (25, 32), radius_x=2, sweep=False)
        self.add_arc('e18', (8, 17), (9, 16), radius_x=1)
        self.add_arc('e19-1', (9, 27), (8, 28), radius_x=1, sweep=False)
        self.add_line('e19-2', (8, 28), (8, 29))
        self.add_line('e20-1', (22, 44), (24, 44))
        self.add_line('e20-2', (24, 44), (25, 44))
        self.add_arc('e21', (39, 17), (38, 16), radius_x=7, sweep=False)
        self.add_arc('e22', (22, 21), (25, 21), radius_x=2, sweep=False)
        self.add_line('e23', (8, 6), (9, 4))
        self.add_arc('e24', (38, 4), (39, 6), radius_x=2)
        self.add_contour('c0', 'e0', 'e17', 'e1')
        self.add_contour('c1', 'e2', 'e18', 'e3')
        self.add_contour('c2', 'e4', 'e19-1', 'e19-2', 'e5', 'e20-1', 'e20-2', 'e6', 'e7', 'e8', 'e9')
        self.add_contour('c3', 'e10', 'e21', 'e11')
        self.add_contour('c4', 'e12', 'e22', 'e13')
        self.add_contour('c5', 'e14', 'e23', 'e15', 'e24', 'e16')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
