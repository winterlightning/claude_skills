"""Navigation up circle (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '49533251-8957-45c5-8d0d-d38335ec9389'
SOURCE_PATH = 'icons-json/interface-essential/navigation up circle_49533251-8957-45c5-8d0d-d38335ec9389.json'
AUTHOR = 'json_to_solo'

class NavigationUpCircle(Solo48):
    icon_id = 'navigation-up-circle'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'up', 'circle', 'interface-essential')

    def build(self):
        self.add_line('e0', (16, 20), (24, 12))
        self.add_line('e1', (24, 36), (24, 12))
        self.add_line('e2', (32, 20), (24, 12))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
