"""Navigation right circle turn (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c28f8d09-f6a4-48f1-a569-24408c30749c'
SOURCE_PATH = 'icons-json/interface-essential/navigation right circle turn_c28f8d09-f6a4-48f1-a569-24408c30749c.json'
AUTHOR = 'json_to_solo'

class NavigationRightCircleTurn(Solo48):
    icon_id = 'navigation-right-circle-turn'
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
        self.add_arc('e4-1', (14, 40), (7, 36), radius_x=11)
        self.add_arc('e4-2', (7, 36), (5, 33), radius_x=12)
        self.add_line('e4-3', (5, 33), (4, 28))
        self.add_line('e4-4', (4, 28), (6, 21))
        self.add_arc('e4-5', (6, 21), (9, 18), radius_x=10)
        self.add_arc('e4-6', (9, 18), (15, 16), radius_x=16)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
