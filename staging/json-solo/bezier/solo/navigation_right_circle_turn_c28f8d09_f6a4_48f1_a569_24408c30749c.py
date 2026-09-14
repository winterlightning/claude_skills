"""Navigation right circle turn (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c28f8d09-f6a4-48f1-a569-24408c30749c'
SOURCE_PATH = 'icons-json/interface-essential/navigation right circle turn_c28f8d09-f6a4-48f1-a569-24408c30749c.json'
AUTHOR = 'json_to_solo'

class NavigationRightCircleTurnInterfaceEssential(Solo48):
    icon_id = 'navigation-right-circle-turn-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'right', 'circle', 'turn', 'interface-essential')

    def build(self):
        self.add_line('e0', (38, 8), (44, 16))
        self.add_line('e1', (19, 40), (14, 40))
        self.add_line('e2', (15, 16), (44, 16))
        self.add_line('e3', (38, 23), (44, 16))
        self.add_bezier('e4', (14, 40), ((13.291, 40), (12.445, 39.67), (11.773, 39.42)), ((7.536, 37.91), (4.009, 33.52), (4.009, 28.44)), ((4.009, 28.342), (4, 28.253), (4, 28.155)), ((4, 28.153), (4, 28.152), (4, 28.15)), ((4, 27.86), (4.009, 27.56), (4.009, 27.27)), ((4.009, 26.08), (4.3, 24.87), (4.636, 23.75)), ((5.864, 19.71), (8.955, 17.37), (12.627, 16.46)), ((13.327, 16.29), (14.3, 16), (15, 16)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e4', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
