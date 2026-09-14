"""Navigation right circle (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9df37805-d24e-447f-86c4-dfef7e691d13'
SOURCE_PATH = 'icons-json/interface-essential/navigation right circle_9df37805-d24e-447f-86c4-dfef7e691d13.json'
AUTHOR = 'json_to_solo'

class NavigationRightCircleInterfaceEssential(Solo48):
    icon_id = 'navigation-right-circle-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'right', 'circle', 'interface-essential')

    def build(self):
        self.add_line('e0', (35, 8), (44, 18))
        self.add_line('e1', (4, 40), (4, 31))
        self.add_line('e2', (17, 18), (44, 18))
        self.add_line('e3', (35, 27), (44, 18))
        self.add_bezier('e4', (4, 31), ((4, 30.07), (4.355, 28.89), (4.645, 28.01)), ((6.2, 23.26), (9.645, 19.58), (14.173, 18.45)), ((14.973, 18.25), (16.2, 18), (17, 18)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e4', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
