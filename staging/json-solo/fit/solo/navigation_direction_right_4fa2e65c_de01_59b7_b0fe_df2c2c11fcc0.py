"""Navigation direction right (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4fa2e65c-de01-59b7-b0fe-df2c2c11fcc0'
SOURCE_PATH = 'icons-json/interface-essential/navigation direction right_4fa2e65c-de01-59b7-b0fe-df2c2c11fcc0.json'
AUTHOR = 'json_to_solo'

class NavigationDirectionRightInterfaceEssential(Solo48):
    icon_id = 'navigation-direction-right-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'direction', 'right', 'interface-essential')

    def build(self):
        self.add_line('e0', (31, 44), (40, 33))
        self.add_line('e1', (40, 33), (21, 33))
        self.add_line('e2', (19, 4), (27, 4))
        self.add_line('e3', (31, 22), (40, 33))
        self.add_arc('e4-1', (21, 33), (9, 24), radius_x=13)
        self.add_line('e4-2', (9, 24), (8, 18))
        self.add_arc('e4-3', (8, 18), (18, 4), radius_x=15)
        self.add_line('e4-4', (18, 4), (19, 4))
        self.add_contour('c0', 'e0', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e2')
        self.add_contour('c1', 'e3')
