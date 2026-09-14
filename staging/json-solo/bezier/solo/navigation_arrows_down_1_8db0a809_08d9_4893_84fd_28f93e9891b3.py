"""Navigation arrows down 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e17', (22, 32), ((23.171, 32.527), (23.821, 32.491), (25, 32)))
        self.add_bezier('e18', (8, 17), ((8.025, 16.873), (8.042, 16.464), (8.067, 16.336)), ((8.236, 16.064), (8.739, 16.173), (9, 16)))
        self.add_bezier('e19', (9, 27), ((8.638, 27.336), (8.017, 27.255), (8.017, 27.845)), ((8.008, 27.873), (8.008, 27.891), (8, 27.918)), ((8, 28.127), (8, 28.791), (8, 29)))
        self.add_bezier('e20', (22, 44), ((22.455, 44), (23.225, 43.991), (23.68, 43.991)), ((23.815, 43.991), (23.941, 43.982), (24.067, 43.982)), ((24.109, 43.991), (24.152, 43.991), (24.185, 44)), ((24.404, 44), (24.781, 44), (25, 44)))
        self.add_bezier('e21', (39, 17), ((38.655, 16.555), (38.328, 16.355), (38, 16)))
        self.add_bezier('e22', (22, 21), ((23.137, 21.5), (23.813, 21.482), (25, 21)))
        self.add_bezier('e23', (8, 6), ((8, 5.845), (8, 5.518), (8, 5.364)), ((8, 4.073), (8.368, 4.509), (9, 4)))
        self.add_bezier('e24', (38, 4), ((38.118, 4.045), (38.552, 4.082), (38.669, 4.127)), ((38.931, 4.273), (39.402, 5.045), (39.402, 5.355)), ((39.318, 5.509), (39.084, 5.845), (39, 6)))
        self.add_contour('c0', 'e0', 'e17', 'e1')
        self.add_contour('c1', 'e2', 'e18', 'e3')
        self.add_contour('c2', 'e4', 'e19', 'e5', 'e20', 'e6', 'e7', 'e8', 'e9')
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
