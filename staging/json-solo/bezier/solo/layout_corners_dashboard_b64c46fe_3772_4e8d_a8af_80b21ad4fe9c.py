"""Layout corners dashboard (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b64c46fe-3772-4e8d-a8af-80b21ad4fe9c'
SOURCE_PATH = 'icons-json/interface-essential/layout corners dashboard_b64c46fe-3772-4e8d-a8af-80b21ad4fe9c.json'
AUTHOR = 'json_to_solo'

class LayoutCornersDashboardInterfaceEssential(Solo48):
    icon_id = 'layout-corners-dashboard-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'corners', 'dashboard', 'interface-essential')

    def build(self):
        self.add_line('e0', (9, 6), (9, 10))
        self.add_line('e1', (6, 10), (9, 10))
        self.add_line('e2', (39, 42), (39, 39))
        self.add_line('e3', (42, 39), (39, 39))
        self.add_line('e4', (9, 10), (35, 10))
        self.add_line('e5', (39, 13), (39, 39))
        self.add_line('e6', (9, 10), (9, 35))
        self.add_line('e7', (13, 39), (39, 39))
        self.add_bezier('e8', (35, 10), ((36.628, 10), (39, 11.372), (39, 13)))
        self.add_bezier('e9', (9, 35), ((9, 36.808), (11.192, 39), (13, 39)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e8', 'e5')
        self.add_contour('c5', 'e6', 'e9', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
