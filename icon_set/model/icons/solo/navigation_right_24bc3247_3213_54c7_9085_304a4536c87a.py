"""Navigation right (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24bc3247-3213-54c7-9085-304a4536c87a'
SOURCE_PATH = 'icons-json/interface-essential/navigation right_24bc3247-3213-54c7-9085-304a4536c87a.json'
AUTHOR = 'json_to_solo'

class NavigationRight(Solo48):
    icon_id = 'navigation-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'right', 'interface-essential')

    def build(self):
        self.add_line('e0', (34, 40), (44, 28))
        self.add_line('e1', (43, 25), (34, 14))
        self.add_line('e2', (44, 28), (43, 25))
        self.add_arc('e3-1', (35, 26), (18, 28), radius_x=74)
        self.add_arc('e3-2', (18, 28), (8, 23), radius_x=11)
        self.add_arc('e3-3', (8, 23), (4, 10), radius_x=32)
        self.add_line('e3-4', (4, 10), (4, 8))
        self.add_contour('c0', 'e0', 'e2', 'e1')
        self.add_contour('c1', 'e3-1', 'e3-2', 'e3-3', 'e3-4')
